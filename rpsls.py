#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈佳韦
日期：2020年11月21日
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name=='石头':
        number=0
    elif name=='史波克':
        number=1
    elif name=='纸':
        number=2
    elif name=='蜥蜴':
        number=3
    else:
        number=4
    return number


def number_to_name(number):
    if number==0:
        name='石头'
    elif number==1:
        name='史波克'
    elif number==2:
        name='纸'
    elif number==3:
        name='蜥蜴'
    else:
        name='剪刀'
    return name

def rpsls(player_choice):
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randint(0, 4)
    comp_number_name = number_to_name(comp_number)
    print('计算机的选择是%s' % (comp_number_name))
    if comp_number == player_choice_number:
        print('您和计算机出的一样呢！')
    elif player_choice_number == 0:
        if comp_number == 3 or comp_number == 4:
            print('您赢了')
        else:
            print('您输了')
    elif player_choice_number == 1:
        if comp_number == 0 or comp_number == 4:
            print('您赢了')
        else:
            print('您输了')
    elif player_choice_number == 2:
        if comp_number == 0 or comp_number == 1:
            print('您赢了')
        else:
            print('您输了')
    elif player_choice_number == 3:
        if comp_number == 1 or comp_number == 2:
            print('您赢了')
        else:
            print('您输了')
    else:
        if comp_number == 2 or comp_number == 3:
            print('您赢了')
        else:
            print('您输了')



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
if input()=='石头'or'剪刀'or'布'or'史波克'or'蜥蜴':
    choice_name=input()
    print('您的选择是：%s'%choice_name)
    rpsls(choice_name)
else:
    input('Error: No Correct Name')


