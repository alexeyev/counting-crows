#!/usr/bin/env python
from time import sleep

from picamera import PiCamera

camera = PiCamera()


def shoot(prefix: str):
    camera.start_preview()
    sleep(5)
    camera.capture(prefix + ".jpg")
    camera.stop_preview()
    return open(prefix + ".jpg", "rb")
