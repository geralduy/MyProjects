import datetime

# Global dictionary to store data
thisdict = {
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

def valid():
    # Function for input and validation
    serial = str(input("Enter BUS SERIAL NUMBER: "))
    thisdict["serial"].append(serial)

    bus = str(input("Enter BUS PLATE NUMBER: "))
    thisdict["bus"].append(bus)

    driver = str(input("Enter Driver Name: "))
    thisdict["driver"].append(driver)

    conductor = str(input("Enter Conductor Name: "))
    thisdict["conductor"].append(conductor)

    fair = float(input("Enter Minimum Fair: "))
    thisdict["fair"].append(fair)

    discount = float(input("Enter Discount: "))
    thisdict["discount"].append(discount)

    if (
        discount == thisdict["discount"][0]
        and bus == thisdict["bus"][0]
        and serial == thisdict["serial"][0]
        and driver == thisdict["driver"][0]
        and conductor == thisdict["conductor"][0]
        and fair == thisdict["fair"][0]
    ):
        while True:
            location()
            printing()
    else:
        print("Error: Input values do not match.")

def location():
    # Function for input of 'From' and 'To' locations
    print("---------------------------------------------")
    print("[1] Calumpang, [2] San Juan")
    From = int(input("From: "))
    to = int(input("To: "))

    if From == 1:
        thisdict["from"][0] = "Calumpang"
    elif From == 2:
        thisdict["from"][0] = "San Juan"
    else:
        print("Error: Invalid 'From' location.")

    if to == 1:
        thisdict["to"][0] = "Calumpang"
    elif to == 2:
        thisdict["to"][0] = "San Juan"
    else:
        print("Error: Invalid 'To' location.")

    # Calculate and store the amount
    fair_value = thisdict["fair"][0]
    discount_value = thisdict["discount"][0]
    result = fair_value - discount_value
    thisdict["amount"].append(result)

def printing():
    # Function to print the receipt
    dt = datetime.datetime.now()

    print("---------------------------------------------")
    print("Gerald Mini Digital Ticket")
    print("Serial #: ", thisdict["serial"][0], "Bus Plate #: ", thisdict["bus"][0])
    print("Driver Name: ", thisdict["driver"][0], "Conductor Name: ", thisdict["conductor"][0])
    
    # Increment the 'OR' (Official Receipt) number
    if thisdict["OR"]:
        latest_OR = int(thisdict["OR"][-1])
        next_OR = latest_OR + 1
    else:
        next_OR = 1

    thisdict["OR"].append(next_OR)
    
    print("OFFICIAL RECEIPT #: ", next_OR)
    print("Date: ", dt.strftime("%B %d, %Y"))
    print("From: ", thisdict["from"][0])
    print("To: ", thisdict["to"][0])
    print("Regular: ", thisdict["fair"][0])
    print("Discount: ", thisdict["discount"][0])
    print("Amount: ", thisdict["amount"][0])
    print("THIS SERVES AS AN OFFICIAL RECEIPT")

valid()



