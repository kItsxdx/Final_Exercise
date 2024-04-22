#66111375 กฤษดา ขันตรี

class Friend:
    def __init__(self, name, highfive_dialogue, gift):
        self.name = name
        self.highfive_dialogue = highfive_dialogue
        self.gift = gift

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_highfive(self, dialogue):
        self.highfive_dialogue = dialogue

    def get_highfive(self):
        return self.highfive_dialogue

    def set_gift(self, gift):
        self.gift = gift

    def get_gift(self):
        return self.gift

    def highfive(self):
        print(f"{self.name} says: {self.highfive_dialogue}")

    def give_gift(self):
        print(f"{self.name} gives you {self.gift}")

    def print_detail(self):
        print(f'====== Monster ({self.name})Detail =========')
        print(f'Health:{self.highfive_dialogue}')
        print(f'Speech:{self.gift}')
        print(f'{self.name} raise his and says...')
        print(f'"We are friend now"')
        print(f'{self.name} give you Toy Bat')
