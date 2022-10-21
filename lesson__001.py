
def result_program():
    i = 1
    res_sum = 0
    while i < len_n:
        if i % 2 != 0:
            res_sum = res_sum + n[i]

        i = i + 1

    return res_sum

def result_print(sum_result):

    print("Сумма нечетных позиций равна: " + str(sum_result))


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

len_n = len(n)

sum = result_program()

result_print(sum)



