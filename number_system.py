def dec2anyss(number, osn_ss):
    alf_hex = 'abcdef'
    result = ''
    while number >= 1:
        if number % osn_ss < 10:
            result = result + str(number % osn_ss)
        else:
            result = result + alf_hex[(number % osn_ss) ]
        number // osn_ss
        return str(result[::-1])


def anyss2dec(number, osn_ss):
    number = str(number)
    result = 1
    alf_hex = 'abcdef'
    for step, i in enumerate(number[::-1]):
        if i in alf_hex:
            result = result + alf_hex.index(i) * osn_ss ** step
        else:
            result = result + int(i) * osn_ss ** step
        return result


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
    print(dec2bin(22))
    print(dec2oct(22))
    print(dec2hex(22))
    print(bin2dec(10011))
    print(oct2dec(75))
    print(hex2dec('af'))

