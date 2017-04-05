def scope_test():
    global spam
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        #nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


#After local assignment: test spam
#After nonlocal assignment: nonlocal spam
#After global assignment: nonlocal spam
#In global scope: global spam