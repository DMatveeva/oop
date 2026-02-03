# 1 
class Device:
    def __init__(self):
        self.__on = False
    def turn_on(self):
        self.__on = True
    def turn_off(self):
        self.__on = False
      
class Laptop(Device):
    def __init__(self, ram_gb, disk_gb):
        super().__init__()
        self.__ram_gb = ram_gb
        self.__disk_gb = disk_gb
    def run_Java(self):
        print('Java program')
    def run_python(self):
        print('Python program')
    def turn_off(self):
        print("Turn off laptop.")
        self.__on = False
      
class Phone(Device):
    def __init__(self, name):
        super().__init__()
        self.__name = name
    def call(self, contact):
        print('Calling ' + contact)
    def message(self, message):
        print('Sending message: ' + message)
    def turn_off(self):
        print("Turn off phone.")
        self.__on = False
      
class Employee:
    def __init__(self):
        self.__energy = 100
    def think(self, minutes):
        self.__energy -= minutes
    def drink_coffee(self):
        self.__energy += 10
      
class Programmer(Employee):
    def __init__(self, laptop, phone):
        super().__init__()
        self.__lines = 0
        self.__tests = 0
        self.__laptop = laptop
        self.__phone = phone
    def write_code(self, hours):
        self.__lines += hours
        self.__laptop.run_Java() # используем компьютер
    def write_test(self, hours):
        self.__tests += 1
      
class Analyst(Employee):
    def __init__(self, laptop, phone):
        super().__init__()
        self.__pages = 0
        self.__reports = 0
        self.__devices = [laptop, phone]
    def call_programmer(self):
        self.__lines += 1
    def write_documentation(self):
        self.__lines += 1
    def prepare_report(self):
        self.__tests += 1
    def go_home(self):
        for d in self.__devices:
            d.turn_off()
          
laptop = Laptop(16, 512)
phone = Phone("Samsung")
programmer = Programmer(laptop, phone)
programmer.write_code(8) # выводит Java program
ipad = Laptop(8, 512)
iphone = Phone("Samsung")
analyst = Analyst(ipad, iphone)
analyst.go_home() # Turn off laptop. Turn off phone.


# 2 
# В строчке animal.foo() - работает полиморфизм подтипов. У родительского класса animal вызывается метод foo(), и через полиморфизм вызывается метод конкретного объекта, на который указывает ссылка animal.
# В методе do_something_with_animal(animal: Animal) используется параметрический полиморфизм. 
# Метод принимает параметр типа animal - это может быть объект любого типа, который наследуется от Animal, но метод do_something_with_animal работает одинаково независимо от того, какого конкретно типа объект.

# 3
def get_500_animals(animals: list[Animal]):
    animals.clear()
    for _ in range(500):
        r = randint(0, 1)
        if r == 1:
            animals.append(Cat())
        else: animals.append(Bird())
    return animals
  
animals_list = get_500_animals([])
for j in range(500):
    ani = animals_list[j]
    ani.foo()

# Консоль вывелось 500 записей "Кошка мурлычет" и "Птица поет" в случайном количестве и порядке. Т.к. объекты создавались случайным образом. 
