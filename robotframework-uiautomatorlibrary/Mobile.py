# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device
import subprocess
import os
import time
import datetime
from robot.output.monitor import CommandLineWriter as clm
from robot.libraries.BuiltIn import BuiltIn
import sys


# print "Importing Android library"
# clm = CommandLineWriter()
# clm.message("Importing Android library")

class TestHelper:
    def __init__(self, adb):
        self.adb = adb

    def __convert_to_unicode_by_text(self, text):
        """
                        將輸入的字串轉換成 Unicode Transformation Format (UTF-8)
        """
        # 由object轉換為string之後，移除前後的unicode標記，例如：將u'abc'轉換為字串abc
        return repr(text)[2:-1]

    def send_set_text_cmd(self, text):
        """
        shell指令使用雙引號括起來，例如：adb shell "am broadcast -a myIME.intent.action.pass.string -e input abc"
                        但由於內容也可能為包含符號或是空白，所以必須再使用雙引號括起來，例如："abc c"
        """
        self.adb.shell_cmd('\"am broadcast -a myIME.intent.action.pass.string -e input \\\"%s\\\"\"' % TestHelper.__convert_to_unicode_by_text(self, text))
        self.adb.shell_cmd('input keyevent KEYCODE_UNKNOWN')

class ADB:
    def __init__(self, android_serial=None):
        self.buf = []
        self.buf.append('adb ')
        self.prefix_cmd = ''.join(self.buf)
        if android_serial is not None :
            self.buf.append('-s %s ' % android_serial)
            self.prefix_cmd = ''.join(self.buf)

    def cmd(self, cmd):
        """
                        將 adb -s SERIAL_NUMBER xxxxxx or adb xxxxxxx 取代成 xxxxxx
        """
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def shell_cmd(self, cmd):
        """
                        將 adb -s SERIAL_NUMBER shell xxxxxx or adb shell xxxxxxx 取代成 xxxxx-x
        """
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append('shell ')
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

class Mobile():
    """
    robotframework-uiautomatorlibrary is an Android device testing library for Robot Framework.

    It uses uiautomator - Python wrapper for Android uiautomator tool (https://pypi.python.org/pypi/uiautomator/0.1.28) internally.

    *Before running tests*

    You can use `Set Serial` to specify which device to perform the test.


    *Identify UI object*

    There are two kinds of keywords.

    
    """

    __version__ = '0.1'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def set_serial(self, android_serial):
        """
        Specify given *android_serial* device to perform test.

        You do not have to specify the device when there is only one device connects to the computer.

        When you need to use multiple devices, do not use this keyword to switch between devices in test execution.

        Using different library name when importing this library according to http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.8.4#setting-custom-name-to-test-library.

        | Setting | Value |  Value |  Value | 
        | Library | Mobile | WITH NAME | Mobile1 |
        | Library | Mobile | WITH NAME | Mobile2 |

        And set the serial to each library.

        | Test Case        | Action             | Argument           |
        | Multiple Devices | Mobile1.Set Serial | device_1's serial  |
        |                  | Mobile2.Set Serial | device_2's serial  |

        """
        self.adb = ADB(android_serial)
        self.device = Device(android_serial)
        self.test_helper = TestHelper(self.adb)

    def get_device_info(self):
        """
        Retrieve the device info.

        The keyword will return a dictionary.

        You can log the information by using the log dictionary keyword in build in Collections library(http://robotframework.googlecode.com/hg/doc/libraries/Collections.html?r=2.8.4).

        Example:
        | ${device_info} | Get Device Info |
        | Log Dictionary | ${device_info}  |

        =>

        Dictionary size is 9 and it contains following items:\n
        currentPackageName: com.android.keyguard\n
        displayHeight: 1776\n
        displayRotation: 0\n
        displaySizeDpX: 360\n
        displaySizeDpY: 640\n
        displayWidth: 1080\n
        naturalOrientation: True\n
        productName: hammerhead\n
        sdkInt: 19\n

        Or get specific information of the device by giving the key.

        | ${device_info}  | Get Device Info | | |
        | ${product_name} | Get From Dictionary | ${device_info} | productName |

        =>

        ${product_name} = hammerhead

        """
        return self.device.info

