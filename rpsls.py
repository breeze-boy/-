#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��¼�Τ
���ڣ�2020��11��21��
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=='ʯͷ':
        number=0
    elif name=='ʷ����':
        number=1
    elif name=='ֽ':
        number=2
    elif name=='����':
        number=3
    else:
        number=4
    return number


def number_to_name(number):
    if number==0:
        name='ʯͷ'
    elif number==1:
        name='ʷ����'
    elif number==2:
        name='ֽ'
    elif number==3:
        name='����'
    else:
        name='����'
    return name

def rpsls(player_choice):
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randint(0, 4)
    comp_number_name = number_to_name(comp_number)
    print('�������ѡ����%s' % (comp_number_name))
    if comp_number == player_choice_number:
        print('���ͼ��������һ���أ�')
    elif player_choice_number == 0:
        if comp_number == 3 or comp_number == 4:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number == 1:
        if comp_number == 0 or comp_number == 4:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number == 2:
        if comp_number == 0 or comp_number == 1:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number == 3:
        if comp_number == 1 or comp_number == 2:
            print('��Ӯ��')
        else:
            print('������')
    else:
        if comp_number == 2 or comp_number == 3:
            print('��Ӯ��')
        else:
            print('������')



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
if input()=='ʯͷ'or'����'or'��'or'ʷ����'or'����':
    choice_name=input()
    print('����ѡ���ǣ�%s'%choice_name)
    rpsls(choice_name)
else:
    input('Error: No Correct Name')


