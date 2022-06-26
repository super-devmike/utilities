'''
This python script open some apps on start.
The apps are defined in the list 'apps_to_open'.
'''

import os


apps_to_open = ['Microsoft\ Edge', 'Visual\ Studio\ Code', 'iTerm']

# write script to open macos apps


def open_apps():
    for app in apps_to_open:
        print('Opening app: ' + app)
        maximise_app(app)
        os.system(f'open -a{ app }')


# maximise app window on start
def maximise_app(app):
    os.system(
        f'osascript -e "tell application {app} activate tell application \"System Events\" keystroke \"f\" using control down, command down"')


if __name__ == '__main__':
    open_apps()