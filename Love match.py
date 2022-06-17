print("Welcome to Match love!")
ready = input("Are you ready? Yes or Not\n")
ready = ready.lower()
if ready == "yes":
    name1 = input("What's your name?\n")
    name2 = input("What's his/her name?\n")
    pairname = name1 + name2
#count letters
    t = pairname.count("t")
    r = pairname.count("r")
    u = pairname.count("u")
    e = pairname.count("e")
    true = t + r + u + e

    l = pairname.count("l")
    o = pairname.count("o")
    v = pairname.count("v")
    e = pairname.count("e")
    love = l + o + v + e
# join numbers
    pair = int(str(true) + str(love))
  
    if pair <10 or pair >90:
        print(f"Your score is {pair}, think about it.")
    elif pair >40 and pair <50:
        print(f"Your score is {pair}, you should be together.")
    else:
        print(f"Your score is {pair}.")
  
else:
    print("Ok, see you later.")
