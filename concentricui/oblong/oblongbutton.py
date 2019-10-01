""" Some notes go here """

all__ = ('OblongButton', )

from concentricui.oblong.concentricoblongs import ConcentricOblongs
from concentricui.behaviours.concentricbutton import ConcentricButton

class OblongButton(ConcentricOblongs, ConcentricButton):

    def __init__(self, **kwargs):
        super(OblongButton, self).__init__(**kwargs)
