# Source: https://github.com/RattusRattusRattus/Rock-Paper-Scissors
import random
import time
choice = input("Enter rock, paper or scissors or type one two or three: ")
print ("‎")
if choice == "rock" or choice == "Rock" or choice == "1" or choice == "one" or choice == "One":
    choice = "Rock"
if choice == "paper" or choice == "Paper" or choice == "2" or choice == "two" or choice == "Two":
    choice = "Paper"
if choice == "scissors" or choice == "Scissors" or choice == "3" or choice == "three" or choice == "Three":
    choice = "Scissor"
computer_choice = str(random.randint(1,3))
if  computer_choice == "1":
    computer_choice = "Rock"
if computer_choice == "2":
    computer_choice = "Paper"
if computer_choice == "3":
    computer_choice = "Scissors"
time.sleep(1)
print ("You choose " + choice)
print ("‎")
time.sleep(1)
print ("The computer chooses " + computer_choice)
print ("‎")
time.sleep(1)
if choice == "Rock" and computer_choice == "Paper":
    print("The computer wins!")
if choice == "Rock" and computer_choice == "Rock":
    print ("It is a Draw!")
if choice == "Rock" and computer_choice == "Scissors":
    print ("You win!")
if choice == "Paper" and computer_choice == "Paper":
    print ("It is a Draw!")
if choice == "Paper" and computer_choice == "Scissors":
    print ("The computer wins!")
if choice == "Paper" and computer_choice == "Rock":
    print ("You win!")
if choice == "Scissors" and computer_choice == "Rock":
    print ("The computer wins!")
if choice == "Scissors" and computer_choice == "Paper":
    print ("You win!")
if choice == "Scissors" and computer_choice == "Scissors":
    print ("It is a Draw!")