import time

a = int(time.time()) + 9 * 3600 # 우리나라 시간

sec = lambda x : x % 60
min = lambda x : x // 60 % 60
hour = lambda x: x//3600 % 24

def year_days(y):
    leap = (y%4 ==0 and (y % 100 !=0 or y % 400 == 0))
    return 366 if leap else 365

def ymd_from_days(days,y):
    leap = (y % 4 ==0 and (y % 100 !=0 or y % 400==0))
    mdays = [31,28 +leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m = 0
    while days >= mdays[m]:
        days -= mdays[m]
        m+=1
        return m+1, days+1

def year_from_days(days):
    y = 1970
    while days >= year_days(y):
        days -= year_days(y)
        y+=1
    return y

days = a//86400 # 총 일수, 하루 : 24*60*60=86400초
y = year_from_days(days)
#월, 일 계산
dd = days - sum(year_days(y) for y in range(1970,y))
mm, d = ymd_from_days(dd,y)
#첬째인자: (햔재까지 모든 일수 - sum()), sum()은 1970~현재연도까지의 1년의 날짜를 모두 합하는 함수
#둘째인자: 윤년 판단을 위해 계산해 둔 올해 연도를 넘긴다.

h = hour(a)
m = min(a)
s = sec(a)

print(f"{y}년, {mm}월, {d}일, {h}시, {m}분, {s}초")