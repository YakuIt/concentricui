""" Some notes go here """

all__ = ('OblongToggleButton', )

from concentricui.oblong.concentricoblongs import ConcentricOblongs
from concentricui.behaviours.concentrictogglebutton import ConcentricToggleButton

class OblongToggleButton(ConcentricOblongs, ConcentricToggleButton):

    def __init__(self, **kwargs):
        super(OblongToggleButton, self).__init__(**kwargs)