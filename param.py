# Import required modules
from dataclasses import dataclass, field

# Custom modules
from ProAug.rangeParam import ContRange, AbstractRangeParam
from ProAug.color import Color

@dataclass
class Param:
    """
    This class will hold the individual parameter information of Augmentation 
    Operator

    @attr 
        name: name of the parameter
        value: current value of the parameter
        range: takes RangeType class as input
    """
    
    name:str=field(default="default_aug")
    value:float=field(default=0.0)
    range:AbstractRangeParam=field(default=ContRange)

    def __repr__(self):
        return "{}Param({}value={}{}{}, range={}{}{}){}".format(
            Color.CYAN,Color.GREEN, Color.MAGENTA, self.value, Color.GREEN,
            Color.MAGENTA, self.range, Color.CYAN, Color.RESET)
