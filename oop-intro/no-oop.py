#!/usr/bin/env python 3

import random

def main():
    """run time code"""
    
    player1_dice = []
    player2_dice = []

    for i in range(3):
        player1_dice.append(random.randint(1,6)) # 1 to 6 inclusive
        player2_dice.append(random.randint(1,6)) # 1 to 6 inclusive

    if sum(player1_dice) == sum(player2_dice):
      print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
      print("Player 1 wins")
    else:
      print("Player 2 wins")
