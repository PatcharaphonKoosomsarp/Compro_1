def digitalClock(hours):
    hours = hours % (24 * 3600)
    minutes = hours % 3600
    seconds = minutes % 60
    return "%d:%02d:%02d" % (hours // 3600, minutes // 60, seconds)

print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))