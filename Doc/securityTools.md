# Security Tools 

A summary of security tools applicable to Akraino Stack.

## General Security Tools:

### 1. Password Complexity Check: 

1.1 John The Ripper: A fast password cracker http://www.openwall.com/john/

1.2 atstaketools: This is an archive of various tools that help perform vulnerability scanning and analysis, information gathering, password auditing, and forensics.http://packetstormsecurity.com/files/50718/AtStakeTools.zip.html

1.3 Cisco-ocs: Cisco Router Default Password Scanner.
http://www.question-defense.com/2013/01/11/ocs-version-2-release-ocs-cisco-router-default-password-scanner

1.4 cisco5/7crack: Crypt and decrypt the cisco enable 5 and 7 passwords.	https://github.com/madrisan/cisco7crack

1.5 Ciscos: Scans class A, B, and C networks for cisco routers which have telnet open and have not changed the default password from cisco.

1.6 climber: Check UNIX/Linux systems for privilege escalation. https://github.com/raffaele-forte/climber

1.7 Clusterd: Automates the fingerprinting, reconnaissance, and exploitation phases of an application server attack. https://github.com/hatRiot/clusterd

1.8 Cmospwd: Decrypts password stored in CMOS used to access BIOS setup. http://www.cgsecurity.org/wiki/CmosPwd


### 2. Fuzzing Tools:

2.1  AFL : American Fuzzy Lop Fuzzer by Michal Zalewski aka lcamtuf http://lcamtuf.coredump.cx/afl/

2.2 Obfuscated String Solver: https://github.com/fireeye/flare-floss

2.3 Cloudfuzzer: Cloud fuzzing framework which makes it possible to easily run automated fuzz-testing in cloud environments. https://github.com/ouspg/cloudfuzzer

2.4 Peach Fuzzer, a Network Protocol Fuzzer which helps to create custom dumb and smart fuzzers. https://sourceforge.net/projects/peachfuzz/

2.5 Spike: A fuzzer development framework like sulley, a predecessor of sulley. http://www.immunitysec.com/downloads/SPIKE2.9.tgz

2.6 Metasploit Framework: A framework which contains some fuzzing capabilities via Auxiliary modules. https://github.com/rapid7/metasploit-framework

2.7 KernelFuzzer: Cross Platform Kernel Fuzzer Framework. https://github.com/mwrlabs/KernelFuzzer



### 3. Taint Analysis Tools:

3.1 PANDA: Platform for Architecture-Neutral Dynamic Analysis. https://github.com/moyix/panda

3.2 QIRA: QEMU Interactive Runtime Analyser. http://qira.me/

3.3 kfetch-toolkit: Tool to perform advanced logging of memory references performed by operating systems’ kernels.  https://github.com/j00ru/kfetch-toolkit

3.4 moflow: A software security framework containing tools for vulnerability, discovery, and triage. https://github.com/vrtadmin/moflow



### 4. Databases:

4.1 Exploit-DB: databases to lookup exploits scripts. https://www.exploit-db.com/

4.2 CVE: database to lookup vulnerabilities reported. https://cve.mitre.org/

4.3 CWE: database to lookup vulnerabilities reported. https://cwe.mitre.org/

4.4 ATT&CK™: curated knowledge base and model for cyber adversary behavior, reflecting the various phases of an adversary’s lifecycle and the platforms they are known to target. https://attack.mitre.org/wiki/Main_Page



### 5. Symbolic Execution SAT and SMT Solvers: 

5.1 Z3: A theorem prover from Microsoft Research. https://github.com/Z3Prover/z3

5.2 SMT-LIB: An international initiative aimed at facilitating research and development in Satisfiability Modulo Theories (SMT). http://smtlib.cs.uiowa.edu/



### 6. Debuggers and Disassemblers

6.1 GDB: The favorite linux debugger. http://www.sourceware.org/gdb/

6.2 Radare2: Framework for reverse-engineering and analyzing binaries. http://www.radare.org/r/

6.3 IDA Pro: The best disassembler. https://www.hex-rays.com/products/ida/index.shtml



### 7. Pentesting

7.1 OpenVAS: OpenVAS is a framework of several services and tools offering a comprehensive and powerful vulnerability scanning and vulnerability management solution. http://www.openvas.org/

7.2 Metasploit Framework: A tool for developing and executing exploit code against a remote target machine. Other important sub-projects include the Opcode Database, shellcode archive and related research. https://github.com/rapid7/metasploit-framework

7.3 Kali: Kali Linux is a Debian-derived Linux distribution designed for digital forensics and penetration testing. Kali Linux is preinstalled with numerous penetration-testing programs, including nmap (a port scanner), Wireshark (a packet analyzer), John the Ripper (a password cracker), and Aircrack-ng (a software suite for penetration-testing wireless LANs). https://www.kali.org/

7.4 pig: A Linux packet crafting tool. https://github.com/rafael-santiago/pig



### 8. Scanning Network:

8.1 Nmap: Nmap is a free and open source utility for network discovery and security auditing. https://nmap.org/

