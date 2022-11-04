import unittest
import re
from gerador_senhas.password_generator import *


class TestPasswordGenerator(unittest.TestCase):
    """Tests of PasswordGenerator class."""
    def test_make_one_special_char_multiple_ranges(self):  # se der erro em alguma vez inclua \ entre o -/
        """Testing cases of make one special char."""
        with self.subTest("Testing if creates a special char."):
            regex = re.compile(r'^[ -/:-@\[-`{-~]$')
            for count in range(99):
                self.assertRegex(make_one_special_char(), regex)

    def test_make_one_uppercase_letter_range_65_90(self):
        """Testing make_one_uppercase_letter() method."""
        with self.subTest('Testing if creates a uppercase letter.'):
            regex = re.compile(r'^[A-Z]$')
            for count in range(99):
                self.assertRegex(make_one_uppercase_letter(), regex)

    def test_make_one_lowercase_letter_range_97_122(self):
        """Testing make_one_lowercase_letter() method."""
        with self.subTest('Testing if creates a lowercase letter.'):
            ord_range = list(range(97, 123))
            for count in range(99):
                self.assertIn(ord(make_one_lowercase_letter()), ord_range)

    def test_make_one_number_range_48_57(self):
        """Testing make_one_number() method."""
        with self.subTest('Testing if creates a numeric char: 0 to 9.'):
            ord_range = list(range(48, 58))
            for count in range(99):
                self.assertIn(ord(make_one_number()), ord_range)

    def test_make_password_length(self):
        """Testing make_password_length() method."""
        with self.subTest('Testing if returns a Value Error with param length lass than 4.'):
            with self.assertRaises(ValueError):
                make_password(length=3)

        with self.subTest('Testing if returns a Type Error with string as param.'):
            with self.assertRaises(TypeError):
                make_password(length='a')

        with self.subTest('Testing if returns a Type Error with float as param.'):
            with self.assertRaises(TypeError):
                make_password(length=8.1)

        with self.subTest('Testing if creates passwords in accepteded cases.'):
            for count in range(4, 100):
                self.assertTrue(len(make_password(length=count)) == count)

        with self.subTest('Testing password creation with all params being True.'):
            regex = re.compile(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -/:-@\[-`{-~]).+$'
            )
            self.assertRegex(make_password(), regex)

        with self.subTest('Testing if returns a Type Error when password creation with all params being False.'):
            with self.assertRaises(TypeError):
                make_password(numbers=False, upper=False, lower=False, chars=False)

        with self.subTest("Testing if creates passwords without chars in uppercase."):
            regex = re.compile(r'^[^A-Z]+$')
            for count in range(4, 100):
                self.assertRegex(make_password(length=count, upper=False), regex)

        with self.subTest('Testing if creates passwords without chars in lowercase.'):
            regex = re.compile(r'[^a-z]+$')
            for count in range(4, 100):
                self.assertRegex(make_password(length=count, lower=False), regex)

        with self.subTest('Testing if creates passwords without chars numerics.'):
            regex = re.compile(r'\D+$')
            for count in range(4, 100):
                self.assertRegex(make_password(length=count, numbers=False), regex)

        with self.subTest('Testing if creates passwords without special chars.'):
            regex = re.compile(r'^[^ -/:-@\[-`{-~]+$')
            for count in range(4, 100):
                self.assertRegex(make_password(length=count, chars=False), regex)

        with self.subTest('Testing if creates passwords with correct sequence.'):
            regex = re.compile(r'^(?:[ -/:-@\[-`{-~][a-z][A-Z][0-9])+$')
            for count in range(4, 100):
                self.assertNotRegex(make_password(length=count), regex)


if __name__ == '__main__':
    unittest.main(verbosity=2)
