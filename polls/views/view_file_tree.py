import os
import pathlib

from django.conf import settings
from django.shortcuts import render

# start point
startpath = '.'

folders = []    # folder store
tuples = []     # folders, subdirs, files


def folder_tree(line, dir):
    one = '|-> V '
    padding = '|   '

    if line == dir:
        # print('V '+line)
        return ('V '+line)

    if line.count(os.sep) == 1:
        line = line.split(os.sep)
        line[0] = one
        # print(''.join(line))
        return (''.join(line))

    if line.count(os.sep) >= 2:
        line = line.split(os.sep)
        line[-2] = one
        for i in range(len(line[:-2])):
            line[i] = padding
        # print(''.join(line))
        return (''.join(line))


def files_tree(dir, *args):
    """

    :param dir: startpath
    :param args: args[0] > tuples, args[1] > folders
    :return: None
    """
    file = '|-> '
    padding = '|   '
    last_file = ''
    tuples = args[0]
    folders_list = args[1]
    for root, subs, files in tuples:
        # no files no worries, skip
        if not files:
            continue

        # will use for padding: padding * sep
        sep = root.count(os.sep)

        # only if root has some files
        if root == dir:
            last_file = [file+str(x) for x in files]
            continue

        if subs:
            # take last elem in subs,
            # use it as value to find the same in folders_list
            # get index + 1 to insert right after
            index = folders_list.index([x for x in folders_list if x.endswith(subs[-1])][0]) + 1

        else:
            # we need name the last of folder in the root
            # to use it to find index
            folder_name = root.split(os.sep)[-1]
            index = folders_list.index([x for x in folders_list if x.endswith(folder_name)][0]) + 1

        # prepare files
        files = [sep * padding + file + x for x in files]

        # now insert files to list
        for i, a in enumerate(range(index, index+len(files))):
            folders_list.insert(a, files[i])

    if last_file:
        # merge files in root dir
        folders_list = folders_list + last_file

    # final print tree
    for elm in folders_list:
        print(elm)


def tree_walk(dir):
    for folder, subs, files in os.walk(dir):
        tuples.append((folder, subs, files))
        folders.append(folder_tree(folder, dir))


def print_dir_tree(path):
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)

###
# https://stackoverflow.com/questions/6297068/whats-the-django-way-to-render-a-tree-of-folders-and-files
#
def view_file_tree(request):

    # List files in "generated_codes"
    f_path = os.path.join(settings.BASE_DIR, 'generated_codes')
    f_list = [p for p in pathlib.Path(f_path).iterdir() if p.is_file()]

    # list the files in the FILE_UPLOAD_DIR
    f_uploaded_list = []
    f_uploaded_path = settings.FILE_UPLOAD_DIR
    # for root, d_names, f_names in os.walk(f_path):
    #     print(root, d_names, f_names)
    for (_, _, filenames) in os.walk(f_uploaded_path):
        f_uploaded_list.extend(filenames)
        break

    context = {
        'f_path': f_path,
        'f_list': f_list,
        'f_uploaded_path': f_uploaded_path,
        'f_uploaded_list': f_uploaded_list,
        'domain': settings.DOMAIN,
    }

    return render(request, 'polls/view_file_tree.html', context)



if __name__ == "__main__":
    # tree_walk(startpath)
    # folder_tree(tuples, startpath)
    # files_tree(startpath, tuples, folders)

    # print_dir_tree('D:\dev\py_django\py_django_pg_heroku')
    print_dir_tree('d:/pics')
