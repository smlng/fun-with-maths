import sys
import logging


#logging.basicConfig(level=logging.DEBUG)


def cross_product(number):
    digits = [int(i) for i in str(number)]
    result = 1
    for digit in digits:
        result *= digit
    return result


def persistence(number):
    steps = 0
    logging.debug("%d %d", number, steps)
    while len(str(number)) > 1:
        number = cross_product(number)
        steps += 1
        logging.debug("%d %d", number, steps)
    return steps


def loop():
    number = 0
    maxnum = 0
    maxper = -1
    while True:
        number += 1
        digits = [int(i) for i in str(number)]
        if 0 in digits:
            continue
        if 5 in digits:
            continue

        digits.sort()
        minnum = int(''.join(str(x) for x in digits))
        if minnum > maxnum:
            maxnum = minnum
            per = persistence(minnum)
            if per > maxper:
                maxper = per
                print("{} {}".format(minnum, per))


def main():
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        per = persistence(num)
        print("{} {}".format(num, per))
    elif len(sys.argv) == 1:
        loop()
    else:
        print("USAGE: {} NUMBER".format(sys.argv[0]))


if __name__ == '__main__':
    main()
