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

#Write your code below this line 👇
abc = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0,2)


if choice == 0 and computer_choice == 2:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You win")
elif choice == 2 and computer_choice == 0:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You lose")
elif choice == 0 and computer_choice == 1:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You lose")
elif choice == 1 and computer_choice == 0:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You win")

elif choice == 2 and computer_choice == 1:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You win")
elif choice == 1 and computer_choice == 2:
    print(abc[computer_choice])
    print("computer chose:")
    print(abc[choice])
    print("You lose")
else:
        print(abc[computer_choice])
        print("computer chose:")
        print(abc[choice])
        print("Draw game")