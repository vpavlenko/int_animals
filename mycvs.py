import os
import sys

command = sys.argv[1]

if command == 'init':
    os.mkdir('mycvs')
