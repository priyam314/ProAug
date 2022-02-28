class UtilClass:
    def __init__(self):
        self.__dataset_size = 0
        self.__batch_size = 0
        self.__total_epochs = 0
        self.__lamda = 0
        self.__omega = 0
    def dataset_size(self, dataset_size):
        self.__dataset_size = dataset_size
        return self
    def batch_size(self, batch_size):
        self.__batch_size = batch_size
        return self
    def total_epochs(self, total_epochs):
        self.__total_epochs = total_epochs
        return self
    def lamda(self, lamda):
        self.__lamda = lamda
        return self
    def omega(self, omega):
        print ("run")
        self.__omega = omega
        return self
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
    @property
    def aug_app(current_epoch:int=1)->float:
        return (self.ds*self.te*(((current_epoch-1)*self.l)//self.te+1))/float(self.bs*self.l*self.o)
        