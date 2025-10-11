import sys
from datetime import datetime

def main():

# confirm two total arguments, script name + log file name = 2
    if len(sys.argv) != 2:
        print("Usage: logger.py <logfile>")
        sys.exit(1)

# retrieve log file name 
    logfile = sys.argv[1]
    # start adding where left off
    with open(logfile, "a") as finalLog:
        # reads all lines written untill "QUIT"
        for line in sys.stdin:
            line = line.rstrip()
            if line == "QUIT":
                break

# split action and message at first whitespace
            spaceSplit = line.split(None, 1)
            action = spaceSplit[0]
            message = spaceSplit[1] if len(spaceSplit) > 1 else ""

            timeStamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Write log entry formatted properly
            finalLog.write(f"{timeStamp} [{action}] {message}\n")
            finalLog.flush()

if __name__ == "__main__":
    main()
