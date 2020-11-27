import os
#build
os.system('cmd /c "sdasz80.exe -l -o -s -p main.o main.asm"')
#link
os.system('cmd /c "sdldz80.exe -n -- -i main.ihx main.o"')
#make binary
os.system('cmd /c "makebin.exe -p < main.ihx > main.z80"')
#remove first 256 bytes
ifile = open("main.z80", "rb")
ofile = open("card.z80", "wb")
ifile.seek(256)
data = ifile.read()
ofile.write(data)
ifile.close()
ofile.close()
os.remove("main.z80")
os.rename(r'card.z80',r'main.z80')
#generate raw and bmp
os.system('cmd /c "nedcmake.exe -i main.z80 -o us -type 1 -region 1 -raw -bmp')
