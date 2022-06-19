print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\nYour journey starts here.")
first_path = input("You are in front of an huge island. \"Go forward\", \"turn left\" or \"right\"?\n").lower()
if first_path == "go forward":
  print("You did not expect a huge hole, you fell and died.")
elif first_path == "turn left":
  print("You found a hand-made boat when you had taken a seek around. You got a map from the boat.")
  sec_answer = input("Do you follow its instructions? \"Yes\" or \"not\"\n").lower()
  if sec_answer == "yes":
    print("You followed the path marked on the sheet, suddenly you fell into quicksands so you died alone and wet.")
  else:
    print("You took a little look around yourself and... there is a red flag a few meters from you. You approched to there slowly.")
    th_answer = input("Do you get the flag off from the palm? it looks so difficult. \"Yes\" or \"Not\"?.\n").lower()
    if th_answer == "yes":
      print("A hidden-door is opened, you just found a treasure. Congratulations. You won.")
    else:
      print("You did not take risks and now you lost.")
else:
  print("A snake crossed on your way and it bited you, it's poisonous. You die.")