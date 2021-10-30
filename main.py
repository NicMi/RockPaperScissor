import random
import json
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
        score["userScore"] = score["userScore"] + 1   
    if(result == "You lose"):
        score["computerScore"] = score["computerScore"] + 1
    
    with open("scoreBoard.json", "w") as file:
     json.dump(score,file, indent = 4)
     
def loadGame(score):
    try:
        with open("scoreBoard.json", "r") as file:
           score = json.load(file)
    except:
        score["userScore"] = 0
        score["computerScore"] = 0
    print(f"The player won {score['userScore']} and the computer won {score['computerScore']}")
#first value-> player score
#second value-> computer score

#Init 
score = dict(userScore = 0, computerScore = 0)
loadGame(score)

playAgain = True
while playAgain:
    humanPick = True
    #check the input
    while humanPick:
        human_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
        if human_input < 0 or human_input > 2:
            print("Don\'t enter numbers out of scope!'")
        else:
            humanPick = False

    hands = [rock, paper, scissors]

    print(hands[human_input])

    computer_input = random.randint(0,2)
    
    #compare result
    print(f"Computer chose: {hands[computer_input]}")
    print(computer_input)
    choice_matrix = [ ["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"], ["You lose", "You win", "It\'s a draw"] ]
    result = choice_matrix[human_input][computer_input]
    
    print(result)
    if result != "It\'s a draw":
        saveResult(result, score)
    
    #Check for play again
    print(f"The player won {score['userScore']} and the computer won {score['computerScore']}")
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