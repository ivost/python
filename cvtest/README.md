'''

brew tap homebrew/science

[Resolving macOS, OpenCV, and Homebrew install errors - PyImageSearch](http://www.pyimagesearch.com/2017/05/15/resolving-macos-opencv-homebrew-install-errors/)

brew install opencv3 --with-contrib --with-python3 —without-python


echo 'export PATH="/usr/local/opt/opencv3/bin:$PATH"' >> ~/.bash_profile

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/opencv3/lib
    CPPFLAGS: -I/usr/local/opt/opencv3/include
For pkg-config to find this software you may need to set:
    PKG_CONFIG_PATH: /usr/local/opt/opencv3/lib/pkgconfig

==> Summary
🍺  /usr/local/Cellar/opencv3/3.2.0_1: 498 files, 63MB, built in 5 minutes 35 seconds
~$ echo 'export PATH="/usr/local/opt/opencv3/bin:$PATH"' >> ~/.bash_profile


#####
python3 --version
Python 3.6.2

~$ which python3
/usr/local/bin/python3

ll /usr/local/bin/python3
lrwxr-xr-x  1 ivo  admin    35B Aug 10 07:55 /usr/local/bin/python3 -> ../Cellar/python3/3.6.2/bin/python3

ls /usr/local/opt/opencv3/lib/python3.6/site-packages/
cv2.cpython-36m-darwin.so

#####
#####   HOW TO FIX opencv site packages problems
#####

import site; site.getsitepackages()

['/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages', '/Library/Python/3.6/site-packages']

echo "/usr/local/lib/python2.7/site-packages/" > /opt/python2.7.2/lib/python2.7/site-packages/usrlocal.pth

ls /Library/Python/3.6/site-packages/*.pth

ll /usr/local/bin/python3
lrwxr-xr-x  1 ivo  admin    35B Aug 10 07:55 /usr/local/bin/python3 -> ../Cellar/python3/3.6.2/bin/python3

sudo mkdir -p /Library/Python/3.6/site-packages

echo "/usr/local/opt/opencv3/lib/python3.6/site-packages/" >  usrlocal.pth
sudo cp usrlocal.pth  /Library/Python/3.6/site-packages



'''
