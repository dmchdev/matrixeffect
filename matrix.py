import random, time, ctypes
#-------------------------------DEFINITIONS AND METHODS-------------------------------
width = 170
msec = 0.1
randomness = 50
lst = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefjhijklmnopqrstuvwxyz$$$@^^^#~&&&()()()()[][][]{}{}{}                      ") #converting string to a list
lst_1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def genFirstStr(): #---this generates the first string to be displayed--a starting point
	echLnLst = []
	i=0
	while i<width:
		echLnLst.append(random.choice(lst_1))
		i+=1           # this variable must be increased after every append call
		blanks = random.randint(2,5) # spaces between characters are randomized
		for echBl in range(0,blanks): #several spaces are inserted 
			echLnLst.append(" ")
			i+=1
			if i==width:
				break # breaking for loop if i reaches desired width
	firstStr = ''.join(echLnLst) #converting list to a string
	return(firstStr)

def randStr(aStr): #randomizing strings by modifying each firstStr element based on whether
                   # the regulating factor variable, randomizer, matches this time. Otherwise,
                   # no change and the new characters will be displayed in same positions
                   # as those in previous string. This creates random vertical columns.
                   # Without it, all columns would always follow the characters of the
                   # first string.

	lst_3 = list(aStr)
	for i in range(0,len(aStr)):
		set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)

		randomizer=random.randint(0,randomness)

		if randomizer==20 and i<len(aStr)-1:
			if lst_3[i] == " " and lst_3[i-1] == " " and lst_3[i+1] == " ":
				lst_3[i] = random.choice(lst_1)
				set_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
			else:
				lst_3[i] = " "
				set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
	rStr = ''.join(lst_3)
	return (rStr)




		

def modFirstStr(gFSresult): # this takes any string and replaces characters in it with 
                            # different ones, leaving blank spaces intact. Vertical
                            # columns have breaks in them because some characters that
                            # replace previous ones are themselves blanks. This is why
                            # 'lst' string variable has so many spaces 

	lst_2 = list(gFSresult)
	
	for i in range(0,len(gFSresult)):
	
		if lst_2[i] != " ": #replacing characters with different characters, ignoring spaces
			lst_2[i] = random.choice(lst)
		
	modStr = ''.join(lst_2)
	return(modStr)
#------------------------------EXECUTION------------------------------------
firstStr = genFirstStr()
print(firstStr)
while True:
	firstStr = randStr(firstStr)
	modStr = modFirstStr(firstStr)
	print(modStr)
	time.sleep(msec)