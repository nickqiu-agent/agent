#基础数据
tasks = [("环境安装", 2), ("类型转换", 0.5), ("运算符联系", 0.5) ,("统计", 0.5),("github账号创建", 1)]

num = len(tasks)
i = 0
while i < num:
    print(tasks[i][0] + ":" + str(tasks[i][1]) + "小时")
    i += 1
#for跑出工作时间超过一小时的工作
for tast in tasks:
    if(tast[1] >= 1):
        print(tast[0] + ":" + str(tast[1]) + "小时")
