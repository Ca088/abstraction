from abc import ABC,abstractmethod
class class1(ABC):
    def print(self,x):
        print("Value:",x)

    @abstractmethod
    def task(self):
        print("Inside abstract method")
class testclass(class1):
    def task(self):
        print("Inside test class")

obj=testclass()
obj.task()
obj.print(100)

class India():
    def capital(self):
        print('New delhi is capital of India')
    def language(self):
        print("Hindi is the most widely spoken language of India")

class USA():
    def capital(self):
        print("Wahington, DC is the capital of Usa")

    def language(self):
        print("English is the primary language of USA")

obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    print("\n")
