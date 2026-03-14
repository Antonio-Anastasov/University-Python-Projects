def calculate_tax(vehicle_info):
    vehicles = vehicle_info.split(">>")
    total_tax = 0.0

    for vehicle in vehicles:
        car_details = vehicle.split()
        if len(car_details) != 3:
            print("Invalid car type.")
            continue

        car_type = car_details[0]
        try:
            years = int(car_details[1])
            kilometers = int(car_details[2])
        except ValueError:
            print("Invalid car type.")
            continue

        tax = 0

        if car_type == "family":
            tax = 50 - (years * 5) + ((kilometers // 3000) * 12)
        elif car_type == "heavyDuty":
            tax = 80 - (years * 8) + ((kilometers // 9000) * 14)
        elif car_type == "sports":
            tax = 100 - (years * 9) + ((kilometers // 2000) * 18)
        else:
            print("Invalid car type.")
            continue

        if tax < 0:
            tax = 0

        total_tax += tax
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")

    print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")


vehicle_info = input()
calculate_tax(vehicle_info)
