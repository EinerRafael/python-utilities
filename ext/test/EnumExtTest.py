import unittest

from ext.src.EnumExt import EnumExt


class Roles(EnumExt):
    ROOT = 0
    ADMINISTRATOR = 1
    MODULE_ADMIN = 2
    VIEWER = 3
    GUEST = 4


class EnumExtTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_roles(self):

        # Get Names and Keys
        self.assertEqual(Roles.ADMINISTRATOR.value, 1)
        self.assertEqual(Roles.ADMINISTRATOR.name, "ADMINISTRATOR")

        _roles_names = Roles.names()

        # Count Enum
        self.assertCountEqual(_roles_names, 5)
        self.assertIn("GUEST", _roles_names)

        # Get By Methods
        self.assertIsNone(Roles.get_by_value(1000))
        self.assertFalse(Roles.exist_name("SUPER_USER"))


if __name__ == '__main__':
    unittest.main()
