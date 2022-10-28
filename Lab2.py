def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print(calc_average(num_list))
    print(find_min_max(num_list))


def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


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
        if number > min:
            min = number

    max = num_list[0]
    for number in num_list:
        if number < max:
            max = number
    return min, max



if __name__ == "__main__":
    main()