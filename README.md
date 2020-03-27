# mkwebfile
Small command line tool for creating web link files (internet shortcuts) for Windows and macOS.

## Synopsis

`mkwebfile.py URL TITLE`

Where `URL` is the web link and `TITLE` is the file name. For the `TITLE`, do not use characters that are not supported by your file system, for example :, \, /, etc. Existing files are overwritten.

### Examples

`mkwebfile.py https://github.com/pixeldyne/ "Pixeldyne on GitHub"`

This creates two files in current folder: `Pixeldyne on GitHub.url` (for Windows) and `Pixeldyne on GitHub.webloc` (for macOS). The script creates both files regardless of the OS you are running. Options will be added in a future version, along with support for other operating systems and browsers.

You may need to run it with the python interpreter. For example, on Windows you would run:

`C:\Python27\python.exe mkwebfile.py https://github.com/pixeldyne/ "Pixeldyne on GitHub"`

On Windows, you can run `where python.exe` to determine the location of the Python interpreter.

## Requirements

Requires Python 2.7 or newer. Tested on Linux, Windows 7 and Mac OS X 10.5. 

## Rationale

I wrote this tool to save URL shortcuts to archived web pages, the shortcut files accompany my collection of retro games and programs. I wrote it in Python because it appears to be the most widely supported script interpreter (language that doesn't require compilation). The script will be improved over time and tested on other platforms such as DOS, Amiga, etc. 

## Author

Written by Mac Plewa.

## Copyright

Copyright (c) 2020 Mac Plewa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
