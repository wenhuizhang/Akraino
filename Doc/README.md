# Readme

Back up the system before proceed.

```
$ rsync -aAXv --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} /* /path/to/backup/folder
```
