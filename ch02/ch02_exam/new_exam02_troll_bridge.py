# Ch02 End of chapter test - 24/11/26
# Because I was not good enough and used help, I retry without help.

# CONSTANTS
PAYMENT = 20
DAMAGE_CHECK = 10
SWORD_BONUS = 2
RIDDLE = "What has teeth but never bites?"
RIDDLE_HINT = "This is an object used to fix your hair."
RIDDLE_ANSWER1 = "A comb"
RIDDLE_ANSWER2 = "comb"
CLASS1 = "Warrior"
CLASS2 = "Thief"
CLASS3 = "Mage"

CLASS1_DISPLAY = f"[1] - {CLASS1}"
CLASS2_DISPLAY = f"[2] - {CLASS2}"
CLASS3_DISPLAY = f"[3] - {CLASS3}"
GAME_TITLE = "The TROLL Bridge"
MENU_WIDTH = 25 + len(GAME_TITLE)
MENU_BAR1 = "#" * MENU_WIDTH
MENU_BAR2 = " " + "=" * (MENU_WIDTH - 4) + " "
CLASS_WIDTH = len(CLASS1_DISPLAY)
MENU_TITLE = f'''
{MENU_BAR1}
#{GAME_TITLE:^{MENU_WIDTH-2}}#
{MENU_BAR1}
#{"Welcome to the Troll Bridge!":^{MENU_WIDTH-2}}#
#{MENU_BAR2}#
#{"Please, select your class !":^{MENU_WIDTH-2}}#
#{MENU_BAR2}#
#{f"{CLASS1_DISPLAY:<{CLASS_WIDTH}}":^{MENU_WIDTH-2}}#
#{f"{CLASS2_DISPLAY:<{CLASS_WIDTH}}":^{MENU_WIDTH-2}}#
#{f"{CLASS3_DISPLAY:<{CLASS_WIDTH}}":^{MENU_WIDTH-2}}#
{MENU_BAR1}
'''

# VARIABLES
ending_score = 0
player_can_start = True
player_item = ""
player_strength = 0
player_gold = 0

player_have_sword = False
player_have_hook = False
player_have_scroll = False

troll_fight = False

# INPUT
player_name = input("What is your name ? : ")

print(MENU_TITLE)
player_choice = input("What do you choose ? : ")
match player_choice:
    case "1" | "Warrior" | "warrior":
        player_class = "Warrior"
    case "2" | "Thief" | "thief":
        player_class = "Thief"
    case "3" | "Mage" | "mage":
        player_class = "Mage"
    case _:
        player_class = "Invalid Class"
        player_can_start = False

if player_class == CLASS1:
    player_item = "Sword"
    player_have_sword = True
    player_gold = 10
    player_strength = 8
elif player_class == CLASS2:
    player_item = "Hook"
    player_have_hook = True
    player_gold = 20
    player_strength = 5
elif player_class == CLASS3:
    player_item = "Scroll"
    player_have_scroll = True
    player_gold = 15
    player_strength = 1

if player_have_sword:
    player_strength += SWORD_BONUS

INVENTORY_WIDTH = 2 + len(f'Class : {player_class}')
INVENTORY = f'''
{MENU_BAR1}
#{player_name:^{MENU_WIDTH-2}}#
#{MENU_BAR2}#
#{f"{f'Class : {player_class}':<{INVENTORY_WIDTH}}":^{MENU_WIDTH-2}}#
#{f"{f'Item : {player_item}':<{INVENTORY_WIDTH}}":^{MENU_WIDTH-2}}#
#{f"{f'Gold : {player_gold}':<{INVENTORY_WIDTH}}":^{MENU_WIDTH-2}}#
#{f"{f'Strength : {player_strength}':<{INVENTORY_WIDTH}}":^{MENU_WIDTH-2}}#
{MENU_BAR1}
'''

INTERACT_MENU_WIDTH = len(f'[3] - Answer')
INTERACT_MENU = f'''
{MENU_BAR2}
{"Choice":^{MENU_WIDTH}}
{MENU_BAR2}
{f"{f'[1] - Pay':<{INTERACT_MENU_WIDTH}}":^{MENU_WIDTH}}
{f"{f'[2] - Fight':<{INTERACT_MENU_WIDTH}}":^{MENU_WIDTH}}
{f"{f'[3] - Answer':<{INTERACT_MENU_WIDTH}}":^{MENU_WIDTH}}
{f"{f'[4] - Flee':<{INTERACT_MENU_WIDTH}}":^{MENU_WIDTH}}
{MENU_BAR2}
'''

if player_can_start:
    player_good_ending = False
    print(INVENTORY)
    input("Press Enter to continue...")
    print(f'''
*You are about to cross a bridge*
*Out of nowhere, a troll appears*
*He tells you*
- "Hey, you there!"
- "To get past me, you'll have to either pay me {PAYMENT} golds, fight me, or answer one of my riddles!"
    ''')
    input("Press Enter to continue...")
    print(INTERACT_MENU)
    player_choice = input("What do you do ? : ")
    match player_choice:
        case "1" | "Pay" | "pay":
            print("You decide to pay the troll.")
            input("Press Enter to continue...")
            if player_gold >= PAYMENT:
                player_gold -= PAYMENT
                print(f"You give him {PAYMENT} golds.")
                print(f"(Gold left: {player_gold})")
                print("")
                print("The troll seems satisfied.")
                print("He lets you pass.")
                player_good_ending = True
                ending_score += 10
            else:
                print(f"You don't have enough gold. ({player_gold}/{PAYMENT})")
                print("The troll gets angry.")
                troll_fight = True
        case "2" | "Fight" | "fight":
            troll_fight = True
        case "3" | "Answer" | "answer":
            print("You decide to solve the riddle.")
            input("Press Enter to continue...")
            print("The troll smiles and says")
            print(RIDDLE)
            if player_have_scroll:
                print("You have an advantage, thanks to your scroll, you have a hint!")
                print(RIDDLE_HINT)
            player_answer = input("What's your answer to the riddle? : ")
            if player_answer == RIDDLE_ANSWER1 or player_answer == RIDDLE_ANSWER2:
                print("You found the right answer!")
                print("The troll moves aside and lets you pass.")
                player_good_ending = True
                ending_score += 10
            else:
                print("That's not the right answer.")
                print("The troll lost patience.")
                troll_fight = True
        case "4" | "Flee" | "flee":
            print("You decide to flee.")
            input("Press Enter to continue...")
            print("You turn back and run away from the troll.")
        case _:
            print("Invalid Choice")
    if troll_fight:
        print("You're going to fight the troll.")
        print("To fight, you'll have to roll a 6-sided die.")
        input("Press Enter to continue...")
        player_dice = input("Which side of the die do you want to land on? (1-6) : ")
        if 1 <= int(player_dice) <= 6:
            player_fight = player_strength + int(player_dice)
            if player_fight >= DAMAGE_CHECK:
                print("You defeat the troll.")
                print("He staggers, steps aside, and lets you pass.")
                player_good_ending = True
                ending_score += 10
            else:
                print("He hits you really hard, and you pass out.")
        else:
            print("Invalid Choice")
    player_score = (player_gold * 2) + ending_score
    if player_good_ending:
        print(f"""
Congratulations! you made it across the troll bridge!
Your score : {player_score}
        """)
    if not player_good_ending:
        print(f"""
You weren't able to cross the bridge.
Your score : {player_score}
        """)
else :
    print("Error, please try again.")