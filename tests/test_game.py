from game_test.game import Dice
class TestDice():
    def test_one_dice(self):
        dice = Dice()
        roll = dice.roll()
        assert type(roll) == int
        assert roll > 0
        assert roll < 7
