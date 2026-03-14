
fat_percent = int(input())
protein_percent = int(input())
carbohydrate_percent = int(input())
total_calories = int(input())
percent_water = int(input())

fat_grams = (fat_percent / 100) * (total_calories / 9)
protein_grams = (protein_percent / 100) * (total_calories / 4)
carb_grams = (carbohydrate_percent / 100) * (total_calories / 4)

total_weight = fat_grams + protein_grams + carb_grams

water_factor = (100 - percent_water) / 100

total_weight_corrected = total_weight / water_factor

calories_per_gram = total_calories / total_weight_corrected


print(f"{calories_per_gram:.4f}")