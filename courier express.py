weight = float(input())
service_type = input()
distance = int(input())

delivery_cost = 0

if service_type == "standard":
    if weight < 1:
        delivery_cost = distance * 0.03
    elif 1 <= weight < 10:
        delivery_cost = distance * 0.05
    elif 10 <= weight < 40:
        delivery_cost = distance * 0.10
    elif 40 <= weight < 90:
        delivery_cost = distance * 0.15
    else:
        delivery_cost = distance * 0.20
elif service_type == "express":
    if weight < 1:
        delivery_cost = distance * 0.03 + (distance * 0.03 * 0.80 * weight)
    elif 1 <= weight < 10:
        delivery_cost = distance * 0.05 + (distance * 0.05 * 0.40 * weight)
    elif 10 <= weight < 40:
        delivery_cost = distance * 0.10 + (distance * 0.10 * 0.05 * weight)
    elif 40 <= weight < 90:
        delivery_cost = distance * 0.15 + (distance * 0.15 * 0.02 * weight)
    else:
        delivery_cost = distance * 0.20 + (distance * 0.20 * 0.01 * weight)

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {delivery_cost:.2f} lv.")
