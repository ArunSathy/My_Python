def scope():
    def local_1():
        test='Test 1'
    def local_2():
        nonlocal test
        test='Test 2'
    def local_3():
        global test
        test='Test 3'

    test='Test main'
    local_1()
    print('Final test result : ',test)
    local_2()
    print('Final test result : ',test)
    local_3()
scope()
print('Final test result main : ',test)