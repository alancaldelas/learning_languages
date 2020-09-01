'''
Alan Caldelas
'''

import time, subprocess,random, webbrowser 

urls = ['https://www.youtube.com/watch?v=F1B9Fk_SgI0', 'https://www.youtube.com/watch?v=RQqJeIyyQBs', "https://www.youtube.com/watch?v=Z-48u_uWMHY", 'https://www.youtube.com/watch?v=l3Cj7Esqr0c']

def start_timer_rest(completed):
	"""
	Starts a timer based on how many completetions have passed
	"""
	if completed == 5:
		print("You have completed this round rest 25 mins")
		completed = 0
		rtime = 25
	else:
		print("You have completed this section {completed} /5")
		rtime = 5
	print("REST TIME HAS BEGUN FOR rtime")
	count = 0
	while(count != rtime):
		time.sleep(60)
		count = count + 1
		print(f"Min elapsed... {count} mins")

	subprocess.run(["zenity","--width=250", "--height=250", "--warning", "--text='finished time'"])
	
	print("Rest time has completed")
	
	retrieve_input(completed)
	
def start_timer_read(completed):
	print(f"You have completed {completed} so far")
	print("TIME HAS BEGUN")
	count = 0
	while(count != 25):
		time.sleep(60)
		count = count + 1
		print(f"Min elapsed... {count} mins")
	completed = completed + 1
	subprocess.run(["zenity","--width=250", "--height=250", "--warning", "--text='finished time'"])
	
	print("Time has completed")
	webbrowser.open(random.choice(urls))
	start_timer_rest(completed)

def retrieve_input(completed):
	user_input = input("Do you wish to begin program?\n>")
	if (str(user_input) == "y"):
		print("Beginning timer for 25 mins")
		start_timer_read(completed)
	else:
		print("Ending program...")
		exit()
def main():
	retrieve_input(0)


main()


