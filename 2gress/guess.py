# _*_ coding: utf-8 _*_

import random

print '******************来猜猜石头哥心里的数字吧！******************'
iMyLove = random.randint(1,10)
iInput = input('你猜是神马数字呢？')
i = 0
while iInput != iMyLove:
    i = i+1
    if i == 3:
        break
    if iInput > iMyLove:
        print('哥，大了，大了.....')
        iInput = input('再试试吧')
    else:
        print('嗨，小了，小了......')
        iInput = input('再试试吧')

if i < 3:
    print('你真是石头哥肚里的蛔虫！ \n猜对了也没有奖励！\n游戏结束。')
else:
    print('太不了解石头哥了，自爆算了！\n游戏结束。')


