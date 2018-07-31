#!/usr/bin/python



# os module imported here
import os 
# sys module imported here
import sys



# get filename to be splited 
filename = "" 
# size of pcap files to be split
size = "10" 
# list of out files 
files = [] 


os.system("rm out.pcap*")

# if input arguments are wrong, print out usage

if len(sys.argv) != 3:
    print >> sys.stderr, "usage: python {0} file size\n".format(sys.argv[0])

    sys.exit(1)

filename = sys.argv[1]
size = sys.argv[2] 


print "................................................................"
print "Spliting file " , filename, "into", size
print "................................................................"



cmd = "tcpdump -r " + filename +  " -w " + "out.pcap -C " + size

os.system(cmd)

print "\n\n\n................................................................"
print "Summary\n"
print "File processed:\t", filename
print "Size in MB:\t", size
print "Output:"
os.system("ls out.pcap* | wc -w")
os.system("ls -lash out.pcap*")
os.system("ls -lash out.pcap* | awk '{print $NF}'")

