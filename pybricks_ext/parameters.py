import pybricks.parameters as params

class ColorUtils():
    """
    Extension class for Color with utility methods
    """
    
    @staticmethod
    def compare(color_a, color_b):
        """Compares two colors to verify that they are equal

        Only one of the color parameters can be a set of Colors.
        If both are sets of Colors, the color_b will be changed to None

        If an invalid color is provided (int, float) then None will be used

        :param color_a: Color a to use for comparison
        :type color_a: Color, int, float, list, tuple, dict
        :param color_b: Color b to use for comparison
        :type color_b: Color, int, float, list, tuple, dict
        :return: Whether or not the colors are equal or the color set contains the alternate color
        :rtype: bool
        """
        if isinstance(color_a, (list, tuple, dict)):
            if not isinstance(color_b, Color):
                color_b = ColorUtils.from_number(color_b)
            return color_b in color_a
        elif isinstance(color_b, (list, tuple, dict)):
            if not isinstance(color_a, Color):
                color_a = ColorUtils.from_number(color_a)
            return color_a in color_b
        else:
            if not isinstance(color_a, Color):
                color_a = ColorUtils.from_number(color_a)
            if not isinstance(color_b, Color):
                color_b = ColorUtils.from_number(color_b)
            return color_a == color_b

    @staticmethod
    def to_number(color):
        """Converts a Color to its number representation.

        Will return 0 (None) if the color is None or invalid

        None: 0
        Color.BLACK: 1
        Color.BLUE: 2
        Color.GREEN: 3
        Color.YELLOW: 4
        Color.RED: 5
        Color.WHITE: 6
        Color.BROWN: 7

        :param color: Color to convert
        :type color: Color
        :return: Number representation for the Color
        :rtype: int
        """
        if not isinstance(color, Color) or color is None:
            return 0
        switch = {
            params.Color.BLACK: 1,
            params.Color.BLUE: 2,
            params.Color.GREEN: 3,
            params.Color.YELLOW: 4,
            params.Color.RED: 5,
            params.Color.WHITE: 6,
            params.Color.BROWN: 7,
            params.Color.ORANGE: 8,
            params.Color.PURPLE: 9
        }
        return switch.get(color, d=0)

    @staticmethod
    def from_number(number):
        """Converts a number to its Color representation.

        Will return None if the number is 0 or invalid

        None: 0
        Color.BLACK: 1
        Color.BLUE: 2
        Color.GREEN: 3
        Color.YELLOW: 4
        Color.RED: 5
        Color.WHITE: 6
        Color.BROWN: 7

        :param number: Number to convert
        :type number: int
        :return: Color representation for the number
        :rtype: Color
        """
        if not isinstance(number, (int, float)) or number == 0:
            return None
        switch = {
            1: params.Color.BLACK,
            2: params.Color.BLUE,
            3: params.Color.GREEN,
            4: params.Color.YELLOW,
            5: params.Color.RED,
            6: params.Color.WHITE,
            7: params.Color.BROWN,
            8: params.Color.ORANGE,
            9: params.Color.PURPLE
        }
        return switch.get(number, d=None)
