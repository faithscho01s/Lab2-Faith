def calculate_bmi (height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = (weight/(height*height))
    if bmi < 18.5:
        print("Under Weight")
        result = -1
        return result
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        result = 0
        return result
    else:
        print("Over Weight")
        result = 1
        return result

