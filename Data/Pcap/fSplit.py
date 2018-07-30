#!/usr/bin/python



# os module imported here
import os 
# sys module imported here
import sys



# get filename to be splited 
filename = "" 
#keep a count of pcap files to be split
splitcounter = 1 
#list of out files 
files = [] 




# if input arguments are wrong, print out usage

if len(sys.argv) != 3:
    print >> sys.stderr, "usage: python {0} file counter\n".format(sys.argv[0])

    sys.exit(1)

filename = sys.argv[1]
splitcounter = sys.argv[2] 


print "................................................................"
print "Spliting file " , filename, "into", splitcounter
print "................................................................"


for file in os.listdir(location):
    try:
        if file.endswith(".pcap"):
            print "pcap file found:\t", pcapcounter+1, ".", file
            pcapfiles.append(str(file))
            pcapcounter = pcapcounter+1
        else:
            #print "non pcap file found:\t", nonpcapcounter+1, ".", file
            otherfiles.append(file)
            nonpcapcounter = nonpcapcounter+1
    	counter = counter+1
    except Exception as e:
        raise e
        print "No files found here!"

print "\n\n\n................................................................"
print "Summary\n"
print "Total files found:\t", counter
print "Total pcap files found:\t", pcapcounter
print "Total non pcap files found:\t", nonpcapcounter
