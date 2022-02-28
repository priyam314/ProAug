# Import required modules
from dataclasses import dataclass, field
from typing import List

# Custom modules
from .param import Param
from .color import Color
from .augUtils import UtilClass


class AugParam:
    """
    @attr
        _paramList: dictionary that would hold all the Param objects for an
        Augmentation Operator
    """
    def __init__(self, *objs:Param)->None:
        self._paramList:dict = {}
        self._add(*objs)
    
    def __repr__(self)->str:
        return "{cyan}AugParam({magenta}{names}{cyan}){reset}".format(
            cyan=Color.CYAN, magenta=Color.MAGENTA, reset=Color.RESET,
            names=", ".join([param_name for param_name in self._paramList])
        )

    def _add(self, *objs:Param)->None:
        """
        @desc
            add the Param object(s) of a parameter to paramList. Can take more
            than one Param objects in parameters
        """
        for obj in objs:
            self._paramList[obj.name]=obj
    
    def parameter(self, name:str="")->Param:
        return self._paramList[name]
    
    def get_parameters(self)->dict:
        params = {}
        for name, param in self._paramList.items():
            params.update({name:param.range.current_value})
        return params
    
    def list(self):
        if self._paramList is not None:
            return self._paramList
        else:
            return None
    
    def update_parameters(self, util:UtilClass, current_epoch:int=1):
        """
        @desc

        """
        for _, param in self._paramList.items():
            param.update(util, current_epoch)
