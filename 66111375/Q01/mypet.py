#6611375 กฤษดา ขันตรี

from pet import Pet

if __name__ == "__main__":
    print(f'-------- My Pet ---------')
    
    pet = Pet("Peter", "a Sun Conure", "medium-sized, predominantly gray, black-billed parrot")

# Display 
    pet.print_details()

    
    pet.set_name("Justin")

    
    pet.set_species("an African Gray")
    print(f'---------- Upgrade My Pet ----------')
    
    #pet.print_upgrade_details()

