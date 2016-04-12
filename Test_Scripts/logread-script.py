import os
import csv
from shutil import move
from os import remove, close

###################################
#   Open RC script and change effort 
###################################

with open("scripts/simd_fpu.rc",'r+') as rcFile:
	with open("scripts/temp.rc", 'w') as outrcFile:
		print "simd_fpu.rc open, r+ mode"
		for line in rcFile:
			if line.startswith("synthesize"):
				print "Line found"
				#line = line[30:33]
				#print l
				line =line.replace("low", "high")
				print "low replaced"
				#print l
			outrcFile.write(line)
###################################
#   Replace RC file with modified script 
###################################
remove('scripts/simd_fpu.rc')
move(('scripts/temp.rc'), ('scripts/simd_fpu.rc'))	
print "rc file saved"			


###################################
#  Execute scripts 
###################################
#os.system("./scripts/compile.sh~")
#os.system("rc -logfile 10 -f scripts/simd_fpu.rc")
#os.system("ecnounter -64 -log denc.log -init scripts/simd_fpu.enc")

###################################
#   Read RC log and output results
###################################
 
with open("dlog34",'r') as logFile:
    print "file open, R mode"
    for line in logFile:
        	if line.startswith(" Slack"):
          	 print "Slack :"
                 l = logFile.next()
		 l = logFile.next()
		 l = l[2: l.find("p")]
           	 print l;            


###################################
#   Read Encounter log and output results
###################################
 
with open("denc.log",'r') as logFile:
	print "file open, R mode"
	for line in logFile:
		if line.startswith("          timeDesign Summary"):
        		n = 0;
		 
		  	while n !=  6:
		  		l = logFile.next()
		   		n = n+1;
				l = l[24: 29]
		   
          	   	print l; 
		    	break;
	           
###################################
#   Print results to CSV file
###################################   
f = open("scripts/enc_results.csv", 'w')
RESULT = ['apple','cherry','orange','pineapple','strawberry']	
c = csv.writer(f, dialect='excel')

c.writerow(RESULT)


