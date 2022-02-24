# Import required modules
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import List, Union

# Import Custom modules
from . import utils
from .color import Color

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
# Dataclasses
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
    Discrete Range class to encapsulate the range which consists of discrete values
    """

    def __init__(self, range_min: float, range_max: float):
        self.range_min: int = range_min
        self.range_max: int = range_max

    def __repr__(self):
        return "{}DiscreteRange({}range_min={}{}{}, range_max={}{}{}){}".format(
            Color.CYAN, Color.GREEN, Color.MAGENTA, self.range_min, Color.GREEN,
            Color.MAGENTA, self.range_max, Color.CYAN, Color.RESET)

    def update(self):
        pass


class ContRange(AbstractRangeParam):
    """
    @desc
    Continuos Range class to encapsulate the range which consists of float values
    between specified range
    """

    def __init__(self, range_min: float, range_max: float):
        self.range_min: float = range_min
        self.range_max: float = range_max
        self.current_value: float = 0.0

    def __repr__(self):
        var = """{cyan}ContRange({green}range_min={magenta}{min}{green}, range_max={magenta}{max}{green}, 
		current_value={magenta}{value}{cyan}){reset}"""
        return var.format(
            cyan=Color.CYAN, green=Color.GREEN, magenta=Color.MAGENTA, 
			min=self.range_min, max=self.range_max,value=self.current_value,
			reset=Color.RESET)

    def update(self):
        AUG_APP = 1


class EnumRange(AbstractRangeParam):
    """
    @desc
    Enum Range class encapsulate the individual strings. These ranges cannot be
    encapsulated under Discrete Range because of their dynamics of being strings.
    """

    def __init__(self, *args: str):
        self.enumsList = [arg for arg in args]

    def __repr__(self):
        return "{}EnumRange({}{}{}){}".format(
            Color.CYAN, Color.MAGENTA, ", ".join(
                [str(arg) for arg in self.enumsList]),
            Color.CYAN, Color.RESET)

    def show(self):
        return self.enumsList

    def update(self):
        pass


class ColorRange(AbstractRangeParam):
    """
    @desc
    Color Range class encapsulate the Color values. because of their nature of 'RGB'
    they cannot be put under Discrete Range too.
    """

    def __init__(self):
        self.red: int = 0
        self.green: int = 0
        self.blue: int = 0

    def __repr__(self):
        return "ColorRange()"

    def update(self):
        pass


class StrRange(AbstractRangeParam):
    """
    @desc

    """

    def __init__(self, size_min: int, size_max: int):
        self.size_min: float = size_min
        self.size_max: float = size_max

    def __repr__(self):
        return "{}StrRange({}size_min={}{}{}, size_max={}{}{}){}".format(
            Color.CYAN, Color.GREEN, Color.MAGENTA, self.size_min, Color.GREEN,
            Color.MAGENTA, self.size_max, Color.CYAN, Color.RESET)

    def update(self):
        pass


"""
@example
a = DiscreteRange(["hello", "f"])
print (a.discreteList[0])
"""
