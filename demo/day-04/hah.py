


def sum(a,b):
    s =a+b
    print(a,'+',b,'=',s)
    return s
def sub(a,b):
    s = a-b
    print(a, '-',b, '=',s)



def div(a,b):
    if (b!=0):
        s = a/b
        print(a, '/',b, '=',s)
    else:
        print('除数不能为0')


def mul(a,b):
    s = a*b
    print(a, '*',b, '=',s)




sum(sum(2,3),4)
sub(5,2)
div(6,2)
mul(15,3)

#有参数无返回值
def say_hello_to(human):
    print(human,'hello')
say_hello_to('小明同学')

#无参数有返回值
def ff():
    return ('小明滚出去')
print(ff())

#有参数有返回值
def ff(hm1,hm2,money):
    return '{}欠{}{}钱' .format(hm1,hm2,money)
print(ff("小明",'小红','五毛'))

def ff(hm1,hm2,money):
    return '{m1}欠{m2}{mon}钱'.format(m1=hm1, m2=hm2,mon = money)
    print(ff("小明", '小红', '五毛'))






