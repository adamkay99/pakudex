from pakudex import Pakudex


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                raise ValueError
            break
        except:
            print("Please enter a valid size.")
    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {pakudex.get_capacity()} species of Pakuri.")
    _menu(pakudex, capacity)


def _menu(paku, capacity):
    print("\nPakudex Main Menu"
          "\n-----------------"
          "\n1. List Pakuri"
          "\n2. Show Pakuri"
          "\n3. Add Pakuri"
          "\n4. Evolve Pakuri"
          "\n5. Sort Pakuri"
          "\n6. Exit")
    while True:
        try:
            user_input = int(input("\nWhat would you like to do? "))
            break
        except:
            print("Unrecognized menu selection!")
            _menu(paku, capacity)
    if user_input == 1:
        if paku.get_size() == 0:
            print("No Pakuri in Pakudex yet!")
            _menu(paku, capacity)
        else:
            print("\nPakuri In Pakudex: ")
            for i in paku.get_species_array():
                print(f"{paku.get_species_array().index(i) + 1}. {i}")
            _menu(paku, capacity)
    elif user_input == 2:
        species_to_display = input("Enter the name of the species to display: ")
        if len(paku.pakudex) == 0:
            print("Error: No such Pakuri!")
            _menu(paku, capacity)
        for i in paku.pakudex:
            if i.get_species() == species_to_display:
                print(f"\nSpecies: {i.get_species()}")
                print(f"Attack: {i.get_attack()}")
                print(f"Defense: {i.get_defense()}")
                print(f"Speed: {i.get_speed()}")
                _menu(paku, capacity)
        print("Error: No such Pakuri!")
        _menu(paku, capacity)
    elif user_input == 3:
        # Add Pakuri (i.e. initialize pakuri class object)
        if len(paku.pakudex) >= paku.capacity:
            print("Error: Pakudex is full!")
            _menu(paku, capacity)
        species_to_add = input("Enter the name of the species to add: ")
        paku.add_pakuri(species_to_add)
        _menu(paku, capacity)
    elif user_input == 4:
        pakuri_to_evolve = input("Enter the name of the species to evolve: ")
        paku.evolve_species(pakuri_to_evolve)
        _menu(paku, capacity)
    elif user_input == 5:
        paku.sort_pakuri()
        print("Pakuri have been sorted!")
        _menu(paku, capacity)
    elif user_input == 6:
        print("Thanks for using Pakudex! Bye!")
        exit()
    else:
        print("Unrecognized menu selection!")
        _menu(paku, capacity)


if __name__ == "__main__":
    main()
