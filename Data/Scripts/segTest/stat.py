#!/usr/bin/python

# multithreading  module imported here
import threading 
from threading import Thread
# os module imported here
import os 
# sys module imported here
import sys
# glob module for file list
import glob



def clean():
	print "................................................................"
	print "Cleaning Environment"
	print "................................................................"

	cmd = "rm /var/log/suricata/eve.json  /var/log/suricata/fast.log  /var/log/suricata/stats.log  /var/log/suricata/suricata.log"
	os.system(cmd)


	
def cleanRes():
	print "................................................................"
	print "Cleaning Environment"
	print "................................................................"

	cmd = "rm ./result*"
	os.system(cmd)



def run(filename, output):
	print "................................................................"
	print "Run run_args.sh"
	print "................................................................"
	
	cmd = "./run_arg.sh " + filename + " " + output
	os.system(cmd)

	

def lsPcap():
	print "................................................................"
	print "Get all Splitted Pcap Files in Current Folder"
	print "................................................................"
	return glob.glob("./out.pcap*")



def lsRes():
	print "................................................................"
	print "Get all Result Files in Current Folder"
	print "................................................................"
 
	return glob.glob("./result*")



def stat(filename):
	print "................................................................"
	print "Get Stats : " + filename
	cmd = "sort -n " + filename + "  | uniq -c"
	os.system(cmd)




counter = 0

for filename in lsRes():
	stat(filename)
	counter = counter + 1




