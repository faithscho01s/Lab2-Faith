import Lab2_Faith.bmi as bmi


def test_bmi_under_weight():
    value = -1
    result = bmi.calculate_bmi(1.73, 20)
    assert (result == value)



def test_bmi_normal_weight():
    value = 0
    result = bmi.calculate_bmi(1.73,57)
    assert (result == value)


def test_bmi_over_weight():
    value = 1
    result = bmi.calculate_bmi(1.73, 80)
    assert (result == value)