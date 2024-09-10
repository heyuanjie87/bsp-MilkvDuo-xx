import os
import sys
import lzma
import string

def filecombine(mbr, boot, out):
    list = []

    list += [mbr]
    list += [boot]

    fname = open(out, "wb")
    for i in list:
        x = open(i, "rb")
        fname.write(x.read())
        x.close()

    fname.close()


def main():
    prjpath = sys.argv[1]
    file = sys.argv[2]
    board = sys.argv[3]

    STORAGE_TYPE = 'emmc'
    if "sd" in board:
        STORAGE_TYPE = "sd"

    dtbpath = fr'{prjpath}/resource/dtb/{board}'

    print("start compress kernel...")
    cmd = fr'lzma -c -9 -f -k {prjpath}/{file} > {dtbpath}/Image.lzma'  
    os.system(cmd)

    installdir = 'install/' + board
    os.makedirs(installdir, exist_ok=True)
    
    if STORAGE_TYPE == "emmc":
        cmd = fr'image_tool/mkimage -f {dtbpath}/multi.its -r {dtbpath}/rtthread.dtb'
        os.system(cmd)

        tmpbootfile=fr"{prjpath}/boot.emmc"
        filecombine("mbr.img", fr"{dtbpath}/rtthread.dtb", tmpbootfile)

        cmd = fr'python3 image_tool/raw2cimg.py tmpbootfile {installdir} partition_emmc.xml'
        os.system(cmd)
        os.remove(tmpbootfile)
    else:
        cmd = fr'image_tool/mkimage -f {dtbpath}/multi.its -r {installdir}/boot.{STORAGE_TYPE}'
        os.system(cmd)

if __name__ == "__main__":
    main()
