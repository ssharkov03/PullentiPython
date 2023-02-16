﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class GarParam(IntEnum):
    """ Типы параметров ГАР """
    UNDEFINED = 0
    """ Не определён """
    GUID = 1
    """ Уникальный GUID """
    KLADRCODE = 2
    """ Код КЛАДР (тип 10 в ГАР) """
    POSTINDEX = 3
    """ Почтовый индекс (тип 5 в ГАР) """
    OKATO = 4
    """ Код ОКАТО (тип 6 в ГАР) """
    OKTMO = 5
    """ Код ОКТМО (тип 7 в ГАР) """
    KADASTERNUMBER = 6
    """ Кадастровый номер (тип 8) """
    REESTERNUMBER = 7
    """ Реестровый номер (тип 13) """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)