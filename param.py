# Import required modules
from dataclasses import dataclass, field

# Custom modules
from .rangeParam import ContRange, AbstractRangeParam

@dataclass
class Param:
    """
    @attr
    name: name of the parameter

    @attr
    value: current value of the parameter

    @attr
    range_min: minimum value that is acceptable for the parameter

    @attr
    range_max: maximum value that is acceptable for the parameter
    """
    """
    @desc
    init method of Param dataclass containing attributes
    """
    name:str=field(default="default_aug")
    value:float=field(default=0.0)
    range:AbstractRangeParam=field(default=ContRange)

    def __repr__(self):
        return "Param(value = {}, range = {})".format(self.value, self.range)
