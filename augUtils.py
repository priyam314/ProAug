class UtilClass:
    def __init__(self):
        self.__dataset_size = 0
        self.__batch_size = 0
        self.__total_epochs = 0
        self.__lamda = 0
        self.__omega = 0
    def dataset_size(self, dataset_size: int=1):
        self.__dataset_size = dataset_size
        return self
    def batch_size(self, batch_size: int=1):
        self.__batch_size = batch_size
        return self
    def total_epochs(self, total_epochs: int=1):
        self.__total_epochs = total_epochs
        return self
    def lamda(self, lamda: int=1):
        self.__lamda = lamda
        return self
    def omega(self, omega: int=1):
        self.__omega = omega
        return self
    def divide_float(self, a: float, b: float)->float:
        try:
            return a/b
        except ZeroDivisionError as exp:
            print(exp)
            raise
    def divide_int(self, a: float, b: float)->int:
        try:
            return a//b
        except ZeroDivisionError as exp:
            print(exp)
            raise
    def isChange(self,current_epoch: int=1)->bool:
        if self.aug_app(current_epoch-1) != self.aug_app(current_epoch):
            return True
        return False
    @property
    def ds(self)->int:
        return self.__dataset_size
    @property
    def bs(self)->int:
        return self.__batch_size
    @property
    def te(self)->int:
        return self.__total_epochs
    @property
    def l(self)->int:
        return self.__lamda
    @property
    def o(self)->int:
        return self.__omega
    def aug_app(self, current_epoch: int=1)->float:
        a = self.ds*self.te 
        ith = self.divide_int( (current_epoch-1)*self.l, self.te)
        i_th = ith + 1
        b = self.bs*self.l*self.o
        return self.divide_float( a*i_th, b)
        