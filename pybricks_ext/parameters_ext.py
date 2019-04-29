from pybricks.parameters import Color
from enum import Enum

class ColorExt(Enum):
    """
    Extension class for Color with utility methods
    """

    BLACK = 1
    PURPLE = 9
    BLUE = 2
    GREEN = 3
    YELLOW = 4
    ORANGE = 8
    RED = 5
    WHITE = 6
    BROWN = 7

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
            Color.BLACK: 1,
            Color.BLUE: 2,
            Color.GREEN: 3,
            Color.YELLOW: 4,
            Color.RED: 5,
            Color.WHITE: 6,
            Color.BROWN: 7,
            Color.ORANGE: 8,
            Color.PURPLE: 9
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
            1: Color.BLACK,
            2: Color.BLUE,
            3: Color.GREEN,
            4: Color.YELLOW,
            5: Color.RED,
            6: Color.WHITE,
            7: Color.BROWN,
            8: Color.ORANGE,
            9: Color.PURPLE
        }
        return switch.get(number, d=None)

class DirectionExt(Enum):

    CLOCKWISE = 0
    ANTICLOCKWISE = 1

class PortExt(Enum):

    A = 65
    B = 66
    C = 67
    D = 68
    S1 = 49
    S2 = 50
    S3 = 51
    S4 = 52

