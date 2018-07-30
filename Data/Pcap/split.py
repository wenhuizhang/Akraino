#!/usr/bin/python

"""
 program to split up a pcap file into smaller pieces.
tethereal and friends can't open files bigger than 2GB: this utility lets
you split a large pcap file into smaller files.

The actual implementation is a total hack based on reading pcap.h and
implementing the bare minimum in python. I wrote this for 32 bit x86
Linux system; types may vary on other OS."""

import struct, sys


# pcap file format definition. Types pulled from pcap.h
pcap_file_header = "IHHiIII"
pcap_pkthdr = "llII"
pcap_file_header_length = struct.calcsize(pcap_file_header)
pcap_pkthdr_length = struct.calcsize(pcap_pkthdr)

outFiles = 0
outBytes = 0
def newOutFile(file_header):
    "Create a new pcap output file with a serial number in the filename"
    global outFiles, outBytes

    # Make up a filename
    fn = "splitpcap.%04d" % outFiles
    outFiles += 1
    print "Writing file %s" % fn
    # Write the file header from the file we read
    fp = open(fn, "wb")
    fp.write(file_header)
    outBytes = len(file_header)
    return fp

def main():
    global outBytes
    maxSize = 1024*1024*1024
    fp = sys.stdin

    # Read the pcap file header. We don't really need to parse this.
    file_header = fp.read(pcap_file_header_length)

    outFP = newOutFile(file_header)

    while True:   # no exit condition, the last read just throws an exception
        # Read the packet header
        pkthdr = fp.read(pcap_pkthdr_length)
        sec, usec, caplen, length = struct.unpack(pcap_pkthdr, pkthdr)
        # Read the packet itself
        pkt = fp.read(caplen)

        # Rotate the file if necessary
        moreBytes = pcap_pkthdr_length + caplen
        if moreBytes + outBytes > maxSize:
            outFP = newOutFile(file_header)

        # Write the packet
        outFP.write(pkthdr)
        outFP.write(pkt)
        outBytes += moreBytes

if __name__ == "__main__":
    main()
    