8.2 Amass: Amass performs DNS subdomain enumeration by scraping the largest number of disparate data sources, recursive brute forcing, crawling of web archives, permuting and altering names, reverse DNS sweeping and other techniques. https://github.com/caffix/amass

8.3 justniffer: Justniffer is a network protocol analyzer that captures network traffic and produces logs in a customized way, can emulate Apache web server log files, track response times and extract all "intercepted" files from the HTTP traffic. http://justniffer.sourceforge.net/

8.4 httpry: httpry is a specialized packet sniffer designed for displaying and logging HTTP traffic. http://dumpsterventures.com/jason/httpry/

8.5 ntopng: Ntopng is a network traffic probe that shows the network usage, similar to what the popular top Unix command does. http://www.ntop.org/products/traffic-analysis/ntop/

8.6 Snort: Snort is a free and open source network intrusion prevention system (NIPS) and network intrusion detection system (NIDS)created by Martin Roesch in 1998. Snort is now developed by Sourcefire, of which Roesch is the founder and CTO. In 2009, Snort entered InfoWorld's Open Source Hall of Fame as one of the "greatest [pieces of] open source software of all time". https://www.snort.org/

8.7 Bro: Bro is a powerful network analysis framework that is much different from the typical IDS you may know. https://www.bro.org/

8.8 Suricata: Suricata is a high performance Network IDS, IPS and Network Security Monitoring engine. Open Source and owned by a community run non-profit foundation, the Open Information Security Foundation (OISF). Suricata is developed by the OISF and its supporting vendors. http://suricata-ids.org/


### 9. Scanning Host:

9.1 scapy: Scapy: the python-based interactive packet manipulation program & library. https://github.com/secdev/scapy

9.2 Pompem: Pompem is an open source tool, which is designed to automate the search for exploits in major databases. Developed in Python, has a system of advanced search, thus facilitating the work of pentesters and ethical hackers. In its current version, performs searches in databases: Exploit-db. https://github.com/rfunix/Pompem



## Specific Security in OPNFV

1. Tools: OpenSCAP (https://github.com/OpenSCAP/openscap)

 	Scanning of NFVs nodes to insure they are hardened and free of known CVEs. 
  
2. Security standards met: DISA STIG and FedRamp
  
  
  
##  Specific Security in Container K8

1. Anchore: Free image scanning service with a commercial offering similar to Docker Cloud. https://anchore.io/

2. Alpine CVE Check: Specialized CVE scanner. https://github.com/tomwillfixit/alpine-cvecheck

3. Banyan Collector: A framework to peek inside containers Framework for peering inside docker images. Useful for rolling your own image scanning system. https://github.com/banyanops/collector

4. CoreOS Clair:  Utility from CoreOS for automated vulnerability analysis for containers. https://coreos.com/blog/vulnerability-analysis-for-containers.html

5. Clair: The Container Image Security Analyzer (by Joey Schorr & Quentin Machu) - Presentation about the Clair platform. https://www.youtube.com/watch?v=Kri67PtPv6s

6. OpenSCAP Container Compliance: Utility for aiding in compliance checks against a container. https://github.com/OpenSCAP/container-compliance

7. Actuary: Automated security profiling for Docker image. https://github.com/diogomonica/actuary

8. drydock: Inspired by docker-bench-security with the ability to apply custom security profiles. https://github.com/zuBux/drydock

9. Docker bench security: One of the first security linting utility for Docker. https://github.com/diogomonica/docker-bench-security


## Specific Security in Openstack-Ocata

1. AIDE: The Advanced Intrusion Detection Environment, developed as a free replacement for Tripwire as a data integrity tool. http://aide.sourceforge.net/

2. Denyhosts: Thwart SSH dictionary based attacks and brute force attacks.http://denyhosts.sourceforge.net/

3. Fail2Ban:  Scans log files and takes action on IPs that show malicious behavior. http://www.fail2ban.org/wiki/index.php/Main_Page

4. nprobe:  NetFlow analysis/audit toolkit.

5. ntopng: High-Speed Web-based Traffic Analysis and Flow Collection.http://www.ntop.org/products/nprobe/

6. OpenVAS: Open-source vulnerability scanner and manager. http://www.openvas.org/

7. Ossec: Host-based Intrusion Detection System that performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response. http://www.ossec.net/

8. Samhain: Host-based intrusion detection system, with file integrity checking, log file monitoring/analysis, rootkit detection, port monitoring, detection of rogue SUID execs and hidden processes. http://la-samhna.de/samhain/

9. Tripwire: Data integrity tool, useful for monitoring and altering on specific file changes. http://sourceforge.net/projects/tripwire/

10. Yasat: Scan configuration files, kernel parameters and shows the best practices for each cases. http://yasat.sourceforge.net/


## Specific Security in OWAP

A set of policy standards for software test 

## Specific Security in VNF

1. reverse engineering tools

2. debugging tools

3. symboic execution tools

4. fuzzing tools

5. policy checking tools



