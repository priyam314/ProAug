# import python modules
from typing import List
from pillow import PIL

# import custom classes
from .augUtils import UtilClass

class AugComposer:

    def __init__(self):

        self.__batch_data = 0
        self.__out_composed_data = 0
    
    def compose(
        self, 
        data: List[PIL.Image.Image],
        util: UtilClass, 
        current_epoch: int=1)->List[PIL.Image.Image]:

        with Pool(util.aug_app(current_epoch)+2) as p:
            self.__out_composed_data = p.map(partial())

