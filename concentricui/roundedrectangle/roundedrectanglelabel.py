""" Some notes go here """

all__ = ('RoundedRectangleLabel', )

from concentricui.roundedrectangle.concentricroundedrectangles import ConcentricRoundedRectangles
from concentricui.behaviours.concentriclabel import ConcentricLabel

class RoundedRectangleLabel(ConcentricRoundedRectangles, ConcentricLabel):

    def __init__(self, **kwargs):
        super(RoundedRectangleLabel, self).__init__(**kwargs)
