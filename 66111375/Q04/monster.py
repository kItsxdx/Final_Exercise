#66111375 กฤษดา ขันตรี
class Monster:
    def __init__(self, name, health, speech):
        self.name = name
        self.health = health
        self.speech = speech

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_speech(self, speech):
        self.speech = speech

    def get_speech(self):
        return self.speech

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def show_detail(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Speech: {self.speech}")