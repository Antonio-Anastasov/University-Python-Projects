price_of_baggage_over_20kg = float(input())
weight_of_baggage = float(input())
days_to_flight = int(input())
count_of_baggage = int(input())
result = 0
total_price_for_weight = 0
days_to_flight_price = 0
if weight_of_baggage < 10 :
    total_price_for_weight = price_of_baggage_over_20kg * 0.2
elif 10 <= weight_of_baggage <= 20:
    total_price_for_weight = price_of_baggage_over_20kg * 0.5
else:
    total_price_for_weight = price_of_baggage_over_20kg
if days_to_flight > 30:
    days_to_flight_price = total_price_for_weight * 0.1
elif 7 <= days_to_flight <= 30:
    days_to_flight_price = total_price_for_weight * 0.15
elif days_to_flight < 7:
    days_to_flight_price = total_price_for_weight * 0.4
total_price = total_price_for_weight + days_to_flight_price
final_price = total_price * count_of_baggage
print(f'The total price of bags is: {final_price:.2f} lv.')
