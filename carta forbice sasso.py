#setup
import random

possible_actions = ("sasso", "carta", "forbice")


#start
print("Let's play some sasso carta forbice")

computer_points = 0

player_points = 0

#pick
computer_pick = random.choice(possible_actions)

player_pick =input("Type: Sasso, Carta, Forbice or q to quit ").lower()
if player_pick == "q":
  quit


#pareggio
elif player_pick == computer_pick:
  print("The computer has chosen", computer_pick, "it's a tie")
  print("You have", player_points, "and the computer has")


#vittorie
if player_pick == "sasso":
  if computer_pick == "forbice":
    print("The computer has chosen", computer_pick, "you won!")
  print("You have", player_points+1, "and the computer has", computer_points)

if player_pick == "carta":
  if computer_pick == "sasso":
    print("The computer has chosen", computer_pick, "you won!")
  print("You have", player_points+1, "and the computer has", computer_points)

if player_pick == "forbice":
  if computer_pick == "carta":
    print("The computer has chosen", computer_pick, "you won!")
  print("You have", player_points+1, "and the computer has", computer_points)


#sconfitte  
if player_pick == "forbice":
  if computer_pick == "sasso":
    print("The computer has chosen", computer_pick, "you lost!")
  print("You have", player_points, "and the computer has", computer_points+1)

if player_pick == "carta":
  if computer_pick == "sasso":
    print("The computer has chosen", computer_pick, "you lost!")
  print("You have", player_points, "and the computer has", computer_points+1)

if player_pick == "carta":
  if computer_pick == "forbice":
    print("The computer has chosen", computer_pick, "you lost!")
  print("You have", player_points, "and the computer has", computer_points+1)
