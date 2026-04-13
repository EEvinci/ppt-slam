# -*- coding: utf-8 -*-
OUTPUT = '/workspace/ppts-demo/index.html'

SLIDES = [
    {
        'type': 'cover',
        'title': 'AGENT 实战',
        'subtitle': '从 单兵作战 到 数字员工集群',
        'edition': 'PRESENTED BY 李琛 | 2026 EDITION',
    },
    {
        'type': 'overview',
        'title': 'CONTENTS · 目录',
        'items': [
            ('01', '范式革命', '为什么 Agent 是 AI 的终局？'),
            ('02', '执行者 Agent', '从对话框到数字员工'),
            ('03', '复制者 Skills', '一切流程与人格皆可 蒸馏'),
            ('04', '工程化思维', 'Context 与 Harness 的深度博弈'),
            ('05', '未来启示', '人是 Agent 与现实之间的桥梁'),
        ],
    },
    {
        'type': 'section',
        'title': '01  范式革命',
        'tag': '为什么 Agent 是 AI 的终局？',
        'cards': [
            ('Copilot：辅助模式的极限', 'Copilot（副驾驶）是辅助模式——你下指令，它执行。人的角色是「决策者+指令者」，AI是「执行者」。这种模式的天花板在于：人成为整个流程的瓶颈。当任务复杂度超过单次指令的承载能力时，Copilot模式就会失效。'),
            ('Agent：自主模式的跃迁', 'Agent（智能体）是自主模式——你给目标，它拆解、思考、调用工具并交付完整结果。人的角色转变为「目标设定者+结果验收者」。这不只是效率的提升，而是人机协作范式的根本转变：AI从工具变成伙伴。'),
            ('Progressive Disclosure', 'Agent 通过交互逐步向用户揭示复杂任务的进展与细节——不是一次性给出全部答案，而是在执行过程中持续反馈。这种「渐进式披露」让用户始终保持对过程的掌控感，同时享受结果的质量。复杂任务从此不再需要人类全程盯守。'),
            ('从工具到伙伴的转折', 'Copilot 时代，AI是「更好的工具」。Agent 时代，AI是「能动的参与者」。这一转折意味着：AI不再被动等待指令，而是能主动理解目标、规划路径、调用资源。人的核心价值随之迁移：不在于「做」，而在于「判断」。'),
            ('Agent 是终局的逻辑', '为什么说 Agent 是 AI 的终局？因为它的本质是「数字化的人」——拥有人类的决策能力，同时具备机器的稳定性和不知疲倦的执行力。当一个数字员工可以24小时运作任何一个可描述的流程，企业的边界将被重新定义。'),
        ],
    },
    {
        'type': 'section',
        'title': '02  执行者 Agent',
        'tag': '三位一体架构',
        'cards': [
            ('大脑：LLM', 'LLM 是 Agent 的推理中枢——负责意图识别、逻辑推理、路径规划、决策判断。一个强大的基座模型决定了 Agent 能处理多复杂的任务。GPT-4、Claude Opus、Qwen-Max……模型能力每上一个台阶，Agent 的边界就向外扩展一圈。'),
            ('手脚：Skills', 'Skills 是 Agent 改变物理世界的接口——通过 API 调用、代码执行、插件操作完成真实任务。没有 Skills 的 Agent 只能「想」，无法「做」。Skills 的丰富程度决定了 Agent 的行动半径。技能库越厚，Agent 的执行力越强。'),
            ('记忆：Context', 'Context 是 Agent 的业务记忆——承载用户偏好、历史交互、组织知识、工作流程。没有持久记忆的 Agent 每次对话都是陌生人，无法积累经验。有记忆的 Agent 才能从「新手」成长为「专家」，提供真正个性化的服务。'),
            ('准则：Harness', 'Harness 是 Agent 的安全护栏——确保在安全、合规、可控的轨道上运行。能力越强，越需要约束。没有 Harness 的 Agent 如同没有刹车系统的汽车，速度越快越危险。Harness Engineering 是 Agent 规模化的必修课。'),
            ('四位一体的协同', '大脑提供判断，手脚执行任务，记忆保持连续，准则保障安全。四者缺一，Agent 就无法真正落地。实际项目中，最大的挑战往往不是「让 Agent 能做」，而是「让它做对、做稳、做出规模」。这是一套系统工程。'),
        ],
    },
    {
        'type': 'section',
        'title': '02  执行者 Agent',
        'tag': '变化的承载体',
        'cards': [
            ('Agent 是业务流程的数字容器', 'Agent 本质上是「数字化了的业务流程」。一个可以被完整描述的流程，就可以被 Agent 承接。这意味着：企业大量标准化的脑力工作，第一次有了自动化的大规模复制手段。知识型工作的「规模瓶颈」将被打破。'),
            ('24小时不知疲倦的执行', '只要逻辑确定，Agent 就能不知疲倦地执行，不会疲劳、不会情绪波动、不会出错。这意味着：一份经验可以同时服务无限多的用户，一个专家的能力可以被放大一千倍。边际成本趋近于零。'),
            ('场景一：职工维权自动分类', '职工提交维权材料，Agent 自动阅读、提取关键信息、分类判断、转派处理人员。从「人工阅读、判断、分派」的5分钟流程，压缩到Agent的秒级自动处理。人力只介入复杂争议案件。'),
            ('场景二：政策咨询智能回复', '企业咨询最新政策，Agent 实时读取政策库，自动匹配最相关条款，生成个性化回复方案。咨询响应从24小时缩短到即时，大幅提升政府服务效率和企业的政策获得感。'),
            ('场景三：项目进度自动追踪', 'Agent 自动从邮件、会议记录、文档中提取项目进展节点，生成可视化追踪看板，向相关负责人推送预警。项目管理者的「信息收集」工作量降低70%，精力集中在决策而非汇总。'),
        ],
    },
    {
        'type': 'section',
        'title': '03  复制者 Skills',
        'tag': 'SOP 压缩凝练的工程化手段',
        'cards': [
            ('Skills 的本质定义', 'Skills 是 Agent 的「动态加载卡片」——一种可被描述、可被调用、可被迭代的工程化能力单元。它介于「工具」和「人格」之间：比工具有个性，比人格有结构。是经验从隐性知识到显性资产的桥梁。'),
            ('内涵：一切皆可 Skill', '只要可被描述，Skills 可以是任何东西——一个 SOP 流程、一个人的沟通风格、一个领域的专业判断、一套反复使用的工具集合。Skills 把「做事的方法」本身变成了可管理、可复制、可交易的生产资料。'),
            ('核心逻辑：卡片化', '性格可以记录，行为可以分析，风格可以迁移，偏好可以被理解。这些原本只存在于人脑中的「隐性经验」，通过 Skills 工程化后变成了可被 Agent 调用和执行的「动态加载卡片」。经验从此可以被打包、复制、分发。'),
            ('与 Prompt 的本质区别', 'Prompt 是一次性的指令，Skills 是持久化的能力。Prompt 告诉 Agent「怎么回答这个问题」，Skills 让 Agent「具备解决这类问题的能力」。从 Prompt Engineering 到 Skills Engineering，是从「临时指导」到「能力固化」的质变。'),
            ('Skills 是经验的动态加载', 'Skills 之于 Agent，如同 App 之于手机。一个 Skills 就是一张「经验卡」——需要时加载，不需要时卸载。Agent 本身不需要具备所有能力，通过 Skills 的灵活组合，随时变成「行业专家」或「特定场景高手」。'),
        ],
    },
    {
        'type': 'section',
        'title': '03  复制者 Skills',
        'tag': '五大蒸馏维度',
        'cards': [
            ('自我蒸馏与元工具', '数字人生：把个人数字痕迹提炼为数字分身；Forge Skill：自我镜像与他人蒸馏的独立流程；反蒸馏 Skill：公有技能与私有经验的拆分管理。这是 Skills 工程的基础层，也是 OPC 的个人基础设施。'),
            ('职场与学术关系', '同事.skill：离职补偿计算的标准化；老板.skill：管理风格与评审预期的精准匹配；导师.skill：指导风格的结构化传承。Skills 让组织知识不再随人员流动而流失。'),
            ('亲密关系与家庭记忆', 'MamaSkill：亲人陪伴型数字助手；兄弟.skill：捕捉说话风格与互动模式；Reunion Skill：已故亲友的数字遗物纪念。Skills 让情感记忆有了可持续承载的形态。'),
            ('公众人物与方法论', '马斯克.skill：第一性原理与产品判断框架；毛选.skill：矛盾分析与战略决策模型；巴菲特思维系统：价值投资的完整操作系统。方法论从此可以被「调用」，而不只是「阅读」。'),
            ('精神性与专门化', '金刚经.skill：佛学讲解与修行指导框架；赛博算命：四柱排盘的数字化；堪舆子：风水顾问的传统智慧工程化。专业垂直领域的知识蒸馏，正在创造全新的 AI 服务形态。'),
        ],
    },
    {
        'type': 'section',
        'title': '04  工程化思维',
        'tag': '从 Prompt 到 Context Engineering',
        'cards': [
            ('Prompt Engineering 的局限', 'Prompt Engineering 是 Context Engineering 的起点——但只是起点。好的 Prompt 能让模型回答正确，但无法让模型记住上下文、保持连续性、积累组织知识。Prompt 是「一次性的对话技巧」，不是「持久的能力建设」。'),
            ('Context 的本质', 'Context 是 Agent 的「工作记忆」。它决定了 Agent 在当前任务中能看到什么、知道什么、能调用什么。Context 质量差，Agent 的判断就差；Context 质量高，Agent 的能力才能真正释放。Context 是 AI 系统的「内存」，而非「硬盘」。'),
            ('构建精准 Context 的核心', '如何构建、筛选和喂给 Agent 最精准的上下文，是 Context Engineering 的核心命题。包括：知识库的结构化程度、检索的准确率、上下文的组织方式、噪声信息的过滤机制。这是一套系统化的工程能力。'),
            ('Context 决定 Agent 上限', '基座模型决定 Agent 的能力天花板，Context Engineering 决定 Agent 能否触碰到这个天花板。一个顶级模型配上一个糟糕的 Context，返回的结果远不如一个普通模型配合精准的 Context 设计。Context 是 AI 落地的最后一道关卡。'),
            ('工程实践的三个关键', '一，知识入库前的清洗与结构化；二、检索召回阶段的准确率优化；三、Context 组装阶段的上下文压缩与排序。三个环节缺一，Context Engineering 就无法真正发挥作用。这是下一个 AI 工程化的主战场。'),
        ],
    },
    {
        'type': 'section',
        'title': '04  工程化思维',
        'tag': 'Harness Engineering：规范化的约束力量',
        'cards': [
            ('Harness 的定义', 'Harness 是对复杂现象的「规范化解释与控制」——在 Agent 的能力与边界之间，建立一套清晰、可控、可预测的运行规则。Harness 不是限制 Agent 的能力，而是确保能力在正确的方向上被使用。'),
            ('为什么 Agent 必须有 Harness', 'Agent 越自主，风险越需要被管控。当 Agent 可以调用 API、发送邮件、执行代码时，一个错误的判断可能导致真实的业务损失。Harness 就是 Agent 的「安全气囊」——平时感知不到，出事时能兜底。'),
            ('工程化的紧箍咒', '通过工程化手段为 Agent 戴上「紧箍咒」：输出内容的安全审核、工具调用的权限分级、异常情况的熔断机制、决策路径的可追溯日志。Harness Engineering 的目标，是让 Agent 的每一步操作都可审计、可回滚、可解释。'),
            ('输出的确定性保障', '企业需要的不是「随机发挥的优秀」，而是「稳定可控的可靠」。Harness Engineering 通过结构化的约束体系，将 Agent 的输出从「概率分布」拉向「确定区间」。这是企业级 AI 应用的核心门槛。'),
            ('安全与能力的平衡', "Harness 的设计本质上是「在安全与能力之间找平衡」。约束太少，风险失控；约束太多，Agent 失去自主价值。优秀的 Harness Engineering 是让 Agent 感觉不到约束的存在，却始终在正确的轨道上运行。"),
        ],
    },
    {
        'type': 'section',
        'title': '05  未来启示',
        'tag': 'OPC：一个人就是一家公司',
        'cards': [
            ('OPC 的核心定义', 'OPC（One Personal Company）：当 Agent 承载执行，Skill 承载经验，个人生产力将发生质变。一个人可以运营过去需要一个团队才能支撑的业务体量。不是「个人品牌」，是「个人系统」。'),
            ('Agent 集群的协同逻辑', '多个专用 Agent 组成集群——一个处理咨询、一个执行操作、一个维护记忆、一个做质量把控。它们像一支军队一样协同工作，而你站在指挥官的位置做最终决策。这是「单兵」到「集群」的又一次范式跃迁。'),
            ('经验的资产化', 'Skills 把经验变成可复制的资产。一次解决问题的过程，可以被固化成一张 Skill 卡，被其他 Agent 调用。这意味着：专家的价值不再被困在他的时间里，而是可以被无限复制和分发。'),
            ('个人生产力的临界点', '当 Agent 可以承担80%的执行工作，Skill 覆盖了90%的专业知识，剩余10%需要人来做的就是「判断、创意、关系」。普通人的生产力边界正在被 AI 大规模向外推。拥有 Agent 集群的人，和单枪匹马用 AI 辅助的人，在产出上将出现数量级的差距。'),
            ('通往 OPC 的路径', '第一步：用 Agent 处理重复性脑力工作；第二步：用 Skills 固化和积累个人经验资产；第三步：建立 Agent 协同网络；第四步：成为真正意义的个人生产系统。OPC 不是终态，是每个小行动积累的结果。'),
        ],
    },
    {
        'type': 'section',
        'title': '05  未来启示',
        'tag': '人是 Agent 与现实之间的桥梁',
        'cards': [
            ('人的不可替代性', 'AI 在特定任务上已经超越人类，但人的价值在于「连接」：连接 AI 与真实需求，连接 Agent 与具体场景，连接 Skill 与人的情感。AI 是发动机，人是方向盘——没有人的判断，Agent 只会跑得更快，但方向未必正确。'),
            ('敢于多用，清楚边界', '敢于多用：用最好的 AI，感受最新能力，让 AI 成为你的默认工作伴侣。清楚边界：明确 AI 的能力极限在哪里，知道什么时候该用 AI，什么时候必须人来做最终决策。两者结合，才是 AI 时代最合理的生存策略。'),
            ('最终决策者的角色', 'AI 擅长处理「有正确答案的问题」，人负责定义「什么是有价值的问题」。当 Agent 能够不知疲倦地执行，人才能真正从执行中抽身，把精力集中在判断与创意上。这是人机协同最健康的形态。'),
            ('金句', '「AI 不会替代你，但会用 Agent 的人会替代你。」拥有 Agent 集群的人，和单枪匹马用 AI 辅助的人，在产出上将出现数量级的差距。这不是技术问题，是战略认知问题。'),
            ('行动纲领', '今天开始，用 Agent 处理一件你一直在自己做的工作；本周内，把这项工作固化成一张 Skill；下个月，建立你的第一个双 Agent 协同节点。OPC 不是终态，是每个小行动积累的结果。路就在脚下，从哪一步开始都不晚。'),
        ],
    },
    {
        'type': 'end',
        'title': 'AGENT 实战',
        'subtitle': '从单兵作战到数字员工集群',
        'edition': 'PRESENTED BY 李琛 | 2026 EDITION',
    },
]

