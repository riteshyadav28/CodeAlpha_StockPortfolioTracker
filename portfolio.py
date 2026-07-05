import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 330,
    "AMZN": 140
}

portfolio = {}
total = 0

print("====== Stock Portfolio Tracker ======")

while True:
    stock = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter Quantity: "))

    portfolio[stock] = quantity

print("\n------- Investment Summary -------")

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Total"])

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        investment = price * qty
        total += investment

        print(f"{stock} : {qty} x ${price} = ${investment}")

        writer.writerow([stock, qty, price, investment])

print("\nTotal Investment = $", total)

print("\nPortfolio saved as portfolio.csv")