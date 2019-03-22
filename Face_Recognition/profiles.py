import json
import os
import enum
currdir = os.path.dirname(os.path.realpath(__file__)) + "\\"

filename = 'profiles.json'


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        print(path+' does not exists.....making one')
        os.makedirs(dir)


def writeDict(dict):
    with open(currdir+filename, 'w') as fp:
        json.dump(dict, fp, sort_keys=True, indent=4)


def readDict():
    with open(currdir+filename, 'r') as fp:
        return json.load(fp)


def addUser(uid, name):
    dct = {}
    dct = readDict()
    dct[str(uid)] = name
    writeDict(dct)


def getUser(uid):
    r = readDict()
    return r.get(str(uid))


def userExist(uid):
    dct = readDict()
    if(str(uid) not in dct.keys()):
        return False
    else:
        return True

class videoSource(enum.Enum):
    webcam = 1
    video = 2
    phonecam = 3

# uid_name={1:'Mehul',2:'Nimmi',3:'Sikhvinder'}
# writeDict(uid_name)
# addUser(4,'raj')
# addUser(4,'raj')
