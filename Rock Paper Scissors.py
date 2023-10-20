import random

Rock = '''

         ___________         
_ _ _'--     _______)
            (_______)
            (_______)
_ _ _        (______)
      ---.__(_____)

'''


Paper ='''

       _______
_ _ _'--    ___)________
                 _______)__
                   ________)
                 _________)
__ _ _ _ ----.  _________)

'''

Scissors ='''

          ________
_ _ _'--       ___)____
                   _______)
                  ________)
_ _ _             (____)
         ---.   (____)

'''
  

while True:
    Genreate = [Rock,Paper,Scissors]
    user_choice = int(input("Enter your Choice:\n 0.Rock \n1.Paper \n2. scissors\n "))
    if user_choice >=3 or user_choice <0 :
        print ("invalid choice ,try again")
    else:
        
        print(Genreate[user_choice])
        computer_choice=random.randint(0,2)
        
        print("Computer choice =",Genreate[computer_choice] )
        if computer_choice == user_choice :
            print("match draw")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lose")
        elif computer_choice == 2 and user_choice == 0:
            print("You Win")
        elif computer_choice > user_choice:
            print("You Lose")
        elif computer_choice < user_choice:
            print("You WIn")
            
        cont=input("dou you want to continue \n 1.YES 2. NO")
        while cont.lower() not in ("1","2"):
            cont=input("Please Enter the Correct Input \n 1.YES 2.")
        if cont == "2":
            print()
            print("thank you")
            break
