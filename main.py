import random
lowest_number = 1
highest_number = 10000
answer = random.randint(lowest_number, highest_number)

guesses = 0

is_running = True
print("Hello welcome to Aliens guessing game")
print(f" Please Enter a number between {lowest_number} and {highest_number}  ")
while is_running:
    guess = input("Enter your guess!: ")
    if guess.isdigit():
     guess = int(guess)
     guesses += 1 
     if guess > highest_number or guess < lowest_number:
       print("number is out of range")
     elif guess > answer:
      print("This number is too high!")
     elif guess < answer:
      print("This number is too low!")
     elif guess == answer:
      print(f"Correct! the number is {answer} You have made {guesses} guesses! ") 
      is_running = False 
    else:
       print("invalid number Please Enter a valid number")

       