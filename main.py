#!/usr/bin/env python
import os
import re
import sys

USAGE = '''
USAGE
==========================================

./py-generate-project YOUR_CONFIG_FILE
'''

#if not file specified
if len(sys.argv) < 2:
    print "ERROR file not found"
    print "You should specify a file"
    sys.exit(USAGE)

filename = sys.argv[1]
separator = os.path.sep
program_path = os.path.abspath(os.curdir)
config_file = file(filename)
lines = file.readlines(config_file)
structures = []

print "reading the file..."
for line in lines:
    folder_code = ('').join(re.compile('(\S)+?').findall(line))
    prefix_splitter = re.compile('(^\-+)').split(folder_code.strip())
    prefix = prefix_splitter[1]
    level = len(prefix)
    name_with_extension = prefix_splitter[2]
    extension_splitter = re.compile('(^\.+?|\.\w+$)').split(name_with_extension)
    extension_splitter = filter(lambda x: len(x) > 0, extension_splitter)
    have_extension = len(extension_splitter) > 1
    parent_candidate = None
    parent = None
    if len(structures) > 0:
        parent_candidate = filter(
                lambda x: x["level"] == level -1 and not x["extension"], structures)
        if len(parent_candidate) > 0:
            parent = parent_candidate[-1]["name"]
    level_info = {
        "level": level,
        "have_extension": have_extension,
        "name": filter(lambda x: x[0] != '.', extension_splitter)[0],
        "extension": filter(lambda x: x[0] == '.', extension_splitter) or None,
        "parent": parent
    }
    structures.append(level_info)


print "building project structure..."
for structure in structures:
    current_path = os.path.abspath(os.curdir)
    current_folder_name = current_path.split("/")[-1]
    while current_folder_name != structure["parent"]:
        upper_folder_list = os.listdir(os.curdir)
        is_in_upper = filter(lambda x: x == structure["parent"], upper_folder_list)
        if structure["parent"] == None:
            os.chdir(program_path)
            break
        elif is_in_upper:
            os.chdir(is_in_upper[0])
        else:
            os.chdir('..')
        current_path = os.path.abspath(os.curdir)
        current_folder_name = current_path.split("/")[-1]
    if structure["have_extension"]:
        os.system('touch ' + structure["name"] + structure["extension"][0])
    elif not structure["have_extension"]:
        os.system('mkdir --parent '+ structure["name"])
    print "- " * int(structure["level"]) + structure["name"]

print "project generated !"
