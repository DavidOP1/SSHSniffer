# SSHSniffer

Name: David Ehevich

Fuzzing detector via auth logs.

How to run:

*Firstly download all of the included libraries in the program, to be able to run the program.

*All of the files in the git repo must be downloaded into the same directory.

*Run the FuzzingDetector.py program first , this program goes through auth.log , this log file logs every log on attempt , remotely or directy , so we check if there are any irregularities , for example : too many errors , connection closed , etc. As seend in the Fuzzing attack lab, when a fuzzing attack occurs , a spam of errors or other suspicious logs appear. Once we detect too many of these suspicious logs , we alert the user that a Fuzzing Attack is occuring, and the program will shut it self.




