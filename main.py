import random
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
human_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if human_input < 0 or human_input > 2:
  print("Don\'t enter numbers out of scope!'")
  exit()

hands = [rock, paper, scissors]

print(hands[human_input])

computer_input = random.randint(0,2)

print(f"Computer chose: {hands[computer_input]}")
print(computer_input)
choice_matrix = [ ["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"], ["You lose", "You win", "It\'s a draw"] ]

print(choice_matrix[human_input][computer_input])
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