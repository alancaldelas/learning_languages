'''
Alan Caldelas
'''

import time, subprocess 

def start_timer_process():
	print("TIME HAS BEGUN")
	count = 24
	while(count != 25):
		print(f"Min elapsed... {count} mins")
		time.sleep(60)
		count = count + 1
	subprocess.run(["zenity","--width=250", "--height=250", "--warning", "--text='finished time'"])
	
	print("Time has completed")
	retrieve_input()

def retrieve_input():
	user_input = input("Do you wish to begin program?\n>")
	if (str(user_input) == "y"):
		print("Beginning timer for 25 mins")
		start_timer_process()
	else:
		print("Ending program...")
		exit()
def main():
	print("Program designed to time 25 mins for reading/work.")
	retrieve_input()


main()


