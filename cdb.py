#cdb kate.exe output0\crashes\id_000000_00_EXCEPTION_ACCESS_VIOLATIO
import os
import sys, subprocess, struct



def windbg(file):
    #cdb -g kate.exe file
    subprocess.call(['cdb.exe','-g','kate.exe', file])
    
    #.cls
    #copy the output
    #g
    #k
    #q
    #exe command inside an



def get_files(path):
  for root, subdirs, files in os.walk(path):
    for file in os.listdir(root):
        filePath = os.path.join(root, file)
        if os.path.isdir(filePath):
            pass
        else:
            if len(filePath) > 3:
                print(filePath)
                windbg(filePath)
                
if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_files(sys.argv[1])
        print("Done !")
    else:
        print("program [folder]")