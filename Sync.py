import filecmp
import shutil
import sys
import time
import datetime
import os
if __name__ == "__main__":
    try:
    	#saving the arguments and making sure we have enough of them
        sourcePath = sys.argv[1]
        replicaPath = sys.argv[2]
        interval=int(sys.argv[3])#interval is in seconds
        logPath =sys.argv[4]
    except:
        print("Please give 4 arguments: <source_path>, <replica_path>, sync_interval, <log_path>")
        exit()
    while True:#needs to work for an unspecified amount of time
        try:
            result=filecmp.dircmp(sourcePath,replicaPath) #dircmp compares all the files, directories and subdirectories of the 2 given paths 
            if result.diff_files or result.left_only or result.right_only: #lists of files that are different or only exist in one directory
            	now=datetime.datetime.now()#logging start
            	print(now)
            	print(f"Copied: {result.diff_files}")
            	print(f"Created: {result.left_only}")
            	print(f"Deleted: {result.right_only}")
            	print("----------------------------------")
            	f = open(logPath, "a")#logPath must include the filename of the log file
            	f.write(f"{now}\n")
            	f.write(f"Copied: {result.diff_files}\n")
            	f.write(f"Created: {result.left_only}\n")
            	f.write(f"Deleted: {result.right_only}\n")
            	f.write("----------------------------------\n")
            	f.close()#logging finish
            	for file in result.diff_files:#copying the different files
            		shutil.copy(sourcePath+file,replicaPath)
            	for file in result.left_only:#copying the files that only exist on source
            		shutil.copy(sourcePath+file,replicaPath)
            	for file in result.right_only:#deleting the files left on replica that are no longer in source
            		os.remove(replicaPath+file)
            time.sleep(interval)#interval in seconds
        except:
            print("Error! Make sure paths are correct!")
            exit()
    
