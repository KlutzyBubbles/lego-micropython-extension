import pytest

from pybricks_ext.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)

class TestPort:

    def test_motor_ports(self):
        assert Port.A.value == 0
        assert Port.B.value == 1
        assert Port.C.value == 2
        assert Port.D.value == 3

    def test_sensor_ports(self):
        assert Port.S1.value == 4
        assert Port.S2.value == 5
        assert Port.S3.value == 6
        assert Port.S4.value == 7

class TestDirection:

    def test_directions(self):
        assert Direction.CLOCKWISE.value == 0
        assert Direction.COUNTERCLOCKWISE.value == 1

class TestStop:

    def test_stops(self):
        assert Stop.COAST.value == 0
        assert Stop.BRAKE.value == 1
        assert Stop.HOLD.value == 2

class TestColor:

    def test_colors(self):
        assert Color.BLACK.value == 0
        assert Color.BLUE.value == 1
        assert Color.GREEN.value == 2
        assert Color.YELLOW.value == 3
        assert Color.RED.value == 4
        assert Color.WHITE.value == 5
        assert Color.BROWN.value == 6
        assert Color.ORANGE.value == 7
        assert Color.PURPLE.value == 8

class TestButton:

    def test_brick_buttons(self):
        assert Button.DOWN.value == 'd'
        assert Button.LEFT.value == 'l'
        assert Button.RIGHT.value == 'r'
        assert Button.UP.value == 'u'
        assert Button.CENTER.value == 'c'

    def test_remote_buttons(self):
        assert Button.LEFT_DOWN.value == 'ld'
        assert Button.LEFT_UP.value == 'lu'
        assert Button.RIGHT_DOWN.value == 'rd'
        assert Button.RIGHT_UP.value == 'ru'
        assert Button.BEACON.value == 'b'

class TestAlign:

    def test_aligns(self):
        assert Align.BOTTOM_LEFT.value == 'bl'
        assert Align.BOTTOM.value == 'b'
        assert Align.BOTTOM_RIGHT.value == 'br'
        assert Align.LEFT.value == 'l'
        assert Align.CENTER.value == 'c'
        assert Align.RIGHT.value == 'r'
        assert Align.TOP_LEFT.value == 'tl'
        assert Align.TOP.value == 't'
        assert Align.TOP_RIGHT.value == 'tr'

class TestImageFile:

    def test_information_images(self):
        assert type(ImageFile.RIGHT.value) is str
        assert type(ImageFile.FORWARD.value) is str
        assert type(ImageFile.ACCEPT.value) is str
        assert type(ImageFile.QUESTION_MARK.value) is str
        assert type(ImageFile.STOP_1.value) is str
        assert type(ImageFile.LEFT.value) is str
        assert type(ImageFile.DECLINE.value) is str
        assert type(ImageFile.THUMBS_DOWN.value) is str
        assert type(ImageFile.BACKWARD.value) is str
        assert type(ImageFile.NO_GO.value) is str
        assert type(ImageFile.WARNING.value) is str
        assert type(ImageFile.STOP_2.value) is str
        assert type(ImageFile.THUMBS_UP.value) is str

    def test_lego_images(self):
        assert type(ImageFile.EV3.value) is str
        assert type(ImageFile.EV3_ICON.value) is str

    def test_object_images(self):
        assert type(ImageFile.TARGET.value) is str

    def test_eye_images(self):
        assert type(ImageFile.BOTTOM_RIGHT.value) is str
        assert type(ImageFile.BOTTOM_LEFT.value) is str
        assert type(ImageFile.EVIL.value) is str
        assert type(ImageFile.CRAZY_2.value) is str
        assert type(ImageFile.KNOCKED_OUT.value) is str
        assert type(ImageFile.PINCHED_RIGHT.value) is str
        assert type(ImageFile.WINKING.value) is str
        assert type(ImageFile.DIZZY.value) is str
        assert type(ImageFile.DOWN.value) is str
        assert type(ImageFile.TIRED_MIDDLE.value) is str
        assert type(ImageFile.MIDDLE_RIGHT.value) is str
        assert type(ImageFile.SLEEPING.value) is str
        assert type(ImageFile.MIDDLE_LEFT.value) is str
        assert type(ImageFile.TIRED_RIGHT.value) is str
        assert type(ImageFile.PINCHED_LEFT.value) is str
        assert type(ImageFile.PINCHED_MIDDLE.value) is str
        assert type(ImageFile.CRAZY_1.value) is str
        assert type(ImageFile.NEUTRAL.value) is str
        assert type(ImageFile.AWAKE.value) is str
        assert type(ImageFile.UP.value) is str
        assert type(ImageFile.TIRED_LEFT.value) is str
        assert type(ImageFile.ANGRY.value) is str

