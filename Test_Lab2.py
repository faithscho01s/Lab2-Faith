import Lab2

def test_find_min_max():
    result = []
    user_input = [34, 56, 78, 90]
    test_min_max = [34, 90]
    min_max = Lab2.find_min_max(user_input)

    assert (min_max == test_min_max)

def test_calc_average():
    result = []
    user_input = [34, 56, 78, 90]
    test_average = 64.5
    average = Lab2.calc_average(user_input)

    assert (average == test_average)


##def test_calc_median_temperature():