from random import randint

secret = randint(0, 100)

def main():
    return guess == secret

while True:
    guess = int(raw_input("What is the secret number (between 0 and 100)? "))
    if secret < guess:
        print "This is not the secret number. The secret number is smaller than your guess!"
    elif secret > guess:
        print "This is not the secret number. The secret number is bigger than your guess!"
    else:
        print "Congratulations! You discovered the secret number!"
        break

