# Coffee Detector

A raspberry pi project for detecting when the coffee machine in the office has finished making a fresh pot of coffee, and send a push notification on Teams.

## How it works
A ThunderBoard Sense 2 with an IMU sensor is running an Edge Impulse machine learning binary that was trained to detect when the coffee machine is making coffee based on vibrations. The python code in this repolistory runs on a raspberry pi and starts the inference process on the ThunderBoard. The code also captures the classification outputs, makes a decision whether a new mug was made based on the classification outputs, and posts a notification in a channel on Teams together with a random quote through a webhook using a HTTP post request. 

<p float="left">
<img src="https://user-images.githubusercontent.com/55540484/128928454-fc2bdda1-df25-4824-88c4-0e7d9db82f53.jpeg" height="500" />
<img src="https://user-images.githubusercontent.com/55540484/128930365-55340637-a6d4-46ad-887e-c1493c7b1242.jpg" height="500" />
</p>

## How to run

Start application by running coffee_machine.py.

### NB
For the raspberry pi in the office, the application will automatically run when the raspberry pi reboots. 
See /etc/rc.local. 

