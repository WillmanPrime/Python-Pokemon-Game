from random import randint
from time import sleep
print "Choose your Pokemon:"
print "Grass Type:"
print "1. Bulbasaur 2. Chikorita 3. Victreebel"
print "Flying Type:"
print "4. Spearow 5. Butterfree 6. Pidgeotto"
print "Ground Type:"
print "7. Onix 8. Sandshrew 9. Geodude"
print "Ghost Type:"
print "10. Haunter 11. Dusknoir 12. Sableye"
print "Nomral Type:"
print "13. Rattata 14. Eevee 15. Snorlax"
print "Fire Type:"
print "16. Charmander 17. Arcanine 18. Torchic"
print "Water Type:"
print "19. Squirtle 20. Poliwag 21. Goldeen"
choice = input("Enter the number associated with the Pokemon you like to choose... ")
choice2 = randint(1,21)

def switch_human(choice):
    switcher = {
        1: "You chose Bulbasaur",
        2: "You chose Chikorita",
        3: "You chose Victreebel",
        4: "You chose Spearow",
        5: "You chose Butterfree",
        6: "You chose Pidgeotto",
        7: "You chose Onix",
        8: "You chose Sandshrew",
        9: "You chose Geodude",
        10: "You chose Haunter",
        11: "You chose Dusknoir",
        12: "You chose Sableye",
        13: "You chose Rattata",
        14: "You chose Eevee",
        15: "You chose Snorlax",
        16: "You chose Charmander",
        17: "You chose Arcanine",
        18: "You chose Torchic",
        19: "You chose Squirtle",
        20: "You chose Poliwag",
        21: "You chose Goldeen",
    }
    return switcher.get(choice)
def switch_computer(choice2):
    switcher = {
        1: "AI chose Bulbasaur",
        2: "AI chose Chikorita",
        3: "AI chose Victreebel",
        4: "AI chose Spearow",
        5: "AI chose Butterfree",
        6: "AI chose Pidgeotto",
        7: "AI chose Onix",
        8: "AI chose Sandshrew",
        9: "AI chose Geodude",
        10: "AI chose haunter",
        11: "AI chose Dusknoir",
        12: "AI chose Sableye",
        13: "AI chose Rattata",
        14: "AI chose Eevee",
        15: "AI chose Snorlax",
        16: "AI chose Charmander",
        17: "AI chose Arcanine",
        18: "AI chose Torchic",
        19: "AI chose Squirtle",
        20: "AI chose Poliwag",
        21: "AI chose Goldeen"
    }
    return switcher.get(choice2)
print switch_human(choice)
print switch_computer(choice2)
Player_HP = 1200
Opponent_HP = 1200
Pmove1 = 10
Pmove2 = 5
Pmove3 = 2
Omove1 = 10
Omove2 = 5
Omove3 = 2
def grass_moves_human(choice2,move1,move2,move3,HP):
    print "1. Leaf Blade", move1
    print "2. Bullet Seed", move2
    print "3. Frenzy Plant", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Leaf Blade Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Bullet Seed Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Frenzy Plant Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(7,10) or choice2 in range(19,22):
        if move_number == 1:
            print "You used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(4,7) or choice2 in range(16,19) or choice2 in range(1,4):
        if move_number == 1:
            print "You used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def flying_moves_human(choice2,move1,move2,move3,HP):
    print "1. Air Cutter", move1
    print "2. Aeroblast", move2
    print "3. Dragon Ascent", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Air Cutter Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Aeroblast Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Dragon Ascent Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(1,4):
        if move_number == 1:
            print "You used Air Cutter"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Aeroblast"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Dragon Ascent"
            move3 -= 1
            HP -= randint(0, 550)
    else:
        if move_number == 1:
            print "You used Air Cutter"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Aeroblast"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Dragon Ascent"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def ground_moves_human(choice2,move1,move2,move3,HP):
    print "1. Bone Rush", move1
    print "2. Drill Run", move2
    print "3. Precipice Blades", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Bone Rush Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Drill Run Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Precipice Blades Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(16,19):
        if move_number == 1:
            print "You used Bone Rush"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Drill Run"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(1,7):
        if move_number == 1:
            print "You used Bone Rush"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Drill Run"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Bone Rush"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Drill Run"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP
