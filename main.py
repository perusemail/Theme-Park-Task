class Attraction():
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity 
        self._status = False
        self._eligible = False

    def get_details(self):
        print("Attraction name:",self._name,"\nCapacity",self._capacity)
    
    def start(self):
        if self._status == True:
            print("The attaction",self._name,"is starting")
        else:
            print("The attaction",self._name,"is closed. Cannot start")

    def open_attraction(self):
        self._status = True

    def close_attraction(self):
        self._status = False
    
    def check_status(self):
        print(self._status)


class Thrillride(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity )
        self._min_height = min_height

    def start(self):
        if self._status == True:
            print(f"Thrillride {self._name} is now starting. Hold on tight!")
        else:
            print("The attaction",self._name,"is closed. Cannot start")

    def is_eligible(self, age, height):
        if height < self._min_height or height < 0:
            print(f"You are too short. You must be {self._min_height}. You are {height}")
            
        else:
            print(f"You are above the min height requirment. You can ride")
            



class FamilyRide(Attraction):
    def __init__ (self, name, capacity, min_age):
        super().__init__(name, capacity)
        self._min_age = min_age
    
    def start(self):
        if self._status == True:
            print(f"FamilyRide {self._name} is now starting. Enjoy the fun!")
        else:
            print("The attaction",self._name,"is closed. Cannot start")

    def is_eligible(self, age, height):
        if age < self._min_age or height < 0 :
            print(f"You are too young. You must be {self._min_age}. You are {age}")
            
        else:
            print(f"You are above the min age requirment. You can ride")



    
class Staff():
    def __init__(self, name, role):
        self._name = name
        self._role = role

    def work(self):
        print(f"Staff {self._name} is performing their role: {self._role}")


class Visitor():
    def __init__ (self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self.ride_history = []

    def ride(self, attraction):
        attraction.is_eligible(self._age, self._height)
        (self.ride_history).append(attraction._name)

    def view_history(self):
        for counter in self.ride_history:
            print(counter)


class Manager(Staff):
    def __init__(self, name, role, team):
        super().__init__(name, role)
        self._team = team

    def add_staff(self, staff):
        (self._team).append(staff)

    def get_team_summary(self):
        for counter in self._team:
            print(f"Name: {counter._name} Role: {counter._role}")

dragon_coaster = Thrillride("Dragon Coaster",20,140)
merry_go_round = FamilyRide("Merry-Go-Round",30,4)
visitor1 = Visitor("John",10,150)
visitor1.ride(dragon_coaster)
visitor1.ride(merry_go_round)
dragon_coaster.open_attraction()
dragon_coaster.start()
merry_go_round.start()

manager1 = Manager("Mike","Operator",[])
staff1 = Staff("Smith","Worker")
manager1.add_staff(staff1)
manager1.get_team_summary()
visitor1.view_history()



