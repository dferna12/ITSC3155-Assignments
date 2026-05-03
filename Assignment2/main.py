import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    resources = data.resources
    recipes = data.recipes

    machine = SandwichMaker(resources)
    cashier = Cashier()

    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            print(f"Bread: {machine.machine_resources['bread']} slices")
            print(f"Ham: {machine.machine_resources['ham']} slices")
            print(f"Cheese: {machine.machine_resources['cheese']} ounces")
        elif choice in recipes:
            order = recipes[choice]
            if machine.check_resources(order["ingredients"]):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, order["cost"]):
                    machine.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
