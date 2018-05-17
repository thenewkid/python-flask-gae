import os
from subprocess import call

def install_python_requirements():
    try:
        call(["pip", "install", "-t", "lib", "-r", "requirements.txt"])
    except Exception as e:
        print "[+] Encountered exception while issuing command pip install -t lib -r requirements.txt"
        print str(e)

install_python_requirements()
