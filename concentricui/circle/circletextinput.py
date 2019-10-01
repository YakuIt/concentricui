""" Some notes go here """

all__ = ('CircleTextInput', )

from concentricui.circle.concentriccircles import ConcentricCircles
from concentricui.behaviours.concentrictextinput import ConcentricTextInput

class CircleTextInput(ConcentricTextInput, ConcentricCircles):

    def __init__(self, **kwargs):
        super(CircleTextInput, self).__init__(**kwargs)