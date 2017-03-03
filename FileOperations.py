def enter_text_file(performances):
	file = open("schedule.txt", 'a')
	for show,time in performances.items():
		file.write(show + ' ' + time + '\n')
		#print("Writing to the file")
	file.close()

def read_text_file():
	file = open("schedule.txt",'r')
	for data in file:
		print(data)
	#print ("Reading"+data)
	file.close()

def read_log_file():
	file = open("apache.txt", 'r')
	for data in file:
		print(data.split()[0] + ' ' + data.split()[5]+data.split()[6])

	file.close()

def read_comma_separated():
	file = open("commas", 'r')
	for data in file:
		print(data.strip().split(','))
	file.close()

def read_log_fixed_length():
	width = [0,12]
	file = open("apache.txt", 'r')
	for data in file:
		print(data[:12] + " ** " + data[18:39] )
#Reverse String  str[::-1]


def main():
	#performances = {'Night at the Museum': '10:00 PM', 'Yanky Doodle': '11:00 AM'}
	#enter_text_file(performances)
	#read_text_file()
	#read_log_file()
	#read_log_fixed_length()
	read_comma_separated()

main()


