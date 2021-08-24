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


if __name__ == "__main__":

    import datetime

    date_part = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prefix = "data/pot_%s" % date_part

    try:
        image = shoot(prefix, timeout_for_focus_seconds=7)
    except Exception as e:
        print("UnSuccessful")
