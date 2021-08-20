# coding: utf-8

from time import sleep
from picamera import PiCamera

camera = PiCamera()


def shoot(prefix: str, timeout_for_focus_seconds=5):
    camera.start_preview()
    sleep(timeout_for_focus_seconds)
    camera.capture(prefix + ".jpg")
    camera.stop_preview()
    return open(prefix + ".jpg", "rb")
