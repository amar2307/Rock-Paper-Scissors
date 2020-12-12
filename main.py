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

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user==0:
	print(rock)
elif user==1:
	print(paper)
elif user==2:
	print(scissors)
print("Computer chose:")
comp=random.randint(0,2)
if comp==0:
	print(rock)
elif comp==1:
	print(paper)
elif comp==2:
	print(scissors)

if user==0:
	if comp==0:
		print("It's a tie.")
	elif comp==1:
		print("You lose.")
	elif comp==2:
		print("You win!")

if user==1:
	if comp==0:
		print("You win!")
	elif comp==1:
		print("It's a tie.")
	elif comp==2:
		print("You lose.")

if user==2:
	if comp==0:
		print("You lose.")
	elif comp==1:
		print("You win!")
	elif comp==2:
		print("It's a tie.")