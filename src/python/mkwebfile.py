#!/usr/bin/python
# mkwebfile - creates web shortcut files for Windows and macOS
#
# Version: 0.1
# Usage: mkwebfile.py <URL> <Title>
# Note: appropriate extension will be added to the title and used as file name.
# Example: mkwebfile.py http://yahoo.com Yahoo

import sys
from string import Template

if len(sys.argv) < 3:
    print("Invalid arguments")
    print("Usage: mkwebfile.py <URL> <Title>")
    exit()

windowsLink = Template('[InternetShortcut]\nURL=$url')
macOsLink = Template('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>URL</key>\n\t<string>$url</string>\n</dict>\n</plist>')

f = open(sys.argv[2] + ".url","w+")
f.write(windowsLink.substitute(url = sys.argv[1]))
f.close()

f = open(sys.argv[2] + ".webloc","w+")
f.write(macOsLink.substitute(url = sys.argv[1]))
f.close()