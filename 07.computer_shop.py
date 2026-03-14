budget = float(input())

video_card_count = int(input())
procesor_count = int(input())
ram_count = int(input())

VIDEO_CARD_PRICE = 250
video_card_price = video_card_count * VIDEO_CARD_PRICE
procesor_price = procesor_count * video_card_price * 0.35
ram_price = ram_count * video_card_price * 0.10

total_price = video_card_price + procesor_price + ram_price

if video_card_count > procesor_count:
    total_price *= 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")