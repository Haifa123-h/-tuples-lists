data = (
    ["Alice", (14, 16, 18)],
    ["Bob", (12, 9, 10)],
    ["Charlie", (19, 20, 17)],
    ["Diana", (8, 7, 10)]
)
selected=[]
count=0
# Sort based on the sum of grades
sorted_data = sorted(data, key=lambda x: sum(x[1])/3)
sorted_data.reverse()
print("data is sorted from highest to lowest scores: ")
print(sorted_data)
for student,scores in sorted_data:
    if (sum(scores))/3 >= 15:
        selected.append(student)
    if (sum(scores))/3 < 10:
        count=count+1
print("student with highest score is: ",selected[0])
print("students with scores >=15: ")
print(selected)
print("number of failed students ",count)
