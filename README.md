# mkwebfile
Small command line tool for creating web link files (internet shortcuts)

## Requirements

Requires Python 2.7 or newer. Tested on Linux, Windows 7 and Mac OS X 10.5. 

## Usage

Run it from the command line or terminal:

`mkwebfile.py <URL> <Title>`

Where `URL` is the web link and `Title` is the file name. For the `Title`, do not use characters that are not supported by your file system, for example :, \, /, etc.

###Example: 

`mkwebfile.py https://github.com/pixeldyne/ "Pixeldyne on GitHub"`

This creates two files in current folder: Pixeldyne on GitHub.url (for Windows) and Pixeldyne on GitHub.webloc (for macOS). The script creates both files regardless of the OS you are running. Options will be added in a future version, along with support for other operating systems and browsers.

You may need to run it with the python interpreter. For example, on Windows you would run:

C:\Python27\python.exe mkwebfile.py https://github.com/pixeldyne/ "Pixeldyne on GitHub"

On Windows, you can run `where python.exe` to determine the location of the Python interpreter.

## Rationale

I wrote this tool to save URL shortcuts to archived web pages, the shortcut files accompany my collection of retro games and programs. I wrote it in Python because it appears to be the most widely supported script interpreter (language that doesn't require compilation). The script will be improved over time and tested on other platforms such as DOS, Amiga, etc. 
