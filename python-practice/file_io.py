# 使用绝对路径
import os

# 获取【脚本所在目录】的绝对路径（不依赖你在哪里运行）
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "var_types.py")

file = open(file_path,"r")
try:
    content = file.read()
    #print(content)
finally:
    file.close()
# 统计行数 初始化变量
total_lines = 0
print_count = 0
print_count = 0
comment_count = 0
with open(file_path, 'r') as file:
    for line in file:
        total_lines += 1
        line_lower = line.lower()
        if "print" in line_lower:
            print_count += 1
        #统计注释行
        if line_lower.startswith("#"):
            comment_count += 1
    print(total_lines)
    print(print_count)
    print(comment_count)
    #content = file.read()
    #print(content)
    #finally:
    #    file.close()


