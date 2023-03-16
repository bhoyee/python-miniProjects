#program that create a small animation program
#zigzag pattern program


# Note : this progrm will continue to run until CTRL-C is press to stop the program 

import time , sys
indent = 0 # How many spaces to indent.
indentIncreasing = True #Wheather  the indentation is increasing or not.

try:
    while True: # The man program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 for a second

        if indentIncreasing:
            # increase the number of soaces:
            indent = indent + 1
            if indent == 20:
                # change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()