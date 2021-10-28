import random
# computer_input = random.randint(0,2)
# print(computer_input)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def saveResult(result, score):
    if(result == "You win"):
        #guardar variable
        score[0] = score[0] + 1
        player = open("scoreplayer.py", "w")
        player.write(str(score[0]))
        player.close()
    if(result == "You lose"):
        #guardar variable
        score[1] = score[1] + 1
        computer = open("scorecomputer.py","w")
        computer.write(str(score[1]))
        computer.close()

def loadGame(score):
    #load player score
    try:
        player = open("scoreplayer.py", "r")
        score[0] = int(player.read())
        player.close()
    except:
        score[0] = 0
    
    #load computer score
    try:
        computer = open("scorecomputer.py", "r")
        score[1] = int(computer.read())
        computer.close()
    except:
        score[1] = 0
    print(f"The player won {score[0]} and the computer won {score[1]}")

#first value-> player score
#second value-> computer score
 
score = [0, 0]
loadGame(score)
playAgain = True
while playAgain:
    humanPick = True
    while humanPick:
        human_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
        if human_input < 0 or human_input > 2:
            print("Don\'t enter numbers out of scope!'")
        else:
            humanPick = False

    hands = [rock, paper, scissors]

    print(hands[human_input])

    computer_input = random.randint(0,2)

    print(f"Computer chose: {hands[computer_input]}")
    print(computer_input)
    choice_matrix = [ ["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"], ["You lose", "You win", "It\'s a draw"] ]
    result = choice_matrix[human_input][computer_input]
    
    print(result)
    saveResult(result, score)
    userChoice = input("Do you want to play again? type n or no to exit the program: ").lower()
    if userChoice == "n" or userChoice == "no":
        playAgain = False

# human_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
# computer_input = random.randint(0,2)
# hands = [rock, paper, scissors]
# if human_input >= 3 or human_input < 0:
#   print("You typed an invalid number, you lose")
# else:
#   print(hands[human_input])
#   print("Computer chose:")
#   print(hands[computer_input])
#   if human_input == 0 and computer_input == 2:
#     print("You win.")
#   elif human_input == 2 and computer_input == 0:
#     print("You lose.")
#   elif computer_input > human_input:
#     print("You lose.")
#   elif human_input > computer_input:
#     print("You win.")
#   elif human_input == computer_input:
#     print("It's a draw")