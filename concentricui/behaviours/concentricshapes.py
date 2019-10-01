""" Some notes go here """

all__ = ('ConcentricShapes',)

from itertools import zip_longest

from kivy.graphics import Color
from kivy.properties import BooleanProperty, NumericProperty, ListProperty, ReferenceListProperty, AliasProperty, \
    OptionProperty

from concentricui.colourscheme.colourwidget import ColourWidget


class ConcentricShapes(ColourWidget):
    trim = OptionProperty(True, options=(True, False, 'state', 'focus', ('state', 'focus')))

    show_trim = BooleanProperty(False)

    allow_concentric = BooleanProperty(True)

    outer_alpha_store = NumericProperty(allownone=True)

    def on_show_trim(self, wid, show_trim):

        print('?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>', show_trim)

        if not self.colour_instruction_list:
            print('rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
            return
        if self.trim:
            if show_trim:
                self.colour_instruction_list[0].a = self.outer_alpha_store
                self.outer_alpha_store = None
            else:
                self.outer_alpha_store = self.colour_instruction_list[0].a
                self.colour_instruction_list[0].a = 0
        else:
            print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')

    """ The most lovely thing about circles is that their width == height
        and even that doesn't do their infinite simplicity justice """

    def get_diameter(self):
        """ This occurs when you want to get the diameter """
        return min(self.height, self.width)

    def set_diameter(self, value):
        """ I'm not too sure what would happen if the diameter was set..
            but i suppose that it would change the size
            meaning that the widget would only take up the size of the circle itself.
            To be seen. """
        self.size = value, value

    diameter = AliasProperty(get_diameter, set_diameter, bind=['width', 'height'])

    shape_list = ListProperty()
    shape_count = NumericProperty()
    shape_size_hint_list = ListProperty([0.5, 0.7, 1])
    shape_colour_list = ListProperty()
    shape_allow_collision_list = ListProperty()
    colour_instruction_list = ListProperty()
    # master_colour = ListProperty()

    #  perhaps i just want to import certain behaviours from concentric shapes, but i dont want to draw an actual shape
    draw_shape_toggle = False

    font_ratio = NumericProperty(0.7)

    def get_shape_dictionary(self):
        """ This occurs when you want to get the shape dictionary """

        #  fixme implement some test for the length of each list
        shape_dictionary_list = [
            {'shape_size_hint': shape_size_hint,
             'shape_colour': shape_colour,
             'shape_allow_collision': shape_allow_collision}
            for shape_size_hint, shape_colour, shape_allow_collision
            in zip_longest(self.shape_size_hint_list, self.shape_colour_list, self.shape_allow_collision_list)
        ]

        sorted_by_size_hint = list(reversed(sorted(shape_dictionary_list, key=lambda k: k['shape_size_hint'])))

        return sorted_by_size_hint

    def set_shape_dictionary(self, value):
        """ This occurs when you want to set the shape dictionary """

        sorted_by_size_hint = list(reversed(sorted(value, key=lambda k: k['shape_size_hint'])))

        self.shape_size_hint_list = [x['shape_size_hint'] for x in sorted_by_size_hint]
        self.shape_colour_list = [x['shape_colour'] for x in sorted_by_size_hint]
        self.shape_allow_collision_list = [x['shape_allow_collision'] for x in sorted_by_size_hint]

    shape_dictionary = AliasProperty(get_shape_dictionary, set_shape_dictionary,
                                     bind=['shape_size_hint_list', 'shape_colour_list'])

    def __init__(self, **kwargs):

        # if 'anchor_x' in kwargs:
        #     kwargs.pop('anchor_x')
        # if 'left' in kwargs:
        #     kwargs.pop('left')
        # if 'anchor_y' in kwargs:
        #     kwargs.pop('anchor_y')
        # if 'top' in kwargs:
        #     kwargs.pop('top')

        super(ConcentricShapes, self).__init__(**kwargs)

        if 'shape_dictionary' in kwargs:
            shape_dictionary = kwargs.pop('shape_dictionary')
            self.shape_dictionary = shape_dictionary
        # else:
        #     self.set_secondary_colours()

        if not self.shape_size_hint_list:
            self.shape_size_hint_list = [1, ]

        """ this will hopefully facilitate setting the master colour to a string,
            declaring a colour attribute from the active colour scheme """
        # try: string_master_colour = ''.join(self.master_colour)
        # except: string_master_colour = None
        # if not string_master_colour:
        #     string_master_colour = 'foreground_colour'

        # print('maaaaybe', string_master_colour)

        # #  do it here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        if self.shape_colour_list:
            pass
        # elif string_master_colour:
        #     pass
        # self.master_colour = getattr(self, string_master_colour)
        # elif not self.master_colour:
        #     self.master_colour = self.foreground_colour
        #
        # print('!!!!!!!', string_master_colour, self.master_colour)

        # self.set_secondary_colours()

        self.draw_shapes()
        self.bind(pos=self.update_shape_list_pos, size=self.update_shape_list_size,
                  master_colour=self.set_secondary_colours)

        # if self.master_colour and self.use_master_colour not in ('foreground_colour', 'background_colour', 'text_colour', 'trim_colour'):
        #     if self.__class__.__name__ == 'ScreenChangeSpinner':
        #         print('kkkkkkkkkkkkkkkkkkkkkk', 'self.master_colour', self.master_colour, 'self.use_master_colour', self.use_master_colour)
        #     self.set_secondary_colours()

        # if self.trim is True:

    def draw_shapes(self):

        if not self.draw_shape_toggle:
            return

        if not self.shape_dictionary:
            return

        self.colour_instruction_list = []

        with self.canvas.before:
            shape_dictionary = self.shape_dictionary if self.allow_concentric else [self.shape_dictionary[0]]
            for dictionary in shape_dictionary:
                shape_colour = dictionary['shape_colour']
                if not shape_colour:
                    #  placeholder color
                    shape_colour = (1, 1, 1, 1)
                colour_instruction = Color(*shape_colour)
                self.colour_instruction_list.append(colour_instruction)
                shape = self.draw_shape(**dictionary)
                self.shape_list.append(shape)

    def draw_shape(self, **kwargs):
        raise Exception("Hey! This class is not meant to be used directly and this method is meant to be overwritten!")

    def update_shape_list_pos(self, *args):

        for shape in self.shape_list:
            #  fixme aww i dont get to use an AliasProperty
            #  i believe it may be impossible, as Elipsis doesn't have a center x, center y, etc..
            #  come to think of it that's the very reason that i'm adding it
            pass
            shape.set_center(self.center)

    def update_shape_list_size(self, *args):
        for shape, size_hint in zip(self.shape_list, self.shape_size_hint_list):
            pass
            shape.set_size(self.size, size_hint)
            shape.set_center(self.center)

        self.update_shape_list_pos()

    def get_inner_shape_width(self):

        if not self.shape_list:
            return None

        return self.shape_list[-1].size[0]

    def set_inner_shape_width(self, value):

        if not self.shape_list:
            return None

        self.shape_list[-1].size[0] = value

    def get_inner_shape_height(self):

        if not self.shape_list:
            return None

        return self.shape_list[-1].size[1]

    def set_inner_shape_height(self, value):

        if not self.shape_list:
            return None

        self.shape_list[-1].size[1] = value

    def get_inner_shape_x(self):

        if not self.shape_list:
            return None

        return self.shape_list[-1].pos[0]

    def set_inner_shape_x(self, value):

        if not self.shape_list:
            return None

        self.shape_list[-1].pos[0] = value

    def get_inner_shape_y(self):

        if not self.shape_list:
            return None

        return self.shape_list[-1].pos[1]

    def set_inner_shape_y(self, value):

        if not self.shape_list:
            return None

        self.shape_list[-1].pos[1] = value

    def get_inner_shape_right(self):

        if not self.shape_list:
            return None

        return self.inner_x + self.inner_width

    def set_inner_shape_right(self, value):

        if not self.shape_list:
            return None

        self.inner_x = value - self.inner_width

    def get_inner_shape_top(self):

        if not self.shape_list:
            return None

        return self.inner_y + self.inner_height

    def set_inner_shape_top(self, value):

        if not self.shape_list:
            return None

        self.inner_y = value - self.inner_height

    inner_width = AliasProperty(get_inner_shape_width, set_inner_shape_width, bind=['size', 'shape_size_hint_list'])
    inner_height = AliasProperty(get_inner_shape_height, set_inner_shape_height, bind=['size', 'shape_size_hint_list'])
    inner_x = AliasProperty(get_inner_shape_x, set_inner_shape_x, bind=['size', 'pos', 'shape_size_hint_list'])
    inner_y = AliasProperty(get_inner_shape_y, set_inner_shape_y, bind=['size', 'pos', 'shape_size_hint_list'])
    inner_right = AliasProperty(get_inner_shape_right, set_inner_shape_right, bind=['inner_x', 'inner_width'])
    inner_top = AliasProperty(get_inner_shape_top, set_inner_shape_top, bind=['inner_y', 'inner_height'])

    inner_size = ReferenceListProperty(inner_width, inner_height)
    inner_pos = ReferenceListProperty(inner_x, inner_y)

    # def to_inner(self, x, y, relative=True):
    #     '''Transform parent coordinates to local coordinates. See
    #     :mod:`~kivy.uix.relativelayout` for details on the coordinate systems.
    #
    #     :Parameters:
    #         `relative`: bool, defaults to False
    #             Change to True if you want to translate coordinates to
    #             relative widget coordinates.
    #     '''
    #     if relative:
    #         return (x - self.inner_x, y - self.inner_y)
    #     return (x, y)

    def get_inner_x_at_y(self, y, both_coordinates=False):

        if not self.draw_shape_toggle:
            return self.x

        _, local_y = self.shape_list[-1].to_inner_center(0, y)

        x_at_y = self.shape_list[-1].get_inner_x_at_y(local_y)

        if not both_coordinates:
            return x_at_y
        else:
            if x_at_y:
                return -x_at_y, x_at_y
            else:
                return None, None

    def get_inner_y_at_x(self, x, both_coordinates=False):

        if not self.draw_shape_toggle:
            return self.y

        local_x, _ = self.shape_list[-1].to_inner_center(x, 0)

        y_at_x = self.shape_list[-1].get_inner_y_at_x(local_x)

        if not both_coordinates:
            return y_at_x
        else:
            if y_at_x:
                return -y_at_x, y_at_x
            else:
                return None, None

    def get_inner_pos_at_pos(self, pos, both_coordinates=False):
        raise Exception('not yet implemented. need to think about this one')

    def get_inner_width_at_y(self, y):

        if not self.draw_shape_toggle:
            return self.width

        min_x, max_x = self.get_inner_x_at_y(y, both_coordinates=True)

        if not min_x or not max_x:
            return None
        return max_x - min_x

    def get_inner_height_at_x(self, x):

        if not self.draw_shape_toggle:
            return self.height

        min_y, max_y = self.get_inner_y_at_x(x, both_coordinates=True)

        if not min_y or not max_y:
            return None
        return max_y - min_y

    def get_inner_size_at_pos(self, pos):

        if not self.draw_shape_toggle:
            return self.size

        x, y = pos

        width = self.get_inner_width_at_y(y)
        height = self.get_inner_height_at_x(x)

        return width, height

    def collide_point(self, x, y):
        '''

        Overwritten to actually reflect the shape!

        '''

        if not self.draw_shape_toggle:
            return super(ConcentricShapes, self).collide_point(x, y)

        local_x, local_y = self.shape_list[-1].to_inner_center(x, y)

        inner_x, inner_right = self.get_inner_x_at_y(y, both_coordinates=True)
        inner_top, inner_y = self.get_inner_y_at_x(x, both_coordinates=True)

        if not all((inner_x, inner_right, inner_y, inner_top)):
            return False

        return inner_x <= local_x <= inner_right and inner_top <= local_y <= inner_y

    """ COLOURS """

    # master_colour = ListProperty()

    @staticmethod
    def set_colour_by_size_hint(colour, size_hint, min_size_hint):
        # size_hint_remainder = 1 - size_hint
        # if not size_hint_remainder:
        #     size_hint_remainder = 1

        original_alpha = colour[3] if len(colour) > 3 else None

        colour_scalar = (size_hint - min_size_hint)

        uncapped_colour_list = [x + colour_scalar for x in colour]
        max_colour_value = max(uncapped_colour_list)
        if max_colour_value > 1:
            capped_colour_list = [x / max_colour_value for x in uncapped_colour_list]
            # capped_colour_list = [x if x < 1 else 1 for x in uncapped_colour_list]

            if original_alpha is not None:
                capped_colour_list[3] = original_alpha

            return capped_colour_list

        else:
            return uncapped_colour_list

    def set_secondary_colours(self, *args):

        print(
            'set_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_coloursset_secondary_colours')

        if not self.master_colour and self.shape_colour_list:
            self.master_colour = self.shape_colour_list[0]

        if self.master_colour and self.shape_list:

            shape_dictionary = self.shape_dictionary
            min_size_hint = min(self.shape_size_hint_list)
            for shape in shape_dictionary:
                base_colour = self.master_colour
                # if i:
                colour_size_hint = shape['shape_size_hint']
                # else:
                #     colour_size_hint = 1
                auto_colour = self.set_colour_by_size_hint(base_colour, colour_size_hint, min_size_hint)

                print('***************', self, auto_colour, colour_size_hint, min_size_hint)

                shape['shape_colour'] = auto_colour

            self.shape_dictionary = shape_dictionary

            self.get_shape_dictionary()

            if self.needs_text_colour:
                #  not my favourite bit of code, but as colour property will fill in as [1, 1, 1, 1], what else can i do
                self.text_colour = shape_dictionary[0]['shape_colour']
            if self.needs_trim_colour:
                self.trim_colour = shape_dictionary[0]['shape_colour']

        # for shape, colour in zip(self.shape_list, self.shape_colour_list):
        #     shape.update_colour(colour)

        # for colour_instruction, colour in zip(self.colour_instruction_list, self.shape_colour_list):
        #     colour_instruction.rgba = colour

        return

    # def get_master_colour(self):
    #     print('this is super good hahah')
    #     super(self, ConcentricShapes).get_master_colour()
    #
    #     self.set_secondary_colours()

    def on_shape_colour_list(self, wid, shape_colour_list):
        if self.colour_instruction_list:
            for instruction, colour in zip(self.colour_instruction_list, shape_colour_list):
                instruction.rgba = colour
            if not self.show_trim and self.allow_concentric:
                self.outer_alpha_store = instruction.a
                self.colour_instruction_list[0].a = 0
            # self.colour_instruction_list[0].a = 1 if self.show_trim else 0

    # def on_master_colour(self, wid=None, master_colour=None):
    #     if master_colour:
    #         #self.set_secondary_colours(master_colour)
    #         if self.shape_list:
    #             self.set_secondary_colours(master_colour)
    #
    # def on_shape_colour_list(self, wid, colour_list):
    #     if self.colour_instruction_list:
    #         for colour, instruction in zip(colour_list, self.colour_instruction_list):
    #             if colour and instruction:
    #                 instruction.rgba = colour

    def set_colours_from_widget(self, widget):
        print('****', self.__class__.__name__)
        super(ConcentricShapes, self).set_colours_from_widget(widget)
        # self.master_colour = self.foreground_colour
        # self.shape_colour_list[0] = self.trim_colour

    #
    # def set_colour_scheme(self):
    #     #  super will set master colour to foreground, and get background, trim and text colours
    #     super(ConcentricShapes, self).set_colour_scheme()
    #
    #     self.shape_colour_list[-1] = self.trim_colour

    def do_colour_update(self, *args):
        super(ConcentricShapes, self).do_colour_update(*args)
        print('please' * 100)
        self.set_secondary_colours()

    def get_inner_colour(self):

        if not self.shape_colour_list:
            return None

        return self.shape_colour_list[0]

    def set_inner_colour(self, value):

        if not self.shape_colour_list:
            return None

        self.shape_colour_list[0] = value
        self.set_secondary_colours()

    inner_colour = AliasProperty(get_inner_colour, set_inner_colour, bind=['shape_colour_list'])

    def get_outer_colour(self, *args):

        if not self.shape_colour_list:
            return None

        if self.trim:
            return self.trim_colour
        else:
            return self.shape_colour_list[0]

        # print(self, self.trim, self.show_trim, '*****'*60)
        #
        # if not self.shape_colour_list:
        #     return None
        #
        # # if self.show_trim:
        # #     outer_colour = self.trim_colour
        # # else:
        # #     outer_colour = (0, 0, 0, 0)
        #
        # if self.trim and self.show_trim:
        #     """ this wants the trim badly """
        #     print('not so sure about this one', self.trim_colour)
        #     outer_colour = self.trim_colour
        #
        # elif self.trim and not self.show_trim:
        #     """ this wants the trim, but trim is denied to it. hence nothing shows """
        #     print('eegehhehehehhehhheh', self)
        #     outer_colour = (0, 0, 0, 0)
        #
        # elif not self.trim and self.show_trim:
        #     """ this is a weird one. it doesnt want the trim, but it's told to have it.
        #         i think it should just be ignored """
        #     #raise Exception("this shouldnt really happen? or if it does try to implement what you want")
        #     print('oh yeah this occurs!', self.shape_colour_list[-1])
        #     outer_colour = self.trim_colour
        #
        #
        # if not self.trim and not self.show_trim:
        #     """ this just doesnt care about or want trim """
        #     print('this would make sense', self.shape_colour_list[-1])
        #     outer_colour = self.shape_colour_list[0]
        #     outer_colour = (0, 0, 0, 0)
        #
        # if self.colour_instruction_list and outer_colour:
        #     self.colour_instruction_list[0].rgba = outer_colour

        return outer_colour

    def set_outer_colour(self, value):

        if not self.shape_colour_list:
            return None

        self.shape_colour_list[0] = value
        self.set_secondary_colours()

    outer_colour = AliasProperty(get_outer_colour, set_outer_colour,
                                 bind=['shape_colour_list', 'colour_instruction_list', 'trim'])


hex_colwormap = {
    'aliceblue': '#f0f8ff',
    'antiquewhite': '#faebd7',
    'aqua': '#00ffff',
    'aquamarine': '#7fffd4',
    'azure': '#f0ffff',
    'beige': '#f5f5dc',
    'bisque': '#ffe4c4',
    'black': '#000000',
    'blanchedalmond': '#ffebcd',
    'blue': '#0000ff',
    'blueviolet': '#8a2be2',
    'brown': '#a52a2a',
    'burlywood': '#deb887',
    'cadetblue': '#5f9ea0',
    'chartreuse': '#7fff00',
    'chocolate': '#d2691e',
    'coral': '#ff7f50',
    'cornflowerblue': '#6495ed',
    'cornsilk': '#fff8dc',
    'crimson': '#dc143c',
    'cyan': '#00ffff',
    'darkblue': '#00008b',
    'darkcyan': '#008b8b',
    'darkgoldenrod': '#b8860b',
    'darkgray': '#a9a9a9',
    'darkgrey': '#a9a9a9',
    'darkgreen': '#006400',
    'darkkhaki': '#bdb76b',
    'darkmagenta': '#8b008b',
    'darkolivegreen': '#556b2f',
    'darkorange': '#ff8c00',
    'darkorchid': '#9932cc',
    'darkred': '#8b0000',
    'darksalmon': '#e9967a',
    'darkseagreen': '#8fbc8f',
    'darkslateblue': '#483d8b',
    'darkslategray': '#2f4f4f',
    'darkslategrey': '#2f4f4f',
    'darkturquoise': '#00ced1',
    'darkviolet': '#9400d3',
    'deeppink': '#ff1493',
    'deepskyblue': '#00bfff',
    'dimgray': '#696969',
    'dimgrey': '#696969',
    'dodgerblue': '#1e90ff',
    'firebrick': '#b22222',
    'floralwhite': '#fffaf0',
    'forestgreen': '#228b22',
    'fuchsia': '#ff00ff',
    'gainsboro': '#dcdcdc',
    'ghostwhite': '#f8f8ff',
    'gold': '#ffd700',
    'goldenrod': '#daa520',
    'gray': '#808080',
    'grey': '#808080',
    'green': '#008000',
    'greenyellow': '#adff2f',
    'honeydew': '#f0fff0',
    'hotpink': '#ff69b4',
    'indianred': '#cd5c5c',
    'indigo': '#4b0082',
    'ivory': '#fffff0',
    'khaki': '#f0e68c',
    'lavender': '#e6e6fa',
    'lavenderblush': '#fff0f5',
    'lawngreen': '#7cfc00',
    'lemonchiffon': '#fffacd',
    'lightblue': '#add8e6',
    'lightcoral': '#f08080',
    'lightcyan': '#e0ffff',
    'lightgoldenrodyellow': '#fafad2',
    'lightgreen': '#90ee90',
    'lightgray': '#d3d3d3',
    'lightgrey': '#d3d3d3',
    'lightpink': '#ffb6c1',
    'lightsalmon': '#ffa07a',
    'lightseagreen': '#20b2aa',
    'lightskyblue': '#87cefa',
    'lightslategray': '#778899',
    'lightslategrey': '#778899',
    'lightsteelblue': '#b0c4de',
    'lightyellow': '#ffffe0',
    'lime': '#00ff00',
    'limegreen': '#32cd32',
    'linen': '#faf0e6',
    'magenta': '#ff00ff',
    'maroon': '#800000',
    'mediumaquamarine': '#66cdaa',
    'mediumblue': '#0000cd',
    'mediumorchid': '#ba55d3',
    'mediumpurple': '#9370db',
    'mediumseagreen': '#3cb371',
    'mediumslateblue': '#7b68ee',
    'mediumspringgreen': '#00fa9a',
    'mediumturquoise': '#48d1cc',
    'mediumvioletred': '#c71585',
    'midnightblue': '#191970',
    'mintcream': '#f5fffa',
    'mistyrose': '#ffe4e1',
    'moccasin': '#ffe4b5',
    'navajowhite': '#ffdead',
    'navy': '#000080',
    'oldlace': '#fdf5e6',
    'olive': '#808000',
    'olivedrab': '#6b8e23',
    'orange': '#ffa500',
    'orangered': '#ff4500',
    'orchid': '#da70d6',
    'palegoldenrod': '#eee8aa',
    'palegreen': '#98fb98',
    'paleturquoise': '#afeeee',
    'palevioletred': '#db7093',
    'papayawhip': '#ffefd5',
    'peachpuff': '#ffdab9',
    'peru': '#cd853f',
    'pink': '#ffc0cb',
    'plum': '#dda0dd',
    'powderblue': '#b0e0e6',
    'purple': '#800080',
    'red': '#ff0000',
    'rosybrown': '#bc8f8f',
    'royalblue': '#4169e1',
    'saddlebrown': '#8b4513',
    'salmon': '#fa8072',
    'sandybrown': '#f4a460',
    'seagreen': '#2e8b57',
    'seashell': '#fff5ee',
    'sienna': '#a0522d',
    'silver': '#c0c0c0',
    'skyblue': '#87ceeb',
    'slateblue': '#6a5acd',
    'slategray': '#708090',
    'slategrey': '#708090',
    'snow': '#fffafa',
    'springgreen': '#00ff7f',
    'steelblue': '#4682b4',
    'tan': '#d2b48c',
    'teal': '#008080',
    'thistle': '#d8bfd8',
    'tomato': '#ff6347',
    'turquoise': '#40e0d0',
    'violet': '#ee82ee',
    'wheat': '#f5deb3',
    'white': '#ffffff',
    'whitesmoke': '#f5f5f5',
    'yellow': '#ffff00',
    'yellowgreen': '#9acd32',
}
