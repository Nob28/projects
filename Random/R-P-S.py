import random


choices = ['R' , 'P' , 'S']

win_against = {
    "R" : "P",
    "P" : "S",
    "S" : "R"
}

player_score = 0
computer_score = 0

print("🎮 Rock - Paper - Scissors Game 🎮")
print("First to 3 wins is the champion!")
print('R = Rock , P = Paper , S = Scissors \n')

while player_score < 3 and computer_score < 3:
    print(f"Score: Player {player_score} - {computer_score} Computer")

    computer_choice = random.choice(choices)
    player_choice = input('choose (R , P , S):').strip().capitalize().upper()


    if player_choice not in choices:
        print("Invalid input! Try again.\n")
        continue

    print(f"Computer chose: {computer_choice}")


    if player_choice == computer_choice :
        print("It's a draw!")
        expected_player_choice = win_against[player_choice]
        computer_second_choice = win_against[expected_player_choice]

    elif win_against[computer_choice] == player_choice:
        print("You won the first round!")
        player_score += 1

        expected_player_choice = win_against[player_choice]
        computer_second_choice = win_against[expected_player_choice]

    else:
        print("Computer won the first round!")
        computer_score += 1
        expected_player_choice = win_against[player_choice]
        computer_second_choice = win_against[expected_player_choice]

    if player_score ==  3 or  computer_score == 3:
        break


    print("\n--- Second Round ---")

    player_choice = input('choos (R , P , S):').strip().capitalize().upper()

    if player_choice not in choices:
        print("Invalid input! Try again.\n")
        continue

    print(f"Computer chose: {computer_choice}")
    if player_choice == computer_choice :
        print("It's a draw!")
        expected_player_choice = win_against[player_choice]
        computer_second_choice = win_against[expected_player_choice]

    elif win_against[computer_choice] == player_choice:
        print("You won the second round!")
        player_score += 1

        expected_player_choice = win_against[player_choice]
        computer_second_choice = win_against[expected_player_choice]

    else:
        print('Computer won the second round!')
        computer_score += 1

    print("\n--- Second Round ---")

if player_choice == 3:
        print("🏆 Congratulations! You are the champion! 🏆")

else:
    print("🤖 Computer is the champion! Better luck next time!")
