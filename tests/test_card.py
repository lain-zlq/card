import unittest

from easycard import bank_no_verify

class TestCard(unittest.TestCase):
    def test_verify_bank_no(self):
        card_no = '6235183145300749825'
        self.assertTrue(bank_no_verify(card_no))

if __name__ == '__main__':
    unittest.main()