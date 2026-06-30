#--------file handling
#1.file handling in python means reading from and writing to files/folder stord on #disk using python.
#2your python code can open a file,oull any data out of it,put data into it and also closes it properly.


#---------what is file
#files are store a data ansd information on the specific parts of device

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
with open ("demo.txt","r") as f:
    r=f.read()
    print(r)
