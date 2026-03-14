deposit_sum = float(input())
term_of_the_deposit = int(input())
annual_interest_rate = float(input()) / 100

final_sum = deposit_sum + term_of_the_deposit * ((deposit_sum * annual_interest_rate)/12)

print(final_sum)
