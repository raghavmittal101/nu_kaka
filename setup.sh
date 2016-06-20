#to install this repo run this file

sudo apt-get install python-virtualenv
cd
git clone https://github.com/raghavmittal101/nu_kaka.git
cd nu_kaka
virtualenv venv
source venv/bin/activate
pip install selenium
pip install python-tk

# to run kaka.py type < python kaka.py >
# CHANGE sample_conf.py to conf.py
# add location to chromedriver
