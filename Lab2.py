import math
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average(num_list))
    print(find_min_max(num_list))
    new_list = sort_temperature(num_list)
    print(new_list)
    print(calc_median_temperature(new_list))


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    print("get_user_input")
    x = input()
    y = x.split(',')
    return y


def calc_average(num_list):
    print("calc_average")
    num_list = list(map(int, num_list))
    average = sum(num_list) / len(num_list)
    return average


def find_min_max(num_list):
    print("find_min_max")

    min = num_list[0]
    for number in num_list:
        if number < min:
            min = number

    max = num_list[0]
    for number in num_list:
        if number > max:
            max = number
    return [min, max]

def sort_temperature(num_list):
    print("sort_temperature")
    num_list.sort()
    return num_list

def calc_median_temperature(new_list):
    print("calc_median_temperature")
    n = len(new_list)

    if n % 2 != 0:
        #odd
        find_index_odd = n / 2
        odd = math.floor(find_index_odd)
        median = new_list[odd]
    else:
        #even
        find_index_even = n / 2
        even = math.ceil(find_index_even)
        middle1 = int(new_list[even])
        middle2 = int(new_list[even - 1])
        median = (middle1 + middle2) / 2

    return median

if __name__ == "__main__":
    main()