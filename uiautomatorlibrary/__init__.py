from Mobile import Mobile

class uiautomatorlibrary(Mobile):
    """
    robotframework-uiautomatorlibrary is an Android device testing library for Robot Framework.

    It uses uiautomator - Python wrapper for Android uiautomator tool (https://pypi.python.org/pypi/uiautomator/0.1.28) internally.

    *Before running tests*

    You can use `Set Serial` to specify which device to perform the test.

    *Identify UI object*

    If the UI object can be identified just by one selector, you can use keyword to manipulate the object directly.

    For example:

    | Swipe Left | description=Settings |                | # swipe the UI object left by description          |
    | Swipe Left | description=Settings | clickable=True | # swipe the UI object left by description and text |

    If the UI object is in other or UI object (other layout or something else), you can always get the object layer by layer.

    For example:

    | ${some_parent_object} | Get Object | className=android.widget.FrameLayout |
    | ${some_child_object}  | Get Child  | ${some_parent_object}                | text=ShownTextOnChildObject |

    *Selectors*

    If the keyword argument expects _**selectors_, the following parameters are supported. (more details https://github.com/xiaocong/uiautomator#selector):

    - text, textContains, textMatches, textStartsWith
    - className, classNameMatches
    - description, descriptionContains, descriptionMatches, descriptionStartsWith
    - checkable, checked, clickable, longClickable
    - scrollable, enabled,focusable, focused, selected
    - packageName, packageNameMatches
    - resourceId, resourceIdMatches
    - index, instance

    p.s. These parameters are case sensitive.

    *Input*

    The keyword Type allows you to type in languages other than English.

    You have to :

    1. Install MyIME.apk (in support folder) to device.

    2. Set MyIME as your input method editor in the setting.

    *Operations without UI*

    If you want to use keywords with *[Test Agent]* tag.

    You have to install TestAgent.apk (in support folder) to device.
    """
    ROBOT_LIBRARY_VERSION = '0.2'
    ROBOT_LIBRARY_DOC_FORMAT = 'ROBOT'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_EXIT_ON_FAILURE = True

    def __init__(self):
        """
        """
        Mobile.__init__(self)