# Import required modules
from dataclasses import dataclass, field
from typing import List

# Custom modules
from .param import Param

@dataclass
class AugParam:
    """
    @attr
    paramList: dictionary that would hold all the Param objects for an
    Augmentation Operator

    @method
    add: if Augmentation Operator has just one arbitrary parameter then
    use add method to add Param Object to paramList

    @method
    addObjs: if Augmentation Operator has more than one arbitrary parameter
    then use addObjs method to add all the Param Objects to paramList
    """

    def __post_init__ (self)->None:
        """
        @desc
        Initiates a private dictionary paramList as empty dictionary
        """
        self._paramList:dict = {}

    def add(self, *objs:Param)->dict:
        """
        @desc
        add the Param object(s) of a parameter to paramList. Can take more than
        one Param objects in parameters
        """
        for obj in objs:
            self._paramList[obj.name]=obj
        return self._paramList
