from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import RPi.GPIO as GPIO
import outVideo
import os
import configparser
import time

if __name__ == "__main__":
    # I/O initialization
    GPIO.setmode(GPIO.BOARD)
    LED_POWER = 7
    LED_RECORDING = 13
    START_SIGNAL = 15

    GPIO.setup(LED_POWER, GPIO.OUT)
    GPIO.setup(LED_RECORDING, GPIO.OUT)
    GPIO.setup(START_SIGNAL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.output(LED_POWER, 1) # Green LED on
    GPIO.output(LED_RECORDING, 0) # Green LED on

    # Configuration variables
    path = f"{os.path.dirname(__file__)}/"
    config = configparser.ConfigParser()
    config.read(f"{path}config.ini")
    vidLenght = int(config.get("Camera","vidLenght"))
    chunkLenght = int(config.get("Camera","chunkLenght"))
    log = "True" == config.get("Camera","log")
    nbrChunks = int(vidLenght/chunkLenght)

    # Camera initialization
    camera = Picamera2()
    camera.resolution = (1920, 1080)
    encoder = H264Encoder()

    if log:
        logFile = open(f"{path}log.log","w",encoding="utf-8")
        logFile.write("Logs enabled\n")

    # Waiting for 5V signal to start recording
    while(not GPIO.input(START_SIGNAL)):
        time.sleep(0.1)

    GPIO.output(LED_RECORDING, 1) # Red LED on
    for i in range(0,nbrChunks+1):
        camera.start_recording(encoder, f"{path}video/{i}.h264")
        time.sleep(5)
        camera.stop_recording()
        if log:
            logFile.write(f"Chunk {i} saved.\n")
            logFile.flush()
    logFile.write(f"Recording completed successfully !\n")
    logFile.flush()
    logFile.close()
    
