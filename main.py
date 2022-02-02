############### Blackjack Project #####################
import art
import random
import replit


def if_hit_yes():
  print('hello')

end_game=False
while not end_game:
  start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  replit.clear()
  if start!='y':
    print("Please run again to play the game.")
    end_game=True
  else :
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_cards=[] 
    user_cards=[]
    computer_cards.append(random.choice(cards))
    cards.remove(computer_cards[0])
    computer_cards.append(random.choice(cards))
    cards.remove(computer_cards[1])
    user_cards.append(random.choice(cards))
    cards.remove(user_cards[0])
    user_cards.append(random.choice(cards))
    cards.remove(user_cards[1])
    current_score=sum(user_cards)
    computer_score=sum(computer_cards)
    
    def if_hit_no(computer_score):
      i=2
      while computer_score < 17:
        computer_cards.append(random.choice(cards))
        cards.remove(computer_cards[i])
        computer_score=sum(computer_cards)
        if(computer_score>21):
          for p in range(len(computer_cards)):
            if computer_cards[p]==11:
              computer_cards[p]=1
          computer_score=sum(computer_cards)
        i+=1
                
      if computer_score>21:
        print( f"Your final hand: {user_cards}, final score: {current_score}\nComputer's final hand: {computer_cards}, final score: {computer_score } \nComputer went over.You won 🥳")
                
      elif current_score> computer_score: 
        print( f"Your final hand: {user_cards}, final score: {current_score}\nComputer's final hand: {computer_cards}, final score: {computer_score } \nYou won 🥳")
                
      elif current_score < computer_score:
        print( f"Your final hand: {user_cards}, final score: {current_score}\nComputer's final hand: {computer_cards}, final score: {computer_score } \nYou lose 😤")
                
      else:
        print(f"Your final hand: {user_cards}, final score: {current_score}\nComputer's final hand: {computer_cards}, final score: {computer_score} \nDraw 🙃")
      return
    
    def game_continue():
      print(f'Your cards: {user_cards}, current score: {current_score}')
      print(f"Computer's first card: {computer_cards[0]}")
      if current_score==21:
        print( f"Your final hand: {user_cards}, final score: 0\nComputer's final hand: {computer_cards}, final score: {computer_score } \nYou have a black Jack 😱. You won 🥳")
      return
    game_continue()  
    user=2
    while current_score<21 :
      hit=input("Type 'y' to get another card, type 'n' to pass: ")
      if not hit=='y':
        if_hit_no(computer_score)
        break
        
      else:
        user_cards.append(random.choice(cards))
        cards.remove(user_cards[user])
        user+=1
        current_score=sum(user_cards)
        if(current_score>21):
          for p in range(len(user_cards)):
            if user_cards[p]==11:
              user_cards[p]=1
          current_score=sum(user_cards)
        if(current_score>21):
          print( f"Your final hand: {user_cards}, final score: {current_score}\nComputer's final hand: {computer_cards}, final score: {computer_score } \nYou went over. You lose 😤")
          break
        else:
          game_continue()
          















