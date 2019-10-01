""" Some notes go here """

all__ = ('ConcentricShapes', )

from kivy.graphics import Color

from concentricui.circle.circle import Circle
from concentricui.behaviours.concentricshapes import ConcentricShapes

class ConcentricCircles(ConcentricShapes):

    draw_shape_toggle = True

    def draw_shape(self, shape_size_hint, shape_colour, **kwargs):
        """ overwrite this function for circle, oblong, rounded rectangle """

        # fixme for now i shall include the circle's draw shape definition
        #Color(*shape_colour)
        #d = shape_size_hint * self.diameter
        #  fixme could diameter somehow be a VariableListProperty one day?

        shape = Circle()
        #shape = Circle(center=self.center, size=(d, d))
        return shape