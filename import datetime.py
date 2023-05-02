import datetime
import time
import os


def set_alarm():
    print("Enter the time to set the alarm in 24-hour format (hh:mm:ss):")
    alarm_time = input("> ")
    alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
    return datetime.time(alarm_hour, alarm_minute, alarm_second)

def play_sound():
    # Replace this with code to play an audio file of your choice
    os.system("start alarm.wav")

def main():
    print("Welcome to Alarm Clock!")
    alarm_time = set_alarm()
    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= alarm_time:
            print("Time to wake up!")
            play_sound()
            break
        time.sleep(1)

if __name__ == '__main__':
    main()
