﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.PullentiPython.ru

from enum import IntEnum

class KeywordType(IntEnum):
    """ Тип ключевой комбинации """
    UNDEFINED = 0
    """ Неопределён """
    OBJECT = 1
    """ Объект (именная группа) """
    REFERENT = 2
    """ Именованная сущность """
    PREDICATE = 3
    """ Предикат (глагол) """
    ANNOTATION = 4
    """ Автоаннотация всего текста """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)