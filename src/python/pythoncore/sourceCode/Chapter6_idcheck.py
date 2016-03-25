# coding:utf-8

import  string

alphas = string.letters + '_'
nums = string.digits

print alphas
print nums

print '欢迎来到标示符检查1.0'
print '测试者必须输入至少2个字符'

myInput = raw_input('Identifier to test?')


if len(myInput) > 1:
    if myInput[0] not in alphas:
        print '''错误:第一个字符必须是 alphabetic'''

    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas+nums:
                print  '''错误:其他字符必须是 alphabetic + 数组'''
                break

        else:
            print '是一个标示符'