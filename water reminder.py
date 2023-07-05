import time
import win32com.client

alert = int(input("I will remind you after how long (hr):"))

while True:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print("Current Time:", current_time)

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Voice = speaker.GetVoices().Item(1)
    speaker.Speak("Time to drink water. Thank you")

    next_reminder_time = time.localtime(time.time() + alert*60*60)
    next_reminder_time_str = time.strftime("%H:%M:%S", next_reminder_time)
    print(f"Next reminder after {next_reminder_time_str}")
    time.sleep(alert*60*60)
