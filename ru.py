#@title JUST UPLOAD:
TARGET_PATH = "" #@param {type:"string"}
LINK_DOWNLOAD = "" #@param {type:"string"}
 
import os
os.chdir(TARGET_PATH)
!wget -c {LINK_DOWNLOAD} --no-check-certificate
