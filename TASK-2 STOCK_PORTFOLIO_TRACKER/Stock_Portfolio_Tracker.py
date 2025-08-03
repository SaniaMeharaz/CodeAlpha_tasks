stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 130,
    "AMZN": 140,
    "MSFT": 300
}
portfolio = {}
total_value = 0
print("📊 Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ', '.join(stock_prices.keys()))
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("⚠️ Stock not found. Please choose from:", ', '.join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"How many shares of {stock} do you own? "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"✅ Added {quantity} share(s) of {stock}")
print("\n💼 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")
print(f"\n💰 Total Investment Value: ${total_value}")
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
    print(f"📁 Portfolio saved to {filename}")
