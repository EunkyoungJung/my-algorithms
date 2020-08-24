def solution(a, b):
    day = {4: 'MON', 5: 'TUE', 6: 'WED', 0: 'THU', 1: 'FRI', 2: 'SAT', 3: 'SUN'}
    months = {1: 31, 2: 29, 3: 31,
              4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30,
              10: 31, 11: 30, 12: 31}

    days = 0
    for m in range(1, a):
        days += months[m]

    days += b

    return day[days % 7]