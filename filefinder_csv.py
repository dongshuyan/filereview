import os	   
import sys 
import platform
from pypinyin import pinyin, lazy_pinyin

def systemopen(dst):
	if(platform.system()=='Windows'):
		os.system('explorer '+dst)
	elif(platform.system()=='Linux'):
		os.system('nautilus '+dst)
	elif(platform.system()=='Darwin'):
		os.system('open '+dst)
	else :
		print("Can't read system!!")

def systemsym():
	if(platform.system()=='Windows'):
		return '\\'
	elif(platform.system()=='Linux'):
		return '/'
	elif(platform.system()=='Darwin'):
		return '/'
	else :
		return '/'

def showfile(pathset,fileset,filepath):

	for path in pathset:
		if os.path.isdir(path):
			if path[-1]!=systemsym():
				path=path+systemsym()
			for child in os.listdir(path):
				child=child.strip()
				if child[0]!='.':
					strstr=child+','+'=HYPERLINK("'+path+child+'")'
					fileset.add(strstr)

	filelist=list(fileset)
	filelist.sort(key=lambda char: lazy_pinyin(char)[0][0])
	f=open(filepath,'w')
	for child in filelist:
		f.write(child.encode('GBK','ignore').decode('GBK')+"\n")
		

#path = sys.argv[1]
#生成的csv路径
filepath="D:\\script\\动漫.csv"
#含有相同类型的文件夹集合
pathset=["H:\\视频\\动漫\\","I:\\视频\\动漫\\","K:\\视频\\动漫\\","L:\\视频\\动漫\\","M:\\视频\\动漫\\"]
fileset=set()
showfile(pathset,fileset,filepath)