from adbpy import adb
from adbpy.device import Device
import os
from threading import Thread
import datetime
import random

test_iterates = 100
cur_dir = os.path.abspath(os.path.dirname(__file__))
record_screen_finished = False
time_stamp_format = "%m-%d %H:%M:%S"


def monkey(device):
    [device_width, device_height] = device.get_screen_size()
    for i in range(0, test_iterates):
        print(datetime.datetime.now().strftime(time_stamp_format) + " iterate " + str(i))
        device.tap(random.randint(1, device_width), random.randint(1, device_height))


def record_screen(device):
    device.record_screen(name="video", dst_path=cur_dir, time=10)


def test_suite(device):
    monkey(device)


def main():
    devices = adb.get_devices()
    for i in range(0, len(devices)):
        device = Device(devices[i])
        Thread(name=device.get_id(), target=test_suite, args=(device,)).start()


if __name__ == '__main__':
    main()
