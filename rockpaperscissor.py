import sys

u1 = input("What's your name?")
u2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % u1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % u2)
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("try again.")
        sys.exit()
