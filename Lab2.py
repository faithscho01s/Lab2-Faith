def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    y = x.split(",")
    print("get_user_input")
    list = []
    for x in y:
        list.append(round(float(x), 1))
    print(list)
    return list

def calc_average(list):
    print("calc_average")
    average = sum(list)/len(list)
    return float(average)


def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")

if __name__ == "__main__":
    main()