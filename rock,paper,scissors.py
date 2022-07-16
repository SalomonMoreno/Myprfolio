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

options = [rock,paper,scissors]

print("Welcome to rock, paper and scissors game!!!.\n")
print(f"0{rock}\n1{paper}\n2{scissors}")

user = int(input("What do your choose?\nType 0 for Rock, 1 for Paper or 2 for scissors.\n"))

import random
pc = random.randint(0,2)

if user <= 2 and user >=0:
    print(f"\nUser choice is {user}\n{options[user]}")
    print(f"\nPc choice is {pc}\n{options[pc]}")
  
    if user == 0 and pc == 2:
        print("You win")
    elif pc == 0 and user == 2: 
        print("You lose")
    elif user > pc:
        print("You win")
    elif pc > user: 
        print("You lose")
    elif user == pc:
        print("It is Draw")
    
else: 
    print("\nReally????\nDo you know how to read???\nYou wrote down an invalid number. Check it.")