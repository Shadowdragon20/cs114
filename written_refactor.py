"""Convert a number in base-10 into a written out number in English."""

def get_number():
    print('test')
    num = int(input('A number between 1 and 99: '))
    return num


def get_tens(num):
    tens = num // 10
    get_tens=tens
    return tens
def get_ones(num):
    ones = num % 10
    return ones

def get_tens(tens):

    if get_tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'

        output = tens_word, ones_word
return output


def get_ones(ones):

    if ones == 9:
         ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'

        output=
return output

def irregualer_out(tens,ones,one_word):
    if tens == 0:
        output = ones_word
    elif tens == 1:
        if ones == 1:
            output = 'eleven'
        elif ones == 2:
            output = 'twelve'
        elif ones == 3:
            output = 'thirteen'
        elif ones == 5
                output = 'fifteen'
        else:
            output = ones_word + 'teen'
        return output




def main():
    num= get_number()
    tens= get_tens(num)
    ones= get_ones(num)
