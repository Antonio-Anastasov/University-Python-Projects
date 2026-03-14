initial_energy = float(input())
energy = initial_energy
mountain_count = 0
artifact_pieces = 0

while True:
    terrain = input().strip().lower()

    if terrain == "journey ends here!":
        break

    if terrain == "mountain":
        energy -= 10
        mountain_count += 1
        if mountain_count % 3 == 0:
            artifact_pieces += 1
    elif terrain == "desert":
        energy -= 15
    elif terrain == "forest":
        energy += 7

    if energy <= 0:
        print("The character is too exhausted to carry on with the journey.")
        break

    if artifact_pieces == 3:
        print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
        break

if energy > 0 and artifact_pieces < 3:
    needed_pieces = 3 - artifact_pieces
    print(
        f"The character could not find all the pieces and needs {needed_pieces} more to complete the legendary artifact.")