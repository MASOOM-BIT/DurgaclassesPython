"""Module Reloading : How to reload a module in Python?
if any module let say modified after N SPECIFIC TIME then we can 
reload it using reload() function.
IMP : reload() function is not available in Python 3.4 or later.
import imp to use reload() function.
"""

try:
    from imp import reload
    import time
    import module_reloading2
    time.sleep(20)
    reload(module_reloading2)
    import module_reloading2
    print("END")
except ModuleNotFoundError as e:
    print(e)
    print("reload() function is not available in Python 3.4 or later.")