import random

'''
1. Adjust dice game
2. Adjust usable items
3. Add more accesbility options
4. Add another stat(Agility/Perception)
'''

def dice_game():
    user=input("\nDo you wish to throw the dice: ")

    while user not in ["yes", "no"]:
        print("\nInvalid input! Please answer with 'yes' or 'no'.")
        user = input("Do you wish to throw the dice (yes/no): ").lower()
    
    if user.lower()=="yes":
        custom_dice=None
        dice_amount=int(input("\nHow many dices do you wish to throw: "))
        print("1.D6")
        print("2.D8")
        print("3.D12")
        print("4.D20")
        print("5.Custom dice")
        dice_choice=input("What kind of dice do you wish to throw: ")

        result_int=0
        while user.lower()=="yes":
            print("\n---------=========+++++++=========---------")
            
            if dice_choice=="1" or dice_choice.lower()=="d6":
                dice=[1, 2, 3, 4, 5, 6,]
                dice_number=random.choice(dice)
                result_int = dice_amount * dice_number
                
            elif dice_choice=="2" or dice_choice.lower()=="d8":
                dice=[1, 2, 3, 4, 5, 6, 7, 8]
                dice_number=random.choice(dice)
                result_int = dice_amount * dice_number
                
            elif dice_choice=="3" or dice_choice.lower()=="d12":
                dice=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                dice_number=random.choice(dice)
                result_int = dice_amount * dice_number
                
            elif dice_choice=="4" or dice_choice.lower()=="d20":
                dice=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
                dice_number=random.choice(dice)
                result_int = dice_amount * dice_number

            elif dice_choice=="5" or dice_choice.lower()=="custom dice":
                if custom_dice==None:
                    sides=int(input("\nHow many sides does your dice have: "))
                    custom_dice=list(range(1, sides+1))
                dice_number=random.choice(custom_dice)
                result_int = dice_amount * dice_number

            else:
                print("\nWrong Input!")
                break

            print(f"\nThe number you rolled is {result_int}\n\n---------=========+++++++=========---------")

            user = input("\nDo you wish to throw the dice again? (yes/no): ").lower()
            
            while user not in ["yes", "no"]:
                print("\nInvalid input! Please answer with 'yes' or 'no'.")
                user = input("Do you wish to throw the dice again? (yes/no): ").lower()

            if user=="no":
                break

        return result_int
        
    else:
        print("You choose not to roll the dice")
        return 0

    
    
users=[]

print("Hello adventurer!")
while True:     
    try:
        number_of_users=int(input("\nHow many people will be venturing into dungeon: "))

        if number_of_users>0:
            for i in range(1, number_of_users+1):
                print("\n---------=========+++++++=========---------")
                name=input(f"\nWhat is your name adventurer {i}: ")
                users.append(name)

            print("\nThe adventure begins!")
            print("Each adventurer will take their turn to act.")
            break

        else:
            print("\n---------=========+++++++=========---------")
            print("\nWrong input! Number of users must be greater then 0!")
            
    except ValueError:
        print("\n---------=========+++++++=========---------")
        print("\nInvalid input! Number of users must be an integer!")

inventory=[]
hp=[100]*number_of_users
player_dmg=[10]*number_of_users
player_def=[0]*number_of_users

enemy = [
    {"name": "Goblin", "health": 30, "damage": 5},  # 3 goblins
    {"name": "Goblin", "health": 30, "damage": 5},
    {"name": "Goblin", "health": 30, "damage": 5},
    {"name": "Orc", "health": 50, "damage": 10},
    {"name": "Orc", "health": 50, "damage": 10},
    {"name": "Dragon", "health": 100, "damage": 20}
]
tresure=["sword", "shield", "health potion", "health potion", "health potion"]
reward=["sword", "shield", "health potion", "health potion", "health potion"]

