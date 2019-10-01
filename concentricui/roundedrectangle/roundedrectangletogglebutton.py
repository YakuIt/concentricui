""" Some notes go here """

all__ = ('RoundedRectangleToggleButton', )

from concentricui.roundedrectangle.concentricroundedrectangles import ConcentricRoundedRectangles
from concentricui.behaviours.concentrictogglebutton import ConcentricToggleButton

class RoundedRectangleToggleButton(ConcentricRoundedRectangles, ConcentricToggleButton):

    def __init__(self, **kwargs):
        super(RoundedRectangleToggleButton, self).__init__(**kwargs)