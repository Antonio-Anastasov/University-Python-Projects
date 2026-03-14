tax_per_year = int(input())

basketball_shoes = tax_per_year - (tax_per_year * 0.4)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_clothes / 4
basketball_accsesoaries = basketball_ball / 5

final_price = basketball_accsesoaries + basketball_shoes + basketball_ball + basketball_clothes + tax_per_year

print(final_price)
