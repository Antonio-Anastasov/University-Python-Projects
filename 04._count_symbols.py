txt = input()

unique_symbols = set()

for char in txt:
    unique_symbols.add(char)

for char in sorted(unique_symbols):
    print(f"{char}: {txt.count(char)} time/s")