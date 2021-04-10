import base64
import pickle

# This script doesn't solve the challenge

debug = False

class Notes:
    name = ''
    notes = ''

    def __reduce__(self):
        return (print, ('./flag.txt',))

outfile = open('output', 'wb')
if debug:
    pickle.dump(Notes(), outfile)
else:
    outfile.write(base64.b64encode(pickle.dumps(Notes())))
outfile.close()

if debug:
    infile = open('output', 'rb')
    data = pickle.load(infile)
    infile.close()
    print(data)
