# File: CS112_A1_T2_3_20231225.py
# Purpose: Subtract-A-Square a Game : It's a two player mathematical game where a pile of coins (or other tokens) is presented. players take turns removing a non-zero squared number of coins (1, 4, 9, etc.) from the pile. The player who removes the last coin wins
# Author: Somaya Tamer Magdy Shoaib
# ID: 20231225


# Function to check if the given value is a postive integer
def Postive_integer_or_not(numb):
  if str(numb).isdigit() :
     int_numb= int(numb)
     if int_numb> 0 :
        return True
     elif int_numb <= 0 :
        return False
  else : 
     return False

# Function to check whether the given value is a non-zero squared number or not
import math
def Squared_numb_or_not (value):
    value= float(value)
    root=math.sqrt(value)
    if root > 0 and root.is_integer() :
       return True  
    else:
        return False     

# Function to generate a random number between specified values of 1 and 300
import random
def Random_numb_generator ():
 list_range = list(range(1,301))
 random_num= random.choice(list_range)
 return random_num
   

# Main game loop
while True:
   # First Menu  
   print('** Welcome to "Subtract-A-Square" Game! **')
   print("A) Play")
   print("B) How to play")
   print("C) Exit")
   option = input("Please enter your choice (A/B/C):")

   if option == 'A' or option=='a':
     while True:
         # Second Menu
         print("A) Generate a random number of tokens")
         print("B) Enter number of tokens")
         other_option= input("Please enter your choice (A/B):")

         if other_option== 'A' or other_option== 'a':
            # Generate a random number of tokens using the specified function
            initial = Random_numb_generator()
            print(f"Initial number of tokens is:{initial}")
            break
         elif other_option=='B' or other_option=='b':    
            # Players enter the initial number of tokens
            initial= input("Enter initial number of tokens:")

            # Check if the input is a valid postive number
            while not Postive_integer_or_not(initial):
              print ("** Please insert a valid postive integer **")
              initial= input("Enter initial number of tokens:")
            break
         else:
            print("** Invalid, Please enter A or B ** ")

      # Loop for both players' turn
     while int(initial) > 0 :
         # Player 1's turn
         player_1= input ("Player 1 enter a squared number: ")

         # Check if player 1's input is a valid postive squared number that is greater than the number of tokens
         if not Postive_integer_or_not(player_1):
            print ("** Please enter a valid squared number **")
            continue
         elif not Squared_numb_or_not(player_1):
            print ("** Please enter a valid squared number **")
            continue
         elif int(player_1)> int(initial):
            print ("** Please enter a valid squared number less than the number of tokens in the pile**")
            continue
         else :
            initial=int(initial) # In case of the players entering the initial number of tokens, we convert str to int so subtraction would be valid
            initial -= int(player_1)
            print (f"Number of tokens is : {initial}")

         # Check if the game continues or player 1 takes the win
         if int(initial) > 0 :          
            while True :
               # Player 2's turn
               player_2= input ("Player 2 inseret a squared number: ")

               # Check if player 2's input is a valid postive squared number that is greater than the number of tokens
               if not Postive_integer_or_not (player_2):  
                  print ("** Please insert a valid squared number **")
               elif not Squared_numb_or_not(player_2):
                  print ("** Please enter a valid squared number **")
               elif int(player_2) > int(initial):
                  print( "** Please enter a valid squared number less than the number of tokens in the pile **")
               else :
                  break 
            
            initial -= int(player_2)

            # Check if the game continues or player 2 takes the win
            if initial >0 :  
               print (f"Number of tokens is : {initial}")
            elif initial==0 :
               print("Player 2 is the WINNER !!!!")    
         elif int(initial) == 0:
            print("Player 1 is the WINNER !!!!")   


   elif option == 'B' or option=='b':
     # Display game instructions
     print('How to play:\nThis is a two-player mathematical game of strategy.\nIt is played by two people with a pile of coins (or other tokens) between them.\nThe players take turns removing coins from the pile, always removing a non-zero square number of coins (1,4,9, etc.).\nThe player who removes the last coin wins.')
   elif option == 'C' or option== 'c':
     # Break loop to exit game
     print("** Game Exited **")
     break 
   else:
     print("** Invalid, Please enter A or B or C **")