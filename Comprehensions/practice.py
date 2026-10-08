#Q1
numbers = [3, 8, 12, 5, 17, 20, 7, 10, 25, 30]
sq_numbers = [nums**2 for nums in numbers if nums%2 == 0]
print(sq_numbers)

#Q2
words = ["python", "machine", "learning", "data", "artificial", "model"]
capitalized_words = [word.upper() for word in words if len(word) > 5]
print(capitalized_words)

#Q3
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
cubed_nums = {num**3 for num in numbers if num > 3}
print(cubed_nums)

#Q4
students = {
    "Rahul": 78,
    "Priya": 92,
    "Aman": 65,
    "Sneha": 88,
    "Karan": 55
}
edited_dict = {name:marks*2 for name,marks in students.items() if marks > 70}
print(edited_dict)

#Q5
data = {
    "age": [18, 22, 25, 17, 30, 21],
    "salary": [25000, 40000, 55000, 18000, 75000, 45000],
    "experience": [0, 1, 2, 0, 5, 1]
}
res_1 = [old_age for old_age in data["age"] if old_age >= 21]
print(res_1)
res_2 = [sal for sal in data["salary"] if sal > 40000]
print(res_2)
res_3 = {index:sal for index,sal in enumerate(data["salary"], start=1) if data["experience"][index-1] >= 1}
print(res_3)