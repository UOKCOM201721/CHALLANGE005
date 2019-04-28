#####################################################################
########## This asks for a number input and the converts it to words
########## By Deno101 <Dennizwarui@gmail.com>
#####################################################################


class App:
    ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 7: 'seven', 8: 'eight', 6: 'six', 9: 'nine'}
    tens = {0: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 7: 'seventy', 8: 'eighty', 6: 'sixty', 9: 'ninety'}
    teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 7: 'seventeen', 8: 'eighteen', 6: 'sixteen' , 9: 'nineteen'}
    level = ['', 'thousand', 'million', 'billion', 'trillion']

    def __init__(self, raw_num):
        raw_str = str(raw_num)
        nums = self.splitint(raw_str)
        result = self.to_words(nums)
        print(self.finalize(result))

    # split the sting into groups of three
    def splitint(self, raw_str):
        trigger = 0
        tmplist = []
        finlist = []

        for i in range(len(raw_str)-1, -1, -1):
            if trigger == 3:
                finlist.append(tmplist[::-1])
                trigger = 0
                tmplist = []
            tmplist.append(int(raw_str[i]))
            trigger += 1
        finlist.append(tmplist[::-1])

        for x in range(3):
            try:
                finlist[len(finlist)-1][x]
            except IndexError:
                finlist[len(finlist)-1].insert(0, 0)

        return finlist[::-1]

    # Returns the num in words
    def to_words(self, formated_nums):

        names = []
        start = len(formated_nums)-1
        for i in formated_nums:

            hundreds = 'Hundred' if not i[0] == 0 else ''
            plus = 'and'

            # defines conditions where and should not be used
            if (i[2] == i[1] and i[2] == 0) or (i[0] == 0):
                plus = ''

            x = 0
            # responsible for breaking the loop if num in teens
            con = True
            while x < 3 and con:
                src = self.ones if not x == 1 else self.tens

                if x == 1 and i[x] == 1:
                    src = self.teens
                    x += 1
                    con = False

                names.append(src[i[x]])
                if x == 0:
                    names.append(hundreds)
                    names.append(plus)

                x += 1

            names.append(self.level[start])
            start -= 1

        return names

    # formats the string output
    def finalize(self, result):

        fin_result = ''
        for x in result:

            if x == '':
                continue

            fin_result += x + ' '

        fin_result += '\n'
        return fin_result


def main():
    data = input("Enter number to convert: ")

    try:
        num = int(data)
    except ValueError:
        print('Please enter valid number:')
        return

    if num > (10 ** 15) - 1:
        raise OverflowError

    App(num)


if __name__ == '__main__':

    try:
        main()
    except OverflowError:
        print('Number cannot exceed 10^15: Hundreds of trillions')
