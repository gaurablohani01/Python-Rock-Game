import random

allchoices=['rock', 'paper', 'scissor']

def computer_choice():
    computerinput=allchoices[random.randint(0,2)]
    return computerinput

def check_game(userinput, cinput,userwin, cwin):
    if userinput=='rock' and cinput=='scissor':
        userwin+=1
        print(f'You Won {userinput.capitalize()} beat {cinput.capitalize()}')
    
    elif userinput=='paper' and cinput=='rock':
        userwin+=1
        print(f'You Won {userinput.capitalize()} beat {cinput.capitalize()}')
    
    elif userinput=='scissor' and cinput=='paper':
        userwin+=1
        print(f'You Won {userinput.capitalize()} beat {cinput.capitalize()}')

    elif userinput==cinput:
        print('Draw')

    else:
        cwin+=1
        print(f'Computer Won {cinput.capitalize()} beat {userinput.capitalize()}')
    return userwin,cwin

def play_game():
    username=input("Enter Your Name: ").capitalize()
    userwin=0
    cwin=0
    while True:
        user_input=input("Enter Your Choice.. Rock,paper and scissor or to exit type quit: ").lower()
        userquit_opinion=['quit','exit']
        if user_input not in userquit_opinion:
                if user_input not in allchoices:
                    print("Invalid Message")
                    continue
                else:
                    userwin,cwin=check_game(user_input, computer_choice(),userwin, cwin)
                    print(f'{username} Score = {userwin}')
                    print(f'Computer Score = {cwin} ')
        else:
            print(f'{username} Score = {userwin}')
            print(f'Computer Score = {cwin} ')
            break

play_game()
