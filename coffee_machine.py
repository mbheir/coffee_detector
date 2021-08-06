import subprocess
import shlex
from datetime import datetime

import spam_teams


RUN_COMMAND = '/home/pi/.npm-global/bin/edge-impulse-run-impulse'
detections = 0
last_detection = datetime.now()
last_confirmation = datetime.now()
coffee_is_detected = False

''' 1.  Perhaps do a weighted sum of confidence / 
        do more detections as a criteria / 
        maybe have "off" values after many "on" values a criteria
    
    2.  Trigger the notification on Teams

'''

def process_detection(confidence):
    global detections
    global last_detection
    global last_confirmation
    global coffee_is_detected

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Time: {current_time} We got ON value = {confidence}")
    
    if (now - last_detection).total_seconds() < 30: #Adds valid detection if they happen rapidly
        detections += 1
    else:
        detections = 0
    if detections >= 10: #10 detections (in a row) is a strong indication someone is making coffee
        if (now-last_confirmation).total_seconds() > 240: #Coffee made more rapid than 4 minutes does not count
            coffee_is_detected = True
            detections = 0
            last_confirmation = now
    last_detection = now
    return


def main():
    global coffee_is_detected
    process_alive = False
    process_alive_time = datetime.now()
    print("Smart coffee detector activated")
    print("Sampling...")
    while True:
        now = datetime.now()
        if process_alive == True:
            if (now - process_alive_time).total_seconds() > 30:
                    delta = (now - process_alive_time).total_seconds()
                    print(f"EDGE IMPULSE HAS DIED, RESTARTING. (Delta time={delta})")
                    process_alive = False
            
            # Reading input
            output = process.stdout.readline() #read line from console
            if output == '' and process.poll() is not None:
                break
            if output:
                process_alive_time = datetime.now()
                line = output.strip().decode("utf-8")
                parsed = line.split()
                if 'on:' in parsed: #
                    confidence = parsed[1]
                    if float(confidence) > 0.80:
                        process_detection(confidence)
            
            if coffee_is_detected and (now - last_detection).total_seconds() > 30: #We need to wait until all the coffee is done to notify
                print("SOMEONE IS MAKING COFFEE!!!")
                # Post a notification on #Kaffe channel on Teams
                spam_teams.post_on_teams()
                coffee_is_detected = False

            
        else:
            process = subprocess.Popen(shlex.split(RUN_COMMAND), stdout=subprocess.PIPE)
            process_alive = True
            process_alive_time = datetime.now()

    rc = process.poll()
    return rc

main()
