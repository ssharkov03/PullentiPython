﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.PullentiPython.ru

from enum import IntEnum

class SemanticRole(IntEnum):
    """ Семантические роли """
    COMMON = 0
    """ Обычная """
    AGENT = 1
    """ Агент """
    PACIENT = 2
    """ Пациент """
    STRONG = 3
    """ Сильная связь """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)