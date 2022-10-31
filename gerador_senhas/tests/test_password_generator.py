import unittest
import re
from gerador_senhas.password_generator import *


class TestPasswordGenerator(unittest.TestCase):
    def test_make_one_special_char_multiple_ranges(self):  # se der erro em alguma vez inclua \ entre o -/
        regex = re.compile(r'^[ -/:-@\[-`{-~]$')
        for count in range(99):
            with self.subTest(count=count):
                self.assertRegex(make_one_special_char(), regex)

    def test_make_one_uppercase_letter_range_65_90(self):
        regex = re.compile(r'^[A-Z]$')
        for count in range(99):
            with self.subTest(count=count):
                self.assertRegex(make_one_uppercase_letter(), regex)

    def test_make_one_lowercase_letter_range_97_122(self):
        ord_range = list(range(97, 123))

        for count in range(99):
            with self.subTest(count=count):
                self.assertIn(ord(make_one_lowercase_letter()), ord_range)

    def test_make_one_number_range_48_57(self):
        ord_range = list(range(48, 58))

        for count in range(99):
            with self.subTest(count=count):
                self.assertIn(ord(make_one_number()), ord_range)

    def test_make_password_length(self):
        with self.assertRaises(ValueError):
            make_passowrd(length=3)

        with self.assertRaises(TypeError):
            make_passowrd(length='a')

        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertTrue(len(make_passowrd(length=count)) == count)

    def test_make_password_all_params_true(self):  # se der erro em alguma vez inclua \ entre o -/
        regex = re.compile(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -/:-@\[-`{-~]).+$'
        )
        self.assertRegex(make_passowrd(), regex)

    def test_make_password_all_params_false(self):  # se der erro em alguma vez inclua \ entre o -/
        with self.assertRaises(TypeError):
            make_passowrd(numbers=False, upper=False, lower=False, chars=False)

    def test_make_password_no_upper(self):
        regex = re.compile(r'^[^A-Z]+$')
        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertRegex(make_passowrd(length=count, upper=False), regex)

    def test_make_password_no_lower(self):
        regex = re.compile(r'[^a-z]+$')
        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertRegex(make_passowrd(length=count, lower=False), regex)

    def test_make_password_no_numbers(self):
        regex = re.compile(r'\D+$')
        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertRegex(make_passowrd(length=count, numbers=False), regex)

    def test_make_password_no_special_chars(self):
        regex = re.compile(r'^[^ -/:-@\[-`{-~]+$')
        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertRegex(make_passowrd(length=count, chars=False), regex)

    def test_make_password_sequence_allowed(self):
        regex = re.compile(r'^(?:[ -/:-@\[-`{-~][a-z][A-Z][0-9])+$')
        for count in range(4, 100):
            with self.subTest(count=count):
                self.assertNotRegex(make_passowrd(length=count), regex)


if __name__ == '__main__':
    unittest.main(verbosity=2)
