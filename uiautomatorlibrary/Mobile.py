# -*- coding: utf-8 -*-
from robot.api import logger
from uiautomator import Device
import subprocess
import os
import time
import datetime
from robot.libraries.BuiltIn import BuiltIn

class TestHelper:
    def __init__(self, adb):
        self.adb = adb

    def __convert_to_unicode_by_text(self, text):
        """
        Transfer input string to UTF-8 format
        """
        # Remove the unicode tag. example: transfer u'abc' to string abc
        return repr(text)[2:-1]

    def send_set_text_cmd(self, text):
        """
        Setting the input string to MyIME
        1. adb shell "am broadcast -a myIME.intent.action.pass.string -e input abc"
        2. adb shell input keyevent KEYCODE_UNKNOWN
        """
        self.adb.shell_cmd('\"am broadcast -a myIME.intent.action.pass.string -e input \\\"\"%s\"\\\"\"' % TestHelper.__convert_to_unicode_by_text(self, text))
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
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    def shell_cmd(self, cmd):
        self.buf = []
        self.buf.append(self.prefix_cmd)
        self.buf.append('shell ')
        self.buf.append(cmd)
        cmd = ''.join(self.buf)
        return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

class Mobile():

    def __init__(self):
        self.set_serial(None)

    def set_serial(self, android_serial):
        """
        Specify given *android_serial* device to perform test.

        You do not have to specify the device when there is only one device connects to the computer.

        When you need to use multiple devices, do not use this keyword to switch between devices in test execution.

        Using different library name when importing this library according to http://robotframework.googlecode.com/hg/doc/userguide/RobotFrameworkUserGuide.html?r=2.8.5.

        | Setting | Value  | Value     | Value   | 
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

        | ${device_info}  | Get Device Info |   |                |
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
        Turn on the screen.
        """
        self.device.screen.on()

    def turn_off_screen(self):
        """
        Turn off the screen.
        """
        self.device.screen.off()

    """
    Press hard/soft key
    """

    def press_key(self, *keys):
        """
        Press *key* keycode.

        You can find all keycode in http://developer.android.com/reference/android/view/KeyEvent.html

        """
        #not tested
        self.device.press(*keys)

    def press_home(self):
        """
        Press home key.
        """
        self.device.press.home()

    def press_back(self):
        """
        Press back key.
        """
        self.device.press.back()

    def press_left(self):
        """
        Press left key.
        """
        self.device.pres.left()

    def press_right(self):
        """
        Press right key.
        """
        self.device.press.right()

    def press_up(self):
        """
        Press up key.
        """
        self.device.press.up()

    def press_down(self):
        """
        Press down key.
        """
        self.device.press.down()

    def press_center(self):
        """
        Press center key.
        """
        self.device.press.center()

    def press_menu(self):
        """
        Press menu key.
        """
        self.device.press.menu()

    def press_search(self):
        """
        Press search key.
        """
        self.device.press.search()

    def press_enter(self):
        """
        Press enter key.
        """
        self.device.press.enter()

    def press_delete(self):
        """
        Press delete key.
        """
        self.device.press.delete()

    def press_recent(self):
        """
        Press recent key.
        """
        self.device.press.recent()

    def press_volume_up(self):
        """
        Press volume up key.
        """
        self.device.press.volume_up()

    def press_volume_down(self):
        """
        Press volume down key.
        """
        self.device.press.volume_down()

    def press_camera(self):
        """
        Press camera key.
        """
        self.device.press.camera()

    def press_power(self):
        """
        Press power key.
        """
        self.device.press.power()

#Gesture interaction of the device

    def click_at_coordinates(self, x, y):
        """
        Click at (x,y) coordinates.
        """
        self.device.click(int(x), int(y))

    def swipe_by_coordinates(self, sx, sy, ex, ey, steps=10):
        """
        Swipe from (sx, sy) to (ex, ey) with *steps* .

        Example:
        | Swipe By Coordinates | 540 | 1340 | 940 | 1340 |     | # Swipe from (540, 1340) to (940, 100) with default steps 10 |
        | Swipe By Coordinates | 540 | 1340 | 940 | 1340 | 100 | # Swipe from (540, 1340) to (940, 100) with steps 100        |
        """
        self.device.swipe(sx, sy, ex, ey, steps)

