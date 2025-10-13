10/10 11:30 AM

Understanding of the project:

cpu.py - lanches mem.py as subprocess and commmunicates
mem.py - reads commands to "write" or "read" until "hault"
logger.py - take input into log file w/ timestamp, action, message until "QUIT"
encryption.py - set passkey,encrypt, or decrypt and output results until "QUIT" 
driver.py - gives menu of commands  where input/result is logged until "QUIT"
logfile.txt - text file of logs 

10/10 12:30 PM
This is the same day, all I have done is gathered ideas about the project along with 
adding cpu.py and mem.py into this respritory as well as the VS code I am using to run the project.
I also ran python cpu.py to confirm cpu.py and mem.py are working correctly. 

The part of my code I will be working on now is the logger.py
You call it by doing "logger.py examplefile.txt"
I will get the [action "Message"] input along with the ouput of 
[timestamp [action] "message"]
The next log will be the final logger.py confirmation along with the push of the code to the 
main branch when it is done. 

10/11 11:15 AM - logger.py
Throughout the last day I have worked on the logger.py file to complete it.
I have: 
1. created a filter to confirm it comes in script name + log file name
2. gets the log file name
3. splits the action and messgae
4. writes output into logfile.txt

This includes running tests  like...
YYYY-MM-DD HH:MM [ACTION] MESSAGE
So, the log message “START Logging Started.”, logged March 2nd, 2025 at 11:32 am would be
recorded as below.
2025-03-02 11:32 [START] Logging Started.
with proper function.

Next I will be working on the encryption.py

This will take "command argument" where it can do: PASS, ENCRYPT, DECRYPT, QUIT, RESULT, ERROR.

10/13 4:00 PM
Throughout the last day I have worked on the encryption.py file to complete it.
I have: 
1. created an ENCRYPT and DECRYPT text using Vigenère cypher
2. created "PASS" command to recieve the key used
3. on "QUIT" quit
4. on "ENCRYPT" or "DECRYPT" if key = None, then "ERROR"
5. print "RESULT" if preceeding command completes

I have confirmed the accuracy of my program by following the example given in the instructions

The next and final part of the project is the driver.py

The drivers job is taking the "driver.py logfile.txt" and create processes linking the
logger and encryption programs, connecting the input and output.
It will have prompted commands being: PASSWORD, ENCRYPT, DECRYPT, HISTORY, QUIT
It will loop until the user "QUIT"s logging everything thr user does.
Also with error buffers!


