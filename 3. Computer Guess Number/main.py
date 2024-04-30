import random

guess_select = int(input("Select guess: "))
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f"Yes! Computer guessed the number, {guess} correctly!")
    
computer_guess(100)