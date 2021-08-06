import subprocess
import shlex

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            line = output.strip().decode("utf-8")
            parsed = line.split()
            if 'on:' in parsed:
                print(f"We got ON value = {parsed[1]}")

    rc = process.poll()
    return rc

run_command('edge-impulse-run-impulse')