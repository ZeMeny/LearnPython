# ex1 program a func that accepts a string representing Roman numeral and returns a number

def romanToInt( s: str):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    # add all of the values together ignoring special cases like IX or IV
    for n in s:
        total += d[n]

    # subtract
    # if we find any of the letters that can have a predecessor that modifies the value
    # subtract twice the value of the predecessor (twice bc we already added it once in the add cycle)
    for n in range(1, len(s)):
        if s[n] == 'V' or s[n] == 'X':
            if s[n - 1] == 'I':
                total -= d['I'] * 2
        elif s[n] == 'L' or s[n] == 'C':
            if s[n - 1] == 'X':
                total -= d['X'] * 2
        elif s[n] == 'D' or s[n] == 'M':
            if s[n - 1] == 'C':
                total -= d['C'] * 2

    return total
print(romanToInt('II'))
