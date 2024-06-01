grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
chisla = []
chisla.append(sum(grades[0])/len(grades[0]))
chisla.append(sum(grades[1])/len(grades[1]))
chisla.append(sum(grades[2])/len(grades[2]))
chisla.append(sum(grades[3])/len(grades[3]))
chisla.append(sum(grades[4])/len(grades[4]))
students = sorted(students)
itog = dict(zip(students, chisla))
print(itog)
