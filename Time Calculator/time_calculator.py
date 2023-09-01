def add_time(start, duration, day=False):

  time = start.split(' ')

  start_hour = int(time[0].split(':')[0])
  start_min = int(time[0].split(':')[1])

  duration_hour = int(duration.split(':')[0])
  duration_min = int(duration.split(':')[1])

  # Convert to 24h format

  if time[1] == 'PM' and start_hour < 12:
    start_hour += 12
  elif time[1] == 'AM' and start_hour == 12:
    start_hour -= 12

  # Sum the total of hours

  days_later = 0
  total_min = start_min + duration_min
  total_hours = start_hour + duration_hour

  if total_min > 60:
    total_hours += 1
    total_min -= 60
  if total_min < 10:
    total_min = '0' + str(total_min)
    
  while total_hours >= 24:
    total_hours -= 24
    days_later += 1

  # Convert to 12h format

  if total_hours == 0:
    total_hours += 12
    time = 'AM'
  elif total_hours < 12:
    time = 'AM'
  elif total_hours == 12:
    time = 'PM'
  else: 
    total_hours -= 12
    time = 'PM'

  # Days of week

  days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  if day != False:
    index = days_of_week.index(day.capitalize())
    days_left = days_later
    while days_left > 0:
      index += 1
      days_left -= 1
      if index == len(days_of_week):
        index = 0
    day = days_of_week[index]

  # Return values

  format_day = '' if day == False else f', {day}'

  if days_later == 0: 
    return f'{total_hours}:{total_min} {time}{format_day}'
  elif days_later == 1:
    return f'{total_hours}:{total_min} {time}{format_day} (next day)'
  else: 
    return f'{total_hours}:{total_min} {time}{format_day} ({days_later} days later)'