class TestSoundFile:

    def test_expression_sounds(self):
        assert type(SoundFile.SHOUTING.value) is str
        assert type(SoundFile.CHEERING.value) is str
        assert type(SoundFile.CRYING.value) is str
        assert type(SoundFile.OUCH.value) is str
        assert type(SoundFile.LAUGHING_2.value) is str
        assert type(SoundFile.SNEEZING.value) is str
        assert type(SoundFile.SMACK.value) is str
        assert type(SoundFile.BOING.value) is str
        assert type(SoundFile.BOO.value) is str
        assert type(SoundFile.UH_OH.value) is str
        assert type(SoundFile.SNORING.value) is str
        assert type(SoundFile.KUNG_FU.value) is str
        assert type(SoundFile.FANFARE.value) is str
        assert type(SoundFile.CRUNCHING.value) is str
        assert type(SoundFile.MAGIC_WAND.value) is str
        assert type(SoundFile.LAUGHING_1.value) is str

    def test_information_sounds(self):
        assert type(SoundFile.LEFT.value) is str
        assert type(SoundFile.BACKWARDS.value) is str
        assert type(SoundFile.RIGHT.value) is str
        assert type(SoundFile.OBJECT.value) is str
        assert type(SoundFile.COLOR.value) is str
        assert type(SoundFile.FLASHING.value) is str
        assert type(SoundFile.ERROR.value) is str
        assert type(SoundFile.ERROR_ALARM.value) is str
        assert type(SoundFile.DOWN.value) is str
        assert type(SoundFile.FORWARD.value) is str
        assert type(SoundFile.ACTIVATE.value) is str
        assert type(SoundFile.SEARCHING.value) is str
        assert type(SoundFile.TOUCH.value) is str
        assert type(SoundFile.UP.value) is str
        assert type(SoundFile.ANALYZE.value) is str
        assert type(SoundFile.STOP.value) is str
        assert type(SoundFile.DETECTED.value) is str
        assert type(SoundFile.TURN.value) is str
        assert type(SoundFile.START.value) is str

    def test_communication_sounds(self):
        assert type(SoundFile.MORNING.value) is str
        assert type(SoundFile.EV3.value) is str
        assert type(SoundFile.GO.value) is str
        assert type(SoundFile.GOOD_JOB.value) is str
        assert type(SoundFile.OKEY_DOKEY.value) is str
        assert type(SoundFile.GOOD.value) is str
        assert type(SoundFile.NO.value) is str
        assert type(SoundFile.THANK_YOU.value) is str
        assert type(SoundFile.YES.value) is str
        assert type(SoundFile.GAME_OVER.value) is str
        assert type(SoundFile.OKAY.value) is str
        assert type(SoundFile.SORRY.value) is str
        assert type(SoundFile.BRAVO.value) is str
        assert type(SoundFile.GOODBYE.value) is str
        assert type(SoundFile.HI.value) is str
        assert type(SoundFile.HELLO.value) is str
        assert type(SoundFile.MINDSTORMS.value) is str
        assert type(SoundFile.LEGO.value) is str
        assert type(SoundFile.FANTASTIC.value) is str

    def test_movements_sounds(self):
        assert type(SoundFile.SPEED_IDLE.value) is str
        assert type(SoundFile.SPEED_DOWN.value) is str
        assert type(SoundFile.SPEED_UP.value) is str

    def test_color_sounds(self):
        assert type(SoundFile.BROWN.value) is str
        assert type(SoundFile.GREEN.value) is str
        assert type(SoundFile.BLACK.value) is str
        assert type(SoundFile.WHITE.value) is str
        assert type(SoundFile.RED.value) is str
        assert type(SoundFile.BLUE.value) is str
        assert type(SoundFile.YELLOW.value) is str

    def test_mechanical_sounds(self):
        assert type(SoundFile.TICK_TACK.value) is str
        assert type(SoundFile.HORN_1.value) is str
        assert type(SoundFile.BACKING_ALERT.value) is str
        assert type(SoundFile.MOTOR_IDLE.value) is str
        assert type(SoundFile.AIR_RELEASE.value) is str
        assert type(SoundFile.AIRBRAKE.value) is str
        assert type(SoundFile.RATCHET.value) is str
        assert type(SoundFile.MOTOR_STOP.value) is str
        assert type(SoundFile.HORN_2.value) is str
        assert type(SoundFile.LASER.value) is str
        assert type(SoundFile.SONAR.value) is str
        assert type(SoundFile.MOTOR_START.value) is str

    def test_animal_sounds(self):
        assert type(SoundFile.INSECT_BUZZ_2.value) is str
        assert type(SoundFile.ELEPHANT_CALL.value) is str
        assert type(SoundFile.SNAKE_HISS.value) is str
        assert type(SoundFile.DOG_BARK_2.value) is str
        assert type(SoundFile.DOG_WHINE.value) is str
        assert type(SoundFile.INSECT_BUZZ_1.value) is str
        assert type(SoundFile.DOG_SNIFF.value) is str
        assert type(SoundFile.T_REX_ROAR.value) is str
        assert type(SoundFile.INSECT_CHIRP.value) is str
        assert type(SoundFile.DOG_GROWL.value) is str
        assert type(SoundFile.SNAKE_RATTLE.value) is str
        assert type(SoundFile.DOG_BARK_1.value) is str
        assert type(SoundFile.CAT_PURR.value) is str

    def test_number_sounds(self):
        assert type(SoundFile.ZERO.value) is str
        assert type(SoundFile.ONE.value) is str
        assert type(SoundFile.TWO.value) is str
        assert type(SoundFile.THREE.value) is str
        assert type(SoundFile.FOUR.value) is str
        assert type(SoundFile.FIVE.value) is str
        assert type(SoundFile.SIX.value) is str
        assert type(SoundFile.SEVEN.value) is str
        assert type(SoundFile.EIGHT.value) is str
        assert type(SoundFile.NINE.value) is str
        assert type(SoundFile.TEN.value) is str

    def test_expression_sounds(self):
        assert type(SoundFile.READY.value) is str
        assert type(SoundFile.CONFIRM.value) is str
        assert type(SoundFile.GENERAL_ALERT.value) is str
        assert type(SoundFile.CLICK.value) is str
        assert type(SoundFile.OVERPOWER.value) is str
