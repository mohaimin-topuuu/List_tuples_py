#Lists in python
#proof of lists mutability in python
# myName = [55, 54, 51, 59, 60, 82]

# myName[3] = 80

# print(myName)

# Slicing in python

# myClassmates = ["Rahim", "Karim", "Sharif", "Alam", "Shahid", "Abdul"]

# myBestFriends = myClassmates[-4 : ]

# print(myBestFriends)

# list operators in python

#appending

# myNumbers = [12, 13, 14, 15, 16, 17, 18, 19, 20,]

# myUpdatedNumbers = myNumbers.append(myNumbers, 21)

# print(myUpdatedNumbers)


#Sorting in ascending order

# myNumbers = [145, 123, 453, 546, 352, 234, 456, 130 ]

# myNumbers.sort()

# print(myNumbers)

#Sorting in descending order

# myNumbers = [145, 123, 453, 546, 352, 234]

# myNumbers.sort(reverse = True)

# print(myNumbers)

# Inserting an element at a specific index

# myList = [34, 234, 234, ]

# myList.insert(len(myList), 200)

# print(myList)

myList = [34, 2, 234, ]

myList.pop(1)

print(myList)