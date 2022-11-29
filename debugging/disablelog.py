import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s -%(levelname)s - %(message)s')
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)  #DISABLES EVERYTHING AFTER
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')

#Logging to a file

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#instead of doing it with comments, it does it in a file that can be opened in the notepad for example