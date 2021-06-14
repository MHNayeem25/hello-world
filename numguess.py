print("Please think of a number between 0 and 100!")
high=100
low=0
""" hello this is test file that returns your number
     Input -  low, high, correct
     Output - The number you are thinking of """





while True:
    guess=(high+low)//2
    print("Is your secret number " + str(guess) + '?')
    while True:
      x=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
      if x not in ('h','l','c',' '):
          print("Sorry, I did not understand your input.")
          print("Is your secret number " + str(guess) + '?')
      else:
          break
    if x=="h":
          high=guess
          #break
    elif x=="l":
          low=guess
    elif x=="c":
          print("Game over. Your secret number was:" , guess)    
          break
      
    
      
    
