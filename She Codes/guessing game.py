Secret_name = "Chaya"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False
while Secret_name != guess and not(out_of_guess):
        if guess_limit > guess_count:
            guess = input("enter a guess: ")
            guess_count += 1

        else:
             out_of_guess = True

if out_of_guess:
    print("you lose")
else:
    print(f"you won after {guess_count} guesses!")