def take_turn(player_name, player_index):
    
            if player_index >= len(hp) or hp[player_index] <= 0:  # Check if the player is eliminated
                print(f"\n{player_name} is eliminated and cannot take a turn!")
                return
            
            print(f"\n---------=========++++++=========---------\n\nIt's {player_name}'s turn!")
            print("Choose your action:")
            print("1. Roll a dice for bonus attack")
            print("2. Check your inventory")
            print("3. Rest and regain strength")
            print("4. Explore")
            action=int(input("What will you do? (1/2/3/4): "))

            for i in range(1, number_of_users+1):
                inventory.append([])

            if action==1:
                print("\nThrow D20 for optimal results!")
                result_int=dice_game()
                if result_int<10:
                    print("Number you rolled is too low!")
                elif result_int>=10 and result_int<=15:
                    new_dmg=player_dmg[player_index]+2
                    player_dmg[player_index]=min(new_dmg, 25)
                    print("\nYou succesfully incressed your dmg by 2!")
                    choice=input("Would you like to know your curent attack demage? (yes/no): ")
                    if choice=="yes":
                        print(f"\n{player_name}'s curent demage is {player_dmg[player_index]}!")
                    elif choice=="no":
                        print(f"\nEnding {player_name}'s turn!")
                    else:
                        print("\nWrong input! Ending this turn!")
                else:
                    new_dmg=player_dmg[player_index]+5
                    player_dmg[player_index]=min(new_dmg, 25)
                    print("You incressed your dmg by 5!!")
                    choice=input("Would you like to know your curent attack demage? (yes/no)")
                    if choice=="yes":
                        print(f"\n{player_name}'s curent demage is {player_dmg[player_index]}!")
                    elif choice=="no":
                        print(f"\nEnding {player_name}'s turn!")
                    else:
                        print("\nWrong input! Ending this turn!")

            if action==2:
                print(f"\n{player_name} chose to check their inventory!")
                print(f"Your inventory: {inventory[player_index]}")
                menage_inventory(player_name, player_index)

            if action==3:
                if hp[player_index]<100:
                    hp[player_index]+=10
                    print(f"\n---------=========+++++++=========---------\n\n{player_name} has gained 10 health by resting!")
                else:
                    print(f"\n---------=========+++++++=========---------\n\n{player_name}'s health is already full!")
                choice=input("Would you like to check your HP? (yes/no): ")
                if choice.lower()=="yes":
                    print(f"{player_name}'s curent HP is {hp[player_index]}")
                elif choice.lower()=="no":
                    print(f"Ending {player_name}'s turn!")
                else:
                    print(f"Invalid input, ending {player_name}'s turn")

            if action==4:
                has_fought=False
                while has_fought==False:
                    warning=input("\nAre you sure you want to proceed: ").lower()
                    if warning=="yes":
                        print(f"\n{player_name} has decided to proceed!")
                        outcome=random.choice(["enemy", "tresure"])
                        if outcome=="tresure":
                            found_tresure=random.choice(tresure)
                            print(f"\n{player_name} found a tresure: {found_tresure}")
                            inventory[player_index].append(found_tresure)
                            print(inventory[player_index])
                            break
                        elif outcome=="enemy":
                            encountered_enemy=random.choice(enemy)
                            print(f"\n{player_name} has encountered {encountered_enemy['name']}")
                            print(f"Stats: Health - {encountered_enemy['health']}, Damage - {encountered_enemy['damage']}")
                            choice=input("Do you wish to fight? (yes/no): ")
                            if choice=="yes":
                                combat_result=combat(player_name, player_index, encountered_enemy)
                                has_fought=True
                                if combat_result:
                                    prize=random.choice(reward)
                                    print("\n---------=========+++++++=========---------")
                                    print(f"\n{player_name} has got {prize} from fighting {encountered_enemy['name']}")
                                    inventory[player_index].append(prize)
                                else:
                                    print("\n---------=========+++++++=========---------")
                                    print(f"{player_name} lost the combat and receives no reward.")     
                            elif choice=="no":
                                print(f"{player_name} chose not to fight!")
                                has_fought=True
                    elif warning=="no":
                        print(f"{player_name} has decided not to proceed!")
                        break
                    else:
                        print("Invalid input! Please answer with 'yes' or 'no'.")
                     
