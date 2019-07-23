def zl(st):
    # 第一步：统一符号  对字符串的处理，用replace（）

    st = st.replace("''",'"')
    print(st)
    # 第二步：去掉中括号 字符串截取  [:: ]
    st = st[2:-2]
    print(st)

    # 第三步：变成list  字符串切片  .split（） 新建一个list变量
    st_li = st.split('" , "')
    print(st_li)

    # 第四步：取出后面的数字  循环遍历取出list里面的每个值，对这个值进行截取
    st_dict = {}
    for i in st_li:
        i_key = i[1:]
        print(i_key)


    # 第五步：统计相同的数字个数  用字典去统计
    if (i_key not in st_dict):
        st_dict[i_key] = 1
    else:
        st_dict[i_key] +=1
    print(st_dict)

    #第六步：判断数据中有没有同时存在三个相同数字和两个相同数字  if判断
    v1 = 0#如果key对应的数值有3的 v1 = 1，如果没有则为0
    v2 = 0# 如果key对应的数值有2的 v2 = 1，如果没有则为0
    for key in st_dict:
        if(st_dict[key] == 3):
            v1 = 1
        if(st_dict[key] == 2):
            v2 = 1
    if (v1 == 1 and v2 == 1):
        print("这把牌可以三带二")
    else:
        print("只能炸了")

#open 是 python提供的一个内置函数:作用就是打开一个文件.参数一:文件路径;参数二:文件的打开模式 r只读,W可写入,a可读可写
#with open() as f 类似于 f = open ()他可以在with 的代码执行出问题的时候,做一些资源释放的工作

with open("D:\\softwaredata\\pychrm\\untitledgy1906A\\demo\\day-04\\cards.txt") as f:
 # 读文件.readlines()作用就是把文件中整个内容按行读取出来,存到一个list中;read()把整个文件的内容读取出来,存到一个字符串中
    f_li=f.readlines()
 # for循环遍历这个列表
    for line in f_li:
        line = line.replace("\n","")
        zl(line)
        # print(line)
    # print(f_li)
    # zl('''["C2" , "D13" , "D2" , "H2" , "H9" , "S13"]''')

