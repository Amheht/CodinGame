# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/ide/puzzle/tricky-number-verifier

# User inputs
n = int(input())
sin_data = [input() for _ in range(n)]

def isValidSyntax(sin: str) -> bool:
    return len(sin) == 10 and sin[0] != "0" and sin.isnumeric()
  
def hasValidCheckDigit(sin: str) -> bool:

    LLL = sin[0:3]
    DDMMYY = sin[4:]

    while True:
        checkSum = 0
        checkSum += int(LLL[0]) * 3
        checkSum += int(LLL[1]) * 7
        checkSum += int(LLL[2]) * 9

        checkSum += int(DDMMYY[0]) * 5
        checkSum += int(DDMMYY[1]) * 8
        checkSum += int(DDMMYY[2]) * 4
        checkSum += int(DDMMYY[3]) * 2
        checkSum += int(DDMMYY[4]) * 1
        checkSum += int(DDMMYY[5]) * 6
        checkDigit = checkSum % 11
        if checkDigit != 10:
            break
        LLL = str(int(LLL) + 1)
    
    if sin[3] != str(checkDigit):
        print(f"{LLL}{str(checkDigit)}{DDMMYY}")
        return False
    else:
        return True

def hasValidDate(sin: str) -> bool:
    DDMMYY = sin[4:]

    DD = sin[4:6]
    MM = sin[6:8]
    YY = sin[8:]

    is_leap_year = False

    DAYS_MONTH = {
        "01":31,
        "02":28,
        "03":31,
        "04":30,
        "05":31,
        "06":30,
        "07":31,
        "08":31,
        "09":30,
        "10":31,
        "11":30,
        "12":31,
    }

    if int(YY) > 24:
        year = 1999 + int(YY)
    else:
        year = 2000 + int(YY)  
    if year % 4 == 0:
        is_leap_year = True

    if not (MM in DAYS_MONTH.keys()):
        return False
    return (int(DD) <= DAYS_MONTH[MM] and int(DD) >= 1) or (is_leap_year and (MM == "02" and int(DD) <= 29))

def validate(sin: str) -> None:
    if not isValidSyntax(sin):
        print("INVALID SYNTAX")
    elif not hasValidDate(sin):
        print("INVALID DATE")
    elif hasValidCheckDigit(sin):
        print("OK")


for sin in sin_data:
    validate(sin)