def combat(player_name, player_index, enemy):
    player_health=hp[player_index]
    player_damage=player_dmg[player_index]
    enemy_health=enemy["health"]
    enemy_damage=enemy["damage"]

    print(f"{player_name} is fighting {enemy['name']}!")

    while player_health>0 and enemy_health>0:
        enemy_health-=player_damage
        print(f"\n{player_name} attacks! {enemy['name']} has {enemy_health} HP left!")
        if enemy_health<=0:
            print(f"\n{player_name} has defeated {enemy['name']}")
            hp[player_index] = player_health
            return True

        damage_taken = max(0, enemy_damage - player_def[player_index])
        player_health-=damage_taken
        print(f"{enemy['name']} attacks! {player_name} has {player_health} HP left!")
        if player_health<=0:
            print(f"\n{player_name} has been defetaed by {enemy['name']} and is eliminated!")
            hp[player_index] = player_health
            users.pop(player_index)
            hp.pop(player_index)
            player_dmg.pop(player_index)
            inventory.pop(player_index)
            return False
    return False
        
                
def menage_inventory(player_name, player_index):
    print("\nChoose your action!")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Use item")
    print("4. End your turn")
    choice=int(input("What would you like to do? (1/2/3): "))

    if choice==1:
        item=input("What would you like to add to your inventory: ")
        inventory[player_index].append(item)
        print(f"\n{item} has been added to your inventory!")

    elif choice==2:
        item=input("What would you like to remove from your inventory: ")
        if item in inventory[player_index]:
            inventory[player_index].remove(item)
            print(f"\n{item} has been successfully removed from your inventory!")
        else:
            print(f"\n{item} not found in your inventory!")

    elif choice==3:
        item=input("Which item would you like to use: ")
        if item.lower()=="health potion" and item.lower() in inventory[player_index]:
            hp[player_index]+=20
            inventory[player_index].remove("health potion")
            print("\n---------=========+++++++=========---------\nYour health has been increased by 20")
            check=input("Would you like to check your HP? (yes/no): ").lower()
            while True:
                if check.lower()=="yes":
                    print(f"\n{player_name}'s current HP is {hp[player_index]}!")
                    break
                elif check.lower()=="no":
                    print(f"Ending {player_name}'s turn!")
                    break
                else:
                    check=input("\nWrong input! Answer with 'yes' or 'no': ").lower()

        elif item.lower()=="health potion" and item.lower() not in inventory[player_index]:
            print("\nItem not found in your inventory! Ending this turn!")

        elif item.lower()=="sword" and item.lower() in inventory[player_index]:
            check=input("Are you sure you want to equip this item? YOU CANT CHANGE THIS LATER: ").lower()
            while True:
                if check.lower()=="yes":
                    player_dmg[player_index]+=10
                    print(f"\n---------=========+++++++=========---------\nYour dmg has been increased to{player_dmg[player_index]})")
                    break
                elif check.lower()=="no":
                    print(f"\nNo changes have been made! Ending {player_name}'s turn!")
                    break
                else:
                    check=input("\nWrong input! Answer with 'yes' or 'no': ").lower()

        elif item.lower()=="sword" and item.lower() not in inventory[player_index]:
            print("\nItem not found in your inventory! Ending this turn!")

        elif item.lower()=="shield" and item.lower() in inventory[player_index]:
            check=input("Are you sure you want to equip this item? YOU CANT CHANGE THIS LATER: ")
            while True:
                if check.lower()=="yes":
                    player_def[player_index]+=10
                    print(f"\n---------=========+++++++=========---------\nYour defence has been increased to{player_def[player_index]}")
                    break
                elif check.lower()=="no":
                    print(f"\nNo changes have been made! Ending {player_name}'s turn!")
                    break
                else:
                    check=input("\nWrong input! Answer with 'yes' or 'no': ").lower()

        elif item=="sword" and item not in inventory[player_index]:
            print(f"\nItem not found in your inventory! Ending {player_name}'s turn!")  

        else:
            print(f"\nWrong input! Ending {player_name}'s turn")

    elif choice==4:
        print(f"\nEnding {player_name}'s turn!")
        
round_number = 1
while True:
    print(f"\n--- Round {round_number} ---")

    for i in range(len(users)):
        if i<len(users):
            take_turn(users[i], i)

    if len(users)==0:
         print("\nAll adventurers have been eliminated. Game over!")
         break
        
    while True:
        continue_game = input("\nDo you want to continue adventuring? (yes/no): ").lower()
        if continue_game=="yes":
            round_number += 1
            break
        elif continue_game == "no":
            print("The adventurers decide to leave the dungeon. Farewell!")
            break
        else:
            print("\nInvalid input! Please answer with 'yes' or 'no'.")
    if continue_game=="no":
        break
