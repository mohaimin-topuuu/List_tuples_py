#Solve the following problems using lists and tuples

#WAP to ask a user to enter names of his her 3 favourite movies and store them in a list

userFirstMovie = input("Enter your first movie name: ")

userSecondMovie = input("Enter your second movie name: ")

userThirdMovie = input("Enter your third movie name: ")

userMovies = [userFirstMovie, userSecondMovie, userThirdMovie]

print(f"Your favourite movies are: {userMovies}")


#WAP to check if a list contains a palindrome of elements 



#WAP to count the number of students with the "A" grade in the following tuple

students = ("A", "B", "C", "D", "A", "B", "C", "D")

studentsWhoGotA = students.count("A")

# Store the given values in a list and sort them from "A" to "D"

students = ("A", "B", "C", "D", "A", "B", "C", "D")

students = list(students)

students.sort()

print(students)


# Store the given values in a list and sort them from "D" to "A"

students = ("A", "B", "C", "D", "A", "B", "C", "D")

students = list(students)

students.sort(reverse = True)

print(students)