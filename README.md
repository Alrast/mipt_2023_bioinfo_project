# mipt_2023_bioinfo_project

# Алгоритм Нидльмана-Вунша
*Постановка задачи:*
Реализовать выравнивание двух последовательностей алгоритмом Нидльмана-Вунша. Данные задаются в формате fasta. Вывод - выравнивание последовательностей. 

gap_penalty = 0.5*mismatch_penalty 

Input: 
>1
1.fa

>2
>2.fa 

Output: 
>
Alignment

Sample_input: 
>1 
TCGT

>2 
ATCAGT


Sample_output: 
>
_TC_GT 

>
ATCAGT 
