N = int(input())
start_day = int(input()) - 1

# 1  2  3  4 5  6 7
# 일 월 화 수 목 금 토

days = [0] * 7

dates = 365

# 윤년 계산
if (N % 4 == 0 and N % 100 != 0 or N % 400 == 0):
    dates = 366

# 1, 3, 5, 7, 8, 10, 12월 31일
# 2월 28일 or 29일
# 4, 6, 9, 11월 30일


result = 0

for month in range(1, 13):
    days = [0] * 8
    date = 1

    if month in [1, 3, 5, 7, 8, 10, 12]:
        while (date <= 31):
            days[(start_day + date) % 7] += 1
            date += 1
    elif month in [4, 6, 9, 11]:
        while (date <= 30):
            days[(start_day + date) % 7] += 1
            date += 1
    elif (month == 2):
        if dates == 365:
            while (date <= 28):
                days[(start_day + date) % 7] += 1
                date += 1
        elif dates == 366:
            while (date <= 29):
                days[(start_day + date) % 7] += 1
                date += 1
    start_day = (start_day + date) % 7

    for day in days:
        if day >= 5:
            result += 1

print(result)
