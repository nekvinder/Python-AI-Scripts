import profiles,os,shutil
profiles.clean()
if os.path.exists(profiles.currdir+'dataset'):
    shutil.rmtree(profiles.currdir+'dataset')   
if os.path.exists(profiles.currdir+'trainer'):
    shutil.rmtree(profiles.currdir+'trainer')   
if os.path.exists(profiles.currdir+'__pycache__'):
    shutil.rmtree(profiles.currdir+'__pycache__')   