from datetime import date, timedelta

# 阶段定义：每阶段 4 周（阶段5 为 3 周），每周 Mon-Fri 给 3 件具体事
phases = [
    {
        "name": "阶段1 基础回炉 + LLM 入门",
        "start": date(2026, 8, 13),
        "goal": "Python 回炉 + LLM 原理 + 调 API + Prompt 工程",
        "weeks": [
            {"theme": "W1 Python 语法回炉（验收：能写 200 行脚本）",
             "Mon": ["装 Python3.12+VS Code，跑通 print 并截图存证", "学变量/类型/运算符，写 10 行练习", "当天笔记推 GitHub"],
             "Tue": ["学 if/for/while + 函数定义", "写 1 个判断奇偶并用循环打印的函数", "笔记提交"],
             "Wed": ["学 list/dict/字符串方法", "写 1 个统计字符串词频的小脚本", "笔记提交"],
             "Thu": ["学文件读写 + try/except", "写 1 个读 txt 统计行数的脚本", "笔记提交"],
             "Fri": ["综合：写读 CSV 统计行数+某列求和的脚本（产出物）", "推送到 GitHub", "周复盘：记下踩的坑"],
             "Sat": ["本周复盘 + 整理 1 篇 Python 笔记", "看 1 个 GitHub 上的 Python 小项目结构"],
             "Sun": ["休息 / 刷 30 分钟 AI 开发岗 JD"]},
            {"theme": "W2 LLM 原理扫盲（验收：能讲清 RAG vs 微调）",
             "Mon": ["学 Token/分词/上下文窗口概念", "用 tokenizer 工具数一段文字的 token 数", "笔记提交"],
             "Tue": ["学温度/top-p/采样参数", "对比同 prompt 不同温度的回复差异", "笔记提交"],
             "Wed": ["学 Embedding 向量概念", "调一次 embedding 接口看向量维度", "笔记提交"],
             "Thu": ["学 RAG 原理（检索增强生成）", "画一张 RAG 流程图笔记", "笔记提交"],
             "Fri": ["整理「微调 vs RAG vs 提示词」对比表（产出物）", "推 GitHub", "周复盘"],
             "Sat": ["本周复盘 + 笔记整理", "看 1 篇讲解 Transformer 的科普文"],
             "Sun": ["休息 / 刷 30 分钟 JD"]},
            {"theme": "W3 调通大模型 API（验收：3 个 API Demo）",
             "Mon": ["注册 DeepSeek/通义，拿到 API key", "用 curl 调通第一个对话请求", "笔记提交"],
             "Tue": ["用 Python requests 调 API 拿到回复", "封装成 1 个 chat() 函数", "笔记提交"],
             "Wed": ["学多轮对话：维护 messages 列表", "实现 1 个能连续对话的脚本", "笔记提交"],
             "Thu": ["学流式输出 stream=True", "改写 chat() 支持逐字输出", "笔记提交"],
             "Fri": ["写 3 个不同场景的 API Demo 放 GitHub（产出物）", "推送", "周复盘"],
             "Sat": ["本周复盘", "重读自己的 3 个 Demo 找可复用点"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W4 Prompt 工程（验收：1 套业务 Prompt 模板）",
             "Mon": ["学角色设定 + 明确指令写法", "给 1 个任务写 2 版 prompt 对比效果", "笔记提交"],
             "Tue": ["学 Few-shot 示例", "用示例让模型稳定输出格式", "笔记提交"],
             "Wed": ["学思维链 CoT", "让模型分步解 1 道逻辑题", "笔记提交"],
             "Thu": ["学结构化输出 JSON 模式", "写 1 个返回 JSON 的解析脚本", "笔记提交"],
             "Fri": ["设计「项目周报生成」Prompt 模板（产出物）", "放 GitHub", "周复盘"],
             "Sat": ["本周复盘 + 模板整理", "试运行模板看效果"],
             "Sun": ["休息 / 刷 JD"]},
        ],
    },
    {
        "name": "阶段2 Agent 开发入门",
        "start": date(2026, 9, 13),
        "goal": "Function Calling + 框架 + RAG 深入 + 多 Agent",
        "weeks": [
            {"theme": "W5 Agent 核心（验收：手写工具调用 Demo）",
             "Mon": ["学 Function Calling 原理", "写 1 个 JSON Schema 工具描述", "笔记提交"],
             "Tue": ["学模型如何决定调工具", "实现「计算器」工具调用循环", "笔记提交"],
             "Wed": ["扩展：加「查时间/天气」工具", "写 1 个多工具路由脚本", "笔记提交"],
             "Thu": ["学 ReAct 模式（推理-行动-观察）", "手画 ReAct 流程图笔记", "笔记提交"],
             "Fri": ["写带记忆的 Agent Demo 放 GitHub（产出物）", "推送", "周复盘"],
             "Sat": ["本周复盘", "读 1 篇 Agent 实战文章"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W6 框架实战 LangGraph（验收：框架版 Agent）",
             "Mon": ["装 LangGraph + 跑官方 Quickstart", "理解 StateGraph 概念", "笔记提交"],
             "Tue": ["学节点/边/状态定义", "写 1 个 2 节点流程图", "笔记提交"],
             "Wed": ["用 LangGraph 写第一个 Agent", "接入昨天 chat() 函数", "笔记提交"],
             "Thu": ["学工具节点 + 条件边", "让 Agent 按结果走不同分支", "笔记提交"],
             "Fri": ["改进 Agent Demo 放 GitHub（产出物）", "推送", "周复盘"],
             "Sat": ["本周复盘", "对比手写 vs 框架的差异笔记"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W7 RAG 深入（验收：公司制度问答 Demo）",
             "Mon": ["学文档切分 chunk size/overlap", "切分 1 个长文档看效果", "笔记提交"],
             "Tue": ["学 Chroma/FAISS 向量库", "把切分文本入库", "笔记提交"],
             "Wed": ["学 Embedding 模型选择", "重建索引并查询", "笔记提交"],
             "Thu": ["学检索 + 重排", "实现 top-k 检索", "笔记提交"],
             "Fri": ["做「公司制度问答」RAG Demo 放 GitHub（产出物）", "推送", "周复盘"],
             "Sat": ["本周复盘", "测 Demo 的边界问题"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W8 多 Agent + 平台（验收：对比笔记）",
             "Mon": ["学多 Agent 协作模式", "画 1 张协作架构图", "笔记提交"],
             "Tue": ["跑 CrewAI 或 LangGraph 多 Agent 示例", "改 1 个参数看变化", "笔记提交"],
             "Wed": ["体验 Dify 平台拖工作流", "搭 1 个简单问答流", "笔记提交"],
             "Thu": ["体验 Coze", "对比 Dify/Coze 差异", "笔记提交"],
             "Fri": ["写「自研 vs 平台」对比笔记（产出物）", "放 GitHub", "周复盘"],
             "Sat": ["本周复盘", "确定主项目用自研还是平台"],
             "Sun": ["休息 / 刷 JD"]},
        ],
    },
    {
        "name": "阶段3 实战项目 + 简历启动（核心项目：AI 项目管理助手）",
        "start": date(2026, 10, 13),
        "goal": "做 1 个完整 Agent 项目 + 双版本简历",
        "weeks": [
            {"theme": "W9 项目设计 + 脚手架",
             "Mon": ["写项目 README + PRD 需求文档", "拆出 3 个核心功能", "放 GitHub"],
             "Tue": ["搭 Streamlit 界面骨架", "能本地起一个空页面", "笔记提交"],
             "Wed": ["接入大模型 API", "页面能发消息收回复", "笔记提交"],
             "Thu": ["写 WBS 拆解 Prompt + 解析逻辑", "输入需求返回任务列表", "笔记提交"],
             "Fri": ["MVP：输入需求输出 WBS 列表（产出物）", "录屏/截图存证", "周复盘"],
             "Sat": ["本周复盘", "读类似开源项目找参考"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W10 核心功能",
             "Mon": ["做甘特图生成（文本/简易图）", "WBS→时间轴", "笔记提交"],
             "Tue": ["做风险识别模块", "基于 WBS 标出风险点", "笔记提交"],
             "Wed": ["做周报生成模块", "输入进度输出周报", "笔记提交"],
             "Thu": ["加会话/记忆管理", "多轮能记住上下文", "笔记提交"],
             "Fri": ["整合跑通 + 演示视频（产出物）", "推 GitHub", "周复盘"],
             "Sat": ["本周复盘", "自己用项目管一个虚拟项目"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W11 打磨",
             "Mon": ["补错误处理 + 边界 case", "列 5 个异常场景测试", "笔记提交"],
             "Tue": ["UI 美化", "调样式到能拿出手", "笔记提交"],
             "Wed": ["用 1 个真实项目跑通", "截图存档", "笔记提交"],
             "Thu": ["写技术博客讲架构", "发到博客/公众号", "笔记提交"],
             "Fri": ["完善 GitHub README（产出物）", "含截图+部署说明", "周复盘"],
             "Sat": ["本周复盘", "准备简历素材"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W12 简历启动",
             "Mon": ["起草「AI 应用开发工程师」简历 v1", "列项目+技能", "存草稿"],
             "Tue": ["起草「AI 技术负责人」简历 v2", "突出管理+PMP+AI", "存草稿"],
             "Wed": ["把项目写进简历", "量化成果", "笔记提交"],
             "Thu": ["读 5 个目标 JD 校准关键词", "补齐缺失关键词", "笔记提交"],
             "Fri": ["简历定稿（产出物）", "两版都导出 PDF", "周复盘"],
             "Sat": ["本周复盘", "让朋友/前同事帮看简历"],
             "Sun": ["休息 / 刷 JD"]},
        ],
    },
    {
        "name": "阶段4 投递 + 面试冲刺",
        "start": date(2026, 11, 13),
        "goal": "开始投递 + 面试题 + 模拟面试",
        "weeks": [
            {"theme": "W13 开始投递",
             "Mon": ["注册 BOSS/拉勾/脉脉 + 完善资料", "上传双版简历", "整理投递表"],
             "Tue": ["按 JD 微调投 10 家", "记录到投递追踪表", "复盘话术"],
             "Wed": ["再投 10 家", "关注回复率", "优化打招呼语"],
             "Thu": ["再投 10 家 + 整理面试问题", "建错题本", "笔记提交"],
             "Fri": ["激活内推（脉脉/前同事）（产出物）", "发 5 条求助", "周复盘"],
             "Sat": ["本周复盘", "统计投递/回复数据"],
             "Sun": ["休息 / 复盘本周"]},
            {"theme": "W14 面试题准备",
             "Mon": ["学 Transformer 原理 + 注意力机制", "写 1 页速记", "笔记提交"],
             "Tue": ["学 RAG 优化面试题", "整理 10 道高频", "笔记提交"],
             "Wed": ["学 Function Calling/Agent 题", "整理 10 道高频", "笔记提交"],
             "Thu": ["学 Python 基础八股", "整理 15 道", "笔记提交"],
             "Fri": ["模拟面试 1 次（产出物）", "录音/录像复盘", "周复盘"],
             "Sat": ["本周复盘", "补薄弱点"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W15 项目深挖 + 复盘",
             "Mon": ["准备项目讲解 3 分钟话术", "对着镜子讲 1 遍", "笔记提交"],
             "Tue": ["复盘 1 次真实面试", "记下面试官问题", "笔记提交"],
             "Wed": ["用 STAR 梳理管理案例（结合 PMP）", "写 3 个案例", "笔记提交"],
             "Thu": ["模拟面试 2", "对比上次改进", "笔记提交"],
             "Fri": ["整理高频题错题本（产出物）", "分类归档", "周复盘"],
             "Sat": ["本周复盘", "强化易错点"],
             "Sun": ["休息 / 刷 JD"]},
            {"theme": "W16 冲刺",
             "Mon": ["继续投递 + 跟进已投", "回复未读", "更新追踪表"],
             "Tue": ["模拟面试 3", "压测真实场景", "笔记提交"],
             "Wed": ["做 offer 对比框架（薪资/成长/AI业务）", "列维度", "笔记提交"],
             "Thu": ["准备谈薪话术", "练 1 遍", "笔记提交"],
             "Fri": ["复盘本周（产出物）", "调整下周重点", "周复盘"],
             "Sat": ["本周复盘", "整理资料"],
             "Sun": ["休息 / 刷 JD"]},
        ],
    },
    {
        "name": "阶段5 交接收尾",
        "start": date(2026, 12, 13),
        "goal": "漂亮离职 + offer 决策 + 入职准备",
        "weeks": [
            {"theme": "W17 离职交接",
             "Mon": ["列交接清单", "盘点项目/账号/文档", "存草稿"],
             "Tue": ["文档归档", "整理可交接材料", "笔记提交"],
             "Wed": ["开交接说明会", "跟接手人过一遍", "笔记提交"],
             "Thu": ["收尾确认", "签字/系统权限处理", "笔记提交"],
             "Fri": ["离职准备完成（产出物）", "确认最后工作日", "周复盘"],
             "Sat": ["本周复盘", "放松一下"],
             "Sun": ["休息"]},
            {"theme": "W18 offer 决策",
             "Mon": ["列 offer 对比表", "填各维度得分", "存草稿"],
             "Tue": ["做最终决策", "和家人/朋友商量", "笔记提交"],
             "Wed": ["确认入职", "回Offer/签协议", "笔记提交"],
             "Thu": ["准备背调材料", "整理证明人", "笔记提交"],
             "Fri": ["缓冲/休息（产出物）", "规划空窗期", "周复盘"],
             "Sat": ["本周复盘", "准备入职"],
             "Sun": ["休息"]},
            {"theme": "W19 入职准备",
             "Mon": ["了解新团队技术栈", "列学习清单", "笔记提交"],
             "Tue": ["前置学 1 个新工具/框架", "跑通环境", "笔记提交"],
             "Wed": ["整理入职材料", "查入职流程", "笔记提交"],
             "Thu": ["做入职前最后准备", "心态调整", "笔记提交"],
             "Fri": ["完成交接，准备入职（产出物）", "周复盘", "庆祝转型成功"],
             "Sat": ["休息", "收拾心情"],
             "Sun": ["休息"]},
        ],
    },
]

end = date(2026, 12, 31)
weekday_cn = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
wd_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

lines = []
lines.append("# Nick 每日执行计划（2026-08-13 → 2026-12-31）\n")
lines.append("> 规则：每天 3 件具体事，每件 ≤2 小时、有明确产出物。周末只复盘+刷 JD，不加压。\n")
lines.append("> 每天早上 9:00 / 晚上 21:00 由 Buddy 督导。没完成找根因，不批评。\n")

# 为每个阶段预生成「按顺序的学习日任务」列表（周一~周五，跨周连续）
phase_study = {}
for p in phases:
    order = []
    for w in p["weeks"]:
        for wd in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
            if wd in w:
                order.append((w["theme"], w[wd]))
    phase_study[p["name"]] = order

cur_phase = None
cur_week_theme = None
ptr = 0
d = date(2026, 8, 13)
while d <= end:
    # 找当前阶段
    phase = None
    for p in phases:
        if p["start"] <= d:
            phase = p
    wd = wd_en[d.weekday()]
    # 阶段标题
    if phase["name"] != cur_phase:
        lines.append(f"\n## {phase['name']}")
        lines.append(f"> 目标：{phase['goal']}\n")
        cur_phase = phase["name"]
        cur_week_theme = None
        ptr = 0
    # 取当天任务
    if wd in ("Sat", "Sun"):
        if wd == "Sat":
            tasks = ["本周复盘 + 整理笔记（1 小时）", "看 1 个相关项目/文章"]
        else:
            tasks = ["休息 / 刷 30 分钟目标岗位 JD"]
    else:
        if ptr < len(phase_study[phase["name"]]):
            theme, tasks = phase_study[phase["name"]][ptr]
            ptr += 1
        else:
            tasks = ["自由复习 / 补进度", "看 1 个相关项目"]
    # 周标题（学习日切换 theme 时）
    if wd not in ("Sat", "Sun") and ptr <= len(phase_study[phase["name"]]):
        # 当前任务所属 theme
        if ptr > 0:
            theme_now = phase_study[phase["name"]][ptr - 1][0]
            if theme_now != cur_week_theme:
                lines.append(f"\n### {theme_now}\n")
                cur_week_theme = theme_now
    date_str = d.strftime("%Y-%m-%d")
    lines.append(f"- **{date_str} {weekday_cn[d.weekday()]}**")
    for i, t in enumerate(tasks, 1):
        lines.append(f"  {i}. {t}")
    d += timedelta(days=1)

with open("/Users/gemini/WorkBuddy/2026-08-12-08-55-50/每日执行计划.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print("生成完成，共 %d 天" % ((end - date(2026,8,13)).days + 1))
