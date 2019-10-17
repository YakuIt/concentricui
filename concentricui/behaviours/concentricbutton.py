""" Some notes go here """

all__ = ('ConcentricButton',)

from kivy.uix.button import ButtonBehavior

from concentricui.behaviours.concentriclabel import ConcentricLabel


class ConcentricButton(ButtonBehavior, ConcentricLabel):

    # def set_trim(self, wid, state):
    #
    #     asdfsadf
    #
    #     if self.state == 'down':
    #         self.show_trim = True
    #         print('self.show_trim = True')
    #     else:
    #         self.show_trim = False
    #         print('self.state = False')
    # #
    # # def on_touch_down(self, touch):
    # #     if self.collide_point(*touch.pos):
    # #         print('okokokok', self.state)
    #
    # def on_press(self, *args):
    #     print('onponpnopnopnop', self.state)
    #
    # def on_release(self, *args):
    #     print('rororororopornr', self.state)

    def on_state(self, *args):

        if self.state == 'down':
            self.show_trim = True
        else:
            self.show_trim = False

        # super(ConcentricButton, self).on_state(*args)

    def __init__(self, **kwargs):

        super(ConcentricButton, self).__init__(**kwargs)

        self.show_trim = False

        self.background_color = None
        self.background_normal = None
        self.background_down = None
        self.background_disabled_normal = None
        self.background_disabled_down = None

        # self.bind(state=self.set_trim)
