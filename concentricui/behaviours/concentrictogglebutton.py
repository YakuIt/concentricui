""" Some notes go here """

all__ = ('ConcentricToggleButton', )

from concentricui.behaviours.concentricbutton import ConcentricButton
from kivy.uix.togglebutton import ToggleButtonBehavior

class ConcentricToggleButton(ConcentricButton, ToggleButtonBehavior):

    def __init__(self, **kwargs):
        super(ConcentricButton, self).__init__(**kwargs)
