"""
.. moduleauthor:: Florin Oncica 

.. versionadded:: 0.9

Created on Nov 12, 2016

This is a small script for creating .rst files for each class in a BiBler module.
"""

#!/usr/bin/python

import sys

file_name  = sys.argv[3]
module_name = sys.argv[2]
package_name = sys.argv[1]

file = open(file_name, 'r')

for line in file:
    if line[0:5] == 'class':
        idx_param = line.find('(')
        idx_s = line.find(':')
        if idx_param != -1:
            class_name = line[6:idx_param]
            class_file = class_name + '.rst'
        else:
            class_name = line[6:idx_s]
            class_file = class_name + '.rst'
            
        print(class_file)
        
        with open(class_file, 'w') as nf:
            nf.write("\n")
            nf.write("Class {}\n".format(class_name))
            sep = '='*(len(class_name) + 6)
            nf.write("{}\n".format(sep))
            autoclass = package_name + '.' + module_name + '.' + class_name
            nf.write(".. autoclass:: {}\n".format(autoclass))
            nf.write("   :members:\n")
            nf.write("   :undoc-members:\n")
            nf.write("   :private-members:\n")
            nf.write("   :show-inheritance:\n")
            nf.write("   :special-members: __init__\n")        
    
file.close()
    