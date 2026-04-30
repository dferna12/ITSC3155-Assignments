class HamSandwichMaker:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True
    @staticmethod
    def process_coins ():
        print("Please insert coins.")
        dollars = int(input("How many $1 coins?: "))
        half_dollars = int(input("How many 50c coins?: "))
        quarters = int(input("How many 25c coins?: "))
        nickels = int(input("How many 5c coins?: "))
        total = dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
        return total
    @staticmethod
    def transaction_result(coins, cost):
        if coins < cost:
            print("Sorry, that’s not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

def main():
    resources = {
        "bread": 12,
        "ham": 18,
        "cheese": 24
    }

    recipes = {
        "small": {
            "ingredients": {
                "bread": 2,
                "ham": 4,
                "cheese": 4,
            },
            "cost": 1.75,
        },
        "medium": {
            "ingredients": {
                "bread": 4,
                "ham": 6,
                "cheese": 8,
            },
            "cost": 3.25,
        },
        "large": {
            "ingredients": {
                "bread": 6,
                "ham": 8,
                "cheese": 12,
            },
            "cost": 5.5,
        }
    }

    machine = HamSandwichMaker(resources)

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
                payment = machine.process_coins()
                if machine.transaction_result(payment, order["cost"]):
                    machine.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
