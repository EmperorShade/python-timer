import fontstyle
from winotify import Notification
from winotify import audio
import time


print(fontstyle.apply('\n \n \ngithub.com/shriramsburger',
 						'bold/Italic/cyan/BALCK_BG'))
time.sleep(2)

#getting input
print(fontstyle.apply('\n\nWhat should I remind you about?',
						'bold/Blink/yellow')) #ex: turn off microwave

text = str(input())

print(fontstyle.apply('\nIn how many minutes should I remind you?',
		'bold/Blink/purple')) #ex: 1, 30, 0.25
local_time = float(input())

print(fontstyle.apply('\nOkay, setting a timer',
						'bold/Italic/Darkcyan'))

#converting timet to seconds
local_time = local_time * 60


# waiting for specified time
time.sleep(local_time)



# after time is completed

	#notification
toast = Notification(app_id="Python Timer",
                     title=text,
                     msg="It has been 5 minutes.",
                     icon="c:\\users\\dhara\\desktop\\clock_red.ico",
                     duration = "long")
	#sound/audio
toast.set_audio(audio.LoopingAlarm3, loop = True)
	
	#quit button
toast.add_actions(label = "Click to close")
	
	#sending notification
toast.show()

time.sleep(3)


print(fontstyle.apply('\nTime"s up!',
						'bold/Italic/underline/red/\n\n'))
	#exiting
quit()