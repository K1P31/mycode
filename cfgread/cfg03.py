#!/usr/bin/env python3

##prompt user for name of file to load then replace 'vlanconfig.cfg' with user  value
userPromptFile = input("What is the name of the file? ")

## create file object in "r"ead mode
with open(userPromptFile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

## customization 03 display lines in file vlanconfig.cfg
print(len(configlist))
