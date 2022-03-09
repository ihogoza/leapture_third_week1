import httplib2


print(httplib2.__version__)
print(httplib2.__copyright__)
print(httplib2.__doc__)

hcl = httplib2.Http()

resph, content = hcl.request('https://edu.gcfglobal.org/en/blogbasics/copyright-and-fair-use/1/')
print('Response Header\n')
print(resph)
print('content-----\n')
print(content)