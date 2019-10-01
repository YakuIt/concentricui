""" Some notes go here """

all__ = ('CircleButton', )

from concentricui.circle.concentriccircles import ConcentricCircles
from concentricui.behaviours.concentricbutton import ConcentricButton

from kivy.properties import ListProperty

class CircleButton(ConcentricCircles, ConcentricButton):

    def __init__(self, **kwargs):
        super(CircleButton, self).__init__(**kwargs)

