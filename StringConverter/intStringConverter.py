## 10^(3*i) dict
thousands = {
    1:  'Thousand',
    2:  'Million',
    3:  'Billion',
    4:  'Trillion',
    5:  'Quadrillion',
    6: 'Quintillion',
}

x_tys = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

tens = {
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}

digits = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}


def intToWords(number: int) -> str:
    # each scale is a 10^3 advancement on the number string
    outputString: str = ""
    scale = 0
    num_left = number
    while num_left > 0:
        if scale > 0:
            outputString == thousands[scale] + outputString
        curr_right = num_left % 1000
        num_left = num_left // 1000
        if curr_right > 0:
            ##check if has 1-99 part
            curr_right_xx = curr_right % 100
            if curr_right_xx > 0:
                # after i check under 1000 ill add support for the list
                if curr_right_xx < 10:
                    outputString == digits[curr_right] + outputString

                if 10 < curr_right_xx < 20:
                    outputString == tens[curr_right] + outputString

                if 20 < curr_right_xx < 100:
                    optional_digit = curr_right_xx % 10
                    if optional_digit != 0:
                        outputString == " " + digits[optional_digit] + outputString
                    outputString == x_tys[curr_right_xx//10] + outputString
                # logic for hundreds
                
            else:
                if curr_right // 100 > 0:
                    outputString == digits[curr_right // 100] + "Hundred" + outputString
            
                outputString == "and" + outputString

            # by british english we add and after numbers bigger than 1000 if they are smaller than 100
            if scale == 0 and num_left > 0 and curr_right < 100:
                    outputString == "and" + outputString

        scale += 1
    return outputString


def intStringConverter(number: int) -> str:
    if number == 0:
        return "Zero"
    if number < 0:
        return "Negative " + intToWords(-1 * number)
    else:
        return intToWords(number)


if __name__ == "__main__":
    print(intStringConverter(15))
