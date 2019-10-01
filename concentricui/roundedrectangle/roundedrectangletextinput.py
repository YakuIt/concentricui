""" Some notes go here """

all__ = ('RoundedRectangleTextInput', )

from concentricui.roundedrectangle.concentricroundedrectangles import ConcentricRoundedRectangles
from concentricui.behaviours.concentrictextinput import ConcentricTextInput

class RoundedRectangleTextInput(ConcentricTextInput, ConcentricRoundedRectangles):

    def __init__(self, **kwargs):
        super(RoundedRectangleTextInput, self).__init__(**kwargs)

        """ Wouldn't it be reasonable to make rounded rec text input be multiline?
            I can't imagine wanting multline oblong. rounded rec is a better shape for multiline """

        self.multiline = True