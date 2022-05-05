import random

def diceRollP1():
 return random.randint(1,6)

def diceRollP2():
 return random.randint(1,6)


player1 = diceRollP1()
player2 = diceRollP2()
P1Score = 0
P2Score = 0

print(f'player 1 rolled a {player1}')
print(f'player 2 rolled a {player2}')
print(' ')

if player1 > player2:
  print(f'player 1 wins ({player1} over {player2})')
  P1Score = (P1Score + 1)
  print('')
  print(f'player 1 score: {P1Score}                         player 2 score: {P2Score}')
if player2 > player1:
  print(f'player 2 wins ({player2} over {player1})')
  P2Score = (P2Score + 1)
  print('')
  print(f'player 1 score: {P1Score}                         player 2 score: {P2Score}')
if player1 == player2:
  print(f'draw! ({player1} and {player2})')
  print('')
  print(f'player 1 score: {P1Score}                         player 2 score: {P2Score}')