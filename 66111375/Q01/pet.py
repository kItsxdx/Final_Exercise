#6611375 กฤษดา ขันตรี

class Pet:
    def __init__(self, name, species, description):
        self.name = name
        self.species = species
        self.description = description

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Species: a {self.species} ")
        print(f"Description: {self.description}.")

    def print_upgrade_details(self):
        print(f"{self.name} is a {self.species} with {self.description}.")




