

import subprocess
import os
import time

test_iterates = 100


def change_dir():
    cur_dir = os.getcwd()
    project_dir = os.path.abspath(os.path.dirname(__file__))
    print(project_dir)
    os.chdir(project_dir + "/libs/platform-tools")
    print(os.getcwd())
    print(project_dir)


def get_devices():
    output = subprocess.check_output("adb devices")
    # print(output)
    lines = output.strip().split("\n")
    # print(lines)
    devices = []

    for i in range(1, len(lines)):
        devices.append(lines[i].split("\t")[0])

    return devices


def test_connect_disconnect(device):
    if "emulator" in device:
        pass

    for i in range(0, test_iterates):
        tap(device, 350, 860)
        time.sleep(2)
        tap(device, 50, 130)


def get_screen_density(device):
    output = subprocess.check_output("adb -s " + device + " shell wm density")
    return int(output.strip().split(":")[1].strip())


def set_screen_density(device, density):
    subprocess.call("adb -s " + device + " shell wm density " + str(density))


def get_screen_size(device):
    output = subprocess.check_output("adb -s " + device + " shell wm size")
    size = output.strip().split(":")[1].strip()
    sizes = size.split("x")
    return [int(sizes[0]), int(sizes[1])]


def tap(device, x, y):
    subprocess.call("adb " + "-s " + device + " shell input tap " + str(x) + " " + str(y))


def swipe(device, x1, y1, x2, y2, duration):
    subprocess.call("adb " + "-s " + device + " shell input swipe "
                    + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(duration))


def long_press(device, x, y, duration):
    swipe(device, x, y, x, y, duration)


def tap_back(device):
    subprocess.call("adb " + "-s " + device + " shell input keyevent " + "KEYCODE_BACK")


def tap_home(device):
    subprocess.call("adb " + "-s " + device + " shell input keyevent --longpress " + "KEYCODE_HOME")


def tap_menu(device):
    subprocess.call("adb " + "-s " + device + " shell input keyevent " + "KEYCODE_MENU")


def main():
    change_dir()
    devices = get_devices()
    print(devices)

    # change_dir()
    # devices = get_devices()
    # print(devices)
    # # tap_home(devices[0])
    # # tap(devices[1], 350, 860)
    # # long_press(devices[0], 400, 1233, 3000)
    # print(get_screen_density(devices[0]))
    # print(get_screen_size(devices[0]))
    # # test_connect_disconnect(devices[0])


if __name__ == '__main__':
    main()
