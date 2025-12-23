# Scenario:
# A teacher wants to process marks for a class of students.
# Task:
#  Input marks of n students using a list
#  Write a function average_marks(marks_list) to compute average
#  Write a function highest_marks(marks_list) to find the top score
#  Write a function grades(marks_list) to assign grades (A:≥90, B:≥75, C:≥60, F:<60)
#  Use list comprehension to create a list of grades
#  Print average, highest, and all student grades

n=int(input("Enter total number of students"))
marks=[int(input("Enter student marks"+str(i+1))) for i in range(n)]
def average(marks):
    sum=0;
    for mark in marks:
        sum=sum+mark
    average=sum/len(marks)
    return average
def highest(marks):
    high=marks[0];
    for mark in marks:
        if mark>high:
            high=mark
    return high
def grade(marks):
    grades=['A' if marks>=90 else 'B' if marks>=75 and marks<90 else 'C' if marks>=60 and marks<75 else 'F' for mark in marks]
    print(grades)
print(average(marks))
print(highest(marks))
grade(marks)

# A school tracks daily attendance of students over a period of 5 days. Each student has a unique
# ID.
# 1. Store attendance data as a list of tuples, where each tuple contains:
# o Student ID
# o List of daily attendance ('P' for Present, 'A' for Absent)
# Example: (101, ['P', 'A', 'P', 'P', 'P'])
# 2. Write a function attendance_percentage(attendance_data) that calculates each
# student’s attendance percentage.
# 3. Write a function low_attendance_students(attendance_data, threshold) that
# returns a list of Student IDs with attendance below a given threshold (e.g., 75%).
# 4. Write a function daily_absences(attendance_data) to count the total number of
# absences per day across all students using list comprehension.
# 5. Print:
# o Each student’s attendance percentage
# o List of students below the threshold
# o Total absences per day

data=[]
n=int(input("Enter total number of students"))
for i in range(n):
    sid=int(input("Enter student ID "))
    att=[]
    for a in range(5):
        att.append(int(input("Enter attendance")))
        data.append([sid,att])
def attendance_percentage(data):
    for sid,record in data:
        count=0
        for r in record:
            if r=='P':
                count+=1
        percentage=count/len(record)*100
        print(sid,":",percentage)
def lowAtendance_Student(data,threshold):
    low=[]
    for sid,record in data:
       count=0
       for r in record:
           if r=='P':
             count+=1
       percentage=count/len(record)*100
       if percentage<threshold:
          low.append(sid)
       return low
def dailyAbsence(data):
    return [sum(1 for sid,record in data if record[i]=='A') for i  in range(5)]
print("Student attendance:")
attendance_percentage(data)
print("low attendance",lowAtendance_Student(data,75))
print("daily absence",dailyAbsence(data))

# Write a Python function that calculates the sum of all integers in a nested list of arbitrary depth.
# Example Input:
# lst = [1, [2, [3, 4], 5], 6]
# Expected Output:
# 21
# Hint:
#  Traverse the list and check if an element is a list.
#  Accumulate all integers in the list, including elements inside sublists.
lst = [1, [2, [3, 4], 5], 6]
def findSum(lst):
    sum=0
    for i in lst:
        if isinstance(i,list):
            for j in i:
                if isinstance(j,list):
                    for k in j:
                            sum=sum+k
                else:
                    sum=sum+j

        else: sum=sum+i

    return sum
print(findSum(lst))


# Problem:
# Given a dictionary of products with nested categories, find the product with the highest price
# and print its name and price.
# Example Input:
# products = {
# "Electronics": {"Laptop": 1200, "Phone": 800},
# "Clothes": {"Shirt": 50, "Shoes": 100},
# "Grocery": {"Rice": 20, "Milk": 10}
# }
# Expected Output:
# Laptop 1200
# Hint:
#  Traverse all categories and products.
#  Keep track of the product with the maximum price.
products = {
"Electronics": {"Laptop": 1200, "Phone": 800},
 "Clothes": {"Shirt": 50, "Shoes": 100},
 "Grocery": {"Rice": 20, "Milk": 10}
 }
max=0
product=""
for key,value in products.items():
    for k,v in value.items():
        if v>max:
            max=v
            product=k
print(max,product)

# Write a Python function that takes a nested list of arbitrary depth and returns a dictionary with
# the frequency count of each integer in the list.
# Example Input:
# lst = [1, [2, [3, 2, 4], 5, 1], 6]
# Expected Output:
# {1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1}
# Hint:
#  Traverse the list and check if an element is a list.
#  Keep a dictionary to store counts of each integer.

lst = [1, [2, [3, 2, 4], 5, 1], 6]
def countIntegers(lst):
    count={}
    def traverse(lists):
        for element in lists:
            if isinstance(element,list):
                traverse(element)
            elif isinstance(element,int):
                count[element]+=1
            else:
                count[element]=1
    traverse(lst)
    return count
print(countIntegers(lst))


