
# Add Disk


1. delete the old partitions that remain on the disk;

2. create the new partition.


## 1. Check Status 
```
# df -h
# fdisk -l
# partprobe
```

## 2. Usage of Fdisk
```
Usage:
 fdisk [options] <disk>      change partition table
 fdisk [options] -l [<disk>] list partition table(s)

Display or manipulate a disk partition table.

Options:
 -b, --sector-size <size>      physical and logical sector size
 -B, --protect-boot            don't erase bootbits when create a new label
 -c, --compatibility[=<mode>]  mode is 'dos' or 'nondos' (default)
 -L, --color[=<when>]          colorize output (auto, always or never)
                                 colors are enabled by default
 -l, --list                    display partitions end exit
 -o, --output <list>           output columns
 -t, --type <type>             recognize specified partition table type only
 -u, --units[=<unit>]          display units: 'cylinders' or 'sectors' (default)
 -s, --getsz                   display device size in 512-byte sectors [DEPRECATED]
     --bytes                   print SIZE in bytes rather than in human readable format

 -C, --cylinders <number>      specify the number of cylinders
 -H, --heads <number>          specify the number of heads
 -S, --sectors <number>        specify the number of sectors per track

 -h, --help     display this help and exit
 -V, --version  output version information and exit

Available columns (for -o):
 gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
 dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S Start-C/H/S
 bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
 sgi: Device Start End Sectors Cylinders Size Type Id Attrs
 sun: Device Start End Sectors Cylinders Size Type Id Flags

For more details see fdisk(8).
```


## 3. Partition 

```
# fdisk /dev/sdb

Command (m for help):n
Command action
　　   e    extended                 
　　   p    primary partition (1-4)      
p
Partion number(1-4)：1      
First cylinder (51-125, default 51):   //start of the partition, just enter
Using default value 51
Last cylinder or +size or +sizeM or +sizeK (51-125, default 125): +200M //size of the partition

Command (m for help): w                     //write and save, enter

```

The check with `fdisk -l`.
If does not work, use `partprobe`.


## 4. Format the Partition

```
# umount -l /dev/sdb1
# mkfs.ext4 /dev/sdb1
```

## 5. Mount and Check
```
# mkdir /data1
# mount /dev/sdb1 /data1
# df -h
```

## 6. Config 
```
vim /etc/fstab
```

Add one line, then save and reboot:

```
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sdc1 during installation
UUID=9b773963-0285-4d33-8d10-0ac76ed63156 /               ext4    errors=remount-ro 0       1
hugetlbfs /hugepages hugetlbfs rw,relatime,pagesize=1G 0 0

/dev/sdb1 /home/wenhui ext4 defaults 0 0
```
