print("Please think of a number between 0 and 50 ")
high = 50
low  = 0
ans = (high+low)//2.0
while(True):
       print("Is your secret number "+str(ans)+" ?")
       cond = input("If yes press ' c', Enter 'h' to indicate the guess is too high or Enter 'l' to indicate the guess is too low ")
       if(cond=="h"):
              high = ans 
              ans = (high+low)//2.0
       elif(cond=="l"):
              low =  ans  
              ans = (high+low)//2.0
       elif(cond=='c'):
              print(" Your secret number is "+ str(ans))
              break
       else:
              print("Sorry, I did not understand your input.")
