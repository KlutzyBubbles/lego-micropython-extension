from pybricks.parameters import Color

class ColorExt():

    '''
    Compares two colors to verify that they are equal

    Only one of the color parameters can be a set of Colors.
    If both are sets of Colors, the color_b will be changed to None

    If an invalid color is provided (int, float) then None will be used

    color_a - Color a to use for comparison (Color, int, float, list, tuple, dict)
    color_b - Color b to use for comparison (Color, int, float, list, tuple, dict)

    return  - Whether or not the colors are equal or the color set contains the alternate color
    '''
    @staticmethod
    def compare(color_a, color_b):
        if isinstance(color_a, (list, tuple, dict)):
            if not isinstance(color_b, Color):
                color_b = ColorExt.from_number(color_b)
            return color_b in color_a
        elif isinstance(color_b, (list, tuple, dict)):
            if not isinstance(color_a, Color):
                color_a = ColorExt.from_number(color_a)
            return color_a in color_b
        else:
            if not isinstance(color_a, Color):
                color_a = ColorExt.from_number(color_a)
            if not isinstance(color_b, Color):
                color_b = ColorExt.from_number(color_b)
            return color_a == color_b

    '''
    Converts a Color to its number representation.

    Will return 0 (None) if the color is None or invalid

    None: 0
    Color.BLACK: 1
    Color.BLUE: 2
    Color.GREEN: 3
    Color.YELLOW: 4
    Color.RED: 5
    Color.WHITE: 6
    Color.BROWN: 7

    color   - Color to convert (from pybricks.parameters)

    return  - Number representation for the Color
    '''
    @staticmethod
    def to_number(color):
        if not isinstance(color, Color) or color is None:
            return 0
        switch = {
            Color.BLACK: 1,
            Color.BLUE: 2,
            Color.GREEN: 3,
            Color.YELLOW: 4,
            Color.RED: 5,
            Color.WHITE: 6,
            Color.BROWN: 7
        }
        return switch.get(color, d=0)

    '''
    Converts a number to its Color representation.

    Will return None if the number is 0 or invalid

    None: 0
    Color.BLACK: 1
    Color.BLUE: 2
    Color.GREEN: 3
    Color.YELLOW: 4
    Color.RED: 5
    Color.WHITE: 6
    Color.BROWN: 7

    number  - Number to convert (int, float)

    return  - Color representation for the number
    '''
    @staticmethod
    def from_number(number):
        if not isinstance(number, (int, float)) or number == 0:
            return None
        switch = {
            1: Color.BLACK,
            2: Color.BLUE,
            3: Color.GREEN,
            4: Color.YELLOW,
            5: Color.RED,
            6: Color.WHITE,
            7: Color.BROWN
        }
        return switch.get(number, d=None)