#Key Event Actions of the device
    """
    Turn on/off screen
    """
    def turn_on_screen(self):
        """
        Turn on screen
        """
        self.device.screen.on()

    def turn_off_screen(self):
        """
        Turn off screen
        """
        self.device.screen.off()

    """
    Press hard/soft key
    """

    def press_key(self, *keys):
        """
        Press *key* keycode.

        You can find all keycode in http://developer.android.com/reference/android/view/KeyEvent.html

        Example:

        |Press Key | 
        """
        self.device.press(*keys)

    def press_home(self):
        """
        Press home key
        """
        self.device.press.home()

    def press_back(self):
        """
        Press back key
        """
        self.device.press.back()

    def press_left(self):
        """
        Press left key
        """
        self.device.pres.left()

    def press_right(self):
        """
        Press right key
        """
        self.device.press.right()

    def press_up(self):
        """
        Press up key
        """
        self.device.press.up()

    def press_down(self):
        """
        Press down key
        """
        self.device.press.down()

    def press_center(self):
        """
        Press center key
        """
        self.device.press.center()

    def press_menu(self):
        """
        Press menu key
        """
        self.device.press.menu()

    def press_search(self):
        """
        Press search key
        """
        self.device.press.search()

    def press_enter(self):
        """
        Press enter key
        """
        self.device.press.enter()

    def press_delete(self):
        """
        Press delete key
        """
        self.device.press.delete()

    def press_recent(self):
        """
        Press recent key
        """
        self.device.press.recent()

    def press_volume_up(self):
        """
        Press volume up key
        """
        self.device.press.volume_up()

    def press_volume_down(self):
        """
        Press volume down key
        """
        self.device.press.volume_down()

    def press_camera(self):
        """
        Press camera key
        """
        self.device.press.camera()

    def press_power(self):
        """
        Press power key
        """
        self.device.press.power()

#Gesture interaction of the device

    def click_at_coordinates(self, x, y):
        """
        Click at (x,y) coordinates.
        """
        self.device.click(x, y)

    def swipe_by_coordinates(self, sx, sy, ex, ey, steps=100):
        """
        Swipe from (sx, sy) to (ex, ey) with *steps* .
        """
        self.device.swipe(sx, sy, ex, ey, steps)

