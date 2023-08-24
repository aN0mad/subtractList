import argparse
from loguru import logger
import os
import sys

# Custom imports
from liblog.liblog import initLogger

# VARS
FILELOGGER = "" # This var is passed to initLogger to log to a file
UPDATED = "cleaned"

def do_argparse():
    '''
    Description:
        argparse creates a commandline and handles argument parsing
    
    Returns:
        dictionary
    '''
    # Vars
    args = {}
    
    # Create the parser
    parser = argparse.ArgumentParser(description="A script to modify the severity of vulnerabilities within a nessus file")
    
    # Add arguments
    parser.add_argument("-b","--base", help="File to use as the base", default="", action="store")
    parser.add_argument("-s","--subtract", help="File subtract from the base file", default="", action="store")
    #parser.add_argument("-d", "--dir", help="Directory to glob configs from",  default="", type=str, action="store")
    parser.add_argument("--debug", help="Enable debug", default=False, action="store_true")
    
    # Parse the arguments
    args_parser = parser.parse_args()

    if args_parser.base == "":
        print("Error: Missing parameter -b/--base")
        print()
        parser.print_help()
        sys.exit(1)
    
    if args_parser.subtract == "":
        print("Error: Missing parameter -s/--subtract")
        print()
        parser.print_help()
        sys.exit(1)
    
    
    # Set arguments
    args["base"] = args_parser.base
    args["subtract"] = args_parser.subtract
    args["debug"] = args_parser.debug
    
    # Return
    return args

def subtractlists():
    args = do_argparse()
    initLogger(args["debug"], False, FILELOGGER, logger)

    # Error checking
    if os.path.exists(args["base"]) and os.path.isfile(args["base"]):
        pass
    else:
        logger.fatal("{base} either does not exist or is a directory".format(base=args["base"]))
        sys.exit(1)
    
    # Error checking
    if os.path.exists(args["subtract"]) and os.path.isfile(args["subtract"]):
        pass
    else:
        logger.fatal("{base} either does not exist or is a directory".format(base=args["subtract"]))
        sys.exit(1)
    
    # Read base file
    logger.info("Reading lines from base {base}".format(base=args["base"]))
    baseLines = open(args["base"], "r").readlines()

    # Read subtraction file
    logger.info("Opening subtraction file {file}".format(file=args["subtract"]))
    with open(args["subtract"], "r") as fhandle:
        for line in fhandle.readlines():
            if line in baseLines:
                logger.log("MODIFICATION", "Removing line {line}".format(line=line.strip()))
                baseLines.remove(line)
                continue
            else:
                if line.strip() == "":
                    line = "<BLANK>"
                logger.debug("Skipping line {0}".format(line.strip()))
    
    # Write base items back out
    file, ext = os.path.splitext(args["base"])
    fname = os.path.join("{bname}-{updated}{ext}".format(bname=file,updated=UPDATED,ext=ext))

    logger.info("Writing output file: {0}".format(fname))
    with open(fname, "w") as fhandle:
        fhandle.writelines(baseLines)
    
    logger.log("FILEWRITE", "Writing output file: {0}".format(fname))

