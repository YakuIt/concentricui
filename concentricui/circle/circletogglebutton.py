""" Some notes go here """

all__ = ('CircleToggleButton', )

from concentricui.circle.concentriccircles import ConcentricCircles
from concentricui.behaviours.concentrictogglebutton import ConcentricToggleButton

class CircleToggleButton(ConcentricCircles, ConcentricToggleButton):

    def __init__(self, **kwargs):
        super(CircleToggleButton, self).__init__(**kwargs)