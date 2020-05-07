def newdeclarator(func):
    def wrap_func():
        print("Started New declarator")
        func()
        print("Declarator completed")
    return wrap_func

def func_need():
    print("I am in func need")

func_need=newdeclarator(func_need)
func_need()
