""" Some notes go here """

all__ = ('RoundedRectangleDropdown', )

from concentricui.roundedrectangle.concentricroundedrectangles import ConcentricRoundedRectangles

from kivy.uix.dropdown import DropDown

class RoundedRectangleDropdown(ConcentricRoundedRectangles, DropDown):

    def __init__(self, **kwargs):
        super(RoundedRectangleDropdown, self).__init__(**kwargs)
