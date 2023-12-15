# coding: utf-8
import os.path
import sys
from algo import needl_wunsh

mismatch_penalty = 2
gap_penalty = 0.5*mismatch_penalty
match_bonus = 0



# здесь вводятся FASTA файлы  и преобразуются в строки (Олег Масенков)
def reading_from_fasta_file(path_to_file):
    sequence = ""
    if os.path.exists(path_to_file): # если такой путь есть в системе
        if os.path.isfile(path_to_file): # если этот путь указывает на файл (а не на папку)
            if path_to_file[-3:]!='.fa':
                print('Это не fasta файл, но я попробую его обработать')
            with open(path_to_file, 'r') as f:
                for line in f:
                    if line[0] not in [";", ">"]:
                        sequence += line.strip()
            if sequence=='':
                print('В файле нет последовательности')
                sys.exit()
            return sequence
        else:
            print('Это не файл!')
            sys.exit()
    else:
        print('Не могу найти файл')
        sys.exit()

#print("Write the name of fasta file with sequence 1.")
path1 = input('1 ')
read1 = reading_from_fasta_file(path1)

#print("Write the name of fasta file with sequence 2.")
path2 = input('2 ')
read2 = reading_from_fasta_file(path2)



# здесь работает нидлман вунш и переводит строки в матрицу (Горшенина Полина)
##            T C G T
#matrix = [[0,1,2,3,4], #
          #[1,2,3,4,5], #A
          #[2,1,2,3,4], #T
          #[3,2,1,2,3], #C
          #[4,3,2,3,4], #A
          #[5,4,3,2,3], #G
          #[6,5,4,3,2]] #T

matrix = needl_wunsh(read1, read2)


# здесь по матрице происходит сборка выравниваний (Ратин Алексей)

# print(matrix[coord_y][coord_x])
# print(read1[coord_x-1])
# print(read2[coord_y-1])

def allignment(read1: "array[string,...]",
               read2: "array[string,...]",
               matrix: "array[array[integer],...]") -> "Tuple[array[string,...], array[string,...]]":
    final1 = []
    final2 = []
    string1 = ''
    string2 = ''
    coord_x = len(read1)
    coord_y = len(read2)
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
    for i in range(len(final1)):
        string1 += final1[::-1][i]
        string2 += final2[::-1][i]
    print(string1)
    print(string2)
    return final1[::-1], final2[::-1]


allignment(read1,read2,matrix)