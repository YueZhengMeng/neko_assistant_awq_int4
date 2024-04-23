import os
os.system(f'apt-get update')
os.system(f'apt-get install git')
os.system(f'apt-get install git-lfs')
os.system(f'python download.py')
os.system(f'python app.py')
