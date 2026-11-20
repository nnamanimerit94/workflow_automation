customers = []

def register_customer(customers):
    while True:
        name = input('Enter name: ').strip().title()
        if name:
            break
        print("Name cannot be empty. Please try again")

    while True:
        email = input('Enter email: ').strip().lower()
        if not email:
            print("Email cannot be empty")

        elif any(customer["email"] == email for customer in customers):
            print("Email already exists. please enter a valid email address")
        else:
            break

    while True:
        country = input("Enter country: ").strip().title()

        if country:
                break
                
        print("Country cannot be empty")


    customer = {
        "name": name,
        "email": email,
        "country": country
    }
    customers.append(customer)

    print("Successfully registered customer\n")

def display_all_customers(customers):
    if not customers:
        print("No registered customers yet")
        return

    for index, customer in enumerate(customers, start=1):
        print(f"Customer{index}:")
        for keys, values in customer.items():
            print(f"{keys}: {values}\n")


def count_customers(customers):
    print(f"Total count of customers is {len(customers)}")

def search_customer(customers, customer_email):
    if not customers:
        print("No resgistered customer yet")
        return 
    for customer in customers:
        if customer["email"] == customer_email:
            print("Customer found")
            print(f"Name: {customer["name"]}")
            print(f"Email: {Customer["email"]}")
            return 

    print(f"Customer with name '{customer_email}' does not exist")

def main():
    while True:
        print("\nCUSTOMER MANAGEMENT SYSTEM")
        print("What would you like to do?")
        print("1. Register a customer")
        print("2. Display registered customers")
        print("3. Count number of customers")
        print("4. Search for a customer")
        print("q. Quit")

        choice = input("Enter choice: ").strip().lower()

        if choice == "1":
            register_customer(customers)

        elif choice == "2":
            display_all_customers(customers)

        elif choice == "3":
            count_customers(customers)
        elif choice == "4":
            customer_email = input("Enter customer email address: ").strip().lower()
            search_customer(customers, customer_email)

        elif choice in ("q","quit"):
            print("Goodbye")
            break
        else:
            print("Invalid choice input, please select the right option")


if __name__ == "__main__":
    main()



        
