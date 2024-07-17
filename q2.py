class Student:
    def __init__(self, name, age, roll_number):
        self.__name = name  # Encapsulated attribute for name
        self.__age = age    # Encapsulated attribute for age
        self.__roll_number = roll_number  # Encapsulated attribute for roll number
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_roll_number(self):
        return self.__roll_number
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number
    
    # Method to display student information
    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Roll Number: {self.__roll_number}")
    
    # Method to update student details
    def update_details(self, name, age, roll_number):
        self.__name = name
        self.__age = age
        self.__roll_number = roll_number

# Testing the Student class
if __name__ == "__main__":
    # Creating instances of Student class
    student1 = Student("Alice", 20, "S001")
    student2 = Student("Bob", 22, "S002")
    
    # Displaying initial information
    print("Initial Information:")
    student1.display_info()
    print()
    student2.display_info()
    print()
    
    # Updating details for student1
    student1.update_details("Alice Smith", 21, "S001")
    
    # Displaying updated information
    print("Updated Information for Student 1:")
    student1.display_info()
    print()
    
    # Testing getter and setter methods
    print("Testing Getter and Setter Methods:")
    print(f"Original Age of Student 2: {student2.get_age()}")
    student2.set_age(23)
    print(f"Updated Age of Student 2: {student2.get_age()}")
