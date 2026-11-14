
# DAY 1 - PYTHON FUNDAMENTALS

# 1. Variables
name = "Preeti"
experience = 3
skills = ["Python", "R", "SAS", "SQL"]

print(name)
print(skills)


# 2. Lists
numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Total:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))


# 3. Loops
for number in numbers:
    print(number)


# 4. Dictionary
student = {
    "name": "Rahul",
    "marks": 85
}

print(student["name"])


# 5. Functions
def calculate_average(values):
    return sum(values) / len(values)


result = calculate_average(numbers)
print("Average:", result)
