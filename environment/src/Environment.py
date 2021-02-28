#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Dict, Union

from ext.src.EnumExt import EnumExt


class EnvironmentKeys(EnumExt):
    MY_ENV_VAR_1 = 0
    MY_ENV_VAR_2 = 1


class EnvironmentType(EnumExt):
    DEVELOP = 1
    TEST = 2
    STAGE = 3
    PRODUCTION = 4


class Environment:

    def __init__(self, env_type: EnvironmentType):
        self.ENV_TYPE: EnvironmentType = env_type
        self.ENV_VARS: Dict = self.__set_env_vars()

    def get_env_var(self, key: EnvironmentKeys, default_var: object = None) -> object:
        return self.ENV_VARS.get(key.name) if key.name in self.ENV_VARS else default_var

    def __set_env_vars(self) -> Union[Dict, None]:
        if self.ENV_TYPE == EnvironmentType.DEVELOP:
            return self.__develop_env()
        if self.ENV_TYPE == EnvironmentType.TEST:
            return self.__test_env()
        if self.ENV_TYPE == EnvironmentType.STAGE:
            return self.__stage_env()
        if self.ENV_TYPE == EnvironmentType.PRODUCTION:
            return self.__prod_env()
        return None

    @staticmethod
    def __develop_env() -> Dict:
        return {
            str(EnvironmentKeys.MY_ENV_VAR_1.name): "dev",
            str(EnvironmentKeys.MY_ENV_VAR_2.name): "localhost",
        }

    @staticmethod
    def __test_env() -> Dict:
        return {
            str(EnvironmentKeys.MY_ENV_VAR_1.name): "test",
            str(EnvironmentKeys.MY_ENV_VAR_2.name): "test-server",
        }

    @staticmethod
    def __stage_env() -> Dict:
        return {
            str(EnvironmentKeys.MY_ENV_VAR_1.name): "stage",
            str(EnvironmentKeys.MY_ENV_VAR_2.name): "stage-server",
        }

    @staticmethod
    def __prod_env() -> Dict:
        return {
            str(EnvironmentKeys.MY_ENV_VAR_1.name): "prod",
            str(EnvironmentKeys.MY_ENV_VAR_2.name): "prod-server",
        }
