from PrettyString.StringConverter.intStringConverter import intStringConverter


def run_test_0():
    # - 10 - +10
    Test_case_0 = [-5, -3, - 1, 0, 1, 4, 5, 7, 8, 9]
    expected_out0 = ["negative five", "negative three", "negative one", "zero", "one", "four", "five", "seven", "eight",
                     "nine"]
    output = []
    for input, expected in zip(Test_case_0, expected_out0):
        pass


def run_test_1():
    # -1000 - + 1000
    Test_case_1 = [-978, -777, - 525, -300, -78, 56, 120, 303, 450, 981]
    expected_out1 = ["negeative nine hundred and seventy eight, negative seven hundred and seventy seven",
                     "negative five hundred and twenty five",
                     "negative three hundred", "negative seventy eight", "fifty six", "One hundred and twenty",
                     "Three hundred and three",
                     "four hundred and fifty", "nine hundred eighty one"]
    output = []
    for input, expected in zip(Test_case_1, expected_out1):
        pass


def run_test_2():
    # large numbers with zeros
    Test_case_2 = [1000000, 20000000, 20050000, 4823000000, 12000000000, 210948040000]
    expected_out2 = ["One Million", "Twenty Million", "Twenty Million and Fifty Thousand",
                     "four billion and eight hundred and twenty three million", "twelve trillion",
                     "two hundred and ten billion, nine hundred forty eight million and forty thousand"]
    output = []
    for input, expected in zip(Test_case_2, expected_out2):
        pass


if __name__ == "__main__":
    run_test_0()
    run_test_1()
    run_test_2()