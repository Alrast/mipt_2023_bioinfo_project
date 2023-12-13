mismatch_penalty = 2
gap_penalty = 0.5*mismatch_penalty
match_bonus = 0

# здесь вводятся FASTA файлы  и преобразуются в строки/массивы (Олег Масенков)

read1 = ['T', 'C', 'G', 'T']
read2 = ['A', 'T', 'C', 'A', 'G', 'T'] #результат должен выглядеть както так
# здесь работает нидлман вунш и переводит строки в матрицу (Горшенина Полина)
#            T C G T
matrix = [[0,1,2,3,4], #
          [1,2,3,4,5], #A
          [2,1,2,3,4], #T
          [3,2,1,2,3], #C
          [4,3,2,3,4], #A
          [5,4,3,2,3], #G
          [6,5,4,3,2]] #T

        # должна получится примерно такая матрица (без декора разумеется)




# здесь по матрице происходит сборка выравниваний (Ратин Алексей)
final1 = []
final2 = []
coord_x = len(read1)
coord_y = len(read2)
# print(matrix[coord_y][coord_x])
# print(read1[coord_x-1])
# print(read2[coord_y-1])
while coord_x + coord_y != 0:
    if coord_x == 0:
        for i in range(coord_y):
            final1.append('_')
            final2.append(read2[coord_y-i-1])
        coord_y = 0
    elif coord_y == 0:
        for i in range(coord_x):
            final1.append(read1[coord_x-i-1])
            final2.append('_')
        coord_x = 0
    else:
        if read1[coord_x-1] == read2[coord_y-1]:
            if matrix[coord_y][coord_x] == matrix[coord_y-1][coord_x-1] + match_bonus:
                final1.append(read1[coord_x-1])
                final2.append(read2[coord_y-1])
                coord_x += -1
                coord_y += -1
            elif matrix[coord_y][coord_x] == matrix[coord_y][coord_x-1] + gap_penalty:
                final1.append(read1[coord_x-1])
                final2.append('_')
                coord_x += -1
            elif matrix[coord_y][coord_x] == matrix[coord_y-1][coord_x] + gap_penalty:
                final1.append('_')
                final2.append(read2[coord_y-1])
                coord_y += -1
        else:
            if matrix[coord_y][coord_x] == matrix[coord_y-1][coord_x-1] + mismatch_penalty:
                final1.append(read1[coord_x-1])
                final2.append(read2[coord_y-1])
                coord_x += -1
                coord_y += -1
            elif matrix[coord_y][coord_x] == matrix[coord_y][coord_x-1] + gap_penalty:
                final1.append(read1[coord_x-1])
                final2.append('_')
                coord_x += -1
            elif matrix[coord_y][coord_x] == matrix[coord_y-1][coord_x] + gap_penalty:
                final1.append('_')
                final2.append(read2[coord_y-1])
                coord_y += -1
string1 = ''
string2 = ''
# print(final1[::-1])
# print(final2[::-1])
for i in range(len(final1)):
    string1 += final1[::-1][i]
    string2 += final2[::-1][i]
print(string1)
print(string2)