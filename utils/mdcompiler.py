'''
Markdown -> HTML Compiler
'''

import argparse
import os
import pathlib
import shutil
import sys

import markdown

exclude_dirs = {'_build'}
exclude_files = {'README.md'}

def compile(args):
    source_dir = args.source
    if os.path.exists(source_dir) and os.path.isdir(source_dir):
        build_dir = os.path.join(source_dir, '_build')
        shutil.rmtree(build_dir)
        pathlib.Path(build_dir).mkdir(parents=True, exist_ok=True)
        for root, subdirs, files in os.walk(source_dir, topdown=True):
            subdirs[:] = [subdir for subdir in subdirs if subdir not in exclude_dirs]
            for file in files:
                filename, extension = os.path.splitext(file)
                if extension.lower() in ('.md', '.markdown'):
                    abs_source_file_path = os.path.join(root, file)
                    with open(abs_source_file_path, 'r') as source_file:
                        source_markdown = source_file.read()
                    output_html = markdown.markdown(source_markdown, extensions=[
                        'markdown.extensions.codehilite'
                    ])
                    rel_output_dir_path = os.path.relpath(root, source_dir)
                    abs_output_dir_path = os.path.join(build_dir, rel_output_dir_path)
                    pathlib.Path(abs_output_dir_path).mkdir(parents=True, exist_ok=True)
                    output_filename = '.'.join([filename, 'html'])
                    abs_output_file_path = os.path.join(abs_output_dir_path, output_filename)
                    with open(abs_output_file_path, 'w') as output_file:
                        output_file.write(output_html)
    else:
        sys.stdout.write('Invalid source path.\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='Source directory')
    args = parser.parse_args()
    compile(args)


if __name__ == '__main__':
    main()