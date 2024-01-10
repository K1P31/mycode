#!/usr/bin/env python3

def getUserInfo(): 
    name = input('Please enter your name:').capitalize()
    age = int( input('How old are you?'))
    favMovie = input('What is your favorite movie?')

    userInfoList = [name, age, favMovie]

    print(f'Hello, {userInfoList[0]}! Y:ou are {userInfoList[1]} years old, and your favorite movie is {userInfoList[2]}.')

getUserInfo(\n)
