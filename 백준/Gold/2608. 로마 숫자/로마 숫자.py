import sys
input = sys.stdin.readline

def boj2608():
    def rom2int(roman):
        dicts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exdicts = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i, value = 0, 0
        while i < len(roman):
            if i+1 < len(roman) and roman[i:i+2] in exdicts:
                value += exdicts[roman[i:i+2]]
                i += 2
            else:
                value += dicts[roman[i]]
                i += 1
        return value

    def int2rom(num):
        dicts = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        buffer = []
        for value, symbol in dicts:
            while not num < value:
                buffer.append(symbol)
                num -= value
        return ''.join(buffer)

    rom1 = input().strip()
    rom2 = input().strip()

    intsum = rom2int(rom1) + rom2int(rom2)
    romstr = int2rom(intsum)
    
    print(intsum)
    print(romstr)

if __name__ == '__main__': boj2608()