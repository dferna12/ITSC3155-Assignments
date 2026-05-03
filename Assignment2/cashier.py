def process_coins():
    print("Please insert coins.")
    dollars = int(input("How many $1 coins?: "))
    half_dollars = int(input("How many 50c coins?: "))
    quarters = int(input("How many 25c coins?: "))
    nickels = int(input("How many 5c coins?: "))
    total = dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
    return total


class Cashier:
    def __init__(self):
        self.profit = 0

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry, that’s not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change")
        self.profit += cost
        return True
