cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020, "available": True},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2022, "available": True},
    {"id": 3, "make": "Ford", "model": "Escape", "year": 2019, "available": False},
]

def view_cars():
    """Returns a list of available cars as a string"""
    available_cars = []
    for car in cars:
        if car["available"]:
            available_cars.append(f"ID: {car['id']}, Make: {car['make']}, Model: {car['model']}, Year: {car['year']}")
    return "\n".join(available_cars)

def rent_car(car_id):
    """Rents a car by marking it as unavailable"""
    for car in cars:
        if car["id"] == car_id and car["available"]:
            car["available"] = False
            return f"Car ID {car_id} rented successfully!"
    return f"Car ID {car_id} is unavailable or does not exist."

def return_car(car_id):
    """Returns a car by marking it as available"""
    for car in cars:
        if car["id"] == car_id and not car["available"]:
            car["available"] = True
            return f"Car ID {car_id} returned successfully!"
    return f"Car ID {car_id} is already available or does not exist."

def main():
    while True:
        print("\nCar Rental Management System")
        print("1. View Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(view_cars())
        elif choice == "2":
            try:
                car_id = int(input("Enter car ID to rent: "))
                print(rent_car(car_id))
            except ValueError:
                print("Please enter a valid integer for the car ID.")
        elif choice == "3":
            try:
                car_id = int(input("Enter car ID to return: "))
                print(return_car(car_id))
            except ValueError:
                print("Please enter a valid integer for the car ID.")
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