def ghost_moves_human(choice2,move1,move2,move3,HP):
    print "1. Astonish", move1
    print "2. Ominous Wind", move2
    print "3. Shadow Force", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Astonish Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Ominous Wind Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Shadow Force Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(10,13):
        if move_number == 1:
            print "You used Astonish"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Shadow Force"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13,16):
        if move_number == 1:
            print "You used Astonish"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Shadow Force"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Astonish"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Shadow Force"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP
def normal_moves_human(choice2,move1,move2,move3,HP):
    print "1. Double Hit", move1
    print "2. Crush Claw", move2
    print "3. Boomburst", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Double Hit Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Crush Claw Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Boomburst Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(10,14):
        if move_number == 1:
            print "You used Double Hit"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Crush Claw"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Boomburst"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Double Hit"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Crush Claw"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Boomburst"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP
def fire_moves_human(choice2,move1,move2,move3,HP):
    print "1. Ember", move1
    print "2. Fire Pledge", move2
    print "3. Flare Blitz", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Ember Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Fire Pledge Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Flare Blitz Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(10,13):
        if move_number == 1:
            print "You used Ember"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13,16):
        if move_number == 1:
            print "You used Ember"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Ember"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP
def water_moves_human(choice2,move1,move2,move3,HP):
    print "1. Aqua Jet", move1
    print "2. Bubble Beam", move2
    print "3. Hydro Cannon", move3
    move_number = input("Enter move number... ")
    if move1 == 0:
        if move_number == 1:
            print "Aqua Jet Unavailable"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "Bubble Beam Unavailable"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "Hydro Cannon Unavailable"
            return move1,move2,move3,HP
    if choice2 in range(7,10) or choice2 in range(16,19):
        if move_number == 1:
            print "You used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "You used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "You used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13,16):
        if move_number == 1:
            print "You used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "You used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "You used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "You used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "You used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "You used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def grass_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Leaf Blade", move1
    print "2. Bullet Seed", move2
    print "3. Frenzy Plant", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(7, 10) or choice2 in range(19, 22):
        if move_number == 1:
            print "AI used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(4, 7) or choice2 in range(16, 19) or choice2 in range(1, 4):
        if move_number == 1:
            print "AI used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Leaf Blade"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Bullet Seed"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Frenzy Plant"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def flying_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Air Cutter", move1
    print "2. Aeroblast", move2
    print "3. Dragon Ascent", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(1, 4):
        if move_number == 1:
            print "AI used Air Cutter"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Aeroblast"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Dragon Ascent"
            move3 -= 1
            HP -= randint(0, 550)
    else:
        if move_number == 1:
            print "AI used Air Cutter"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Aeroblast"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Dragon Ascent"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def ground_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Bone Rush", move1
    print "2. Drill Run", move2
    print "3. Precipice Blades", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(16, 19):
        if move_number == 1:
            print "AI used Bone Rush"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Drill Run"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(1, 7):
        if move_number == 1:
            print "AI used Bone Rush"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Drill Run"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Bone Rush"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Drill Run"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Precipice Blades"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def ghost_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Astonish", move1
    print "2. Ominous Wind", move2
    print "3. Shadow Force", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(10, 13):
        if move_number == 1:
            print "AI used Astonish"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Shadow Force"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13, 16):
        if move_number == 1:
            print "AI used Astonish"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Shadow Force"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Astonish"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Ominous Wind"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Shadow Force"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def normal_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Double Hit", move1
    print "2. Crush Claw", move2
    print "3. Boomburst", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(10, 14):
        if move_number == 1:
            print "AI used Double Hit"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Crush Claw"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Boomburst"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Double Hit"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Crush Claw"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Boomburst"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def fire_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Ember", move1
    print "2. Fire Pledge", move2
    print "3. Flare Blitz", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(10, 13):
        if move_number == 1:
            print "AI used Ember"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13, 16):
        if move_number == 1:
            print "AI used Ember"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Ember"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Fire Pledge"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Flare Blitz"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def water_moves_ai(choice2, move1, move2, move3, HP):
    print "1. Aqua Jet", move1
    print "2. Bubble Beam", move2
    print "3. Hydro Cannon", move3
    move_number = randint(1,3)
    if move1 == 0:
        if move_number == 1:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move2 == 0:
        if move_number == 2:
            print "AI Missed!"
            return move1,move2,move3,HP
    if move3 == 0:
        if move_number == 3:
            print "AI Missed!"
            return move1,move2,move3,HP
    if choice2 in range(7, 10) or choice2 in range(16, 19):
        if move_number == 1:
            print "AI used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 250)
        elif move_number == 2:
            print "AI used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 500)
        elif move_number == 3:
            print "AI used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 550)
    elif choice2 in range(13, 16):
        if move_number == 1:
            print "AI used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 50)
        elif move_number == 2:
            print "AI used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 50)
        elif move_number == 3:
            print "AI used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 50)
    else:
        if move_number == 1:
            print "AI used Aqua Jet"
            move1 -= 1
            HP -= randint(0, 150)
        elif move_number == 2:
            print "AI used Bubble Beam"
            move2 -= 1
            HP -= randint(0, 200)
        elif move_number == 3:
            print "AI used Hydro Cannon"
            move3 -= 1
            HP -= randint(0, 250)
    return move1,move2,move3,HP

