from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass

    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    View = autoclass('android.view.View')
    Params = autoclass('android.view.WindowManager$LayoutParams')
    from android.runnable import run_on_ui_thread


class ScreenFlagSetter(object):

    def __init__(self):
        pass

    def set_screen_on_flag(self, *args):
        if platform == 'android':
            self.android_setflag()

    def clear_screen_on_flag(self, *args):
        if platform == 'android':
            self.android_clearflag()

    if platform == 'android':
        @run_on_ui_thread
        def android_setflag(self):
            PythonActivity.mActivity.getWindow().addFlags(Params.FLAG_KEEP_SCREEN_ON)

    if platform == 'android':
        @run_on_ui_thread
        def android_clearflag(self):
            PythonActivity.mActivity.getWindow().clearFlags(Params.FLAG_KEEP_SCREEN_ON)
