import picamera

camera = picamera.PiCamera()

def CameraON():
    camera.start_preview(fullscreen=False, window = (600, 50, 320, 240))

def CameraOFF():
    camera.stop_preview()
    