def the_game(php,ohp,pmove1,pmove2,pmove3,omove1,omove2,omove3,choice,choice2):
    if pmove1+pmove2+pmove3 == 0 and omove1+omove2+omove3 == 0:
        print "Nobody has moves left! Match draw!"
        return
    elif pmove1+pmove2+pmove3 == 0:
        print "No moves left. Opponent's turn!"
    elif php <= 0:
        print "You lose!"
        return
    else:
        if choice in range(1,4):
            pmove1,pmove2,pmove3,ohp = grass_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
        if choice in range(4, 7):
            pmove1,pmove2,pmove3,ohp = flying_moves_human(choice2, pmove1, pmove2, pmove3, ohp)
        if choice in range(7,10):
            pmove1,pmove2,pmove3,ohp = ground_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
        if choice in range(10,13):
            pmove1,pmove2,pmove3,ohp = ghost_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
        if choice in range(13,16):
            pmove1,pmove2,pmove3,ohp = normal_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
        if choice in range(16,19):
            pmove1,pmove2,pmove3,ohp = fire_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
        if choice in range(19,22):
            pmove1,pmove2,pmove3,ohp = water_moves_human(choice2,pmove1,pmove2,pmove3,ohp)
    print "Player HP is {} and Opponent HP is {}".format(php,ohp)

    if omove1+omove2+omove3 == 0:
        print "Opponent has no moves left. Your turn!"
    elif ohp <= 0:
        print "You win!"
        return
    else:
        print "Opponent is attacking..."
        sleep(2)
        if choice2 in range(1,4):
            omove1,omove2,omove3,php = grass_moves_ai(choice2,omove1,omove2,omove3,php)
        if choice2 in range(4, 7):
            omove1,omove2,omove3,php = flying_moves_ai(choice2, omove1, omove2, omove3, php)
        if choice2 in range(7,10):
            omove1,omove2,omove3,php = ground_moves_ai(choice2,omove1,omove2,omove3,php)
        if choice2 in range(10,13):
            omove1,omove2,omove3,php = ghost_moves_ai(choice2,omove1,omove2,omove3,php)
        if choice2 in range(13,16):
            omove1,omove2,omove3,php = normal_moves_ai(choice2,omove1,omove2,omove3,php)
        if choice2 in range(16,19):
            omove1,omove2,omove3,php = fire_moves_ai(choice2,omove1,omove2,omove3,php)
        if choice2 in range(19,22):
            omove1,omove2,omove3,php = water_moves_ai(choice2,omove1,omove2,omove3,php)
    print "Player HP is {} and Opponent HP is {}".format(php, ohp)
    return the_game(php,ohp,pmove1,pmove2,pmove3,omove1,omove2,omove3,choice,choice2)

the_game(Player_HP,Opponent_HP,Pmove1,Pmove2,Pmove3,Omove1,Omove2,Omove3,choice,choice2)