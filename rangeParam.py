# Import required modules
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Union
from random import shuffle, choice, choices
from string import ascii_uppercase, ascii_lowercase

# Import Custom modules
from .color import Color
from .augUtils import UtilClass


# Practice
"""
    total number of iterations = (dataset_size/batch_size)*total_epochs

    atmost number of augmentations to compose = λ (default is 5)

    total number of iterations per composition = total number of iterations/λ

    total number of augmentations in augmentation pool = Ꞷ

    since every augmentation would be applied approximately same number of times

    number of times any augmentation has been applied in 1st composition 
        = total number of iterations per composition/Ꞷ

    number of time any augmentaitons has been applied in ith composition
        = total number of iterations per compostiion*i/Ꞷ
        
    i = (current_epoch-1)*λ//total_epochs
    Aug_app = (dataset_size*total_epochs*i)/(batch_size*λ*Ꞷ)
            = dataset_size*total_epochs*(((current_epoch-1)*λ)//total_epochs+1)/(batch_size*λ*Ꞷ)
            
"""

class AbstractRangeParam(ABC):
    """
    @desc
    Abstract class for Range
    """
    @abstractmethod
    def update(self):
        pass


class DiscreteRange(AbstractRangeParam):
    """
    @desc
    >>> Discrete Range class to encapsulate the range which consists of discrete values
    """

    def __init__(self, range_min: int, range_max: int):
        self.__range_min: int = range_min
        self.__range_max: int = range_max
        self.__current_value :int = self.__range_min

    def __repr__(self):
        var = """{cyan}DiscreteRange({green}
                        range_min={magenta}{range_min}{green},
                        range_max={magenta}{range_max}{green},
                        current_value={magenta}{current_value}{cyan}){reset}"""
        return var.format(
            cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA, range_min=self.__range_min, 
            range_max=self.__range_max, current_value=self.__current_value, reset=Color.RESET)

    def update(self, util: UtilClass, current_epoch: int=1):
        if self.__current_value>self.__range_max: # reset
            self.__current_value=self.__range_min
        else:
            self.__current_value += util.divide_float(
                self.__range_max-self.__range_min,util.aug_app(current_epoch))
    
    @property
    def get_value(self)->int:
        return int(self.__current_value)

class ContRange(AbstractRangeParam):
    """
    @desc
        Continuos Range class to encapsulate the range which consists of float values
        between specified range
    
    @working
        current value is initiated as minimum range value, then in AUG_APP steps that
        completes base composition time(t number of epochs) current value is gradually 
        increased from range_min to range_max
    """

    def __init__(self, range_min: float, range_max: float):
        self.__range_min: float = range_min
        self.__range_max: float = range_max
        self.__current_value: float = self.__range_min

    def __repr__(self):
        var = """{cyan}ContRange({green}
                        range_min={magenta}{min}{green}, 
                        range_max={magenta}{max}{green},
                        current_value={magenta}{value}{cyan}){reset}"""
        return var.format(
            cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA, 
			min=self.__range_min, max=self.__range_max,value=self.__current_value,
			reset=Color.RESET)

    def update(self, util: UtilClass, current_epoch:int=1)->float:
        if self.__current_value>self.__range_max:
                self.__current_value=self.__range_min
        else:
            self.__current_value += util.divide_float(
                self.__range_max-self.__range_min,util.aug_app(current_epoch))
             
    @property 
    def get_value(self)->float:
        return self.__current_value

class DecContRange(AbstractRangeParam):
    """
    @desc
        Continuos Range class to encapsulate the range which consists of float values
        between specified range
    
    @working
        current value is initiated as minimum range value, then in AUG_APP steps that
        completes base composition time(t number of epochs) current value is gradually 
        increased from range_min to range_max
    """

    def __init__(self, range_min: float, range_max: float):
        self.__range_min: float = range_min
        self.__range_max: float = range_max
        self.__current_value: float = self.__range_min

    def __repr__(self):
        var = """{cyan}DecContRange({green}
                        range_min={magenta}{min}{green}, 
                        range_max={magenta}{max}{green},
                        current_value={magenta}{value}{cyan}){reset}"""
        return var.format(
            cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA, 
			min=self.__range_min, max=self.__range_max,value=self.__current_value,
			reset=Color.RESET)

    def update(self, util: UtilClass, current_epoch:int=1)->float:
        if self.__current_value<self.__range_max:
                self.__current_value=self.__range_min
        else:
            self.__current_value -= util.divide_float(
                self.__range_min-self.__range_max,util.aug_app(current_epoch))
        
    @property 
    def get_value(self)->float:
        return self.__current_value


