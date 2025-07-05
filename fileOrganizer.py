import os
from pathlib import Path

class File:
    def __init__(self, fname, ftype, src_path):
        self.fname = fname
        self.ftype = ftype
        self.src_path = src_path
    
    def fmove(self, des_path):
        src_path = Path(self.src_path)
        dst_path = Path(des_path)
        src_path.rename(dst_path)

cwd = os.getcwd()
print(cwd)
dir_list = os.listdir(cwd) 



for files in dir_list:
    
    src_path = os.path.join(cwd, files)
    
    dotIndex = files.find(".")

    if(dotIndex == -1):
        continue

    ftype = files[dotIndex + 1:]
    fname = files[:dotIndex]
    type_dir = os.path.join(cwd, ftype)
    Path(type_dir).mkdir(parents=True, exist_ok=True)


    des_path = os.path.join(type_dir, files)
    print(des_path)

    moveFile = File(fname, ftype, src_path)

    print(moveFile.fname)
    moveFile.fmove(des_path)




