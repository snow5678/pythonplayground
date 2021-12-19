main.py will be the main file you going to run
- in this file, it will take 2 different parameter
- `-q` for question number, expecting int value, currently having 2 question
- `-m` for mode, when no value was passed in, it will default to test

in main.py file line 2, 19 and 21 (will have more trigger in future)
it will call to another file named question(question.py) in the same folder

in question.py, it will have the question in print() statement
based on the mode being passin, it will show the output of the function in test.py or answer.py

so what you have to do is modify the test.py and make sure you get similar/same output as answer.py

everytime you made changes in test.py, you can just trigger `python main.py -q {question number}` to test

