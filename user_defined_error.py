# class ConnectionIssue(Exception):
#     def __init__(z,c):
#         z.c = c
#
# try:
#     a=int(input('enter a value : '))
#     if a<20:
#         raise ConnectionIssue('NETWORK PROBLEM')
#
# except ConnectionIssue as i:
#     print (i.c)

class ConnectionError(Exception):
    def __init__(z,c):
        z.c=c
try:
    a=int(input('Enter a value : '))
    if a>20:
        raise ConnectionError('Network issue')
except ConnectionError as i:
    print(i.c)

