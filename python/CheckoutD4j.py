'''

Created on Dec. 15, 2017

@author Andrew Habib

'''

import os
import subprocess
import sys

def exec_cmd(cmd):
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def check_out_each_project(d4j_binary, dist, proj, ver, ver_type):
    print("Checkingout:", proj, ver, ver_type)
    ver = str(ver)
    proj_dist = dist + '/' + proj + '-' + ver
    
    cmd = [d4j_binary, 'checkout', '-p', proj, '-v', ver + ver_type, '-w', proj_dist]
    exec_cmd(cmd)
    
    print("Getting properties:", proj, ver, ver_type)
    os.chdir(proj_dist)
    
    cmd = [d4j_binary, 'export', '-p', 'classes.modified', '-o', 'prop-buggy-classes']
    exec_cmd(cmd)
 
    cmd = [d4j_binary, 'export', '-p', 'dir.src.classes', '-o', 'prop-source-dir']
    exec_cmd(cmd)
 
    cmd = [d4j_binary, 'export', '-p', 'cp.compile', '-o', 'prop-compile-path']
    exec_cmd(cmd)

    print("Compiling:", proj, ver, ver_type)
    cmd = [d4j_binary, 'compile']
    exec_cmd(cmd)

if __name__ == '__main__':
    
    path_d4j = sys.argv[1] if sys.argv[1].startswith("/") else os.path.join(os.getcwd(), sys.argv[1])
    ver_type = sys.argv[2]
    
    d4j_binary = os.path.join(path_d4j, 'framework/bin/defects4j')
    dist = os.path.join(path_d4j, 'projects', ver_type)
    
    print(dist)
    if not os.path.isdir(dist):
        os.makedirs(dist)
        
    projects = {
        'Chart': list(range(1, 27)),
        'Cli': list(range(1, 6)) + list(range(7, 41)),
        'Closure': list(range(1, 63)) + list(range(64, 93)) + list(range(94, 177)),
        'Codec': list(range(1, 19)),
        'Collections': list(range(25, 29)),
        'Compress': list(range(1, 48)),
        'Csv': list(range(1, 17)),
        'Gson': list(range(1, 19)),
        'JacksonCore': list(range(1, 27)),
        'JacksonDatabind': list(range(1, 113)),
        'JacksonXml': list(range(1, 7)),
        'Jsoup': list(range(1, 94)),
        'JxPath': list(range(1, 23)),
        'Lang': [1] + list(range(3, 66)),
        'Math': list(range(1, 107)),
        'Mockito': list(range(1, 39)),
        'Time': list(range(1, 21)) + list(range(22, 28))
    }

    for proj, list_ids in projects.items():
        for ver in list_ids:
            check_out_each_project(d4j_binary, dist, proj, ver, ver_type)