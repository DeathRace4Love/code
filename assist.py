# -------------------------------
# PYTHON EXAM ALL-IN-ONE PROGRAM
# -------------------------------




# -------- INPUT / OUTPUT --------
# Ask the user for input and convert it
name = input("Enter your name: ")  # input() returns a string
age = int(input("Enter your age: "))  # convert to int
numbers = input("Enter 3 numbers separated by spaces: ")
print()
print()

# map() converts each value to int
num1, num2, num3 = map(int, numbers.split())

# f-string for formatted output
print(f"Hello {name}, you are {age} years old.")
print()



# -------- CONDITIONALS --------
# Check age category using if/elif/else
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
print()



# Logical operators
if age >= 18 and age <= 65:
    print("You are of working age.")
    print()

# -------- STRINGS --------
text = "  Python Is Fun  "

print(len(text))           # length of string
print(text.lower())        # lowercase
print(text.upper())        # uppercase
print(text.strip())        # remove spaces
words = text.split()       # split into list
print(words)
print()



# -------- LOOPS --------
# for loop (definite loop)
print("For loop example:")
for i in range(5):
    if i == 3:
        continue  # skip 3
    print(i)
print()

# while loop (indefinite loop)
print("While loop example:")
count = 0
while count < 5:
    if count == 4:
        break  # stop early
    print(count)
    count += 1
print()



# -------- FUNCTIONS --------
# Function that takes a parameter and returns a value
def add_numbers(a, b):
    return a + b

result = add_numbers(num1, num2)
print(f"Sum of first two numbers: {result}")
print()




# -------- INDEXING & SLICING --------
sample = "Python"

print(sample[0])      # first character
print(sample[-1])     # last character
print(sample[1:4])    # slice from index 1 to 3
print(sample[::-1])   # reverse string
print()



# -------- LISTS --------
my_list = [num1, num2, num3]

my_list.append(10)  # add item to list

print("List items:")
for item in my_list:  # iterate through list
    print(item)

print(my_list[1:3])  # slicing list
print()



# -------- SETS --------
my_set = set(my_list)  # remove duplicates

print("Set (unique values):", my_set)
print()

# membership testing
if num1 in my_set:
    print(f"{num1} is in the set")



# -------- DICTIONARIES --------
# Count how many times each word appears
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:", word_count)
print()



# -------- SORTING --------
# sorted() returns a new sorted list
sorted_list = sorted(my_list)
print("Sorted list:", sorted_list)



# Custom sorting (by absolute value example)
custom_sorted = sorted(my_list, key=lambda x: -x)
print("Custom sorted (descending):", custom_sorted)
