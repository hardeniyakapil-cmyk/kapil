#--------file handling
#1.file handling in python means reading from and writing to files/folder stord on #disk using python.
#2your python code can open a fil,out any data out of it,put data into it and also closes it properly.


#---------what is file
#files are store a data and information on the specific parts of device

#types of file path
#1. absolute path: the complete path from the root of the filesystem.
#2.relative path :tha path relative to where your current folder(current working dir)


# file made
#1. a: append ,a+append and read 
#2. w: write , w+:write and read
#3. r: read , r+ : read and write 
#4. x:strictly create file


#python file handling methods.
#1.open(file_name<mode): opens file
#2.close():close file 
#3.flush():memory cleanup


#4.read():file read
#5.readlines(): file read line by line
#6.write():writes data in file only take string
#write data in file of any data types.

#8.tail():cursor move
#9.seek():specific position set of cursor


#1. create a file in strict mode
#try:
#file =open("strict.txt","x")
#print("file created...")
#except exception as e:
 #   print("error:file nahi ban skti pehle se hai...")

#file =open("write.txt","w")
#file.write("this is python file handling....")
#file.flush()
#file.close()
#print("file created....")

#context manager
#with open ("manager."txt","w+") as file:
 #    file.write("this is completely python file handling....")
  #   file.seek(0)
   #  r=file.read(4)
    # print("file created and written.....")
     #print(f"file content:{r}")
#with open ("demo.txt","r") as f:
 #   r=f.read()
  #  print(r)
#emp_list=["aman","shivam","shubham","anshu","kamal"]
#emp name individual file create txt type.
#for i in emp_list:
 #   with open(i+"txt","w") as file:
  #      print("file created")

#import os
#with open("kapil+.txt","w") as file:
 #   file.write
 #  print("file created")


#open a file
#file=open("example.txt","w+")
#print("file created...")

#file=open("example.txt","w")
#print("file created...")

#file=open("example.txt","r+")
# file.write()
#content=file.read()
#print(content)
#file.close()


#file=open("example2.txt","w+") #write a file
#file.write("namaste kapil you are so hot")
#file.close()

#file=open("example2.txt","r") #write a file
#file.readline("yooo dawg python class is best")
#file.close()

#file=open("example2.txt","r") #reads entire data
#print(file.readlines())
#file.close()
#print("program started")
#file=open("example2.txt","r") #reads only one line
#print(file.readline())
#file.close()