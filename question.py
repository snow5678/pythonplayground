import test
import answer

def question1(mode):
    # question info
    print("If statement & number operator: \nIn test.py, add in new function named question1() to different messages \nThe question1() function should take a number input from users and return the message accordingly. \n 1 - first \n 2 - second \n 3 - third \n 4~5 - top 5 \n 6~10 - top 10 \nAny number that out of the range of 1~10 will print out 'Invalid Number'.")

    # assign the value return from question1() to result variable
    if mode == "test":
        result = test.question1()
    else:
        result = answer.question1()

    # message returned from question1 will be printed here
    print(result)


def question2(mode):
    print("Loop: \nUsing loop through a list with elements of different data type and categorize them into different list")
    print("The output should be in dict format")

    sample_list = [
        "sample1",
        1,
        18,
        22.5,
        "sample2",
        "merry",
        "christmas",
        True,
        False,
        ["array", "of", "string"],
        [1, 5, 8],
        {"name": "something"}
    ]

    if mode =="test":
        # result = test.question2()
        print("uncomment here after declare the function question2()")
    else:
        result = answer.question2(sample_list)

    print(result)
