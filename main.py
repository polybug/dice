import random

def diceRollP1():
 return random.randint(1,6)

def diceRollP2():
 return random.randint(1,6)


player1 = diceRollP1()
player2 = diceRollP2()

print(f'player 1 rolled a {player1}')
print(f'player 2 rolled a {player2}')

if player1 > player2:
  print('player 1 wins')

if player2 > player1:
  print('player 2 wins')

if player1 == player2:
  print('draw')