# Imprimir números que no sumen el valor de n.
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k) != n])
'''

# Ejercicio aún sin resolver
'''
n = int(input())
arr = map(int, input().split())
print()
print("El valor de n es: ",n)
print("respecto del array", list(arr))
'''

# Problem: Finding the percentage (students grades)
# with 2 places after floating point.
'''
n = int(input())
student_marks = {}
for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	student_marks[name] = scores
query_name = input()
sum = 0.00
for grade in student_marks[query_name]:
	sum = float(sum+grade)
percentage = sum/3
print(f"{percentage:.2f}")
'''

# Zipped!!
