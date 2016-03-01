import unittest


class TestThatStuffWorks(unittest.TestCase):
    def test_this_thing_is_on(self):
        self.assertEquals(1, 1)


# class TestVendingMachine( unittest.TestCase):
#     def give_change(self, amount):
#         return[10, 5, 2]

    def test_return_change( self) :
        coins=  self.give_change(0)
        self.assertEqual(coins,  [])
