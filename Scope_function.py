# def check_scope():
#     def do_local():
#         test='A test'
#         print('a :',test)
#     def do_non_local():
#         nonlocal test
#         test='B test'
#     def do_global():
#         global test
#         test='C global'
#     def loca():
#         test='goal'
#
#     test='default local'
#     do_local()
#     print('hiiiii : ',test)
#     do_non_local()
#     print('heyyyy : ',test)
#     do_global()
#     print('hoiiii',test)
#     loca()
#     print('hiddddididd',test)
#
# check_scope()
# print('main : ',test)


#------------------------------------------------------

def main():
    def A():
        test='Test A'
        # print('value :',test)
    def B():
        nonlocal test
        test='Test B'
    def C():
        global test
        test='Test C'
    test='General Test'
    A()
    print('value 1 : ',test)
    B()
    print('value 2 : ',test)
    C()
    print('value 3 : ',test)

main()
print('value 4 : ',test)




