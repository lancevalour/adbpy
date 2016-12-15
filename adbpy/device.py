"""
Device class to control the connected Android device through Android Debug Bridge.

"""
import subprocess
import os


class Device:
    def __init__(self, device_id):
        self.__device_id = device_id

    # Device properties
    def get_id(self):
        return self.__device_id

    def get_screen_density(self):
        output = subprocess.check_output("adb -s " + self.__device_id + " shell wm density")
        return int(output.strip().split(":")[1].strip())

    def get_screen_size(self):
        output = subprocess.check_output("adb -s " + self.__device_id + " shell wm size")
        size = output.strip().split(":")[1].strip()
        sizes = size.split("x")
        return [int(sizes[0]), int(sizes[1])]

    def set_screen_density(self, density):
        subprocess.call("adb -s " + self.__device_id + " shell wm density " + str(density))

    # Installation
    def install_apk(self, apk_path):
        subprocess.call("adb -s " + self.__device_id + " install" + str(apk_path))

    # Control
    def tap(self, x, y):
        subprocess.call("adb " + "-s " + self.__device_id + " shell input tap " + str(x) + " " + str(y))

    def tap_back(self):
        subprocess.call("adb " + "-s " + self.__device_id + " shell input keyevent " + "KEYCODE_BACK")

    def tap_home(self):
        subprocess.call("adb " + "-s " + self.__device_id + " shell input keyevent --longpress " + "KEYCODE_HOME")

    def tap_menu(self):
        subprocess.call("adb " + "-s " + self.__device_id + " shell input keyevent " + "KEYCODE_MENU")

    def swipe(self, x1, y1, x2, y2, duration):
        subprocess.call("adb " + "-s " + self.__device_id + " shell input swipe "
                        + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(duration))

    def long_press(self, x, y, duration):
        self.swipe(x, y, x, y, duration=duration)

    # Screen capture
    def take_screenshot(self, name, dst_path=os.path.abspath(os.path.dirname(__file__))):
        subprocess.call("adb " + "-s " + self.__device_id + " shell screencap /sdcard/" + name + ".png")
        subprocess.call("adb " + "-s " + self.__device_id + " pull /sdcard/" + name + ".png " + dst_path)
        subprocess.call("adb " + "-s " + self.__device_id + " shell rm /sdcard/" + name + ".png")

    def record_screen(self, name, dst_path=os.path.abspath(os.path.dirname(__file__)), time=10):
        subprocess.call("adb " + "-s " + self.__device_id + " shell screenrecord --time-limit " + str(
            time) + " /sdcard/" + name + ".mp4")
        subprocess.call("adb " + "-s " + self.__device_id + " pull /sdcard/" + name + ".mp4 " + dst_path)
        subprocess.call("adb " + "-s " + self.__device_id + " shell rm /sdcard/" + name + ".mp4")
