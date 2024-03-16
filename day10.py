# #------OOPS------------
# class Student:      #student is a class n from this class we can create number of objects like student1,student2....

#      def set_name(self, name):
#           self.name=name
#      def get_name(self):
#           return self.name
     
# student1=Student()
# student1.set_name("akash")
# print(student1.name)
# #---or
# print(student1.get_name())

# student2=Student()
# student2.set_name("kumar")
# print(student2.get_name())

# #------Question--------
# class Rectangle:
#      def set_dimensions(self, height, width):
#           self.height=height
#           self.width=width

#      def area(self):
#           return self.height*self.width
#      def perimeter(self):
#           return 2*(self.height+self.width)

# #     creating object
# rectangle1=Rectangle()
# rectangle1.set_dimensions(4,3)
# print("the height and width are:",rectangle1.height,rectangle1.width)
# print("the area is:",rectangle1.area())
# print("the perimeter is:",rectangle1.perimeter())

# #------class constructor--------
# class Rectangle:
#      def __init__(self,height,width):
#           print(f"A rectangle is created with height:{height} and width:{width}")
#           self.height=height
#           self.width=width
#      def area(self):
#           return self.height*self.width
#      def perimeter(self):
#           return 2*(self.height+self.width)
# rectangle1=Rectangle(4,3)
# rectangle2=Rectangle(2,9)
# rectangle3=Rectangle(4,7)
# print("the area is:",rectangle1.area(),"and","the perimeter is:",rectangle1.perimeter())

# #-------Attributes-----------
# class Student:

#      def set_name(self, name):
#           self.name=name       #class attributes
#      def get_name(self):
#           return self.name
     
# student1=Student()
# student1.set_name("akash")
# print(student1.name)
# #---or
# print(student1.get_name())
# student1.eng_marks=56                 #instance attributes
# print(student1.eng_marks)

# student2=Student()
# student2.set_name("kumar")
# print(student2.get_name())

#--------Access modifier
# #------public modifier
# class ABC:
#      def __init__(self):
#          self.public_attribute=None    #public attribute
#      def public_function():             #public function
#           pass
# obj1=ABC()
# obj2.public_attribute
# obj1.public_function()

# #---------private modifier----------
# class ABC:
#      def __init__(self):
#          self.__private_attribute=None    #private attribute
#      def __private_function():             #private function
#           pass
# obj1=ABC()
# print(obj1.__private_attribute)     #give attribute error

# #--------protected modifier-------
# class ABC:
#      def __init__(self):
#          self._protected_attribute=None    #protected attribute
#      def _protected_function():             #protected function
#           pass
# obj1=ABC()
# obj2.public_attribute
# obj1.public_function()

#--------inheritance------
#-------vehicle question
# class Vehicle:
#      def __init__(self,seating_capacity):
#           self.seating_capacity=seating_capacity
#      def get_fare(self):
#           return self.seating_capacity*100

# class Bus(Vehicle):
#      def __init__(self,seating_capacity):
#           super().__init__(seating_capacity)
#      def get_fare(self):
#           vehicle_fare=super().get_fare()
#           maintenance_fare=0.1*vehicle_fare
#           total_fare=vehicle_fare+maintenance_fare
#           return total_fare

# vehicle1=Vehicle(50)
# print("Vehicle fare:",vehicle1.get_fare())

# bus1=Bus(50)
# print("bus fare:",bus1.get_fare())

#------Polymorphism----
# class Animal:
#      def speaks(self):
#           pass

# class Dog(Animal):
#      def speaks(self):
#           print("barks")

# class Cat(Animal):
#      def speaks(self):
#           print("meaw")

# class Cow(Animal):
#      def speaks(self):
#           print("Moooo")

# dog=Dog()
# cat=Cat()
# cow=Cow()
# dog.speaks()
# cat.speaks()
# cow.speaks()

#-----methodoverloading----
# class Add:
#      def sum(self,a,b):
#           print(a+b)
#      def sum(self,a,b,c):
#           print(a+b+c)

# #-----operator overloading-------
# class ComplexNumber:
#      def __init__(self,real,img):
#           self.real=real
#           self.img=img
#      def __add__(self,other):
#           return ComplexNumber(self.real+other.real,self.img+other.img)

# c1=ComplexNumber(1,2)
# c2=ComplexNumber(3,4)
# c3=c1+c2
# print(c3.real,"+i",c3.img)

#------exception handling
a=int(input("Enter a:"))
b=int(input("Enter b:"))
try:
     result=a/b
except:
     result=None
     print("Error: Cannot divide by 0")
finally:
     print("Division operation completed:",result)