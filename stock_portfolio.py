stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 200
}

total_investment = 0

print("Stock Portfolio Tracker")
print("-----------------------")

while True:
    stock = input("Enter stock name (or done to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stocks[stock] * quantity
    total_investment = total_investment + investment

    print("Stock:", stock)
    print("Price:", stocks[stock])
    print("Quantity:", quantity)
    print("Investment:", investment)
    print()

print("-----------------------")
print("Total Investment:", total_investment)
