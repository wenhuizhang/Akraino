#/usr/bin/python



# os module imported here
import os 
# sys module imported here
import sys



# get present working directory location as default
location = os.getcwd() 
#keep a count of all files found
counter = 0 
#keep a count of pcap files found
pcapcounter = 0 
#keep a count of non pcap  files found
nonpcapcounter = 0 
#list to store all pcap files found at location
pcapfiles = []
#list to keep any other file that do not match the criteria
otherfiles = [] 




# if input arguments are wrong, print out usage

if len(sys.argv) != 2:
    print >> sys.stderr, "usage: python {0} folder\n".format(sys.argv[0])

    sys.exit(1)

location = sys.argv[1]


print "................................................................"
print "Analyzing files in" , location
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
