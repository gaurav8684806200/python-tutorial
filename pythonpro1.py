import random
print("welcome in number gusseing game ")
print ("i'am thinking of a number between 1 to 50 .")

# genrate random number 

secret_number = random.randint(1,50)
guess = None
attempts = 0

while guess != secret_number:
    guess = int(input("enter your guess:"))
    attempts += 1

if guess < secret_number:
    print("Too low .Try again")

elif guess > secret_number:
    print (" Too high.Try agin ")

print (f"congratulation ! you gusseed the number {attempts} attempts.")    