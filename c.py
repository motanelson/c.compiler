from io import StringIO
from ppci.api import ir_to_object, get_arch,objcopy, link
import io
from ppci.api import cc
from ppci.api import asm
source_files = io.StringIO("""
start:
db 0xb8 
db 0xff 
db 0x4c 
db 0xcd 
db 0x21
db 0x90
db 0x90	
db 0x90	
db 0x90	
db 0x90	
db 0x90	
""")
obj2 = asm(source_files, 'x86_64')
files=input("give me a .c file? ")
print(files)
f1=open(files,"r")
codes=f1.read()
f1.close()
try:
    source_file = io.StringIO(codes)
    obj = cc(source_file, 'x86_64')
    obj=link([obj2,obj])
except Exception as e:
    print(e)
    print ("error:")
     
else:
    
    f1=open(files+".bin","wb")
    f1.write(obj.sections[0].data)
    
    f1.close()