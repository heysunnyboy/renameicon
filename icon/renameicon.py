#encoding:utf-8  
import os  
import sys  
import os.path  

def mv_3x_file():
        dir = cur_file_dir()
        files = os.listdir(dir)
        for name in files:
            nameArr=name.split(".")
            if nameArr[1] == 'png':
                os.rename(os.path.join(dir,name),os.path.join(dir,nameArr[0]+"@3x.png"))
                print name
        	#os.rename(name, nameArr[1])  

def mv_file():
        dir = cur_file_dir()
        files = os.listdir(dir)
        for name in files:
            nameArr=name.split(".")
            if nameArr[1] == 'png':
                os.rename(os.path.join(dir,name),os.path.join(dir,nameArr[0]+"@2x.png"))
                print name


def cur_file_dir():
     #获取脚本路径
        path = sys.path[0]
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)


if __name__=="__main__":
	   mv_file()
