# make a docker file with specific file requirements

# ******************** TEXTFILE ********************
# OS: Ubuntu
# OS_VERSION:18.02
# PYTHON:3.7
# numpy:1.21
# pandas:0.20.3
# tensorflow:1.13.1

# ******************** TEXTFILE ********************
# FROM ubuntu:18.02
# RUN apt-get install python3.7

# RUN python -m pip install numpy=1.21
# RUN python -m pip install pandas=0.20.3
# RUN python -m pip install tensorflow=1.31.1

# Run echo "Compilation Successful"


# **********************************************************************************

import sys
import os

a = sys.version.split(' ')[0]
print(a)

if (a == '3.7.0'):
    print("YES")
else:
    print("NO")
