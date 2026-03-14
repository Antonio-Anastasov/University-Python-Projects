daily_income = float(input())
daily_earnings = float(input())
expenses = float(input())
gift_price = float(input())

total_income = 5 * daily_income
total_earnings = 5 * daily_earnings

total_money = total_earnings + total_income
available_money = total_money - expenses

if available_money >= gift_price:
    print(f"Profit: {available_money:.2f} BGN, the gift has been purchased.")
else:
    needed_money = gift_price - available_money
    print(f"Insufficient money: {needed_money:.2f} BGN.")