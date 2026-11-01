
# 1.String Concatenation

str1 = "Hello "
str2 = input("Enter your Name: ")

# Concatenate two strings
result = str1 + str2
print(result)

# Add another string
str3 = ", welcome to Python programming"
result = result + str3

print(result)


#String Slicing and Indexing



#2. String Slicing and Indexing

str1 = "Hello Zara, welcome to Python programming"

# a. First character
print("First character:", str1[0])

# b. Last character
print("Last character:", str1[-1])

# c. First 5 characters
print("First 5 characters:", str1[:5])

# d. Last 11 characters
print("Last 11 characters:", str1[-11:])

# e. Reverse the string
print("Reverse:", str1[::-1])

# f. Print the word Python
print("Python:", str1[23:29])



#3.String Methods


# String Methods

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize the sentence
print("Capitalize:", strM.capitalize())

# d. Count occurrences of 't'
print("Count of t:", strM.count('t'))

# e. Replace Python with Machine Learning
print("Replaced:", strM.replace("Python", "Machine Learning"))


#4.Tuples


# Tuple Operations

# Create two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate two tuples
t_combine = t1 + t2
print("Combined tuple:", t_combine)

# b. Repeat elements 3 times
print("Repeated tuple:", t_combine * 3)

# c. Access the 3rd element
print("Third element:", t_combine[2])

# d. Access first three elements
print("First three elements:", t_combine[:3])

# e. Access last three elements
print("Last three elements:", t_combine[-3:])

