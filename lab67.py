#!/usr/bin/env python3

## read in content of Dracula novel as a file object
with open("dracula.txt", "r") as foo:

## loop every line in Dracula and print each line
   # for line in foo
   #    print(line)


## fix loop to only print out if the word vampire is in it
   # for line in foo:
   #     if "vampire" in line:
   #         print(line)


## make sure it prints the line no matter what case "vampire" is 
    for line in foo:
        if "vampire" in line.lower():
            print(line)


## count how many lines contain vampire
count = 0 ; 
for line in foo:
    if "vampire"in line.lower():
        count += 1
 print(count)


## take the lines from Dracula that have "vampire" in it and write to a second file named vampytimes.txt
count = 0

with open("dracula.txt","r") as foo:
    with open("vampytimex.txt","w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                count += 1
                fang.write(line)

print(count)

