import urllib.parse

outfile = open('postb', 'w')
params = ({ 'vote': 'b' })
encoded = urllib.parse.urlencode(params)
outfile.write(encoded)
outfile.close()
outfile = open('posta', 'w')
params = ({ 'vote': 'a' })
encoded = urllib.parse.urlencode(params)
outfile.write(encoded)
outfile.close()
outfile = open('postc', 'w')
params = ({ 'vote': 'c' })
encoded = urllib.parse.urlencode(params)
outfile.write(encoded)
outfile.close()