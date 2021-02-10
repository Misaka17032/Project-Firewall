import os
import operator
import beep
def get_filelist(dir, Filelist):
	newDir = dir
	if os.path.isfile(dir):
		Filelist.append(dir)
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			get_filelist(newDir, Filelist)
	return Filelist
path = input()
flist = get_filelist(path,[])
while True:
	flist_now = get_filelist(path,[])
	if operator.eq(flist,flist_now) != True:
		print("warning")
		beep.beep()
	flist = flist_now