def main():
    substances = list(map(int, input().split(', ')))
    crystals = list(map(int, input().split(', ')))

    potions = {
        "Brew of Immortality": 110,
        "Essence of Resilience": 100,
        "Draught of Wisdom": 90,
        "Potion of Agility": 80,
        "Elixir of Strength": 70
    }

    crafted_potions = []
    crafted_energies = set()

    while substances and crystals:
        substance = substances.pop()
        crystal = crystals.pop(0)

        total_energy = substance + crystal

        potion_crafted = False
        for potion, energy in potions.items():
            if total_energy == energy and energy not in crafted_energies:
                crafted_potions.append(potion)
                crafted_energies.add(energy)
                potion_crafted = True
                break

        if potion_crafted:
            if len(crafted_potions) == 5:
                break
            continue

        possible_potions = [p for p, e in potions.items() if e < total_energy and e not in crafted_energies]
        if possible_potions:
            possible_potions.sort(key=lambda x: potions[x], reverse=True)
            potion_to_craft = possible_potions[0]
            crafted_potions.append(potion_to_craft)
            crafted_energies.add(potions[potion_to_craft])
            crystal -= 20
            if crystal > 0:
                crystals.append(crystal)
        else:
            crystal -= 5
            if crystal > 0:
                crystals.append(crystal)

        if len(crafted_potions) == 5:
            break

    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
    else:
        print("The alchemist failed to complete his quest.")

    if crafted_potions:
        print(f"Crafted potions: {', '.join(crafted_potions)}")

    if substances:
        print(f"Substances: {', '.join(map(str, reversed(substances)))}")

    if crystals:
        print(f"Crystals: {', '.join(map(str, crystals))}")


if __name__ == "__main__":
    main()