def build():
    html_parts = []
    html_parts.append('''<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent实战：从单兵作战到数字员工集群</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
body { background:#000; display:flex; justify-content:center; align-items:center; min-height:100vh; }
.slide { width:1280px; min-height:720px; background:#FFD700; color:#000; display:none; flex-direction:column; position:relative; overflow:hidden; }
.slide.active { display:flex; }
.cover-wrap, .end-wrap { display:flex; flex-direction:column; height:100%; }
.cover-header, .end-header { height:90px; border-bottom:5px solid #000; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.cover-header h1, .end-header h1 { font-family:'Montserrat',sans-serif; font-weight:900; font-size:26px; letter-spacing:0.2em; text-transform:uppercase; color:#000; }
.cover-body, .end-body { flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:40px 80px; border:7px solid #000; margin:28px 44px; }
.cover-main, .end-main-title { font-family:'Montserrat',sans-serif; font-weight:900; font-size:58px; text-transform:uppercase; color:#000; text-align:center; line-height:1.15; }
.red { color:#FF0000; }
.cover-edition, .end-edition { font-family:'Inter',sans-serif; font-size:20px; color:#000; margin-top:24px; text-align:center; }
.cover-sub-edition, .end-sub { font-family:'Montserrat',sans-serif; font-weight:700; font-size:13px; letter-spacing:0.15em; text-transform:uppercase; color:#000; margin-top:16px; border-top:3px solid #000; padding-top:16px; }
.cover-footer, .end-footer { height:52px; border-top:5px solid #000; display:flex; align-items:center; justify-content:flex-end; padding:0 48px; flex-shrink:0; }
.footer-page { font-family:'Montserrat',sans-serif; font-weight:900; font-size:18px; color:#FF0000; }
.slide-header { height:90px; border-bottom:5px solid #000; display:flex; align-items:center; justify-content:center; flex-shrink:0; }
.slide-header h2 { font-family:'Montserrat',sans-serif; font-weight:900; font-size:24px; letter-spacing:0.15em; text-transform:uppercase; color:#000; }
.ov-grid { display:grid; grid-template-columns:repeat(2, 1fr); gap:20px; padding:36px 52px; flex:1; }
.ov-item { border:4px solid #000; padding:22px 26px; display:flex; flex-direction:column; gap:8px; }
.ov-num { font-family:'Montserrat',sans-serif; font-weight:900; font-size:52px; color:#FF0000; line-height:1; }
.ov-title { font-family:'Montserrat',sans-serif; font-weight:900; font-size:20px; text-transform:uppercase; letter-spacing:0.04em; color:#000; }
.ov-desc { font-family:'Inter',sans-serif; font-size:16px; color:#000; line-height:1.5; margin-top:4px; }
.section-wrap { flex:1; display:flex; flex-direction:column; }
.section-body { display:flex; flex-direction:column; padding:14px 52px 12px; flex:1; }
.tag-badge { display:inline-block; border:3px solid #FF0000; padding:5px 16px; font-family:'Montserrat',sans-serif; font-weight:900; font-size:12px; text-transform:uppercase; letter-spacing:0.1em; color:#FF0000; align-self:flex-start; margin-bottom:10px; }
.cards { display:flex; flex-direction:column; gap:8px; flex:1; }
.card { border:3px solid #000; padding:12px 18px; display:flex; flex-direction:column; gap:5px; }
.card-title { font-family:'Montserrat',sans-serif; font-weight:900; font-size:15px; text-transform:uppercase; letter-spacing:0.04em; color:#000; text-align:left; }
.card-title::before { content:'\\25b6 '; color:#FF0000; font-size:11px; }
.card-body { font-family:'Inter',sans-serif; font-size:15.5px; line-height:1.72; color:#000; text-align:left; }
.slide-footer { height:52px; border-top:5px solid #000; display:flex; align-items:center; justify-content:space-between; padding:0 48px; flex-shrink:0; margin-top:auto; }
.footer-title { font-family:'Montserrat',sans-serif; font-weight:700; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; color:#000; }
.nav { position:fixed; bottom:20px; left:50%; transform:translateX(-50%); display:flex; gap:12px; z-index:100; }
.nav button { background:#000; color:#FFD700; border:none; padding:10px 28px; font-family:'Montserrat',sans-serif; font-weight:900; font-size:13px; cursor:pointer; letter-spacing:0.1em; }
.dots { position:fixed; bottom:20px; right:40px; display:flex; gap:8px; align-items:center; z-index:100; }
.dot { width:12px; height:12px; background:#FFD700; border:2px solid #000; cursor:pointer; }
.dot.active { background:#FF0000; border-color:#FF0000; }
</style>
</head>
<body>
''')

    page = 1
    total = len(SLIDES)

    for slide in SLIDES:
        t = slide['type']
        if t == 'cover':
            html_parts.append('<div class="slide active" id="s{}">'.format(page))
            html_parts.append('<div class="cover-wrap">')
            html_parts.append('<div class="cover-header"><h1>AGENT 实战</h1></div>')
            html_parts.append('<div class="cover-body">')
            html_parts.append('<div class="cover-main">从 <span class="red">单兵作战</span><br>到 数字员工集群</div>')
            html_parts.append('<div class="cover-edition">{}</div>'.format(slide['subtitle']))
            html_parts.append('<div class="cover-sub-edition">{}</div>'.format(slide['edition']))
            html_parts.append('</div>')
            html_parts.append('<div class="cover-footer">')
            html_parts.append('<div class="footer-page">{} / {}</div>'.format(page, total))
            html_parts.append('</div></div></div>')

        elif t == 'overview':
            html_parts.append('<div class="slide" id="s{}">'.format(page))
            html_parts.append('<div class="slide-header"><h2>{}</h2></div>'.format(slide['title']))
            html_parts.append('<div class="ov-grid">')
            for num, title, desc in slide['items']:
                html_parts.append('<div class="ov-item">')
                html_parts.append('<div class="ov-num">{}</div>'.format(num))
                html_parts.append('<div class="ov-title">{}</div>'.format(title))
                html_parts.append('<div class="ov-desc">{}</div>'.format(desc))
                html_parts.append('</div>')
            html_parts.append('</div>')
            html_parts.append('<div class="slide-footer">')
            html_parts.append('<div class="footer-title">AGENT 实战</div>')
            html_parts.append('<div class="footer-page">{} / {}</div>'.format(page, total))
            html_parts.append('</div></div>')

        elif t == 'section':
            html_parts.append('<div class="slide" id="s{}">'.format(page))
            html_parts.append('<div class="slide-header"><h2>{}</h2></div>'.format(slide['title']))
            html_parts.append('<div class="section-wrap">')
            html_parts.append('<div style="padding:14px 52px 0;"><span class="tag-badge">{}</span></div>'.format(slide['tag']))
            html_parts.append('<div class="section-body">')
            html_parts.append('<div class="cards">')
            for ct, cb in slide['cards']:
                html_parts.append('<div class="card">')
                html_parts.append('<div class="card-title">{}</div>'.format(ct))
                html_parts.append('<div class="card-body">{}</div>'.format(cb))
                html_parts.append('</div>')
            html_parts.append('</div></div></div>')
            html_parts.append('<div class="slide-footer">')
            html_parts.append('<div class="footer-title">AGENT 实战</div>')
            html_parts.append('<div class="footer-page">{} / {}</div>'.format(page, total))
            html_parts.append('</div></div>')

        elif t == 'end':
            html_parts.append('<div class="slide" id="s{}">'.format(page))
            html_parts.append('<div class="end-wrap">')
            html_parts.append('<div class="end-header"><h1>AGENT 实战</h1></div>')
            html_parts.append('<div class="end-body">')
            html_parts.append('<div class="cover-main">从 <span class="red">单兵作战</span><br>到 数字员工集群</div>')
            html_parts.append('<div class="end-sub">{}</div>'.format(slide['subtitle']))
            html_parts.append('<div class="cover-sub-edition">{}</div>'.format(slide['edition']))
            html_parts.append('</div>')
            html_parts.append('<div class="end-footer">')
            html_parts.append('<div class="footer-page">{} / {}</div>'.format(page, total))
            html_parts.append('</div></div></div>')

        page += 1

    html_parts.append('<div class="nav"><button onclick="prev()">◀ PREV</button><button onclick="next()">NEXT ▶</button></div>')
    html_parts.append('<div class="dots" id="dots"></div>')
    html_parts.append('''<script>
var cur = 0;
var slides = document.querySelectorAll('.slide');
var total = slides.length;
function show(i){slides.forEach(function(s){s.classList.remove('active');});slides[i].classList.add('active');renderDots(i);}
function next(){cur=(cur+1)%total;show(cur);}
function prev(){cur=(cur-1+total)%total;show(cur);}
function renderDots(idx){
  var c=document.getElementById('dots');c.innerHTML='';
  for(var i=0;i<total;i++){
    var d=document.createElement('div');
    d.className='dot'+(i===idx?' active':'');
    d.onclick=(function(i){return function(){cur=i;show(i);};})(i);
    c.appendChild(d);
  }
}
document.addEventListener('keydown',function(e){
  if(e.key==='ArrowRight'||e.key===' ')next();
  if(e.key==='ArrowLeft')prev();
});
renderDots(0);
</script></body></html>''')

    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
    print('Done: {} ({} slides)'.format(OUTPUT, total))

build()
