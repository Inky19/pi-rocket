# pi-rocket

A small script to record a video using a Raspberry Pi inside a rocket.  
The video is cut into chunks to avoid losing the whole recording if the power is cut at any time during the flight.

## Installation
- Place the script and the config file where you want.
- Create a `video` folder, in the same folder as the script.

You can then run the script with `python camera.py`.

## Requirements
Python modules:
- PiCamera2
- RPi.GPIO
- configparser
