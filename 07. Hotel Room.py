months = input()
nights = int(input())

studio = 0
apartment = 0

if months == 'May' or months == 'October':
    studio = 50
    apartment = 65

    if nights > 14:
        studio *= 0.70

    elif nights > 7:
        studio *= 0.95

elif months == 'June' or months == 'September':
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= 0.80

elif months == 'July' or months == 'August':
    studio = 76
    apartment = 77

if nights > 14:
    apartment *= 0.90

print(f"Apartment: {apartment * nights:.2f} lv.")
print(f"Studio: {studio * nights:.2f} lv.")