""" Some notes go here """

all__ = ('CircleLabel', )

from concentricui.circle.concentriccircles import ConcentricCircles
from concentricui.behaviours.concentriclabel import ConcentricLabel

class CircleLabel(ConcentricCircles, ConcentricLabel):

    def __init__(self, **kwargs):
        super(CircleLabel, self).__init__(**kwargs)

    def on_size(self, wid, size):

        print('dododoodododod!!!!!', self.master_colour)

