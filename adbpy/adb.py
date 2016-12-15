"""
This module load the necessary libraries and files of Android Debug Bridge.

"""

import subprocess
import os
from device import Device

test_iterates = 100


def change_dir():
    project_dir = os.path.abspath(os.path.dirname(__file__))
    os.chdir("..")
    os.chdir(os.getcwd() + "/libs/platform-tools")


def get_devices():
    change_dir()
    output = subprocess.check_output("adb devices")
    # print(output)
    lines = output.strip().split("\n")
    # print(lines)
    devices = []

    for i in range(1, len(lines)):
        # device = Device(lines[i].split("\t")[0])
        device_name = lines[i].split("\t")[0]
        if "emulator" not in device_name:
            devices.append(device_name)

    return devices
