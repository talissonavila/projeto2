import unittest
from user.user_creation import user


class TestUser(unittest.TestCase):
    def test_make_user(self):
        """Testing user() Method."""
        with self.subTest('Testing user param as boolean'):
            user1 = True
            with self.assertRaises(TypeError):
                user(user1)

        with self.subTest('Testing user param as integer.'):
            user1 = -12
            with self.assertRaises(TypeError):
                user(user1)

        with self.subTest('Testing user param as float.'):
            user1 = 15.3
            with self.assertRaises(TypeError):
                user(user1)

        with self.subTest('Testing user param as string but length less than 4.'):
            user1 = 'sid'
            with self.assertRaises(ValueError):
                user(user1)


if __name__ == '__main__':
    unittest.main()
