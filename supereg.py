class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def fullname(self):
        print(firstname, ' ', lastname)
    
class student(person):
    def __init__(self, firstname, lastname, grade):
        self.grade = grade
        super().__init__(firstname, lastname) # calling base constructor
    def display_details():
        super().fullname() # calling base class method
        print('Grade ', self.grade)
        
std = student('James', 'Bond', '10')
std.display_details()
