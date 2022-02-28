# Import required modules
from dataclasses import dataclass, field
from typing import Callable, Optional
import PIL

# Custom modules
from .augParam import AugParam
from .param import Param
from .color import Color
from .augUtils import UtilClass

# from augSeq import AugSeq

class AugOperator:
    """
    Dataclass object for Augmentation Operator

    @attr
        name: name of the augmentation operator 
        func: function id of the augmentation operator. By default '' 
        probability: probability of applying the very augmentation operator 
            on batch 
        params: dictionary of parameters of augmentation operator 
        add_to: takes AugSeq() as a parameter. Adds the current AugOperator() to that
                AugSeq().
    """
    def __init__(self, name:str, func:Callable, probability:float
        ,params:Optional[AugParam] = AugParam(), add_to:Optional[Callable] = None)->None:

        self.name = name
        self.func = func
        self.probability = probability
        self.params = params
        self.add_to = add_to

    def __post_init__(self):
        """
        @desc
        Initiates after init method automatically
        """
        if self.add_to is not None:self.add_to.add(self)

    def __repr__(self):
        var = """{cyan}AugOperator({green}func={yellow}{func_name}{green}, probability={magenta}{prob}{green},
        params={params}{cyan}){reset}"""
        return var.format(
            green=Color.GREEN, yellow=Color.YELLOW, func_name=self.func,
            magenta=Color.MAGENTA, cyan=Color.CYAN, reset=Color.RESET,
            params=self.params, prob=self.probability)
    
    def parameter(self, name:str="")->Param:
        return self.params.parameter(name)

    def update_probability(self)->None:
        """
        @desc
        updates the probability of the Augmentation Operator using certain heuristic
        p->1/(1+p)

        @example
        if p=1, then
        probability would transition in certain way
        1->1/2->1/3->1/4...

        @also
        p->1/(1+p)->[1/(1+p)]/(1+[1/(1+p)])=1/(2+p)->1/(3+p)
        """
        self.probability = 1.0/(1.0/self.probability+1.0)

    def update_parameters(self, util:UtilClass, current_epoch:int=1):
        self.params.update_parameters(util, current_epoch)
    
    def get_parameters(self)->dict:
        return self.params.get_parameters()

