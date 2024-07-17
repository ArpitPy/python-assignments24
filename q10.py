class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats):
        self.__flight_number = flight_number
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time
        self.__available_seats = total_seats
        self.__flight_id = hash(flight_number + departure_airport + arrival_airport)  # Encapsulated unique identifier

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            print("Seat booked successfully.")
        else:
            print("No available seats.")

    def cancel_reservation(self):
        self.__available_seats += 1
        print("Reservation cancelled successfully.")

    def get_remaining_seats(self):
        return self.__available_seats

    def get_flight_details(self):
        return {
            "Flight Number": self.__flight_number,
            "Departure Airport": self.__departure_airport,
            "Arrival Airport": self.__arrival_airport,
            "Departure Time": self.__departure_time,
            "Arrival Time": self.__arrival_time,
            "Available Seats": self.get_remaining_seats()
        }

    def get_flight_id(self):
        return self.__flight_id


class DomesticFlight(Flight):
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats, in_flight_service):
        super().__init__(flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats)
        self.__in_flight_service = in_flight_service  # e.g., 'Snacks', 'Meals'

    def get_flight_details(self):
        details = super().get_flight_details()
        details["In-flight Service"] = self.__in_flight_service
        return details


class InternationalFlight(Flight):
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats, passport_required):
        super().__init__(flight_number, departure_airport, arrival_airport, departure_time, arrival_time, total_seats)
        self.__passport_required = passport_required  # e.g., True or False

    def get_flight_details(self):
        details = super().get_flight_details()
        details["Passport Required"] = self.__passport_required
        return details


# Example usage:
# Creating a domestic flight
domestic_flight = DomesticFlight("DF123", "LAX", "SFO", "2024-08-01 09:00", "2024-08-01 11:00", 150, "Snacks")
domestic_flight.book_seat()
domestic_flight.book_seat()
domestic_flight.cancel_reservation()

print(domestic_flight.get_flight_details())

# Creating an international flight
international_flight = InternationalFlight("IF456", "JFK", "LHR", "2024-08-05 19:00", "2024-08-06 07:00", 200, True)
international_flight.book_seat()
international_flight.book_seat()
international_flight.cancel_reservation()

print(international_flight.get_flight_details())
