def question1():
    num = input("Enter a number:")
    num = int(num)
    if num == 1:
        return "first"
    elif num == 2:
        return "second"
    elif num == 3:
        return "third"
    elif num in [4,5]:
        return "top 5"
    elif num >= 6 and num <= 10:
        return "top 10"
    else:
        return "Invalid Number"


def question2(sample_list):
    result = dict()
    for item in sample_list:
        temp_list = result[type(item)] if type(item) in result else []
        temp_list.append(item)
        result[type(item)] = temp_list

    return result
