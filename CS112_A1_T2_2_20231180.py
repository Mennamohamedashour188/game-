#file:CS112_A1_T2_2_20231180.py
#purpose:The game consists of a list containing numbers from 1 to 9, from which each player can extract a number
#which will be deleted from the list so that in the end there are 3 numbers with a total of 15. If none of the players is able to win, it will be a draw.
#Author:menna mohamed ashour ali
#id:20231180
list=[1,2,3,4,5,6,7,8,9]
list1,list2=[],[] # two empty list to put  players's choice
#how this game play
print("welcom to the game")
print("numbers of list is from 1 to 9 and you will choose numbers to collect three numbers that their sum is 15 to be winner.")
temp=True # to control the loop and end it when one of player wins
while (temp==True ):
  cout=0
  while(cout<=8 and temp==True ):
      while True: #to make sure that the user enter a valid number
         try:
           move_player=int(input("player:please enter  number from 1 to 9:"))
           if(move_player in list):
            break
           else:
             print(" please enter a valid number from 1 to 9") 
         except ValueError:print("please enter a valid value")
         #to make eaach player's numbers in a list
      if(cout%2==0):
        list1.append(move_player)
        #to remove the choice number from list
        list.remove(move_player)
        #to sum the first three numbers to check
        if(len(list1)==3):
           sum1=0
           for i in list1:
              sum1=sum1+i
           if(sum1==15):
                 temp=False
                 print("player1 is winer")
        if(len(list1)>=4):# if the user insert more than three number
            
            if(list1[0]+list1[1]+list1[2]==15):
              temp=False
              print("player1 is winner")
            elif(list1[0]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[0]+list1[1]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[0]+list1[1]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
            elif(list1[1]+list1[2]+list1[3]==15):
               temp=False
               print("player1 is winner")
        if(temp==True):
         # to print the new list to be easy for the user
         print("NOW OUR LIST IS",list)
      else:
         list2.append(move_player)
         list.remove(move_player)
         if(len(list2)==3):
           sum2=0
           for i in list2:
              sum2=sum2+i
           if(sum2==15):
                 temp=False
                 print("player2 is winer")
         if(len(list2)>=4):
            if(list2[0]+list2[1]+list2[2]==15):
              temp=False
              print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[0]+list2[2]+list2[3]==15):
               temp=False 
               print("player2 is winner")
            elif(list2[0]+list2[1]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[0]+list2[1]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
            elif(list2[1]+list2[2]+list2[3]==15):
               temp=False
               print("player2 is winner")
         if(temp==True):
          print("NOW OUR LIST IS",list)
      cout=cout+1
        # if the game is draw 
      if(len(list)==0 or (len(list)==1 and temp==True)):
         temp=False
         print("the game is draw")
    


    
    


