def make_readable(seconds):
    hours = 0
    minutes = 0

    if seconds >= 3600:
        hours = int(seconds / 3600)
        hour_remainder = seconds % 3600
        minutes = int(hour_remainder / 60)
        lastseconds = hour_remainder % 60
    elif seconds > 59 and seconds < 3600:
        minutes = int(seconds/60)
        lastseconds = seconds % 60
    elif seconds < 60:
        lastseconds = seconds
        
    return(f'{"{:0>2d}".format(hours)}:{"{:0>2d}".format(minutes)}:{"{:0>2d}".format(lastseconds)}')

print(make_readable(0))