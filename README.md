# SSHSniffer

Name: David Ehevich

Name: Dvir Biton 

ssh packet sniffer to detect fuzzing attacks

How to run:

*Firstly download all of the included libraries in the program(pyenchant & scappy), to be able to run the program.

*All of the files in the git repo must be downloaded into the same directory.

*Run the main.py program first , this is the program which sniffs the SSH packets. Then run send_p.py program, this program sends the SSH packets for testing 

Inside the the send function we can send what ever payload we want.

Fuzzing detected:

If Fuzzing attack is detected in the pay load of the ssh packet, The user will be notified via terminal that a Fuzzing attack has occured.


