import os

def main():
	print("Current Working Directory " , os.getcwd())
	try:
		# Change the current working Directory on Actual Directory   
		os.chdir(os.getcwd())
		print("Directory changed")
	except OSError:
		print("Can't change the Current Working Directory")        
		print("Current Working Directory " , os.getcwd())
	# Check if New path exists
	if os.path.exists(os.getcwd()) :
		# Change the current working Directory    
		os.chdir(os.getcwd())
	else:
		print("Can't change the Current Working Directory")    
		print("Current Working Directory " , os.getcwd())
if __name__ == '__main__':
	main()