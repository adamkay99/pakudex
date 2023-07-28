class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity
        # Initializes the object as storing 0 pakuri, and to
        # contain exactly "capacity" objects when completely full.
        pass

    def get_size(self):
        # Returns # of critters currently being stored in the pakudex
        pass

    def get_capacity(self):
        # Returns # of critters that the pakudex has the capacity to hold at most
        return self.capacity
        pass

    def get_species_array(self):
        # Returns a string list containing the species of the critters
        # as ordered in the pakudex.
        # If there are no species added yet, this method should return None.
        pass

    def get_stats(self, species):
        # Returns an int list containing the attack, defense, and speed statistics
        # of species in that order.
        # If species DNE, return None
        pass

    def sort_pakuri(self):
        # Sorts pakuri objects in this pakudex according to
        # Python standard lexicographical ordering of species names.
        pass

    def add_pakuri(self):
        # Adds species to the pakudex
        # If successful, return True. Otherwise, return False.
        pass

    def evolve_species(self, species):
        # Attempts to evolve the corresponding Pakuri within the pakudex.
        # If successful, return True. Otherwise, return False.
        pass
