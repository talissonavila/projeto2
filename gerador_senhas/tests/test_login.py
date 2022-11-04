import unittest
from login.login_creation import login
from gerador_senhas.password_generator import make_password


class TestLogin(unittest.TestCase):
    def test_make_login(self):
        """Testing login() Method."""
        passsword_1 = make_password(length=6, chars=False)
        make_password.return_value = passsword_1
        with self.subTest('Testing user as bool.'):
            user5 = True
            with self.assertRaises(TypeError):
                login(user5, passsword_1)

        with self.subTest('Testing login with user and password params being correct.'):
            user2 = 'doka'
            account = dict()
            account[user2] = passsword_1
            self.assertEqual(account, login('doka', passsword_1))

        with self.subTest('Testing if not equal login with different user'):
            user2 = 'doka'
            account = dict()
            account[user2] = passsword_1
            self.assertNotEqual(account, login('dokas', passsword_1))

        with self.subTest('Testing if not equal login with different password'):
            user2 = 'doka'
            account = dict()
            account[user2] = passsword_1
            self.assertNotEqual(account, login('doka', 'as#12s'))

        with self.subTest('Testing password less than 4.'):
            password = '123'
            user2 = 'doka'
            with self.assertRaises(ValueError):
                login(user2, password)


if __name__ == '__main__':
    unittest.main()
