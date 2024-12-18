from io import StringIO
from ppci.api import ir_to_object, get_arch,objcopy, link
import io
from ppci.api import cc
files=input("give me a .c file? ")
f1=open(files,"r")
codes=f1.read()
f1.close()
try:
    source_file = io.StringIO(codes)
    obj = cc(source_file, 'x86_64')
    obj=link([obj])
except Exception as e:
    print(e)
    print ("error:")
     
else:
    # Salve o objeto
    f1=open(files+".o","wb")
    f1.write(obj.sections[1].data)
    f1.close()