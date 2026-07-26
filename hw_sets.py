



student1 = {"Math", "Science", "English"}
student2 = {"Science", "History", "Spanish"}


print("Common Subjects:")
print(student1 & student2)


print("All Subjects:")
print(student1 | student2)


print("Subjects only chosen by Student1")
print(student1 - student2)

print("Subjects only chosen by student2")
print(student2-student1)


if student1 == student2:
    print("Both students have exactly the same set of subjects.")
else:
    print("Both students do NOT have the same set of subjects.")



