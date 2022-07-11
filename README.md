# folder-sync
Python program that syncs 2 folders


Tested on linux.

Program needs 4 arguments: <source_path>, <replica_path>, sync_interval(number), <log_path>

Interval is in seconds.

Paths to folders must end with / and log path argument must contain the log filename aswell, example: python3 Sync.py /home/usr/example/source/ /home/usr/example/replica/ 5 /home/usr/example/logfile.txt
