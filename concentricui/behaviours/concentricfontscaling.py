from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty, AliasProperty
from kivy.uix.widget import Widget


class ConcentricFontScaling(Widget):
    font_size_hint = NumericProperty()
    inner_width, inner_height = NumericProperty(), NumericProperty()
    inner_size = ReferenceListProperty(inner_width, inner_height)

    def __init__(self, **kwargs):
        super(ConcentricFontScaling, self).__init__(**kwargs)

        if self.font_size_hint:
            self.bind(size=Clock.schedule_once(self.set_font_size_from_hint, -1),
                      font_size_hint=Clock.schedule_once(self.set_font_size_from_hint, -1))
            # Clock.schedule_once(self.set_font_size_from_hint, 1)
        else:
            self.bind(size=Clock.schedule_once(self.set_font_size, -1))
            # Clock.schedule_once(self.set_font_size, 1)

        self.bind(text=self.initially_set_font_size)

    def initially_set_font_size(self, wid, text):

        print('did ity intially. did this work??')

        if not text:
            return

        if self.font_size_hint:
            Clock.schedule_once(self.set_font_size_from_hint)
        else:
            Clock.schedule_once(self.set_font_size)

        self.unbind(text=self.initially_set_font_size)

    def update(self, *args):
        raise Exception('This is set when subclassed!')

    def get_texture_size(self):
        texture_size = self._label.content_size
        if any(texture_size):
            return texture_size
        else:
            return False

    def set_texture_size(self, value):
        raise Exception('certainly not yet implemented')

    texture_size = AliasProperty(get_texture_size, set_texture_size)

    def set_font_size_from_hint(self, *args):
        self.font_size = self.inner_height * self.font_size_hint
        self.update()

    def set_font_size(self, *args):

        if not self.get_texture_size():
            return

        self.font_size = self.height / 2

        self.update()

        height_at_texture_start = self.get_inner_height_at_x(self.center_x - self.texture_size[0] / 2)

        width_at_texture_start = self.get_inner_width_at_y(self.center_y - self.texture_size[1] / 2)

        if not height_at_texture_start:
            height_at_texture_start = self.inner_height
        if not width_at_texture_start:
            width_at_texture_start = self.inner_width

        width_scale = width_at_texture_start / self.texture_size[0]

        height_scale = height_at_texture_start / self.texture_size[1]

        scale = min((width_scale, height_scale))

        self.font_size *= scale

        self.update()
