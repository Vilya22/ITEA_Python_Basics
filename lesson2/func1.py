# function that calculates the arithmetic average
def arithmetic_average(num):
        sum = 0
        for i in num:
            sum += int(i)
        return sum / len(num)

if __name__ == '__main__':
    list = input('Instert numbers separated by spaces ')
    split_list = list.split(' ')
    print('Arithmetic average is ', arithmetic_average(split_list))
