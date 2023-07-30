
import os

def inputCMD(cmd):

    cmd1 = " ".join(os.popen(cmd))
    myfile = "C:/Users/59754/OneDrive/desktop/CMDtest.txt"

    with open(myfile, 'a') as f:
        f.write(cmd1)


inputCMD("disk part")
inputCMD("list disk")
inputCMD("detail disk")