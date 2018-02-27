##Roman to integer
def romanToInt(s):
    r = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}##定义罗马字母表的哈希表
    n = 0 ##创建一个变量存储转换结果，初始化为0
    i = 0 ##如果s长度为1，下面的转换循环算法会直接跳过，这里设置i = 0可以在n = n + r[s[i]]处加上s[0]
    for i in range(0,len(s)-1):##for循环，范围为s的第一个元素到到倒数第二个元素
        ##根据罗马数字转化规则设置条件判断算法
        if r[s[i]] >= r[s[i+1]]:
            n = n + r[s[i]]
            i += 1
        else:
            n = n - r[s[i]]
            i += 1
    n = n + r[s[i]]##循环结束后n的值还缺少最后一个罗马字母未累加（如果s长度为1，则循环结束后的n为初始化时的值，需要加上s[0]，这里可以先初始化i=0）
    return n
##Roman to integer




###########测试数据##########
print(romanToInt('CMXCIX')) ##999
print(romanToInt('LXV')) ##65
print(romanToInt('XL')) ## 40
print(romanToInt('D')) ##500
###########测试数据##########

