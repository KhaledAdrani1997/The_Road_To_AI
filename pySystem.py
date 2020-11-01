import os
import json
from zipfile import ZipFile

my_token = {"username":"khaledadrani","key":"d107a1e80e2adb538ad9511678c62614"}
command = 'kaggle datasets download -d sudalairajkumar/novel-corona-virus-2019-dataset'
pathFrom='/content/datasets/ntnu-testimon/paysim1/paysim1.zip'



#my classic routine to setup a colab environment for downloading datasets from kaggle
def setup_for_kaggle(my_token):
    os.system('pip install kaggle')
    os.system('mkdir .kaggle')
    with open('/content/.kaggle/kaggle.json', 'w') as file:
        json.dump(my_token, file)
    os.system('chmod 600 /content/.kaggle/kaggle.json')
    os.system('mkdir ~/.kaggle')
    os.system('cp /content/.kaggle/kaggle.json ~/.kaggle/kaggle.json')
    os.system('kaggle config set -n path -v /content')


def download_from_kaggle(command): #need more work here
    os.system(command)

def extract_zip(pathFrom):# Extract all the contents of zip file in current directory
  cwd = os.getcwd()
  with ZipFile(pathFrom, 'r') as zipObj:
   zipObj.extractall(cwd+'/extracted_datasets/')

setup_for_kaggle(token)
download_from_kaggle(command)

def walk_into_folder(path_folder): #I guess it shows all files included within this path; you can then copy the file
    #from kaggle standared kernel
    import os
    for dirname, _, filenames in os.walk(path_folder):
        for filename in filenames:
            print(os.path.join(dirname, filename))

    print(os.listdir("../input")) #this too is helpful






