secret = 17
guess = int(raw_input("What is the secret number?"))


if secret == guess:
    res = "Congratulations! You discovered the secret number!"
else:
    res = "This is not the secret number. Try again!"

print res
