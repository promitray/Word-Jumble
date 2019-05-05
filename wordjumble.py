import random

def list_4():
 words = ['best', 'easy', 'fair', 'fame', 'ease', 'calm', 'cool', 'cute', 'dope', 'duty', 'food', 'spur' , 'gift', 'glow', 'good', 'grow', 'blow', ]
 ans = random.choice(words)
 return ans

def list_5():
 words = ['about', 'above', 'abuse', 'actor', 'acute', 'ahead', 'alarm', 'alike', 'allow', 'angry', 'asset', 'audio', 'avoid', 'aside', 'array']
 ans = random.choice(words)
 return ans

def list_6():
 words = ['absent', 'afresh', 'ageing', 'allies', 'parrot', 'pawing', 'peanut']
 ans = random.choice(words)
 return ans

def jumbled_word(ans):
 lett_random = random.sample(ans, len(ans))
 jumbled =''. join(lett_random)
 return jumbled

def thanks(player_name, score, words_number):
 print player_name, 'Your total score is', score, 'out of', words_number, '!!'
 print('Thank you for playing word jumble :-)')

def main_game():
 print('Welcome to word Jumble!') 
 pname = raw_input('What is your name? ')
 print 'Hello',pname, ', thanks for playing word jumble!'
 words_number = input('How many words would you like to guess? ')
 print 'You could either have words with equal number of letters at every turn or choose at every turn. We have 4, 5 and 6 lettered words.'
 choice = raw_input('Would you like to choose at every turn (Y) or choose once and have the same numbers of letters in all your words (N)? Please choose any option if you choose only one word. ')
 score = 0
 if choice != 'N' and choice != 'n' and choice != 'Y' and choice != 'y':
  choice = raw_input('please enter a valid input ')
  if choice != 'N' and choice != 'n' and choice != 'Y' and choice != 'y':
   choice = raw_input('This is your last chance to enter a valid input: either Y or N ')
 if choice == 'N' or choice == 'N':
  list_number = input('Would you like four, five or six letter words? Please enter 4,5 or 6 as your choice. ')
  for i in range(1,words_number+1):
   if list_number == 4: 
    picked_word = list_4()
   if list_number == 5:
    picked_word = list_5()
   if list_number == 6:
    picked_word = list_6()
   jumbled = jumbled_word(picked_word)
   if jumbled == picked_word:
    jumbled = jumbled_word(picked_word)
   print 'Jumbled word is', jumbled
   guess = raw_input('what is on your mind? ')
   if guess == picked_word:
    print('Yes, that is correct! You get 1 point!! -:)')
    score = score + 1
   else:
    print('Nope, sorry! No points, not what we had in mind. Is there more than one possibility? Please try again. You have one more chance. You could use a hint.')
    response = raw_input('Would you like a hint? Y/N ')
    if response == 'Y' or response == 'y':
     if list_number == 4:  
      print 'The word is',picked_word[0],'**',picked_word[-1]
     if list_number == 5:
      print 'The word is',picked_word[0],'***',picked_word[-1]
     if list_number == 6:
      print 'The word is',picked_word[0],'****',picked_word[-1]
    if response == 'N' or response == 'n':
     print 'Brave of you!'
    guess = raw_input('What is your second try? ')
    if guess == picked_word:
     print('Yes, that is correct. Second time lucky! ') 
     score = score + 1
    else:
     print 'Nope, sorry! The word is', picked_word
  thanks(pname,score, words_number)
  
 if choice == 'Y' or choice == 'y':
  for i in range(1,words_number+1):
   list_number = input('Would you like a four, five or six letter word? Please enter 4,5 or 6 as your choice. ')
   if list_number == 4: 
    picked_word = list_4()
   if list_number == 5:
    picked_word = list_5()
   if list_number == 6:
    picked_word = list_6()
   jumbled = jumbled_word(picked_word)
   if jumbled == picked_word:
    jumbled = jumbled_word(picked_word)
   print 'Jumbled word is', jumbled
   guess = raw_input('what is on your mind? ')
   if guess == picked_word:
    print('Yes, that is correct! You get 1 point!! -:)')
    score = score + 1
   else:
    print('Nope, sorry! No points, not what we had in mind. Is there more than one possibility? Please try again. You have one more chance. You could use a hint.')
    response = raw_input('Would you like a hint? Y/N ')
    if response == 'Y' or response == 'y':
     if list_number == 4:  
      print 'The word is',picked_word[0],'**',picked_word[-1]
     if list_number == 5:
      print 'The word is',picked_word[0],'***',picked_word[-1]
     if list_number == 6:
      print 'The word is',picked_word[0],'****',picked_word[-1] 
    if response == 'N' or response == 'n':
     print 'That is brave of you! '
    guess = raw_input('What is your second try? ')
    if guess == picked_word:
     print('Yes, that is correct! Second time lucky!') 
     score = score + 1
    else:
     print 'Nope, sorry! The word is', picked_word

  thanks(pname,score, words_number) 
 
main_game()


 