class SoundFileExt(Enum):

    BRAVO = "/usr/share/sounds/ev3dev/communication/bravo.wav"
    LEGO = "/usr/share/sounds/ev3dev/communication/lego.wav"
    GENERAL_ALERT = "/usr/share/sounds/ev3dev/system/general_alert.wav"
    SONAR = "/usr/share/sounds/ev3dev/mechanical/sonar.wav"
    EIGHT = "/usr/share/sounds/ev3dev/numbers/eight.wav"
    CAT_PURR = "/usr/share/sounds/ev3dev/animals/cat_purr.wav"
    ANALYZE = "/usr/share/sounds/ev3dev/information/analyze.wav"
    UP = "/usr/share/sounds/ev3dev/information/up.wav"
    FLASHING = "/usr/share/sounds/ev3dev/information/flashing.wav"
    FOUR = "/usr/share/sounds/ev3dev/numbers/four.wav"
    MINDSTORMS = "/usr/share/sounds/ev3dev/communication/mindstorms.wav"
    DOG_GROWL = "/usr/share/sounds/ev3dev/animals/dog_growl.wav"
    FIVE = "/usr/share/sounds/ev3dev/numbers/five.wav"
    SEVEN = "/usr/share/sounds/ev3dev/numbers/seven.wav"
    GREEN = "/usr/share/sounds/ev3dev/colors/green.wav"
    SHOUTING = "/usr/share/sounds/ev3dev/expressions/shouting.wav"
    THANK_YOU = "/usr/share/sounds/ev3dev/communication/thank_you.wav"
    COLOR = "/usr/share/sounds/ev3dev/information/color.wav"
    EV3 = "/usr/share/sounds/ev3dev/communication/ev3.wav"
    OVERPOWER = "/usr/share/sounds/ev3dev/system/overpower.wav"
    SNAKE_HISS = "/usr/share/sounds/ev3dev/animals/snake_hiss.wav"
    TEN = "/usr/share/sounds/ev3dev/numbers/ten.wav"
    ERROR_ALARM = "/usr/share/sounds/ev3dev/information/error_alarm.wav"
    BLACK = "/usr/share/sounds/ev3dev/colors/black.wav"
    RED = "/usr/share/sounds/ev3dev/colors/red.wav"
    CLICK = "/usr/share/sounds/ev3dev/system/click.wav"
    GAME_OVER = "/usr/share/sounds/ev3dev/communication/game_over.wav"
    SPEED_IDLE = "/usr/share/sounds/ev3dev/movements/speed_idle.wav"
    WHITE = "/usr/share/sounds/ev3dev/colors/white.wav"
    OKEY_DOKEY = "/usr/share/sounds/ev3dev/communication/okey-dokey.wav"
    HI = "/usr/share/sounds/ev3dev/communication/hi.wav"
    BOING = "/usr/share/sounds/ev3dev/expressions/boing.wav"
    TOUCH = "/usr/share/sounds/ev3dev/information/touch.wav"
    MOTOR_STOP = "/usr/share/sounds/ev3dev/mechanical/motor_stop.wav"
    SIX = "/usr/share/sounds/ev3dev/numbers/six.wav"
    BLUE = "/usr/share/sounds/ev3dev/colors/blue.wav"
    DETECTED = "/usr/share/sounds/ev3dev/information/detected.wav"
    CRYING = "/usr/share/sounds/ev3dev/expressions/crying.wav"
    GOODBYE = "/usr/share/sounds/ev3dev/communication/goodbye.wav"
    OBJECT = "/usr/share/sounds/ev3dev/information/object.wav"
    RATCHET = "/usr/share/sounds/ev3dev/mechanical/ratchet.wav"
    SNORING = "/usr/share/sounds/ev3dev/expressions/snoring.wav"
    TURN = "/usr/share/sounds/ev3dev/information/turn.wav"
    RIGHT = "/usr/share/sounds/ev3dev/information/right.wav"
    SPEED_UP = "/usr/share/sounds/ev3dev/movements/speed_up.wav"
    AIRBRAKE = "/usr/share/sounds/ev3dev/mechanical/airbrake.wav"
    LASER = "/usr/share/sounds/ev3dev/mechanical/laser.wav"
    DOG_WHINE = "/usr/share/sounds/ev3dev/animals/dog_whine.wav"
    DOG_SNIFF = "/usr/share/sounds/ev3dev/animals/dog_sniff.wav"
    AIR_RELEASE = "/usr/share/sounds/ev3dev/mechanical/air_release.wav"
    UH_OH = "/usr/share/sounds/ev3dev/expressions/uh-oh.wav"
    YES = "/usr/share/sounds/ev3dev/communication/yes.wav"
    CRUNCHING = "/usr/share/sounds/ev3dev/expressions/crunching.wav"
    LAUGHING_1 = "/usr/share/sounds/ev3dev/expressions/laughing_1.wav"
    SEARCHING = "/usr/share/sounds/ev3dev/information/searching.wav"
    MORNING = "/usr/share/sounds/ev3dev/communication/morning.wav"
    LAUGHING_2 = "/usr/share/sounds/ev3dev/expressions/laughing_2.wav"
    START = "/usr/share/sounds/ev3dev/information/start.wav"
    ELEPHANT_CALL = "/usr/share/sounds/ev3dev/animals/elephant_call.wav"
    _BASE_PATH = "/usr/share/sounds/ev3dev/"
    OKAY = "/usr/share/sounds/ev3dev/communication/okay.wav"
    ACTIVATE = "/usr/share/sounds/ev3dev/information/activate.wav"
    FANFARE = "/usr/share/sounds/ev3dev/expressions/fanfare.wav"
    DOWN = "/usr/share/sounds/ev3dev/information/down.wav"
    INSECT_CHIRP = "/usr/share/sounds/ev3dev/animals/insect_chirp.wav"
    ERROR = "/usr/share/sounds/ev3dev/information/error.wav"
    FANTASTIC = "/usr/share/sounds/ev3dev/communication/fantastic.wav"
    BOO = "/usr/share/sounds/ev3dev/expressions/boo.wav"
    HELLO = "/usr/share/sounds/ev3dev/communication/hello.wav"
    YELLOW = "/usr/share/sounds/ev3dev/colors/yellow.wav"
    T_REX_ROAR = "/usr/share/sounds/ev3dev/animals/t-rex_roar.wav"
    INSECT_BUZZ_2 = "/usr/share/sounds/ev3dev/animals/insect_buzz_2.wav"
    INSECT_BUZZ_1 = "/usr/share/sounds/ev3dev/animals/insect_buzz_1.wav"
    SNAKE_RATTLE = "/usr/share/sounds/ev3dev/animals/snake_rattle.wav"
    KUNG_FU = "/usr/share/sounds/ev3dev/expressions/kung_fu.wav"
    GOOD = "/usr/share/sounds/ev3dev/communication/good.wav"
    SPEED_DOWN = "/usr/share/sounds/ev3dev/movements/speed_down.wav"
    STOP = "/usr/share/sounds/ev3dev/information/stop.wav"
    DOG_BARK_2 = "/usr/share/sounds/ev3dev/animals/dog_bark_2.wav"
    DOG_BARK_1 = "/usr/share/sounds/ev3dev/animals/dog_bark_1.wav"
    GOOD_JOB = "/usr/share/sounds/ev3dev/communication/good_job.wav"
    TICK_TACK = "/usr/share/sounds/ev3dev/mechanical/tick_tack.wav"
    MOTOR_START = "/usr/share/sounds/ev3dev/mechanical/motor_start.wav"
    MAGIC_WAND = "/usr/share/sounds/ev3dev/expressions/magic_wand.wav"
    HORN_1 = "/usr/share/sounds/ev3dev/mechanical/horn_1.wav"
    OUCH = "/usr/share/sounds/ev3dev/expressions/ouch.wav"
    GO = "/usr/share/sounds/ev3dev/communication/go.wav"
    HORN_2 = "/usr/share/sounds/ev3dev/mechanical/horn_2.wav"
    SMACK = "/usr/share/sounds/ev3dev/expressions/smack.wav"
    BROWN = "/usr/share/sounds/ev3dev/colors/brown.wav"
    CHEERING = "/usr/share/sounds/ev3dev/expressions/cheering.wav"
    NO = "/usr/share/sounds/ev3dev/communication/no.wav"
    ONE = "/usr/share/sounds/ev3dev/numbers/one.wav"
    TWO = "/usr/share/sounds/ev3dev/numbers/two.wav"
    THREE = "/usr/share/sounds/ev3dev/numbers/three.wav"
    ZERO = "/usr/share/sounds/ev3dev/numbers/zero.wav"
    MOTOR_IDLE = "/usr/share/sounds/ev3dev/mechanical/motor_idle.wav"
    NINE = "/usr/share/sounds/ev3dev/numbers/nine.wav"
    READY = "/usr/share/sounds/ev3dev/system/ready.wav"
    CONFIRM = "/usr/share/sounds/ev3dev/system/confirm.wav"
    BACKING_ALERT = "/usr/share/sounds/ev3dev/mechanical/backing_alert.wav"
    BACKWARDS = "/usr/share/sounds/ev3dev/information/backwards.wav"
    SORRY = "/usr/share/sounds/ev3dev/communication/sorry.wav"
    FORWARD = "/usr/share/sounds/ev3dev/information/forward.wav"
    LEFT = "/usr/share/sounds/ev3dev/information/left.wav"
    SNEEZING = "/usr/share/sounds/ev3dev/expressions/sneezing.wav"

