﻿# SDK Pullenti Address, version 4.14, september 2022. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

import typing
import io
from pullenti.unisharp.Utils import Utils

from pullenti.ner.core.ReferentsEqualType import ReferentsEqualType
from pullenti.ner.core.MiscHelper import MiscHelper
from pullenti.ner.business.BusinessFactKind import BusinessFactKind
from pullenti.ner.metadata.ReferentClass import ReferentClass
from pullenti.ner.business.internal.MetaBusinessFact import MetaBusinessFact
from pullenti.ner.Referent import Referent

class BusinessFactReferent(Referent):
    """ Сущность для бизнес-факта
    
    """
    
    def __init__(self) -> None:
        super().__init__(BusinessFactReferent.OBJ_TYPENAME)
        self.instance_of = MetaBusinessFact.GLOBAL_META
    
    OBJ_TYPENAME = "BUSINESSFACT"
    """ Имя типа сущности TypeName ("BUSINESSFACT") """
    
    ATTR_KIND = "KIND"
    """ Имя атрибута - класс (BusinessFactKind) """
    
    ATTR_TYPE = "TYPE"
    """ Имя атрибута - тип """
    
    ATTR_WHO = "WHO"
    """ Имя атрибута - кто """
    
    ATTR_WHOM = "WHOM"
    """ Имя атрибута - кого """
    
    ATTR_WHEN = "WHEN"
    """ Имя атрибута - когда """
    
    ATTR_WHAT = "WHAT"
    """ Имя атрибута - что """
    
    ATTR_MISC = "MISC"
    """ Имя атрибута - разное """
    
    @property
    def kind(self) -> 'BusinessFactKind':
        """ Классификатор бизнес-факта """
        s = self.get_string_value(BusinessFactReferent.ATTR_KIND)
        if (s is None): 
            return BusinessFactKind.UNDEFINED
        try: 
            res = Utils.valToEnum(s, BusinessFactKind)
            if (isinstance(res, BusinessFactKind)): 
                return Utils.valToEnum(res, BusinessFactKind)
        except Exception as ex543: 
            pass
        return BusinessFactKind.UNDEFINED
    @kind.setter
    def kind(self, value) -> 'BusinessFactKind':
        if (value != BusinessFactKind.UNDEFINED): 
            self.add_slot(BusinessFactReferent.ATTR_KIND, Utils.enumToString(value), True, 0)
        return value
    
    @property
    def typ(self) -> str:
        """ Краткое описание факта (тип) """
        typ_ = self.get_string_value(BusinessFactReferent.ATTR_TYPE)
        if (typ_ is not None): 
            return typ_
        kind_ = self.get_string_value(BusinessFactReferent.ATTR_KIND)
        if (kind_ is not None): 
            typ_ = (Utils.asObjectOrNull(MetaBusinessFact.GLOBAL_META.kind_feature.convert_inner_value_to_outer_value(kind_, None), str))
        if (typ_ is not None): 
            return typ_.lower()
        return None
    @typ.setter
    def typ(self, value) -> str:
        self.add_slot(BusinessFactReferent.ATTR_TYPE, value, True, 0)
        return value
    
    @property
    def who(self) -> 'Referent':
        """ Кто (действительный залог) """
        return Utils.asObjectOrNull(self.get_slot_value(BusinessFactReferent.ATTR_WHO), Referent)
    @who.setter
    def who(self, value) -> 'Referent':
        self.add_slot(BusinessFactReferent.ATTR_WHO, value, True, 0)
        return value
    
    @property
    def who2(self) -> 'Referent':
        """ Второй "Кто" (действительный залог) """
        i = 2
        for s in self.slots: 
            if (s.type_name == BusinessFactReferent.ATTR_WHO): 
                i -= 1
                if (i == 0): 
                    return Utils.asObjectOrNull(s.value, Referent)
        return None
    @who2.setter
    def who2(self, value) -> 'Referent':
        self.add_slot(BusinessFactReferent.ATTR_WHO, value, False, 0)
        return value
    
    @property
    def whom(self) -> 'Referent':
        """ Кого (страдательный залог) """
        return Utils.asObjectOrNull(self.get_slot_value(BusinessFactReferent.ATTR_WHOM), Referent)
    @whom.setter
    def whom(self, value) -> 'Referent':
        self.add_slot(BusinessFactReferent.ATTR_WHOM, value, True, 0)
        return value
    
    @property
    def when(self) -> 'Referent':
        """ Когда (DateReferent или DateRangeReferent) """
        return Utils.asObjectOrNull(self.get_slot_value(BusinessFactReferent.ATTR_WHEN), Referent)
    @when.setter
    def when(self, value) -> 'Referent':
        self.add_slot(BusinessFactReferent.ATTR_WHEN, value, True, 0)
        return value
    
    @property
    def whats(self) -> typing.List['Referent']:
        """ Что (артефакты события) - список Referent """
        res = list()
        for s in self.slots: 
            if (s.type_name == BusinessFactReferent.ATTR_WHAT and (isinstance(s.value, Referent))): 
                res.append(Utils.asObjectOrNull(s.value, Referent))
        return res
    
    def _add_what(self, w : object) -> None:
        if (isinstance(w, Referent)): 
            self.add_slot(BusinessFactReferent.ATTR_WHAT, w, False, 0)
    
    def to_string_ex(self, short_variant : bool, lang : 'MorphLang', lev : int=0) -> str:
        res = io.StringIO()
        typ_ = Utils.ifNotNull(self.typ, "Бизнес-факт")
        print(MiscHelper.convert_first_char_upper_and_other_lower(typ_), end="", file=res)
        v = None
        v = self.get_slot_value(BusinessFactReferent.ATTR_WHO)
        if (isinstance((v), Referent)): 
            print("; Кто: {0}".format(v.to_string_ex(True, lang, 0)), end="", file=res, flush=True)
            if (self.who2 is not None): 
                print(" и {0}".format(self.who2.to_string_ex(True, lang, 0)), end="", file=res, flush=True)
        v = self.get_slot_value(BusinessFactReferent.ATTR_WHOM)
        if (isinstance((v), Referent)): 
            print("; Кого: {0}".format(v.to_string_ex(True, lang, 0)), end="", file=res, flush=True)
        if (not short_variant): 
            v = self.get_slot_value(BusinessFactReferent.ATTR_WHAT)
            if ((v) is not None): 
                print("; Что: {0}".format(v), end="", file=res, flush=True)
            v = self.get_slot_value(BusinessFactReferent.ATTR_WHEN)
            if (isinstance((v), Referent)): 
                print("; Когда: {0}".format(v.to_string_ex(short_variant, lang, 0)), end="", file=res, flush=True)
            for s in self.slots: 
                if (s.type_name == BusinessFactReferent.ATTR_MISC): 
                    print("; {0}".format(s.value), end="", file=res, flush=True)
        return Utils.toStringStringIO(res)
    
    def can_be_equals(self, obj : 'Referent', typ_ : 'ReferentsEqualType'=ReferentsEqualType.WITHINONETEXT) -> bool:
        br = Utils.asObjectOrNull(obj, BusinessFactReferent)
        if (br is None): 
            return False
        if (br.kind != self.kind): 
            return False
        if (br.typ != self.typ): 
            return False
        if (br.who != self.who or br.whom != self.whom): 
            return False
        if (self.when is not None and br.when is not None): 
            if (not self.when.can_be_equals(br.when, ReferentsEqualType.WITHINONETEXT)): 
                return False
        mi1 = Utils.asObjectOrNull(self.get_slot_value(BusinessFactReferent.ATTR_WHAT), Referent)
        mi2 = Utils.asObjectOrNull(br.get_slot_value(BusinessFactReferent.ATTR_WHAT), Referent)
        if (mi1 is not None and mi2 is not None): 
            if (not mi1.can_be_equals(mi2, ReferentsEqualType.WITHINONETEXT)): 
                return False
        return True
    
    @staticmethod
    def _new531(_arg1 : 'BusinessFactKind') -> 'BusinessFactReferent':
        res = BusinessFactReferent()
        res.kind = _arg1
        return res
    
    @staticmethod
    def _new542(_arg1 : 'BusinessFactKind', _arg2 : str) -> 'BusinessFactReferent':
        res = BusinessFactReferent()
        res.kind = _arg1
        res.typ = _arg2
        return res