'''
#.字典的特性：
1.字典的key是唯一的,不允许同一个键出现两次,后一个值会被记住
2.key是不可以改变的
 元组(1,2,3,45)可以作为key,但是(1,[3])不可以作为一个key
'''
#增
#创建
a = {}
#字典中新增一对数据
a["姓名"] = '张莉'
print(a)
a[1] = 333
print(a)
a[(1,2)] = 333
print(a)

#删
#删除某一对值,pop的参数只能为key
a.pop(1)
del a["姓名"]
print(a)
#清空字典
a.clear()
print(a)

#改
a["姓名"] = '小明同学'
print(a)

#查
#根据key查value
print(a["姓名"])

#遍历字典（借助循环）
for key in a:
    print(a[key])

#字典合并
#把一个字典合并到另一个字典中
c = {'姓名':'小明',"班级":"三年级二班"}
d = {'性别':'男'}
# c.update(d)
# print(c)
#两个字典合并,生成一个新字典
print(dict(c,**d))
print(c)
print(d)

#成员判断（key)
if("性别" in c):
    print("存在字典中")
else:
    print("不存在字典中")