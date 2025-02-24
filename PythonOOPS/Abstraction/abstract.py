from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(DBInterface):
    def connect(self):
        print('Connecting to Oracle DB')
    def disconnect(self):
        print('Disconnecting from Oracle DB')

class Mysql(DBInterface):
    def connect(self):
        print('Connecting to Mysql DB')
    def disconnect(self):
        print('Disconnecting from Mysql DB')

class PostgreSQL(DBInterface):
    def connect(self):
        print('Connecting to PostgreSQL DB')
    def disconnect(self):
        print('Disconnecting from PostgreSQL DB')


dbname=input('Enter Db Name: ')
classname=globals()[dbname] #inbuilt function 'globals' converts string into class and return the class name
x=classname()
x.connect()
x.disconnect()