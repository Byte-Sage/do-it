marks = []

m1 = int(input("Enter marks for subject 1: "))
marks.append(m1)
m2 = int(input("Enter marks for subject 2: "))
marks.append(m2)
m3 = int(input("Enter marks for subject 3: "))
marks.append(m3)
m4 = int(input("Enter marks for subject 4: "))
marks.append(m4)   
marks.sort()  # Sort the marks in ascending order 
print(marks)