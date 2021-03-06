# scheduleapi-server [![Build Status](https://travis-ci.org/phille97/scheduleapi-server.svg?branch=master)](https://travis-ci.org/phille97/scheduleapi-server)


*Someday there will be descriptive text here about this project.*
##### [API documentation](https://github.com/phille97/scheduleapi-server/blob/master/api_doc.md)
<hr>
## How to install and run the server
#### Install dependencies on Ubuntu
```bash
sudo apt-get update
sudo apt-get install git python python-setuptools nodejs npm
```

#### Install dependencies on Arch Linux
```bash
sudo pacman -Sy git python python-setuptools nodejs npm
```

#### Install dependencies on Mac 
1. [Install XCode](http://developer.apple.com/xcode/)
2. `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" `
3. Add homebrew to your PATH (eg. `export PATH=/usr/local/bin:/usr/local/sbin:$PATH`)
4. `brew install python node`

### How to install on Mac and Linux
Make sure you have Python, git, pip installed on you computer
```bash
# Clone the git repo
git clone https://github.com/phille97/scheduleapi.git
# Go into the project
cd scheduleapi
# Install & Setup virtualenv (Check: http://iamzed.com/2009/05/07/a-primer-on-virtualenv/)
sudo easy_install virtualenv
virtualenv venv
. venv/bin/activate 
# Install dependencies
python setup.py install
npm install
# Generate static files
grunt
```
Then you can run it by typing `python runserver.py`
### How to install on Windows
1. Turn off computer
2. Go outside