class LoopContRange(AbstractRangeParam):
    """
    @desc
        its similar to ContRange class, except
        it first goes from range_min to range_max, and then in reverse in same AUG_APP steps
    """
    def __init__(self, range_min: float, range_max: float):
        self.__range_min: float = range_min
        self.__range_max: float = range_max
        self.__current_value: float = self.__range_min
        self.__positive:bool = True

    def __repr__(self):
        var = """{cyan}LoopContRange({green}
                        range_min={magenta}{min}{green}, 
                        range_max={magenta}{max}{green},
                        current_value={magenta}{value}{green},
                        positive={magenta}{positive_value}{cyan}){reset}"""
        return var.format(
            cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA, 
			min=self.__range_min, max=self.__range_max,value=self.__current_value,
			reset=Color.RESET, positive_value=self.__positive)

    def update(self, util:UtilClass, current_epoch:int=1)->float:

        if self.__current_value<=self.__range_max and self.__positive:
            self.__current_value += 2*util.divide_float(
                self.__range_max-self.__range_min, util.aug_app(current_epoch))

        if self.__current_value>=self.__range_max and self.__positive:self.__positive=False

        if self.__current_value>=self.__range_min and not self.__positive:
            self.__current_value -= 2*util.divide_float(
                self.__range_max-self.__range_min, util.aug_app(current_epoch))

        if self.__current_value<=self.__range_min and not self.__positive:self.__positive=True
    
    @property 
    def get_value(self)->float:
        return self.__current_value

class EnumRange(AbstractRangeParam):
    """
    @desc
    Enum Range class encapsulate the individual strings. These ranges cannot be
    encapsulated under Discrete Range because of their dynamics of being strings.
    """

    def __init__(self, *args: str):
        self.__enumsList: list = [arg for arg in args]
        self.__choice_enum: str = ""

    def __repr__(self):
        return "{}EnumRange({}{}{}){}".format(
            Color.CYAN, Color.MAGENTA, ", ".join(
                [str(arg) for arg in self.__enumsList]),
            Color.CYAN, Color.RESET)

    def show(self):
        return self.__enumsList

    def update(self, util: UtilClass, current_epoch: int=1):
        shuffle(self.__enumsList)
        self.__choice_enum = choice(self.__enumsList)
    
    @property
    def get_value(self)->str:
        return self.__choice_enum

class ColorRange(AbstractRangeParam):
    """
    @desc
    Color Range class encapsulate the Color values. because of their nature of 'RGB'
    they cannot be put under Discrete Range too.
    """

    def __init__(self):
        self.__red: int = 0
        self.__green: int = 0
        self.__blue: int = 0
        self.__range_list: list = [i for i in range(256)]

    def __repr__(self):
        var = """{cyan}ColorRange({green}
                        red={magenta}{red_value}{green}, 
                        green={magenta}{green_value}{green},
                        blue={magenta}{blue_value}{cyan}){reset}"""
        return var.format(cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA,
        red_value= self.__red, green_value= self.__green, blue_value=self.__blue,
        reset=Color.RESET)

    def update(self):
        self.__red, self.__green, self.__blue = choices(self.__range_list, k=3)
    
    @property
    def get_value(self)->List:
        return [self.__red, self.__green, self.__blue]

class StrRange(AbstractRangeParam):
    """
    @desc
    
    """

    def __init__(self, range_min: int, range_max: int):
        self.__range_min: float = range_min
        self.__range_max: float = range_max
        self.__current_string_len: int = 1
        self.__string: str = ""

    def __repr__(self):
        return "{}StrRange({}range_min={}{}{}, range_max={}{}{}){}".format(
            Color.CYAN, Color.GREEN, Color.MAGENTA, self.__range_min, Color.GREEN,
            Color.MAGENTA, self.__range_max, Color.CYAN, Color.RESET)

    def update(self, util: UtilClass, current_epoch: int=1):
        if util.isChange(current_epoch):
            self.__current_string_len = 1
        self.__current_string_len += util.divide_float(
            self.__range_max-self.__range_min, util.aug_app(current_epoch))
        self.__string = self.__out_n_len_str(int(self.__current_string_len))

    def __out_n_len_str(self, n: int=1)->str:
        return "".join([str(choice(ascii_uppercase + ascii_lowercase)) for i in range(n)])
    
    @property
    def get_value(self)->str:
        return self.__string