import fileinput

def settings_rewriter(file_path_settings, app_name):

    # app_name added in INSTALLED_APPS
    for line in fileinput.FileInput(file_path_settings, inplace=1):
        if '"django.contrib.staticfiles",' in line or "'django.contrib.staticfiles'," in line:
            line = line.rstrip()
            line = line.replace(line,line + f'\n    "{app_name}",\n')
        print(line.rstrip()) # print will write the app_name one by one


def static_writer(file_path_settings):

    # import os - manual writer bot
    for line in fileinput.FileInput(file_path_settings, inplace=1):
        if 'from pathlib import Path' in line:
            line = line.rstrip()
            line = line.replace(line,line +'\nimport os'+'\n')
        print(line.rstrip())

    # custom "template" path added in DIRS
    for line in fileinput.FileInput(file_path_settings, inplace=1):
        if '"DIRS": [],' in line or "'DIRS': []," in line:
            line = line.rstrip()
            line = line.replace(line,'        "DIRS": [os.path.join(BASE_DIR,"templates")],'+'\n')
        print(line.rstrip())


    # static files setup - manual writer bot
    for line in fileinput.FileInput(file_path_settings, inplace=1):
        if 'STATIC_URL = "static/"' in line or "STATIC_URL = 'static/'" in line:
            line = line.rstrip()
            line = line.replace(line,line+'\nSTATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]\nSTATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")\n# media folder setup\nMEDIA_URL = "media/"\nMEDIA_ROOT = os.path.join(BASE_DIR, "media/")'+'\n')
        print(line.rstrip())