class ImageFileExt(Enum):

    TIRED_MIDDLE = "/usr/share/images/ev3dev/mono/eyes/tired_middle.png"
    FORWARD = "/usr/share/images/ev3dev/mono/information/forward.png"
    TARGET = "/usr/share/images/ev3dev/mono/objects/target.png"
    MIDDLE_LEFT = "/usr/share/images/ev3dev/mono/eyes/middle_left.png"
    CRAZY_1 = "/usr/share/images/ev3dev/mono/eyes/crazy_1.png"
    LEFT = "/usr/share/images/ev3dev/mono/information/left.png"
    CRAZY_2 = "/usr/share/images/ev3dev/mono/eyes/crazy_2.png"
    MIDDLE_RIGHT = "/usr/share/images/ev3dev/mono/eyes/middle_right.png"
    AWAKE = "/usr/share/images/ev3dev/mono/eyes/awake.png"
    UP = "/usr/share/images/ev3dev/mono/eyes/up.png"
    PINCHED_RIGHT = "/usr/share/images/ev3dev/mono/eyes/pinched_right.png"
    RIGHT = "/usr/share/images/ev3dev/mono/information/right.png"
    BACKWARD = "/usr/share/images/ev3dev/mono/information/backward.png"
    ANGRY = "/usr/share/images/ev3dev/mono/eyes/angry.png"
    BOTTOM_LEFT = "/usr/share/images/ev3dev/mono/eyes/bottom_left.png"
    KNOCKED_OUT = "/usr/share/images/ev3dev/mono/eyes/knocked_out.png"
    EVIL = "/usr/share/images/ev3dev/mono/eyes/evil.png"
    DECLINE = "/usr/share/images/ev3dev/mono/information/decline.png"
    PINCHED_LEFT = "/usr/share/images/ev3dev/mono/eyes/pinched_left.png"
    TIRED_LEFT = "/usr/share/images/ev3dev/mono/eyes/tired_left.png"
    NO_GO = "/usr/share/images/ev3dev/mono/information/no_go.png"
    EV3 = "/usr/share/images/ev3dev/mono/lego/ev3.png"
    TIRED_RIGHT = "/usr/share/images/ev3dev/mono/eyes/tired_right.png"
    _BASE_PATH = "/usr/share/images/ev3dev/mono/"
    BOTTOM_RIGHT = "/usr/share/images/ev3dev/mono/eyes/bottom_right.png"
    THUMBS_DOWN = "/usr/share/images/ev3dev/mono/information/thumbs_down.png"
    NEUTRAL = "/usr/share/images/ev3dev/mono/eyes/neutral.png"
    PINCHED_MIDDLE = "/usr/share/images/ev3dev/mono/eyes/pinched_middle.png"
    SLEEPING = "/usr/share/images/ev3dev/mono/eyes/sleeping.png"
    STOP_2 = "/usr/share/images/ev3dev/mono/information/stop_2.png"
    STOP_1 = "/usr/share/images/ev3dev/mono/information/stop_1.png"
    QUESTION_MARK = "/usr/share/images/ev3dev/mono/information/question_mark.png"
    DIZZY = "/usr/share/images/ev3dev/mono/eyes/dizzy.png"
    WARNING = "/usr/share/images/ev3dev/mono/information/warning.png"
    EV3_ICON = "/usr/share/images/ev3dev/mono/lego/ev3_icon.png"
    ACCEPT = "/usr/share/images/ev3dev/mono/information/accept.png"
    WINKING = "/usr/share/images/ev3dev/mono/eyes/winking.png"
    THUMBS_UP = "/usr/share/images/ev3dev/mono/information/thumbs_up.png"
    DOWN = "/usr/share/images/ev3dev/mono/eyes/down.png"

class ButtonExt(Enum):

    UP = 256
    DOWN = 4
    LEFT = 16
    RIGHT = 64
    CENTER = 32
    LEFT_UP = 128
    LEFT_DOWN = 2
    RIGHT_UP = 512
    RIGHT_DOWN = 8
    BEACON = 256

class StopExt(Enum):

    COAST = 0
    BRAKE = 1
    HOLD = 2

class AlignExt(Enum):

    BOTTOM_LEFT = 1
    TOP_LEFT = 7
    TOP_RIGHT = 9
    TOP = 8
    BOTTOM = 2
    LEFT = 4
    BOTTOM_RIGHT = 3
    RIGHT = 6
    CENTER = 5