#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]

#print IP - concat using list place [0]
print("The first item in the list (IP): " + my_list[0])

#print port as string - concat using list place [1]
print("The second item in the list (port): " + str(my_list[1]) )

#print last item as string - concat using list place [2]
print("The last item in the list (state): " + my_list[2] )

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# ex 1 - add up the strings
print("IP addresses: " + iplist[3] + ", and " + iplist[4])

# example 2 - use the comma separator
print("IP addresses:", iplist[3], ", and", iplist[4])

# example 3 - use an 'f-string'
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")

