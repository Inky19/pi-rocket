# pi-rocket

A small script to record video using a Raspberry Pi inside a rocket.  
The video is splitted in chunks to prevent the loss of all the record if the power is cut off at any moment during flight.

## Installation
- Place the script and the config file where you want.
- Create a `video` folder, in the same folder as the script.

You can then run the script with `python camera.py`.

## Requirements
Python modules:
- PiCamera2
- RPi.GPIO
- configparser
