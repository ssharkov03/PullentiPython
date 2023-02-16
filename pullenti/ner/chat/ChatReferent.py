﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import io
import typing
from pullenti.unisharp.Utils import Utils

from pullenti.ner.chat.VerbType import VerbType
from pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from pullenti.ner.Referent import Referent
from pullenti.ner.metadata.ReferentClass import ReferentClass
from pullenti.ner.chat.internal.MetaChat import MetaChat
from pullenti.ner.chat.ChatType import ChatType

class ChatReferent(Referent):
    
    def __init__(self) -> None:
        super().__init__(ChatReferent.OBJ_TYPENAME)
        self.instance_of = MetaChat._global_meta
    
    OBJ_TYPENAME = "CHAT"
    
    ATTR_TYPE = "TYPE"
    
    ATTR_VALUE = "VALUE"
    
    ATTR_NOT = "NOT"
    
    ATTR_VERBTYPE = "VERBTYPE"
    
    def to_string_ex(self, short_variant : bool, lang : 'MorphLang', lev : int=0) -> str:
        res = io.StringIO()
        print(Utils.enumToString(self.typ), end="", file=res)
        if (self.not0_): 
            print(" not", end="", file=res)
        val = self.value
        if (val is not None): 
            print(" {0}".format(val), end="", file=res, flush=True)
        vty = self.verb_types
        if (len(vty) > 0): 
            print("[", end="", file=res)
            i = 0
            while i < len(vty): 
                if (i > 0): 
                    print(", ", end="", file=res)
                print(Utils.enumToString(vty[i]), end="", file=res)
                i += 1
            print("]", end="", file=res)
        return Utils.toStringStringIO(res)
    
    @property
    def typ(self) -> 'ChatType':
        str0_ = self.get_string_value(ChatReferent.ATTR_TYPE)
        if (Utils.isNullOrEmpty(str0_)): 
            return ChatType.UNDEFINED
        try: 
            return Utils.valToEnum(str0_, ChatType)
        except Exception as ex567: 
            pass
        return ChatType.UNDEFINED
    @typ.setter
    def typ(self, value_) -> 'ChatType':
        self.add_slot(ChatReferent.ATTR_TYPE, Utils.enumToString(value_).upper(), True, 0)
        return value_
    
    @property
    def not0_(self) -> bool:
        return self.get_string_value(ChatReferent.ATTR_NOT) == "true"
    @not0_.setter
    def not0_(self, value_) -> bool:
        if (not value_): 
            self.add_slot(ChatReferent.ATTR_NOT, None, True, 0)
        else: 
            self.add_slot(ChatReferent.ATTR_NOT, "true", True, 0)
        return value_
    
    @property
    def value(self) -> str:
        return self.get_string_value(ChatReferent.ATTR_VALUE)
    @value.setter
    def value(self, value_) -> str:
        self.add_slot(ChatReferent.ATTR_VALUE, value_, True, 0)
        return value_
    
    @property
    def verb_types(self) -> typing.List['VerbType']:
        res = list()
        for s in self.slots: 
            if (s.type_name == ChatReferent.ATTR_VERBTYPE): 
                try: 
                    res.append(Utils.valToEnum(Utils.asObjectOrNull(s.value, str), VerbType))
                except Exception as ex568: 
                    pass
        return res
    
    def add_verb_type(self, vt : 'VerbType') -> None:
        self.add_slot(ChatReferent.ATTR_VERBTYPE, Utils.enumToString(vt).upper(), False, 0)
    
    def can_be_equals(self, obj : 'Referent', typ_ : 'ReferentsEqualType'=ReferentsEqualType.WITHINONETEXT) -> bool:
        tr = Utils.asObjectOrNull(obj, ChatReferent)
        if (tr is None): 
            return False
        if (tr.typ != self.typ): 
            return False
        if (tr.value != self.value): 
            return False
        if (tr.not0_ != self.not0_): 
            return False
        return True
    
    @staticmethod
    def _new566(_arg1 : 'ChatType') -> 'ChatReferent':
        res = ChatReferent()
        res.typ = _arg1
        return res