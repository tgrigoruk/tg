

def convert1(dec_num, base):
    quotient = dec_num
    new_num = 0
    place = 0
    while True:
        if quotient < base:
            new_num += quotient * (10 ** place)
            break
        new_num += ((quotient % base) * (10 ** place))
        quotient //= base
        place += 1
    return new_num


def convert2(dec_num, base):
    quotient = base10
    new_num = ""
    while True:
        if quotient < base:
            new_num = str(quotient) + new_num
            break
        new_num = str(quotient % base) + new_num
        quotient //= base

dec_num = 1
while dec_num != 0:
    base = int(input("Choose a base: "))
    dec_num = int(input("Enter a base 10 number: "))
    print(f"The number {dec_num} converted into base {base} is {convert1(dec_num, base)}\n")

