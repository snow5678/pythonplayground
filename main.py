import argparse
import question

default_mode = "test"
default_question = 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--question")
    parser.add_argument("-m", "--mode")
    inputs = parser.parse_args()

    mode = default_mode if inputs.mode is None else inputs.mode
    question_num = default_question if (
        inputs.question is None or int(inputs.question) <= 0
    ) else int(inputs.question)

    if question_num == 1:
        question.question1(mode)
    elif question_num == 2:
        question.question2(mode)

if __name__ == "__main__":
    main()
