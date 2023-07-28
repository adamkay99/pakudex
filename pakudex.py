from pakuri import Pakuri


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakudex = []
        # IMPORTANT: I need my list to be a list of class objects, not just strings of the
        # species. This is so I can save my stats for each pakuri along the way.
        # Initializes the object as storing 0 pakuri, and to
        # contain exactly "capacity" objects when completely full.

    def get_size(self):
        # Returns # of critters currently being stored in the pakudex
        return len(self.pakudex)

    def get_capacity(self):
        # Returns # of critters that the pakudex has the capacity to hold at most
        return self.capacity

    def get_species_array(self):
        # Returns a string list containing the species of the critters
        # as ordered in the pakudex.
        # If there are no species added yet, this method should return None.
        if len(self.pakudex) == 0:
            return None
        else:
            names_list = []
            for i in self.pakudex:
                names_list.append(i.get_species())
            return names_list

    def get_stats(self, species):
        # Returns an int list containing the attack, defense, and speed statistics
        # of species in that order.
        # If species DNE, return None
        stat_list = []
        for i in self.pakudex:
            if i.get_species() == species:
                stat_list.append(i.get_attack())
                stat_list.append(i.get_defense())
                stat_list.append(i.get_speed())
                return stat_list
        return None  # This will only execute if the species is not found in the pakudex.

    def sort_pakuri(self):
        # Sorts pakuri objects in this pakudex according to
        # Python standard lexicographical ordering of species names.
        self.pakudex.sort()

    def add_pakuri(self, species):
        # Adds species to the pakudex
        # If successful, return True. Otherwise, return False.
        list_of_pakuri = self.get_species_array()
        if len(self.pakudex) == 0:
            self.pakudex.append(Pakuri(species))
            print(f"Pakuri species {species} successfully added!")
            return True
        elif species in list_of_pakuri:
            print("Error: Pakudex already contains this species!")
            return False
        elif len(list_of_pakuri) >= self.capacity:
            print("Error: Pakudex is full!")
            return False
        else:
            self.pakudex.append(Pakuri(species))
            print(f"Pakuri species {species} successfully added!")
            return True

    def evolve_species(self, species):
        # Attempts to evolve the corresponding Pakuri within the pakudex.
        # If successful, return True. Otherwise, return False.
        for i in self.pakudex:
            if i.get_species() == species:
                i.evolve()
                print(f"{species} has evolved!")
                return True
        print("Error: No such Pakuri!")
        return False
