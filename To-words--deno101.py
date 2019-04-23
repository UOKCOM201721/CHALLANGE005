#####################################################################
########## This asks for a number input and the converts it to words
########## By Deno101 <Dennizwarui@gmail.com>
#####################################################################


class App:
    def __init__(self, raw_num):
        raw_str = str(raw_num)
        print(self.splitint(raw_str))

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


def main():
    data = input("Enter number to convert: ")
    try:
        num = int(data)
    except ValueError:
        print('Please enter valid number:')
        return

    App(num)


if __name__ == '__main__':
    main()
