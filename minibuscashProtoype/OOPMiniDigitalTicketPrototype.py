import datetime

class TicketSystem:
    def __init__(self):
        # Initialize an empty dictionary to store data
        self.data_dict = {
            "serial": [],
            "bus": [],
            "driver": [],
            "conductor": [],
            "fair": [],
            "discount": [],
            "OR": [],
            "amount": [],
            "from": [""],
            "to": [""]
        }

    def valid(self):
        # Function for input and validation
        serial = str(input("Enter BUS SERIAL NUMBER: "))
        self.data_dict["serial"].append(serial)

        bus = str(input("Enter BUS PLATE NUMBER: "))
        self.data_dict["bus"].append(bus)

        driver = str(input("Enter Driver Name: "))
        self.data_dict["driver"].append(driver)

        conductor = str(input("Enter Conductor Name: "))
        self.data_dict["conductor"].append(conductor)

        fair = float(input("Enter Minimum Fair: "))
        self.data_dict["fair"].append(fair)

        discount = float(input("Enter Discount: "))
        self.data_dict["discount"].append(discount)

        if (
            discount == self.data_dict["discount"][0]
            and bus == self.data_dict["bus"][0]
            and serial == self.data_dict["serial"][0]
            and driver == self.data_dict["driver"][0]
            and conductor == self.data_dict["conductor"][0]
            and fair == self.data_dict["fair"][0]
        ):
            while True:
                print("---------------------------------------------")
                print("[1] Student/Senior, [2] Regular")
                passenger = int(input("Enter passenger: "))

                if passenger == 1:
                    self.student()

                elif passenger == 2:
                    self.regular()

                else:
                    print("Error: Input values do not match.")
        else:
            print("Error: Input values do not match.")

    def student(self):
        # Function for input of 'From' and 'To' locations for student/senior
        print("---------------------------------------------")
        print("[1] Calumpang, [2] San Juan")
        From = int(input("From: "))
        to = int(input("To: "))

        if From == 1:
            self.data_dict["from"][0] = "Calumpang"
        elif From == 2:
            self.data_dict["from"][0] = "San Juan"
        else:
            print("Error: Invalid 'From' location.")

        if to == 1:
            self.data_dict["to"][0] = "Calumpang"
        elif to == 2:
            self.data_dict["to"][0] = "San Juan"
        else:
            print("Error: Invalid 'To' location.")

        # Calculate and store the amount for student/senior
        fair_value = self.data_dict["fair"][0]
        discount_value = self.data_dict["discount"][0]
        result = fair_value - discount_value
        self.data_dict["amount"].append(result)

        # For date and time
        dt = datetime.datetime.now()

        print("---------------------------------------------")
        print("Gerald Mini Digital Ticket")
        print("Serial #: ", self.data_dict["serial"][0], "Bus Plate #: ", self.data_dict["bus"][0])
        print("Driver Name: ", self.data_dict["driver"][0], "Conductor Name: ", self.data_dict["conductor"][0])

        # Increment the 'OR' (Official Receipt) number
        if self.data_dict["OR"]:
            latest_OR = int(self.data_dict["OR"][-1])
            next_OR = latest_OR + 1
        else:
            next_OR = 1

        self.data_dict["OR"].append(next_OR)

        print("OFFICIAL RECEIPT #: ", next_OR)
        print("Date: ", dt.strftime("%B %d, %Y"))
        print("From: ", self.data_dict["from"][0])
        print("To: ", self.data_dict["to"][0])
        print("Regular: ", self.data_dict["fair"][0])
        print("Discount: ", self.data_dict["discount"][0])
        print("Amount: ", self.data_dict["amount"][0])
        print("STUDENT/SENIOR")
        print("THIS SERVES AS AN OFFICIAL RECEIPT")

    def regular(self):
        # Function for input of 'From' and 'To' locations for regular passenger
        print("---------------------------------------------")
        print("[1] Calumpang, [2] San Juan")
        From = int(input("From: "))
        to = int(input("To: "))

        if From == 1:
            self.data_dict["from"][0] = "Calumpang"
        elif From == 2:
            self.data_dict["from"][0] = "San Juan"
        else:
            print("Error: Invalid 'From' location.")

        if to == 1:
            self.data_dict["to"][0] = "Calumpang"
        elif to == 2:
            self.data_dict["to"][0] = "San Juan"
        else:
            print("Error: Invalid 'To' location.")

        # Calculate and store the amount for regular passenger
        fair_value = self.data_dict["fair"][0]
        discount_value = self.data_dict["discount"][0]
        result = fair_value - discount_value
        self.data_dict["amount"].append(result)

        # For date and time
        dt = datetime.datetime.now()

        print("---------------------------------------------")
        print("Gerald Mini Digital Ticket")
        print("Serial #: ", self.data_dict["serial"][0], "Bus Plate #: ", self.data_dict["bus"][0])
        print("Driver Name: ", self.data_dict["driver"][0], "Conductor Name: ", self.data_dict["conductor"][0])

        # Increment the 'OR' (Official Receipt) number
        if self.data_dict["OR"]:
            latest_OR = int(self.data_dict["OR"][-1])
            next_OR = latest_OR + 1
        else:
            next_OR = 1

        self.data_dict["OR"].append(next_OR)

        print("OFFICIAL RECEIPT #: ", next_OR)
        print("Date: ", dt.strftime("%B %d, %Y"))
        print("From: ", self.data_dict["from"][0])
        print("To: ", self.data_dict["to"][0])
        print("Regular: ", self.data_dict["fair"][0])
        print("Amount: ", self.data_dict["fair"][0])
        print("REGULAR")
        print("THIS SERVES AS AN OFFICIAL RECEIPT")

if __name__ == "__main__":
    ticket_system = TicketSystem()
    ticket_system.valid()
