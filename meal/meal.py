def main():
    time = input('What time is it? ')
    time_float = convert(time)

    if 7.0 <= time_float <= 8.0:
      print('breakfast time')
    elif 12.0 <= time_float <= 13.0:
      print('lunch time')
    elif 18.0 <= time_float <= 19.0:
      print('dinner time')

def convert(time):
  hour_str, minutes_str = time.split(':')
  hour = float(hour_str)
  minutes = float(minutes_str)

  return hour + minutes / 60.0

if __name__ == "__main__":
    main()