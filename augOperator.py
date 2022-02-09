# Import required modules
from dataclasses import dataclass, field
from typing import Callable, Optional
import PIL

# Custom modules
from .augParam import AugParam
# from augSeq import AugSeq

@dataclass
class AugOperator:
    """
    Dataclass object for Augmentation Operator

    @attr
    func: function id of the augmentation operator. By default ''

    @attr
    add_to: takes AugSeq() as a parameter. Adds the current AugOperator() to that
    AugSeq().

    @attr
    name: name of the augmentation operator

    @attr
    probability: probability of applying the very augmentation operator on batch

    @attr
    AUG_PARAM: dictionary of parameters of augmentation operator

    @method
    update_prob: updates the probability of the Augmentation Operator to be
    choosen randomly. if 'p' is the current probability then it would be updated to
    p -> 1/(1+p)
    """

    """
    @desc
    init method for AugOperator dataclass containing attributes
    """
    name:str
    func:Callable
    probability:float
    params:Optional[AugParam] = None
    add_to:Optional[Callable] = None

    def __repr__(self):
        return "AugOperator() for " + "\033[4m" + str(self.name) + "\033[0m" #+ ", id : " + str(id(self))

    def __post_init__(self):
        """
        @desc
        Initiates after init method automatically
        """
        if self.add_to is not None:self.add_to.add(self)

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
