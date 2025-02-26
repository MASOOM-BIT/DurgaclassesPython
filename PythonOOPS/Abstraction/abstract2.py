from abc import *

class Printer(ABC):
    @abstractmethod
    def print_it(self,text):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    
class Epson(Printer):
    def print_it(self,text):
        print('Printing from Epson Printer')
        print(text)
    def disconnect(self):
        print('Disconnecting from Epson Printer')

class HP(Printer):
    def print_it(self,text):
        print('Printing from HP Printer')
        print(text)
    def disconnect(self):
        print('Disconnecting from HP Printer')
with open('RESOURCES/config.txt','r') as file:
    printer_name=file.readline()
classname=globals()[printer_name]
x=classname()
x.print_it('This is Data text to print')
x.disconnect()