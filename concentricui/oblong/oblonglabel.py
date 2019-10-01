""" Some notes go here """

all__ = ('OblongLabel', )

from concentricui.oblong.concentricoblongs import ConcentricOblongs
from concentricui.behaviours.concentriclabel import ConcentricLabel

class OblongLabel(ConcentricOblongs, ConcentricLabel):

    def __init__(self, **kwargs):
        super(OblongLabel, self).__init__(**kwargs)
