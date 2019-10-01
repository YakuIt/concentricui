

from kivy.properties import BooleanProperty, NumericProperty, ReferenceListProperty

from concentricui.behaviours.concentricfontscaling import ConcentricFontScaling

from kivy.uix.label import Label

from concentricui.colourscheme.colourwidget import ColourProperties

class ConcentricLabel(Label, ConcentricFontScaling):

    scale_text = BooleanProperty(True)
    inner_width, inner_height = NumericProperty(), NumericProperty()
    inner_size = ReferenceListProperty(inner_width, inner_height)

    def update(self, *args):

        print('self.text_colour!!!!!!!!', self, self.text_colour)

        self.texture_update()

    def __init__(self, **kwargs):
        super(ConcentricLabel, self).__init__(**kwargs)

        self.color = self.text_colour
        self.bind(text_colour=self.set_colour)

    def set_colour(self, wid, colour):
        print('belblelbelbele')
        self.color = self.text_colour