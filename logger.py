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
            space_split = line.split(None, 1)
            action = space_split[0]
            message = space_split[1] if len(space_split) > 1 else ""

            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M")

# Write log entry formatted properly
            finalLog.write(f"{time_stamp} [{action}] {message}\n")
            finalLog.flush()

if __name__ == "__main__":
    main()
