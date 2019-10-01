""" Some notes go here """

all__ = ('ConcentricToggleButton',)

from kivy.uix.togglebutton import ToggleButtonBehavior

from concentricui.behaviours.concentricbutton import ConcentricButton


class ConcentricToggleButton(ConcentricButton, ToggleButtonBehavior):

    def __init__(self, **kwargs):
        super(ConcentricButton, self).__init__(**kwargs)
