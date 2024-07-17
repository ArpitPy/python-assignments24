class Event:
    def __init__(self, name, date, time, location):
        self.__name = name
        self.__date = date
        self.__time = time
        self.__location = location
        self.__attendees = []
        self.__event_id = hash(name + date + time + location)  # Encapsulated unique identifier

    def create_event(self, name, date, time, location):
        return Event(name, date, time, location)

    def add_attendee(self, attendee):
        if attendee not in self.__attendees:
            self.__attendees.append(attendee)
            print(f"Attendee {attendee} added.")
        else:
            print(f"Attendee {attendee} is already in the list.")

    def remove_attendee(self, attendee):
        if attendee in self.__attendees:
            self.__attendees.remove(attendee)
            print(f"Attendee {attendee} removed.")
        else:
            print(f"Attendee {attendee} not found in the list.")

    def get_total_attendees(self):
        return len(self.__attendees)

    def get_event_details(self):
        return {
            "Name": self.__name,
            "Date": self.__date,
            "Time": self.__time,
            "Location": self.__location,
            "Total Attendees": self.get_total_attendees()
        }

    def get_event_id(self):
        return self.__event_id


class PrivateEvent(Event):
    def __init__(self, name, date, time, location, invite_code):
        super().__init__(name, date, time, location)
        self.__invite_code = invite_code

    def validate_invite_code(self, invite_code):
        return self.__invite_code == invite_code

    def get_event_details(self):
        details = super().get_event_details()
        details["Invite Code"] = self.__invite_code
        return details


class PublicEvent(Event):
    def __init__(self, name, date, time, location, publicity_level):
        super().__init__(name, date, time, location)
        self.__publicity_level = publicity_level  # e.g., 'Local', 'National', 'International'

    def get_event_details(self):
        details = super().get_event_details()
        details["Publicity Level"] = self.__publicity_level
        return details


# Example usage:
# Creating a private event
private_event = PrivateEvent("Private Meeting", "2024-07-20", "10:00", "Conference Room 1", "INV123")
private_event.add_attendee("John Doe")
private_event.add_attendee("Jane Smith")

print(private_event.get_event_details())

# Creating a public event
public_event = PublicEvent("Public Concert", "2024-08-15", "18:00", "City Park", "International")
public_event.add_attendee("Alice Brown")
public_event.add_attendee("Bob Johnson")

print(public_event.get_event_details())
