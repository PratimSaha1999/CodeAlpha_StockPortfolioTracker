import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2800,
    "AMZN": 140,
    "MSFT": 300
}

portfolio = {}  # To store user's stock holdings

total_investment = 0

print("\n📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} - ${price}")

# Taking user input for stocks and quantities
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock_name == 'DONE':
        break
    if stock_name not in stock_prices:
        print("❌ Stock not found. Please choose from the list above.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculating total investment
for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional: Save results to CSV
save_choice = input("Do you want to save the portfolio to a CSV file? (y/n): ").lower()
if save_choice == 'y':
    with open("portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for stock, quantity in portfolio.items():
            writer.writerow([stock, quantity, stock_prices[stock], stock_prices[stock] * quantity])
        writer.writerow(["Total Investment", "", "", total_investment])
    print("✅ Portfolio saved to portfolio.csv")
