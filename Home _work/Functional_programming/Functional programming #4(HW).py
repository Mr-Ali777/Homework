#1
array = [[1, 10, 6],
         [8, 5, 6],
         [7, 1, 8]]


def matrix(array, column):
    for x in array:
        for i in x:
            print(i, end=" ")
        print()
    column = int(input("Столбик: "))
    summary = 0
    for x in range(len(array)):
        summary += array[x][column]
    return summary


print(matrix(array, column=0))

#2
def date(day, month, year: str):
    if (day, month, year) == True:
        print(f'{day}.{month}.{year}')
    return f"{year}.{month}.{day}"
print(date(22, 12,2024))