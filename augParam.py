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
        self.__paramList:dict = {}
        self.__add(*objs)
    
    def __repr__(self)->str:
        return "{cyan}AugParam({magenta}{names}{cyan}){reset}".format(
            cyan=Color.CYAN, magenta=Color.MAGENTA, reset=Color.RESET,
            names=", ".join([param_name for param_name in self.__paramList])
        )

    def __add(self, *objs:Param)->None:
        """
        @desc
            add the Param object(s) of a parameter to paramList. Can take more
            than one Param objects in parameters
        """
        for obj in objs:
            self.__paramList[obj.name]=obj
        
    def reset_parameters(self)->None:
        """
        @desc
        >>> sends the request to reset the parameters values to all the available params objs
        """
        for _, param in self.__paramList.items():
            param.reset_parameter()
    
    def load_param(self,
        param: dict)->None:
        """
        @desc
        >>> update each param of the operator
        """
        for name, value in param.items():
            self.parameter(name).load_param(value)
    
    def parameter(self, name:str="")->Param:
        return self.__paramList[name]
    
    def get_parameters(self, update: bool=True)->dict:
        params = {}
        for name, param in self.__paramList.items():
            if update:
                params.update({name:param.get_value()})
            else:
                params.update({name:param.get_default_value()})
        return params
    
    def list(self):
        if self.__paramList is not None:
            return self.__paramList
        else:
            return None
    
    def update_parameters(self, util: UtilClass, current_epoch: int=1):
        """
        @desc

        """
        for _, param in self.__paramList.items():
            param.update(util, current_epoch)
