import picamera
import outVideo
import os
import configparser

if __name__ == "__main__":
    path = f"{os.path.dirname(__file__)}/"
    config = configparser.ConfigParser()
    config.read(f"{path}config.ini")
    vidLenght = config.get("Camera","vidLenght")
    chunkLenght = config.get("Camera","chunkLenght")
    log = "True" == config.get("Camera","log")

    camera = picamera.PiCamera()
    camera.resolution = (1920, 1080)

    if log:
        logFile = open(f"{path}log.log","w",encoding="utf-8")
        logFile.write("Logs enabled\n")

    nbrChunks = int(vidLenght/chunkLenght)
    for i in range(0,nbrChunks+1):
        vidFile = outVideo.vidFile(f"{path}video/{i}")
        camera.start_recording(vidFile, format="h264")
        camera.wait_recording(5)
        camera.stop_recording()
        if log:
            logFile.write(f"Chunk {i} saved.\n")
            logFile.flush()
    logFile.write(f"Recording completed successfully !\n")
    logFile.flush()
    logFile.close()
    