# Swipe from the center of the ui object to its edge

    def swipe_left(self, steps=100, *args, **attributes):
        """
        Swipe the UI object with *attributes* from center to left.
        """
        self.device(**attributes).swipe.left(steps=steps)

    def swipe_right(self, steps=100, *args, **attributes):
        """
        Swipe the UI object with *attributes* from center to right
        """
        self.device(**attributes).swipe.right(steps=steps)

    def swipe_top(self, steps=100, *args, **attributes):
        """
        Swipe the UI object with *attributes* from center to top
        """
        self.device(**attributes).swipe.up(steps=steps)

    def swipe_bottom(self, steps=100, *args, **attributes):
        """
        Swipe the UI object with *attributes* from center to bottom
        """
        self.device(**attributes).swipe.down(steps=steps)

    def object_swipe_left(self, obj, steps=100):
        """
        Swipe the *obj* from center to left
        """
        obj.swipe.left(steps=steps)

    def object_swipe_right(self, obj, steps=100):
        """
        Swipe the *obj* from center to right
        """
        obj.swipe.right(steps=steps)

    def object_swipe_top(self, obj, steps=100):
        """
        Swipe the *obj* from center to top
        """
        obj.swipe.up(steps=steps)

    def object_swipe_bottom(self, obj, steps=100):
        """
        Swipe the *obj* from center to bottom
        """
        obj.swipe.down(steps=steps)

    def drag(self,sx, sy, ex, ey, steps=100):
        """
        drag from (sx, sy) to (ex, ey) with steps
        """
        self.device.drag(sx, sy, ex, ey, steps)

    #Wait until the specific ui object appears or gone

    # wait until the ui object appears
    def wait_for_exists(self, timeout=0, *args, **attribute):
        """
        true means the object which has *attribute* exist
        false means the object does not exist
        in the given timeout
        """
        return self.device(**attribute).wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_gone(self, timeout=0, *args, **attribute):
        """
        true means the object which has *attribute* disappear
        false means the object exist
        in the given timeout
        """
        return self.device(**attribute).wait.gone(timeout=timeout)

    def wait_for_object_exists(self, obj, timeout=0):
        """
        true means the object exist
        false means the object does not exist
        in the given timeout
        """
        return obj.wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_object_gone(self, obj, timeout=0):
        """
        true means the object disappear
        false means the object exist
        in the given timeout
        """
        return obj.wait.gone(timeout=timeout)


    # Perform fling on the specific ui object(scrollable)
    def fling_forward_horizontally(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.horiz.forward()

    def fling_backward_horizontally(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.horiz.backward()

    def fling_forward_vertically(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.vert.forward()

    def fling_backward_vertically(self, obj):
        """
        return whether the object can be fling or not
        """
        return obj.fling.vert.backward()

    # Perform scroll on the specific ui object(scrollable)

    def scroll_to_beginning_vertically(self, steps=10, **attributes):
        """
        """
        return self.device(**attributes).scroll.vert.toBeginning(steps=steps)

    def scroll_to_end_vertically(self, steps=10, **attributes):
        """
        """
        return self.device(**attributes).scroll.vert.toEnd(steps=steps)

    def scroll_object_to_beginning_vertically(self, obj, steps=10):
        """
        """
        return obj.scroll.vert.toBeginning(steps=steps)

    def scroll_object_to_end_vertically(self, obj, steps=10):
        """
        """
        return obj.scroll.vert.toEnd(steps=steps)

    def scroll_forward_horizontally(self, obj, steps=10):
        """
        return whether the object can be scroll or not
        """
        return obj.scroll.horiz.forward(steps=steps)

    def scroll_backward_horizontally(self, obj, steps=10):
        """
        return whether the object can be scroll or not
        """
        return obj.scroll.horiz.backward(steps=steps)

    def scroll_to_horizontally(self, obj, *args,**attribute):
        """
        return whether the object can be scroll or not
        """
        return obj.scroll.horiz.to(**attribute)

    def scroll_forward_vertically(self, obj, steps=10):
        """
        return whether the object can be scroll or not
        """
        return obj.scroll.vert.forward(steps=steps)

    def scroll_backward_vertically(self, obj, steps=10):
        """
        return whether the object can be scroll or not
        """
        return obj.scroll.vert.backward(steps=steps)

    def scroll_to_vertically(self, obj, *args, **attribute):
        """
        return whether the object exists or not
        """
        return obj.scroll.vert.to(**attribute)

#Screen Actions of the device

    def screenshot(self, scale=None, quality=None):
        """
        Take a screenshot of device and log in the report with timestamp, scale for screenshot size and quality for screenshot quality
        default scale=1.0 quality=100
        """
        output_dir = BuiltIn().get_variable_value('${OUTPUTDIR}')
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
        screenshot_path = '%s%s%s.png' % (output_dir, os.sep, st)
        self.device.screenshot(screenshot_path, scale, quality)
        logger.info('\n<a href="%s">%s</a><br><img src="%s">' % (screenshot_path, st, screenshot_path), html=True)

#Watcher
#     def register_click_watcher(self, watcher_name, attributes, *condition_list):
#         """
#         The watcher click on the object which has the attributes when conditions match
#         """
#         print type(attributes)
#         watcher = self.device.watcher(watcher_name)
#         for condition in condition_list:
#             watcher.when(**condition)
#         watcher.click(**attributes)
#         self.device.watchers.run()
#         print 'register watcher:%s' % watcher_name
#         return

    def __unicode_to_dict(self, a_unicode):
        a_dict = dict()
        dict_item_count = a_unicode.count('=')
        for count in range(dict_item_count):
            equal_sign_position = a_unicode.find('=')
            comma_position = a_unicode.find(',')
            a_key = a_unicode[0:equal_sign_position]
            if comma_position == -1:
                a_value = a_unicode[equal_sign_position + 1:]
            else:
                a_value = a_unicode[equal_sign_position + 1:comma_position]
                a_unicode = a_unicode[comma_position + 1:]
            a_dict[a_key] = a_value
        return a_dict

    def register_click_watcher(self, watcher_name, attributes, *condition_list):
        """
        The watcher click on the object which has the *attributes* when conditions match
        """
        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.click(**self.__unicode_to_dict(attributes))
        self.device.watchers.run()

    def register_press_watcher(self, watcher_name, press_keys, *condition_list):
        """
        The watcher perform *press_keys* action sequentially when conditions match
        """
        def unicode_to_list(a_unicode):
            a_list = list()
            comma_count = a_unicode.count(',')
            for count in range(comma_count + 1):
                comma_position = a_unicode.find(',')
                if comma_position == -1:
                    a_list.append(str(a_unicode))
                else:
                    a_list.append(a_unicode[0:comma_position])
                    a_unicode = a_unicode[comma_position + 1:]
            return a_list

        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.press(*unicode_to_list(press_keys))
        self.device.watchers.run()

    def remove_watchers(self, watcher_name = None):
        """
        Remove watcher with *watcher_name* or remove all watchers
        """
        if watcher_name == None:
            self.device.watchers.remove()
        else:
            self.device.watchers.remove(watcher_name)

    def list_all_watchers(self):
        """
        return the watcher list
        """
        return self.device.watchers

#Selector

    def get_object(self, *args, **attribute):
        """
        Get the ui object with attribute *attribute*
        """
        return self.device(*args, **attribute)

    def get_count_of_object(self, obj):
        """
        Return the count of given *obj*
        """
        return len(obj)

    def get_info_of_object(self, obj, attribute=None):
        """
        return info dictionary of the *obj*
        The info example:
        {
         u'contentDescription': u'',
         u'checked': False,
         u'scrollable': True,
         u'text': u'',
         u'packageName': u'com.android.launcher',
         u'selected': False,
         u'enabled': True,
         u'bounds': 
                   {
                    u'top': 231,
                    u'left': 0,
                    u'right': 1080,
                    u'bottom': 1776
                   },
         u'className': u'android.view.View',
         u'focusable': False,
         u'focused': False,
         u'clickable': False,
         u'checkable': False,
         u'chileCount': 1,
         u'longClickable': False,
         u'visibleBounds':
                          {
                           u'top': 231,
                           u'left': 0,
                           u'right': 1080,
                           u'bottom': 1776
                          }
        }
        """
        if attribute:
            return obj.info.get(attribute)
        else:
            return obj.info

    def click_on(self, *args, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).click()

    def long_click_on(self, *args, **attribute):
        """
        click on the object with *attribute*
        """
        self.device(**attribute).long_click()

    def call(self, obj, method, *args, **attribute):
        func = getattr(obj, method)
        return func(**attribute)

    def set_text(self, input_text, *args, **attribute):
        """
        set *text* to the Component which has the *attribute* 
        """
        self.device(**attribute).set_text(input_text)

# Other feature

    def clear_text(self, *args, **attributes):
        """
        Clear text of the component  with *attributes*
        """
        while True:
            target = self.device(**attributes)
            text = target.info['text']
            target.clear_text()
            remain_text = target.info['text']
            if text == ''  or remain_text == text:
                break

    def open_notification(self):
        """
        open notification
        Built in support for Android 4.3 (API level 18)
        Using swipe action as a workaround for API level lower 18
        """
        sdk_version = self.device.info['sdkInt']
        if sdk_version < 18:
            height = self.device.info['displayHeight']
            self.device.swipe(1, 1, 1, height - 1, 1)
        else:
            self.device.open.notification()

    def open_quick_settings(self):
        """
        open quick settings
        Work for Android 4.3 (API level 18)
        """
        self.device.open.quick_settings()

    def sleep(self, time):
        """
        sleep(no action) for *time* (in millisecond)
        """
        target = 'wait for %s' % str(time)
        self.device(text=target).wait.exists(timeout=time)

    def install(self, apk_path):
        """
        Install apk to the device
        """
        self.adb.cmd('install "%s"' % apk_path)

    def uninstall(self, package_name):
        """
        Uninstall the APP with *package_name*
        """
        self.adb.cmd('uninstall %s' % package_name)

    def execute_adb_command(self, cmd):
        """
        Execute adb *cmd*
        """
        self.adb.cmd(cmd)

    def execute_adb_shell_command(self,cmd):
        """
        Execute adb shell *cmd*
        """
        self.adb.shell_cmd(cmd)

    def type(self, text):
        """
        Type *text* at current focused component
        """
        self.test_helper.send_set_text_cmd(text)

    def start_test_agent(self):
        """
        [Test Agent]
        Start Test Agent Service
        """
        cmd = 'am start edu.ntut.csie.sslab1321.testagent/edu.ntut.csie.sslab1321.testagent.DummyActivity'
        self.adb.shell_cmd(cmd)

    def stop_test_agent(self):
        """
        [Test Agent]
        Stop Test Agent Service
        """
        cmd = 'am broadcast -a testagent -e action STOP_TESTAGENT'
        self.adb.shell_cmd(cmd)

    def connect_to_wifi(self, ssid, password):
        """
        [Test Agent]
        Connect to *ssid* with *password*
        """
        cmd = 'adb shell am start edu.ntut.csie.sslab1321.testagent/edu.ntut.csie.sslab1321.testagent.DummyActivity'
        cmd = 'adb shell am broadcast -a testagent -e action CONNECT_TO_WIFI -e ssid WEP -e password 12345'
        cmd = 'am broadcast -a testagent -e action CONNECT_TO_WIFI -e ssid %s -e password %s' % (ssid, password)
        self.adb.shell_cmd(cmd)

    def clear_connected_wifi(self):
        """
        [Test Agent]
        Clear all existed Wi-Fi connection
        """
        cmd = 'am broadcast -a testagent -e action CLEAR_CONNECTED_WIFIS'
        self.adb.shell_cmd(cmd)

    def foo(self):
        pass
#         logger.info('\nGot arg %s %s' % (output_dir, st), also_console=True)
#         clm = CommandLineWriter()
        # output some messages on console
#         clm.message(' ')
#         clm.message(u'中文')
#         clm.message(u'2----------2')

    def test(self):
        pass

if __name__ == '__main__':
    print 'start'

    m = Mobile()

    print 'end'