#This def will analyse and store the quantity of numbers, letters and symbols
def analysis(text):
    letters = 0
    numbers = 0
    symbols = 0

    for caractere in text:
        if caractere.isalpha():
            letters += 1
        elif caractere.isdigit():
            numbers += 1
        else:
            symbols += 1

    return letters, numbers, symbols

#The variable who defines the final strength
pontuation = 3

#The def for the logical thinking
def strong(letters, numbers, symbols, pontuation):
    
    if letters >= 5:
        pontuation += 1
    else:
        pontuation -= 1

    if numbers >= 3:
        pontuation += 1
    else:
        pontuation -= 1

    if symbols >= 2:
        pontuation += 1
    else:
        pontuation -= 1

    if pontuation == 0:
        print("Strong 0 [--/--/--]")
    elif pontuation == 2:
        print("Strong 1 [##/--/--]")
    elif pontuation == 4:
        print("Strong 2 [##/##/--]")
    elif pontuation == 6:
        print("Strong 3 [##/##/##]")

#In the end the looping to the software ask every time until it closes
while True:
    user_input = input("Write your password:")
    letters, numbers, symbols = analysis(user_input)

    strong(letters, numbers, symbols, pontuation)