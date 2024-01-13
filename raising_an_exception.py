# try:
#     a = int(input('enter a value'))
#     if a > 10:
#         raise ImportError
#
# except ImportError as i:
#     print('error', i)

# try:
#     a=int(input('enter a value : '))
#     if a<10:
#         raise ImportError
# except ImportError as i:
#     print('error',i)

try:
    a=9
    if a <=10:
        raise ImportError
except ImportError as i:
    print('backoff',i)
