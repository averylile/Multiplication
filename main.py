import random

count = 0
while count < 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    product = num1 * num2
    inner_count = 1

    print(f"Question {count + 1}: What is {num1} x {num2}?")
    while inner_count < 5:
        guess = int(input("What do you think it is?"))
        print(f"Your answer: {guess}")
        if product == guess:
            print("Correct!")
            break
        else:
            print("Incorrect. Try again")
    count+=1