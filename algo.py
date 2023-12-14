# coding: utf-8
def needl_wunsh(a,b, mismatch=2, match=0):
    """
    реализация алгоритма глобального выравнивания на основе расстояния Левенштейна, 
    на вход подаются 2 строки, 
    на выходе матрица с подсчитанными редакционными расстояниями
    решение методом динамического программировани
    space complexity O((n+1)^2)
    time complexity O(n*m)
    """
    gap=0.5*mismatch
    #инициализация
    f=[[gap*(i+j) if i*j==0 else 0 for j in range(len(a)+1)] for i in range(len(b)+1)]
    #заполнение матрицы
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1]==b[j-1]:
                f[j][i]=f[j-1][i-1]+match
            else:
                f[j][i]=min(f[j-1][i-1]+mismatch, f[j][i-1]+gap,f[j-1][i]+gap)
    return f
##проверка
#read1 = ['T', 'C', 'G', 'T']
#read2 = ['A', 'T', 'C', 'A', 'G', 'T']
#ans= needl_wunsh(read1, read2)
#for row in ans:
    #print(row)