#!/usr/bin/python3

import argparse
import os
import subprocess

def artifacts_path(version: str) -> str:
    path = f'/mnt/gravytrain/release/{version}'
    if not os.path.isdir(path):
        print(f'${path} is not a directory - do you need to mount gravytrain?')
        exit(-1)
    return path

def unzip_core(filename: str) -> str:
    if not os.path.isfile(filename):
        print(f'{filename} does not exist')
        exit(-1)

    if filename.endswith('.gz'): 
        decompressed = filename[:-3]
        if not os.path.isfile(decompressed):
            print(f'decompressing {filename}')
            subprocess.run(['gunzip', '-k', f'{filename}'])
        return decompressed
    return filename

def load_core(filename: str, path: str) -> None:
    cmd = ['gdb', f'{path}/src/build/release/qfsd/qfsd', f'{filename}', '-ex', '"set', 'solib-search-path', f'{path}/src/build/release/lib"']
    print(' '.join(cmd))
    subprocess.run(cmd)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Load a qfsd core in gdb using artifacts from gravytrain")
    parser.add_argument('filename', help='the qfsd core file')
    parser.add_argument('version', help='the qfsd version of the core, e.g. "7.0.0"')
    args = parser.parse_args()

    load_core(unzip_core(args.filename), artifacts_path(args.version))
