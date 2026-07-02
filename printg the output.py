Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=[9,1,5,2,8,4,6,3,7,0]
... #[7,6,4,3,0,9,8,5,2,1]
>>> a[:5]
[9, 1, 5, 2, 8]
>>> a[5:]
[4, 6, 3, 7, 0]
>>> a=[9, 1, 5, 2, 8]
>>> b=[4, 6, 3, 7, 0]
>>> a.sort()
>>> b.sort()
>>> a
[1, 2, 5, 8, 9]
>>> b
[0, 3, 4, 6, 7]
>>> a.reverse()
>>> b.reverse()
>>> b+a
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