# Swipe from the center of the ui object to its edge

    def swipe_left(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to left.

        Example:

        | Swipe Left | description=Home screen 3 |                           | # swipe the UI object left              |
        | Swipe Left | 5                         | description=Home screen 3 | # swipe the UI object left with steps=5 |

        See `introduction` for details about Identified UI object.
        """
        self.device(**selectors).swipe.left(steps=steps)

    def swipe_right(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to right

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.right(steps=steps)

    def swipe_top(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to top

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.up(steps=steps)

    def swipe_bottom(self, steps=10, *args, **selectors):
        """
        Swipe the UI object with *selectors* from center to bottom

        See `Swipe Left` for more details.
        """
        self.device(**selectors).swipe.down(steps=steps)

    def object_swipe_left(self, obj, steps=10):
        """
        Swipe the *obj* from center to left

        Example:

        | ${object}         | Get Object | description=Home screen 3 | # Get the UI object                     |
        | Object Swipe Left | ${object}  |                           | # Swipe the UI object left              |
        | Object Swipe Left | ${object}  | 5                         | # Swipe the UI object left with steps=5 |
        | Object Swipe Left | ${object}  | steps=5                   | # Swipe the UI object left with steps=5 |

        See `introduction` for details about identified UI object.
        """
        obj.swipe.left(steps=steps)

    def object_swipe_right(self, obj, steps=10):
        """
        Swipe the *obj* from center to right

        See `Object Swipe Left` for more details.
        """
        obj.swipe.right(steps=steps)

    def object_swipe_top(self, obj, steps=10):
        """
        Swipe the *obj* from center to top

        See `Object Swipe Left` for more details.
        """
        obj.swipe.up(steps=steps)

    def object_swipe_bottom(self, obj, steps=10):
        """
        Swipe the *obj* from center to bottom

        See `Object Swipe Left` for more details.
        """
        obj.swipe.down(steps=steps)

    def drag_by_coordinates(self,sx, sy, ex, ey, steps=10):
        """
        Drag from (sx, sy) to (ex, ey) with steps

        See `Swipe By Coordinates` also.
        """
        self.device.drag(sx, sy, ex, ey, steps)

    #Wait until the specific ui object appears or gone

    # wait until the ui object appears
    def wait_for_exists(self, timeout=0, *args, **selectors):
        """
        Wait for the object which has *selectors* within the given timeout.

        Return true if the object *appear* in the given timeout. Else return false.
        """
        return self.device(**selectors).wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_gone(self, timeout=0, *args, **selectors):
        """
        Wait for the object which has *selectors* within the given timeout.

        Return true if the object *disappear* in the given timeout. Else return false.
        """
        return self.device(**selectors).wait.gone(timeout=timeout)

    def wait_for_object_exists(self, obj, timeout=0):
        """
        Wait for the object: obj within the given timeout.

        Return true if the object *appear* in the given timeout. Else return false.
        """
        return obj.wait.exists(timeout=timeout)

    # wait until the ui object gone
    def wait_until_object_gone(self, obj, timeout=0):
        """
        Wait for the object: obj within the given timeout.

        Return true if the object *disappear* in the given timeout. Else return false.
        """
        return obj.wait.gone(timeout=timeout)


    # Perform fling on the specific ui object(scrollable)
    def fling_forward_horizontally(self, *args, **selectors):
        """
        Perform fling forward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.horiz.forward()

    def fling_backward_horizontally(self, *args, **selectors):
        """
        Perform fling backward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.horiz.backward()

    def fling_forward_vertically(self, *args, **selectors):
        """
        Perform fling forward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.vert.forward()

    def fling_backward_vertically(self, *args, **selectors):
        """
        Perform fling backward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be fling or not.
        """
        return self.device(**selectors).fling.vert.backward()

    # Perform scroll on the specific ui object(scrollable)

    # horizontal
    def scroll_to_beginning_horizontally(self, steps=10, *args,**selectors):
        """
        Scroll the object which has *selectors* attributes to *beginning* horizontally.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.toBeginning(steps=steps)

    def scroll_to_end_horizontally(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *end* horizontally.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.toEnd(steps=steps)

    def scroll_forward_horizontally(self, steps=10, *args, **selectors):
        """
        Perform scroll forward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.forward(steps=steps)

    def scroll_backward_horizontally(self, steps=10, *args, **selectors):
        """
        Perform scroll backward (horizontally)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.horiz.backward(steps=steps)

    def scroll_to_horizontally(self, obj, *args,**selectors):
        """
        Scroll(horizontally) on the object: obj to specific UI object which has *selectors* attributes appears.

        Return true if the UI object, else return false.

        See `Scroll To Vertically` for more details.
        """
        return obj.scroll.horiz.to(**selectors)

    # vertical
    def scroll_to_beginning_vertically(self, steps=10, *args,**selectors):
        """
        Scroll the object which has *selectors* attributes to *beginning* vertically.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.toBeginning(steps=steps)

    def scroll_to_end_vertically(self, steps=10, *args, **selectors):
        """
        Scroll the object which has *selectors* attributes to *end* vertically.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.toEnd(steps=steps)

    def scroll_forward_vertically(self, steps=10, *args, **selectors):
        """
        Perform scroll forward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        Example:
        | ${can_be_scroll} | Scroll Forward Vertically | className=android.widget.ListView       |                                   | # Scroll forward the UI object with class name |
        | ${can_be_scroll} | Scroll Forward Vertically | 100                                     | className=android.widget.ListView | # Scroll with steps |
        """
        return self.device(**selectors).scroll.vert.forward(steps=steps)

    def scroll_backward_vertically(self, steps=10, *args, **selectors):
        """
        Perform scroll backward (vertically)action on the object which has *selectors* attributes.

        Return whether the object can be Scroll or not.

        See `Scroll Forward Vertically` for more details.
        """
        return self.device(**selectors).scroll.vert.backward(steps=steps)

    def scroll_to_vertically(self, obj, *args,**selectors):
        """
        Scroll(vertically) on the object: obj to specific UI object which has *selectors* attributes appears.

        Return true if the UI object, else return false.

        Example:

        | ${list}        | Get Object           | className=android.widget.ListView |              | # Get the list object     |
        | ${is_web_view} | Scroll To Vertically | ${list}                           | text=WebView | # Scroll to text:WebView. |
        """
        return obj.scroll.vert.to(**selectors)

#Screen Actions of the device

    def get_screen_orientation(self):
        """
        Get the screen orientation.

        Possible result: natural, left, right, upsidedown

        See for more details: https://github.com/xiaocong/uiautomator#screen-actions-of-the-device
        """
        return self.device.orientation

    def set_screen_orientation(self, orientation):
        """
        Set the screen orientation.

        Input *orientation* : natural or n, left or l, right or r, upsidedown (support android version above 4.3)

        The keyword will unfreeze the screen rotation first.

        See for more details: https://github.com/xiaocong/uiautomator#screen-actions-of-the-device

        Example:

        | Set Screen Orientation | n       | # Set orientation to natural |
        | Set Screen Orientation | natural | # Do the same thing          |
        """
        self.device.orientation = orientation

    def freeze_screen_rotation(self):
        """
        Freeze the screen auto rotation
        """
        self.device.freeze_rotation()

    def unfreeze_screen_rotation(self):
        """
        Un-Freeze the screen auto rotation
        """
        self.device.freeze_rotation(False)

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

    def register_click_watcher(self, watcher_name, selectors, *condition_list):
        """
        The watcher click on the object which has the *selectors* when conditions match.
        """
        watcher = self.device.watcher(watcher_name)
        for condition in condition_list:
            watcher.when(**self.__unicode_to_dict(condition))
        watcher.click(**self.__unicode_to_dict(selectors))
        self.device.watchers.run()

    def register_press_watcher(self, watcher_name, press_keys, *condition_list):
        """
        The watcher perform *press_keys* action sequentially when conditions match.
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
        Remove watcher with *watcher_name* or remove all watchers.
        """
        if watcher_name == None:
            self.device.watchers.remove()
        else:
            self.device.watchers.remove(watcher_name)

    def list_all_watchers(self):
        """
        Return the watcher list.
        """
        return self.device.watchers

#Selector

    def get_object(self, *args, **selectors):
        """
        Get the UI object with selectors *selectors*

        See `introduction` for details about identified UI object.
        
        Example:
        | ${main_layer} | Get Object | className=android.widget.FrameLayout | index=0 | # Get main layer which class name is FrameLayout |
        """
        return self.device(*args, **selectors)

    def get_child(self, object, *args, **selectors):
        """
        Get the child or grandchild UI object from the *object* with *selectors*
        Example:
        | ${root_layout}   | Get Object | className=android.widget.FrameLayout |
        | ${child_layout}  | Get Child  | ${root_layout}                       | className=LinearLayout |
        """
        return object.child(*args, **selectors)

    def get_sibling(self, object, *args, **selectors):
        """
        Get the sibling or child of sibling UI object from the *object* with *selectors*
        Example:
        | ${root_layout}     | Get Object   | className=android.widget.FrameLayout |
        | ${sibling_layout}  | Get Sibling  | ${root_layout}                       | className=LinearLayout |
        """
        return object.sibling(*args, **selectors) 

    def get_count(self, *args, **selectors):
        """
        Return the count of UI object with *selectors*

        Example:

        | ${count}              | Get Count           | text=Accessibility    | # Get the count of UI object text=Accessibility |
        | ${accessibility_text} | Get Object          | text=Accessibility    | # These two keywords combination                |
        | ${count}              | Get Count Of Object | ${accessibility_text} | # do the same thing.                            |

        """
        obj = self.get_object(**selectors)
        return self.get_count_of_object(obj)

#     def get_count_of_object(self, obj):
#         """
#         Return the count of given UI object
# 
#         See `Get Count` for more details.
#         """
#         return len(obj)

    def get_info_of_object(self, obj, selector=None):
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
        if selector:
            return obj.info.get(selector)
        else:
            return obj.info

    def click(self, *args, **selectors):
        """
        Click on the UI object with *selectors*

        | Click | text=Accessibility | className=android.widget.Button | # Click the object with class name and text |
        """
        self.device(**selectors).click()

    def click_on_object(self, object):
        """
        Click on the UI object which is gained by `Get Object`.

        Example:
        | ${button_ok}    | text=OK      | className=android.widget.Button |
        | Click on Object | ${button_ok} |
        """
        return object.click()

    def long_click(self, *args, **selectors):
        """
        Long click on the UI object with *selectors*

        See `Click` for more details.
        """
        self.device(**selectors).long_click()

    def call(self, obj, method, *args, **selectors):
        """
        This keyword can use object method from original python uiautomator

        See more details from https://github.com/xiaocong/uiautomator

        Example:

        | ${accessibility_text} | Get Object            | text=Accessibility | # Get the UI object                        |
        | Call                  | ${accessibility_text} | click              | # Call the method of the UI object 'click' |
        """
        func = getattr(obj, method)
        return func(**selectors)

    def set_text(self, input_text, *args, **selectors):
        """
        Set *input_text* to the UI object with *selectors* 
        """
        self.device(**selectors).set_text(input_text)

    def set_object_text(self, input_text, object):
        """
        Set *input_text* the *object* which could be selected by *Get Object* or *Get Child*
        """
        object.set_text(input_text)

# Other feature

    def clear_text(self, *args, **selectors):
        """
        Clear text of the UI object  with *selectors*
        """
        while True:
            target = self.device(**selectors)
            text = target.info['text']
            target.clear_text()
            remain_text = target.info['text']
            if text == ''  or remain_text == text:
                break

    def open_notification(self):
        """
        Open notification

        Built in support for Android 4.3 (API level 18)

        Using swipe action as a workaround for API level lower than 18

        """
        sdk_version = self.device.info['sdkInt']
        if sdk_version < 18:
            height = self.device.info['displayHeight']
            self.device.swipe(1, 1, 1, height - 1, 1)
        else:
            self.device.open.notification()

    def open_quick_settings(self):
        """
        Open quick settings

        Work for Android 4.3 above (API level 18)

        """
        self.device.open.quick_settings()

    def sleep(self, time):
        """
        Sleep(no action) for *time* (in millisecond)
        """
        target = 'wait for %s' % str(time)
        self.device(text=target).wait.exists(timeout=time)

    def install(self, apk_path):
        """
        Install apk to the device.

        Example:

        | Install | ${CURDIR}${/}com.hmh.api_4.0.apk | # Given the absolute path to the apk file |
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
        return self.adb.cmd(cmd)

    def execute_adb_shell_command(self,cmd):
        """
        Execute adb shell *cmd*
        """
        return self.adb.shell_cmd(cmd)

    def type(self, input_text):
        """
        [IME]

        Type *text* at current focused UI object
        """
        self.test_helper.send_set_text_cmd(input_text)

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

    def connect_to_wifi(self, ssid, password=None):
        """
        [Test Agent]

        Connect to *ssid* with *password*
        """
        cmd = 'am broadcast -a testagent -e action CONNECT_TO_WIFI -e ssid %s -e password %s' % (ssid, password)
        self.adb.shell_cmd(cmd)

    def clear_connected_wifi(self):
        """
        [Test Agent]

        Clear all existed Wi-Fi connection
        """
        cmd = 'am broadcast -a testagent -e action CLEAR_CONNECTED_WIFIS'
        self.adb.shell_cmd(cmd)