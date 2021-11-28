# Первый вариант, рабочий но не красивый на мой взгляд
duration = int(input())
if duration < 60:
    print(f'{duration} сек')
elif 60 <= duration < 3600:
    print(f'{duration // 60} мин {duration % 60} сек')
elif 3600 <= duration < 86400:
    print(f'{duration // 3600} ч {(duration % 3600) // 60} минут {(duration % 3600) % 60} сек')
elif 86400 <= duration:
    print(
        f'{duration // 86400} дн {(duration % 86400) // 3600} ч {(duration % 86400) % 3600 // 60} минут {((duration % 86400) % 3600) % 60} сек ')

# Второй вариант , длиннее но более читабелен

duration = int(input())
day, hour, minute = 0, 0, 0
result = ""

if duration >= 86400:
    day += duration // 86400
    duration -= day * 86400
    result = "".join(str(day) + " дн ")

if 3600 <= duration < 86400:
    hour += duration // 3600
    duration -= hour * 3600
    result += "".join(str(hour) + " ч ")

if duration < 3600:
    minute += duration // 60
    duration -= minute * 60
    result += "".join(str(minute) + " мин ")

print(result + str(duration) + " сек")
