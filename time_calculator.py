def add_time(start, duration, week=None):
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    ampm = startArr[1]

    durationTime = duration.split(':')

    endHour = (int(startTime[0]) + int(durationTime[0])) % 12
    tmpEndMinute = (int(startTime[1]) + int(durationTime[1]))
    if(tmpEndMinute > 59):
        endHour += 1
    
    endMinute = tmpEndMinute % 60


    endTime = str(endHour) + ':' + str(endMinute).zfill(2)

    return endTime