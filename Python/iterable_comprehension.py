cubic = [i**3 for i in range(5)]
print(cubic)
cubic = [pow(i,3) for i in range(5)]
print(cubic)
even_num = [i for i in range(20) if i%2==0]
print(even_num)
text = [i for i in 'Python is a programming language' if i != ' ']
print(text)
languages = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'PHP']
lang_list = [i.upper() for i in languages if 't' in i]
print(lang_list)
python = list(map(lambda i:i,'Python'))
print(python)
empty_matrix = [[i for i in range(5)]for j in range(5)]
print(empty_matrix)
matrix = [[0.577, 1.618, 0],[2.718, 3.14, 1],[6, 28, 28]]
transpose_matrix = [[i[j] for i in matrix] for j in range(len(matrix))]
print(transpose_matrix)
n = int(input('Enter a number: '))
insect_num = [n*(2**i) for i in range(0,12)]
print(insect_num)

C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\iterables.py 
[0, 1, 8, 27, 64]
[0, 1, 8, 27, 64]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
['P', 'y', 't', 'h', 'o', 'n', 'i', 's', 'a', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']
['PYTHON', 'JAVASCRIPT']
['P', 'y', 't', 'h', 'o', 'n']
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
[[0.577, 2.718, 6], [1.618, 3.14, 28], [0, 1, 28]]
Enter a number: 10
[10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
