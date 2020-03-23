password = []
guess = []
close = 0

def create_password():
    password.append(1)
    password.append(2)
    password.append(3)
    password.append(4)
    
def get_guess():
    temp = []
    
    for i in range(4):
        word = input('give me a number fool!')
        number = int(word)
        temp.append(number)
        
    return temp
def is_correct(guess):
    for i in range(4):
        if guess[i] != password[i]:
            return False
    return True
        

def main_game():
    # Create the password first
    create_password()
    guess = get_guess()
    while is_correct(guess) == False:
        print('you got it wrong!')
        guess = get_guess()
    print('correct!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    
main_game()
