'''
This python script open some apps on start.
The apps are defined in the list 'apps_to_open'.

METHODS OF LOADING

PLIST
1. Create a plist file similar to example_plist in the folder apps_on_startup.
2. Add the plist file to the list of plist files in ~/Library/LaunchAgents
3. launchctl load /path/to/plist/file

SHELL SCRIPT
1. Create a shell script in the folder apps_on_startup.
2. Example 
`#!/bin/bash
python3 /absolute/path/to/pyfile`
3. add the .sh file to "System Preference -> Users and Groups -> Login items", the .sh script will call the python file.
'''

import os


apps_to_open = ['Microsoft\ Edge', 'Visual\ Studio\ Code', 'iTerm']


def open_apps():
    for app in apps_to_open:
        print('Opening app: ' + app)
        maximise_app(app)
        os.system(f'open -a{ app }')
# maximise window on start
def maximise_app(app):
    os.system(
        f'osascript -e "tell application {app} activate tell application \"System Events\" keystroke \"f\" using control down, command down"')


if __name__ == '__main__':
    open_apps()
