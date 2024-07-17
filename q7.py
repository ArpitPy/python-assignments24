class Room:
    def __init__(self, room_number, room_type, rate):
        self.__id = Room.__generate_id()
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.__is_available = True

    __id_counter = 1

    @classmethod
    def __generate_id(cls):
        id_ = cls.__id_counter
        cls.__id_counter += 1
        return id_

    def get_id(self):
        return self.__id

    def is_available(self):
        return self.__is_available

    def book_room(self):
        if self.__is_available:
            self.__is_available = False
            return f"Room {self.room_number} is booked."
        else:
            return f"Room {self.room_number} is already booked."

    def check_in(self):
        if not self.__is_available:
            return f"Checked in to Room {self.room_number}."
        else:
            return f"Room {self.room_number} is not booked yet."

    def check_out(self):
        if not self.__is_available:
            self.__is_available = True
            return f"Checked out of Room {self.room_number}."
        else:
            return f"Room {self.room_number} is already available."

    def display(self):
        availability_status = "Available" if self.__is_available else "Not Available"
        return f"ID: {self.get_id()}, Room Number: {self.room_number}, Room Type: {self.room_type}, Rate: ${self.rate:.2f}, Availability: {availability_status}"

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book_room()
        return f"Room {room_number} not found."

    def check_in(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.check_in()
        return f"Room {room_number} not found."

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.check_out()
        return f"Room {room_number} not found."

    def display_rooms(self):
        for room in self.rooms:
            print(room.display())

class SuiteRoom(Room):
    def __init__(self, room_number, rate, has_jacuzzi=False):
        super().__init__(room_number, "Suite", rate)
        self.has_jacuzzi = has_jacuzzi

    def display(self):
        jacuzzi_status = "with Jacuzzi" if self.has_jacuzzi else "without Jacuzzi"
        return f"{super().display()}, {jacuzzi_status}"

class StandardRoom(Room):
    def __init__(self, room_number, rate):
        super().__init__(room_number, "Standard", rate)

    def display(self):
        return super().display()

# Test the Hotel Management System

# Create a Hotel instance
hotel = Hotel()

# Create Room instances
suite1 = SuiteRoom(room_number=101, rate=150.00, has_jacuzzi=True)
suite2 = SuiteRoom(room_number=102, rate=140.00, has_jacuzzi=False)
standard1 = StandardRoom(room_number=201, rate=80.00)
standard2 = StandardRoom(room_number=202, rate=85.00)

# Add rooms to the hotel
hotel.add_room(suite1)
hotel.add_room(suite2)
hotel.add_room(standard1)
hotel.add_room(standard2)

# Display the rooms
print("Initial Room Status:")
hotel.display_rooms()

# Book a room
print("\nBooking Room 101...")
print(hotel.book_room(101))

# Check in to a room
print("\nChecking in to Room 101...")
print(hotel.check_in(101))

# Check out of a room
print("\nChecking out of Room 101...")
print(hotel.check_out(101))

# Display the updated rooms
print("\nUpdated Room Status:")
hotel.display_rooms()
