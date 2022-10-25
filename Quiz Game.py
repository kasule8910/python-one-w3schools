print("--------------------Welcome to my Quiz Game!------------------------")

UserInput = input("Do you want to play(yes/no)? ").lower()
score = 0
if UserInput != "yes":
    print("Thank you for passing by")
    quit()
    
print("#####Okay, Let's play######")

answer1 = input("1.What is CPU in full? \n")
if answer1.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer2 = input("2.Which programming language are you using? \n")
if answer2.lower() == "python":
    print("correct")
    score += 1
else:
    print("incorrect")

answer3 = input("3.Is python a general-purpose programming language(yes/no)? \n")
if answer3.lower() == "yes":
    print("correct")
    score += 1
else:
    print("incorrect")

answer4 = input("4.Is python a high-level programming language \n")
if answer4.lower() == "yes":
    print("correct")
    score += 1
else:
    print("incorrect")

answer5 = input("5.What is the name of this application? \n")
if answer5.lower() == "quiz game":
    print("correct")
    score += 1
else:
    print("incorrect")

answer6 = input("6.which framework of python do you wish to use? \n")
if answer6.lower() == "Django":
    print("Correct")
    score += 1
else:
    print("incorrect")

print("You got "+ str(score)+" or " + str((score / 6) * 100)+" % correct answers")
