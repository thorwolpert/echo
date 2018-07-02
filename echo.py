import os
import sys

for k,v in os.environ.items():
    print ( k,'=',v, file=sys.stderr)

