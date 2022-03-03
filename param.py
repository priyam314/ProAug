# Import required modules
from dataclasses import dataclass, field

# Custom modules
from .rangeParam import ContRange, AbstractRangeParam
from .color import Color
from .augUtils import UtilClass


@dataclass
class Param:
    """
    This class will hold the individual parameter information of Augmentation 
    Operator

    @attr 
        name: name of the parameter
        default_value: default value of the parameter
        range: takes RangeType class as input
    """
    
    name:str=field(default="default_aug")
    default_value:float=field(default=0.0)
    range:AbstractRangeParam=field(default=ContRange)

    def __repr__(self):
        return "{}Param({}value={}{}{}, range={}{}{}){}".format(
            Color.CYAN,Color.GREEN, Color.MAGENTA, self.default_value, Color.GREEN,
            Color.MAGENTA, self.range, Color.CYAN, Color.RESET)
    
    def update(self, util: UtilClass, current_epoch: int=1)->None:
        self.range.update(util, current_epoch)
    
    def get_value(self):
        return self.range.get_value
    
    def get_default_value(self):
        return self.default_value
    
    def reset_parameter(self)->None:
        self.range.reset()
