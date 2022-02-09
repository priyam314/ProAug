# Import required modules
from dataclasses import dataclass, field
from numpy.random import choice
from typing import List, Union
from sys import getsizeof

# Custom modules
from .augOperator import AugOperator
from ProAug import utils

@dataclass
class AugSeq:
    """
    @attr
    _augList: private data member. Dictionary to store all the AugOperators

    @attr
    _choice_name: private data member. Holds the name of randomly choosen
    Augmentation Operator

	@method
    size: returns the size of auglist in bytes

    @method
    addObjs: add all the AugOperators to augList

    @method
    show: returns the augList

    @method
    _maxProb: Private method. Find the names of all the Augmentation
    Operator with highest probability

    @method
    chooseRandom: chooses random Augmentation Operator name

    @method
    update: it updates the probability of the choosen Augmentation Operator.
    Should be called after chooseRandom()

    @method
    probabilities: it returns the probabilities of all the Augmentation
    Operators
    """

    """
    @desc
    init method for AugSeq, containing attributes
    """
    _choice_name:str=field(default='blur')

    def __post_init__(self):
        """
        @desc
        Initiates after init method automatically
        """
        self._AugObjList:List = []
        self._augList:dict = {}

    def operator(self, string:str)->AugOperator:
        """
        @desc
        functional form of indexing a list

        @example
        >>> from ProAugs.augs import Augs
        >>> Augs.init()
        >>> Blur = Augs.operator('blur')
        >>> Blur.probability()
        1.0
        """
        return self._augList[string]

    def add_AugObj_List(self, augObj:List)->None:
        """
        @desc
        adds the Augmentation Operator Objects to a list.
        """
        self._AugObjList = augObj

    def init(self, add_after_epochs:int)->str:
        """
        @desc
        add all the objects to _augList

        @example
        >>> Augs.show()
        {}
        >>> Augs.init(5)
        >>> Augs.show()
        { key:value ...}
        """
        utils.aae = add_after_epochs
        self.addObjs(self._AugObjList)
        return "Initiated with add_after_epochs : {}".format(utils.aae)

    def reset(self, this:str)->None:
        """
        @desc
        reset the values

        @example
        >>> Augs.reset("probabilities")
        >>> Augs.probabilities()
        <all probabilities would be reseted to 1.0>
        """
        if this == "probabilities":
            for _, values in self._augList.items():
                values.probability = 1

    def __repr__(self):
        return self.__class__.__name__

    def size(self)->str:
        """
        @desc
        returns the size of whole _augList dictionary in bytes, and string
        format.

        @example
        >>> Augs.size()
        345 bytes
        """
        return self._string_size()

    def _string_size(self)->str:
        """
        @desc
        get the size of whole _augList dictionary in bytes
        """
        size = str(getsizeof(self._augList)) + " bytes"
        return size

    def addObjs(self, objs:List[AugOperator])->dict:
        """
        @desc
        adds the list of Augmentation Operator objects to _augList dictionary.
        If objs doesn't exist then objs would be added to _augList.
        """
        for obj in objs:
            self._augList.update({obj.name:obj})
        return self._augList

    def add(self, obj:AugOperator)->None:
        """
        @desc
        add the Augmentation Operator object to _augList dictionary

        @example
        >>> trialOpr = AugOperator(...)
        >>> Augs.add(trialOpr)
        >>> Augs.show()
        {
        ... ,
        'trial': Augmentation Operator() .. ,
        }
        """
        self._augList.update({obj.name:obj})
        return self._augList

    def show(self)->Union[dict,str]:
        """
        @desc
        return the _augList dictionary
        """
        return self._augList

    def _maxProb(self)->List[str]:
        """
        @desc
        find the list of names of those Augmentation Operator Objects which have
        highest probability
        """
        max_value = max([value.probability for key, value in self._augList.items()])
        max_aug_names = [key for key,value in self._augList.items() if value.probability==max_value]
        return max_aug_names

    def chooseRandom(self)->str:
        """
        @desc
        chooses a random Augmentation Operator from list of Augmentation Operator
        objects which have highest probabilities or from the list generate by
        self._maxProb()
        """
        max_prob_names = self._maxProb()
        self._choice_name = choice(max_prob_names)
        return self._choice_name

    def update(self)->None:
        """
        @desc
        updates the probability of the randomly choosen Augmentation Operator.
        It works in conjunction with chooseRandom(). attribute _choice_name is
        assigned the chooseRandom() value, which is now publicily accessible in
        the dataclass.

        @example
        >>> Augs.chooseRandom()
        >>> Augs.update()
        """
        self._augList[self._choice_name].update_prob()

    def probabilities(self)->dict:
        """
        @desc
        gives a dictionary of all the probabilities of augmentation operator objects
        """
        new_dict = {}
        for key, value in self._augList.items():
            new_dict.update({key: value.probability})
        return new_dict

    def frequency(self)->dict:
        """
        @desc
        gives a dictionary of all the frequency of augmentation operator objects
        """
        new_dict = {}
        for key, value in self._augList.items():
            new_dict.update({key: 1.0//value.probability})
        return new_dict
