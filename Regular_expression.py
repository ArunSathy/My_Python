# import re

#1. match
#2. search
#3. findall
#4. find & replace

# pat=r"arun"

#------match-----------

# if re.match(pat,'arun sathyan, how are you doing'):
#     print('present')
# else:
#     print('absent')

#--------search----------

# if re.search(pat,'hello arun sathyan'):
#     print('present')
# else:
#     print('absent')

#---------findall---------------

# print(re.findall(pat,'arun sathyan hello arun where are you arun'))

#------find&replace-------------

# strg="I'm arun Sathyan, I'm an amazonian"
# new=re.sub('arun','Arun',strg) # first element is the pattern 'arun' & second one is the replacement'Arun'
# print(new)

#---------.match------------------

# pat=r'a..n'
#
# if re.match(pat,'arun'):
#     print('present')
# else:
#     print('absent')

#--------------character class----------------------

# pat=r'[A-Z][0-9][a-z]'
#
# if re.search(pat,'B8i'):
#     print('preset')
# else:
#     print('absent')

#---------------------------------------------------------

# import re
#
# s=r'arun'
#
# str1='arun sathyan and arun good and arun bad'
#
# if re.match(s,str1):
#     print('present')
# else:
#     print('absent')
#
# print('----------------------------')
#
# if re.search(s,str1):
#     print('present')
# else:
#     print('absent')
#
# print('----------------------------')
#
# print(re.findall(s,str1))
#
# print('----------------------------')
#
# str2=re.sub(s,'Arun',str1)
#
# print(str2)
#
# print('----------------------------')
#
# if re.match('ar.n','aroun sathyan'):
#     print('present')
# else:
#     print('absent')
#
# print('----------------------------')



