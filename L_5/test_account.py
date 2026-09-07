import unittest

from account import *


class TestAccount(unittest.TestCase):
    def test_strip_space(self):
        self.assertEqual(clean_name(" sVeta "), "Sveta")

    def test_capitalize(self):
        self.assertEqual(clean_name("sveta"), "Sveta")

    def test_username_from_first_last(self):
        self.assertEqual(make_username("Sveta", "Sveta"), "sveta_sveta")

    def test_valid_email(self):
        self.assertTrue(is_valid_email("sveta123@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("sveta.sdfg.rt"))
        self.assertFalse(is_valid_email("sveta@sdfg"))

    def test_valid_email_second(self):
        self.assertTrue(is_valid_email_second("sveta123@gmail.com"))

    def test_invalid_email_second(self):
        self.assertFalse(is_valid_email_second("sveta123@gmai.c"))

    def test_invalid_email_without_at_second(self):
        self.assertFalse(is_valid_email_second("sveta123gmial.com"))

    def test_invalid_email_without_domain_second(self):
        self.assertFalse(is_valid_email_second("sveta123@.com"))

    def test_invalid_email_without_username_second(self):
        self.assertFalse(is_valid_email_second("@gmail.com"))
    
    def test_invalid_email_without_dot_second(self):
        self.assertFalse(is_valid_email_second("sveta123gmialcom"))

class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.user = {
            "name": "Sveta",
            "email": "sveta123@gmail.com",
            "role": ["user"],
            "password": "password123",
        }

    def test_profile_has_name(self):
        self.assertEqual(self.user["name"],"Sveta")

    def test_valid_email(self):
        self.assertTrue(is_valid_email_second(self.user["email"]))

    def test_add_role(self):
        self.user["role"].append("admin")
        self.assertIn("admin", self.user["role"])
        self.assertEqual(len(self.user["role"]),2)

    def test_check_length_role(self):
        self.assertEqual(len(self.user["role"]),1)

class TestGetInitials(unittest.TestCase):
    def test_get_normal_initials(self):
        self.assertEqual(initials("sveta svetlaya"), "S.S.")

    def test_str_empty_with_raise(self):
        with self.assertRaises(ValueError):
            initials("  ")

    


    
    


if __name__ == "__main__":
    unittest.main()
