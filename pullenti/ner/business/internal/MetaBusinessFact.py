﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from pullenti.unisharp.Utils import Utils

from pullenti.ner.metadata.ReferentClass import ReferentClass
from pullenti.ner.business.BusinessFactKind import BusinessFactKind

class MetaBusinessFact(ReferentClass):
    
    def __init__(self) -> None:
        super().__init__()
        self.kind_feature = None;
    
    @staticmethod
    def initialize() -> None:
        from pullenti.ner.business.BusinessFactReferent import BusinessFactReferent
        MetaBusinessFact.GLOBAL_META = MetaBusinessFact()
        f = MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_KIND, "Класс", 0, 1)
        MetaBusinessFact.GLOBAL_META.kind_feature = f
        f.add_value(Utils.enumToString(BusinessFactKind.CREATE), "Создавать", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.DELETE), "Удалять", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.HAVE), "Иметь", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.GET), "Приобретать", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.SELL), "Продавать", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.PROFIT), "Доход", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.DAMAGES), "Убытки", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.AGREEMENT), "Соглашение", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.SUBSIDIARY), "Дочернее предприятие", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.FINANCE), "Финансировать", None, None)
        f.add_value(Utils.enumToString(BusinessFactKind.LAWSUIT), "Судебный иск", None, None)
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_TYPE, "Тип", 0, 1)
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_WHO, "Кто", 0, 1).show_as_parent = True
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_WHOM, "Кого\\Кому", 0, 1).show_as_parent = True
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_WHEN, "Когда", 0, 1).show_as_parent = True
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_WHAT, "Что", 0, 0).show_as_parent = True
        MetaBusinessFact.GLOBAL_META.add_feature(BusinessFactReferent.ATTR_MISC, "Дополнительная информация", 0, 0).show_as_parent = True
    
    @property
    def name(self) -> str:
        from pullenti.ner.business.BusinessFactReferent import BusinessFactReferent
        return BusinessFactReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Бизнес-факт"
    
    IMAGE_ID = "businessfact"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        return MetaBusinessFact.IMAGE_ID
    
    GLOBAL_META = None