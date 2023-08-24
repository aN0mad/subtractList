import sys

def initLogger(DEBUG, QUIET, FILELOGGER, logger):
    logger.remove(0)
    level_fileWrite = logger.level("FILEWRITE", no=31, color="<blue>")
    level_modification = logger.level("MODIFICATION", no=31, color="<yellow>")
    
    if QUIET:
        logger.add(sys.stdout, colorize=True, format="{time} | <level>{level}</level> | {message}", level=100)
        return
    
    if DEBUG:
        logger.add(sys.stdout, colorize=True, format="{time} | <level>{level}</level> | {message}", level="DEBUG")
        if FILELOGGER != "":
            logger.add(FILELOGGER, colorize=True, format="{time} | <level>{level}</level> | {message}", level="DEBUG")
    else:
        logger.add(sys.stdout, colorize=True, format="{time} | <level>{level}</level> | {message}", level="INFO")
        if FILELOGGER != "":
            logger.add(FILELOGGER, colorize=True, format="{time} | <level>{level}</level> | {message}", level="INFO")