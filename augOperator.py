# Import required modules
from dataclasses import dataclass, field
from typing import Callable, Optional
import PIL

# Custom modules
from ProAug.augParam import AugParam
from ProAug.color import Color
# from augSeq import AugSeq

@dataclass
class AugOperator:
    """
    Dataclass object for Augmentation Operator

    @attr
        name: name of the augmentation operator
        func: function id of the augmentation operator. By default ''
        probability: probability of applying the very augmentation operator on batch
        params: dictionary of parameters of augmentation operator
        add_to: takes AugSeq() as a parameter. Adds the current AugOperator() to that
                AugSeq().
    """

    name:str
    func:Callable
    probability:float
    params:Optional[AugParam] = None
    add_to:Optional[Callable] = None

    def __post_init__(self):
        """
        @desc
        Initiates after init method automatically
        """
        if self.add_to is not None:self.add_to.add(self)

    def __repr__(self):
        return "{}AugOperator() for {}{}{}, id : {}{}{}".format(
            Color.GREEN, Color.YELLOW, str(self.name), Color.GREEN,
            Color.MAGENTA, str(id(self)), Color.RESET)

    def update_prob(self)->None:
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

    def update_params(self):
        pass
