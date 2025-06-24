import glob
from os.path import dirname, isfile

def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*.py") 

    all_modules = [
        (f.replace(work_dir + "/", "").replace(".py", ""))
        for f in mod_paths
        if isfile(f) and not f.endswith("__init__.py")
    ]

    return all_modules
