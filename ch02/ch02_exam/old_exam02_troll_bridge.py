# Ch02 End of chapter test - 21/11/26
TOLL = 20
WIN_THRESHOLD = 10
SWORD_BONUS = 2
GOLD_MULTIPLIER = 2

PAY_BONUS = 10
FIGHT_BONUS = 20
RIDDLE_BONUS = 15
LOSS_BONUS = 0
FLEE_BONUS = 0

INVALID_ENDING = "The troll gets impatient and throws you into the river."

MENU_WIDTH = 30
BAR1 = "#" * MENU_WIDTH
BAR2 = "-" * MENU_WIDTH
MENU = f"""
{BAR1}
{"Choose your class !":^{MENU_WIDTH}}
{BAR2}
{"[1] Warrior"}
{"[2] Thief"}
{"[3] Mage"}
{BAR1}
"""

ending_message = INVALID_ENDING
ending_bonus = 0
score = 0

print(MENU)
player_choice = input("What is your class ? : ")
match player_choice:
    case "1" | "Warrior" | "warrior":
        player_class = "Warrior"
        player_weapon = "Sword"
        player_strength = 10 + SWORD_BONUS
        player_gold = 10
    case "2" | "Thief" | "thief":
        player_class = "Thief"
        player_weapon = "Hook"
        player_strength = 8
        player_gold = 15
    case "3" | "Mage" | "mage":
        player_class = "Mage"
        player_weapon = "Scroll"
        player_strength = 6
        player_gold = 20
    case _:
        player_class = ""
        player_weapon = ""
        player_strength = 0
        player_gold = 0

valid_game = player_class != ""
if valid_game:
    print(f"""
    You are a {player_class}, you have:
    - {player_gold} gold
    - {player_strength} strength
    - Item {player_weapon}

    A huge troll blocks your path.
    "Pay 20 coins, fight or answer my riddle!"
    """)
    action = input("What do you do ? (pay/fight/riddle/flee) : ")
    can_pay = player_gold >= TOLL
    must_fight = False

    match action:
        case "pay":
            if can_pay:
                player_gold -= TOLL
                ending_message = "You pay the toll and cross the bridge."
                ending_bonus = PAY_BONUS
            else:
                print("You don't have enough money, the troll is now angry.")
                must_fight = True
        case "fight":
            must_fight = True
        case "riddle":
            print("What has teeth but never bites?")
            if player_class == "Mage":
                print("Parchment index: it's used to style your hair.")
            answer = input("Your answer ? : ")
            if answer == "a comb" or answer == "comb":
                ending_message = "That is the right answer ! The troll steps aside, grumbling."
                ending_bonus = RIDDLE_BONUS
            else:
                ending_message = "The troll laughs at you and kills you."
                ending_bonus = LOSS_BONUS
        case "flee":
            ending_message = "You flee."
            ending_bonus = FLEE_BONUS
        case _:
            valid_game = False

    if must_fight:
        dice_choice = input("What do you roll ? (1-6): ")
        match dice_choice:
            case "1" | "2" | "3" | "4" | "5" | "6":
                dice_roll = int(dice_choice)
                if player_strength + dice_roll >= WIN_THRESHOLD:
                    ending_message = "Tu bats le troll et traverses le pont."
                    ending_bonus = FIGHT_BONUS
                else:
                    ending_message = "Le troll te terrasse au combat."
                    ending_bonus = LOSS_BONUS
            case _:
                valid_game = False

if valid_game:
    score = player_gold * GOLD_MULTIPLIER + ending_bonus

print(ending_message)
print(f"Score : {score}")