class Member:
    def __init__(self, name, age, membership_type):
        self.__id = Member.__generate_id()
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.__membership_status = "Active"

    __id_counter = 1

    @classmethod
    def __generate_id(cls):
        id_ = cls.__id_counter
        cls.__id_counter += 1
        return id_

    def get_id(self):
        return self.__id

    def get_membership_status(self):
        return self.__membership_status

    def register(self):
        self.__membership_status = "Active"
        return f"Member {self.name} is registered."

    def renew_membership(self):
        self.__membership_status = "Active"
        return f"Member {self.name}'s membership is renewed."

    def cancel_membership(self):
        self.__membership_status = "Cancelled"
        return f"Member {self.name}'s membership is cancelled."

    def display(self):
        return f"ID: {self.get_id()}, Name: {self.name}, Age: {self.age}, Membership Type: {self.membership_type}, Membership Status: {self.get_membership_status()}"

class FitnessClub:
    def __init__(self):
        self.members = []

    def register_member(self, member):
        self.members.append(member)
        return member.register()

    def renew_membership(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                return member.renew_membership()
        return f"Member ID {member_id} not found."

    def cancel_membership(self, member_id):
        for member in self.members:
            if member.get_id() == member_id:
                return member.cancel_membership()
        return f"Member ID {member_id} not found."

    def display_members(self):
        for member in self.members:
            print(member.display())

class FamilyMember(Member):
    def __init__(self, name, age, family_name):
        super().__init__(name, age, "Family")
        self.family_name = family_name

    def display(self):
        return f"{super().display()}, Family Name: {self.family_name}"

class IndividualMember(Member):
    def __init__(self, name, age):
        super().__init__(name, age, "Individual")

    def display(self):
        return super().display()

# Test the Fitness Club Management System

# Create a FitnessClub instance
fitness_club = FitnessClub()

# Create Member instances
member1 = IndividualMember(name="Alice", age=30)
member2 = FamilyMember(name="Bob", age=40, family_name="Smith")
member3 = IndividualMember(name="Charlie", age=25)
member4 = FamilyMember(name="Diana", age=35, family_name="Johnson")

# Register members
print(fitness_club.register_member(member1))
print(fitness_club.register_member(member2))
print(fitness_club.register_member(member3))
print(fitness_club.register_member(member4))

# Display the members
print("\nInitial Member List:")
fitness_club.display_members()

# Renew a membership
print("\nRenewing Membership for Member ID 1...")
print(fitness_club.renew_membership(1))

# Cancel a membership
print("\nCancelling Membership for Member ID 3...")
print(fitness_club.cancel_membership(3))

# Display the updated members
print("\nUpdated Member List:")
fitness_club.display_members()
