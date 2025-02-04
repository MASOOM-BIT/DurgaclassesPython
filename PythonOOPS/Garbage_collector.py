'''
> in Old programming launguage it was programmer who was responsble for creating object and delting it
> But in Python it is GC : garbage Collecter responsible for destroy useless onjects
> If the objects does not have any reference variable then that object is eligible for gc

> In python based on requirement we can enable and disable GC in our program

>>> Grabage Collector module name is : gc
1> gc.isenabled() #true if GC is enable ,false if disabled
2> gc.disable() #disble GC
3> gc.enable #Enable GC
> By default , GC is enabled
'''

import gc
print(gc.isenabled())

gc.disable()
print(gc.isenabled())

gc.enable()
print(gc.isenabled())

#GC is kind