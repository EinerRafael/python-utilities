import os
import unittest

from environment.src.Environment import EnvironmentType, Environment, EnvironmentKeys


class EnvironmentTest(unittest.TestCase):

    def setUp(self) -> None:
        _env_name = os.getenv("ENVIRONMENT", "DEVELOP")
        self.current_environment = Environment(EnvironmentType.get_by_name(_env_name))

    def test_current_environment(self):
        self.assertIsNotNone(self.current_environment.get_env_var(EnvironmentKeys.MY_ENV_VAR_1))
        self.assertCountEqual(self.current_environment.ENV_VARS, EnvironmentKeys.names())
