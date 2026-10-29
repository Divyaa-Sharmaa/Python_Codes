#The Boss Battle Capstone Project

import random

player_health = 50
player_potions = 3
dragon_health = 100

print("A wild Dragon appears!")

while dragon_health>0 and player_health>0:
    print(f"\nYour HP: {player_health} | Dragon HP: {dragon_health} | Potions: {player_potions}")
    action = input("want to attack(A) or heal(H)?: ").upper()
    if action == "A":
        print("You strike the Dragon for 15 damage!")
        dragon_health -= 15
    elif action=="H":
        if player_potions>0:
            player_health += 20
            player_potions -= 1 
        else:
            print("Out of Potions!!! pick something else")
            continue    
    else:
        print("Invalid move! You stumble and lose your turn.") 
        
    #The Dragon's turn:
    if dragon_health>0:
        dragon_damage = random.randint(5,15)
        print(f"The Dragon breathes fire and deals {dragon_damage} damage!")
        player_health -= dragon_damage      

print("\n--- BATTLE OVER ---")
if player_health<= 0:
    print("You died!!")
else:
    print("You slayed the Dragon!")    
                    