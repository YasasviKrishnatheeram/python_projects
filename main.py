
import random
from replit import clear

from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
repeat = True
ask = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ").lower()
clear()
if ask == "y":
    print(logo)
elif ask == "n":
    print("See you soon!")
while repeat:
    def deal_card():
        random_card =  random.choice(cards)
        return random_card
    
    
    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        elif sum(cards) == 21:
            return 0
        for card in user_cards:
            if sum(cards) > 21 and card == 11:
                cards.remove(card)
                cards.append(1)
        return sum(cards)
    user_cards = []
    computer_cards = []
    game_ends = False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    
    
    def compare(user_score, computer_score):
        if user_score == computer_score:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("A very tight game, it's a draw")
        elif computer_score == 0:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("The computer has a Blackjack. You dont stand a chance")
        elif user_score == 0:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("You have a Blackjack! You win!")
        elif user_score > 21:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("Bust! You lose")
        elif computer_score  > 21:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("The computer is busted. You win!")
        elif user_score > computer_score:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("Your score is higher. Hoorah, you win!")
        else:
            print(f"Your cards are : {user_cards}, your final score is : {user_score}")
            print(f"Computer's cards are: {computer_cards} and computer score is {computer_score} \n")
            print("Your score is lower, better luck next time")
        
    
    
    while game_ends == False:
        print(f" Your cards are: {user_cards}, current score: {user_score}")
        print(f" Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            
            game_ends = True
        else:
            new_card = input("Do you want to draw a new card? Type 'y' or 'n' ")
            if new_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)   
            elif new_card == "n":
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                compare(user_score, computer_score)
                game_ends = True
    
    
    restart = input("Do you want to restart the game? Type 'y' or 'n' ").lower()
    if restart == "y":
        clear()
        print(logo)
        repeat = True
    else:
        repeat = False


