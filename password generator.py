import random
import string 

# Uppercase Letters 
uppercase = string.ascii_uppercase

# Lowercase Letters 
lowercase = string.ascii_lowercase

# Digits
digits = string.digits

# Symbols
symbols = string.punctuation

chars = uppercase + lowercase + digits + symbols 


   
    #Length Of the inpts to be enter
password_len = int(input("What length you like your pasword to be : "))
    
    # how many password you want
password_count=int(input("How many password would you like :"))
    
for x in range(0,password_count):
    password = ""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password      = password + password_char
    print("here is your password:",password)
    continue
        
    cont=input("dou you want to continue \n 1.YES 2. NO")
    while cont.lower() not in ("1","2"):
        cont=input("Please Enter the Correct Input \n 1.YES 2.")
    if cont == "2":
        print()
        print("thank you")
        break
        
       
