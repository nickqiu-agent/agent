# 事2 交付物：变量 / 类型 / 运算符练习（≥30 行，带注释）
# 运行：python3 var_types.py
# TODO(你填)：把下面每个 # === 处的练习补全，跑通并打印结果


# === 1. 四种基本类型 + 类型互转 ===
hours_dev = 8          # int
hours_pm = 2.5         # float
role = "技术总监"       # str
is_critical = True     # bool

# 互转示例（取消注释并补完）
# total_hours = hours_dev + int(hours_pm)
# print("总工时:", total_hours, type(total_hours))

hours_dev = float(hours_dev)
print(type(hours_dev))
# float转换为str
hours_pm = str(hours_pm)
print(type(hours_pm))
hours_dev = bool(hours_dev)
print(hours_dev)
print(type(hours_dev))


# === 2. 算术 / 比较 / 逻辑运算符 ===
a, b = 10, 3
# print("a + b =", a + b)
# print("a > b ?", a > b)
# print("a > b and is_critical ?", a > b and is_critical)
x = a - b
print(x)
x = a + b
print(x)
x = a * b
print(x)
x = a / b
print(x)
x = a % b
print(x)
x = a // b
print(x)

print(a == b)
print(a > b)






# === 3. 项目工时小统计（用上面学到的）===
# tasks = [("需求评审", 4), ("方案设计", 8), ("联调", 6)]
# total = sum(h for _, h in tasks)
# print("本周任务总工时:", total)
checks = 4
sj = 8
lt = 6
total = checks + sj + lt
print(total)
# if __name__ == "__main__":
#     # 先保证事1 的痕迹也在：最低限度先能跑
#     print("hello ai")