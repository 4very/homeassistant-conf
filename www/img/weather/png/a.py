import os
import shutil

for name in os.listdir("."):
    if name[-3:] == '.py': continue
    check = name[:4] + ('0' if name[4] == '1' else '1') + name[5:]
    

    if not os.path.exists(check):
        shutil.copyfile(name,check)
        print(name, check)

    