#!/opt/qumulo/toolchain/bin/python

import os
import requests
import sys

url = requests.utils.unquote(sys.argv[1])
offset = url.find('com') + 4
gravypath = os.path.join('/mnt/gravytrain', url[offset:])
isspath = os.path.join('/mnt/iss', url[offset:])
if os.path.exists(gravypath):
    print(gravypath)
elif os.path.exists(isspath):
    print(isspath)
