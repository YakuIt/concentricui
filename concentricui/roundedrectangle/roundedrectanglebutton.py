""" Some notes go here """

all__ = ('RoundedRectangleButton', )

from concentricui.roundedrectangle.concentricroundedrectangles import ConcentricRoundedRectangles
from concentricui.behaviours.concentricbutton import ConcentricButton

class RoundedRectangleButton(ConcentricRoundedRectangles, ConcentricButton):

    def __init__(self, **kwargs):
        super(RoundedRectangleButton, self).__init__(**kwargs)
