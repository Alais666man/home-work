def anyss2dec(number, osn_ss):
    number = str(number[::-1])
    result = 0
    alf_hex = ('a', 'b', 'c', 'd', 'e', 'f')
    for i in range(len(number)):
        if number[i] in alf_hex:
            result += (alf_hex.index(number[i]) + 10) * osn_ss ** i
        else:
            result += int(number[i]) * osn_ss ** i
    return result


def dec2anyss(number, osn_ss):
    alf_hex = ('a', 'b', 'c', 'd', 'e', 'f')
    result = ''
    while number != 0:
        if number % osn_ss >= 10:
            result += alf_hex[(number % osn_ss) - 10]
        else:
            result += str(number % osn_ss)
        number = number // osn_ss
    return result[::-1]


def dec2bin(number):
    osn_ss = 2
    return dec2anyss(number, osn_ss)


def dec2oct(number):
    osn_ss = 8
    return dec2anyss(number, osn_ss)


def dec2hex(number):
    osn_ss = 16
    return dec2anyss(number, osn_ss)


def bin2dec(number):
    osn_ss = 2
    return anyss2dec(number, osn_ss)


def oct2dec(number):
    osn_ss = 8
    return anyss2dec(number, osn_ss)


def hex2dec(number):
    osn_ss = 16
    return anyss2dec(number, osn_ss)


if __name__ == '__main__':
    print(dec2bin(250))
    # print(dec2oct(22))
    # print(dec2hex(22))
    print(bin2dec('1010011010'))
    print(oct2dec('755'))
    print(hex2dec('abcdef'))

