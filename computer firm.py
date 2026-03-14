n = int(input())
total_sales = 0
total_rating = 0
models = 0
for _ in range(n):
    model = int(input())
    sale = model // 10
    rating = model % 10
    total_rating += rating
    models += 1
    if rating == 2:
        total_sales += 0
    elif rating == 3:
        total_sales += 0.5 * sale
    elif rating == 4:
        total_sales += 0.7 * sale
    elif rating == 5:
        total_sales += 0.85 * sale
    elif rating == 6:
        total_sales += 1 * sale

average_rating = total_rating / models

print(f"{total_sales:.2f}")
print(f"{average_rating:.2f}")
