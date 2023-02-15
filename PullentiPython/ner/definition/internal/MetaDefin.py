﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.PullentiPython.ru

from PullentiPython.unisharp.Utils import Utils

from PullentiPython.ner.metadata.ReferentClass import ReferentClass
from PullentiPython.ner.definition.DefinitionKind import DefinitionKind

class MetaDefin(ReferentClass):
    
    @staticmethod
    def initialize() -> None:
        from PullentiPython.ner.definition.DefinitionReferent import DefinitionReferent
        MetaDefin._global_meta = MetaDefin()
        MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_TERMIN, "Термин", 1, 0)
        MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_TERMIN_ADD, "Дополнение термина", 0, 0)
        MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_VALUE, "Значение", 1, 0)
        MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_MISC, "Мелочь", 0, 0)
        MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_DECREE, "Ссылка на НПА", 0, 0)
        fi = MetaDefin._global_meta.add_feature(DefinitionReferent.ATTR_KIND, "Тип", 1, 1)
        fi.add_value(Utils.enumToString(DefinitionKind.ASSERTATION), "Утверждение", None, None)
        fi.add_value(Utils.enumToString(DefinitionKind.DEFINITION), "Определение", None, None)
        fi.add_value(Utils.enumToString(DefinitionKind.NEGATION), "Отрицание", None, None)
    
    @property
    def name(self) -> str:
        from PullentiPython.ner.definition.DefinitionReferent import DefinitionReferent
        return DefinitionReferent.OBJ_TYPENAME
    
    @property
    def caption(self) -> str:
        return "Тезис"
    
    IMAGE_DEF_ID = "defin"
    
    IMAGE_ASS_ID = "assert"
    
    def get_image_id(self, obj : 'Referent'=None) -> str:
        from PullentiPython.ner.definition.DefinitionReferent import DefinitionReferent
        if (isinstance(obj, DefinitionReferent)): 
            ki = obj.kind
            if (ki == DefinitionKind.DEFINITION): 
                return MetaDefin.IMAGE_DEF_ID
        return MetaDefin.IMAGE_ASS_ID
    
    _global_meta = None