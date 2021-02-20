# -*- coding: utf-8 -*-
from enum import Enum
from typing import List, Dict, Union, Any


class EnumExt(Enum):

    @classmethod
    def names(cls):
        return [str(e.name) for e in cls]

    @classmethod
    def to_array(cls) -> List[Dict]:
        return [{'name': a.name, 'value': a.value} for a in cls]

    @classmethod
    def to_dict(cls) -> Dict:
        _result = {}
        for e in cls:
            _result[e.name] = e.value
        return _result

    @classmethod
    def exist_value(cls, _value) -> bool:
        return cls.get_by_value(_value) is not None

    @classmethod
    def exist_name(cls, _name) -> bool:
        return cls.get_by_name(_name) is not None

    @classmethod
    def get_by_value(cls, _value: int) -> Union[Any, None]:
        try:
            return cls(_value)
        except:
            return None

    @classmethod
    def get_by_name(cls, _name) -> Union[Any, None]:
        try:
            return cls[_name]
        except:
            return None
