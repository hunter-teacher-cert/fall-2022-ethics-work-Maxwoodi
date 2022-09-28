# File Name: Game of Nim
#First Last Maxwell Yearwood
#CSCI 77800 Fall 2022
#Collaborators: Christine Marra
#Consulted

import random
# Game of Nim


stones = 12
stonesTaken = 0
playerStatus = "Human Wins!"

    



#loop until game ends
while stones > 0: 
#prompt for user input : num of stones
#Human Withdrawals
  
      stonesTaken = int(input((" How many stones would you like to remove from the bag(1,2,3)" ))) 

      #calculate number of stones remaining, print
      stones = stones - stonesTaken
      print("There are now" + " " + str(stones) + " stone(s) remaining")
  
      #check for win
      if stones < 1:
          break
      
      
      #machine turn
      print(" Computer's Turn!")
      if stones > 0:
          print("Computer randomly withdraws stones from the bag (1,2, 0r 3)")
          
          stonesTaken = random.randrange(1,4)
          print("The computer selects:" + str(stonesTaken))
          #stones-= stonesTaken
         # print("There are"+ " "+ str(stones) + " remainig in the bag")
      
      #check for win
      if stones <=0:
         playerStatus = "Computer Wins!"
        
      #calculate number of stones remaining, print
      stones-= stonesTaken
      print("There are"+ " "+ str(stones) + " remaining in the bag")
      #check for win
    
print("Who wins?" + " " + playerStatus)
