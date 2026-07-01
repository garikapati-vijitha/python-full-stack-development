Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
# POSITIVE STRIDING
a = "cloud computing"
>>> a[::5]
'c u'
>>> a[::4]
'cdmi'
>>> a[::8]
'cm'
>>> a[2:]
'oud computing'
>>> a[::2]
'codcmuig'
>>> a[:9]
'cloud com'
>>> a[3:11]
'ud compu'
>>> b = "machine learing"
>>> b[1:9:2]
'ahn '
>>> b[3]
'h'
>>> b[3:14:2]
'hn ern'
>>> b[5:15:4]
'nen'
>>> b[2:12:3]
'cnlr'
>>> b[0:10:1]
'machine le'
>>> 
>>> # NEGATIVE STRIDING
>>> c = "python course"
>>> c[-1:-10:-2]
'ero o'
>>> c[-3:-13:-4]
'r t'
>>> c[-5:-11:-3]
'on'
