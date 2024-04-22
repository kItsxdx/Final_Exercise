#66111375 กฤษดา ขันตรี
from friend import Friend
from monster import Monster
from enermy import Enemy


if __name__ == "__main__":
    

    friend_1 = Friend("Dave", "50", "Hi Let'be friend")
    friend_1.print_detail()
    

    monster_1 = Monster("Gobin",90,"GO GO")
    monster_1.show_detail()
    monster_1.take_damage(70)
    
    enmy_1 = Enemy("Payut",800,"Go the hell i will to kill you","Fucking eat everything","Power")
    enmy_1.print_detail()
    enmy_1.take_damage(900)
    

    
    



    









    


