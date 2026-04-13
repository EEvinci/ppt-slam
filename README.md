# ppt-slam · 极简高对比度演示文稿

> 高对比度黄黑红配色，讲座级视觉冲击力。适合：路演 / 演讲 / 课程 / 观点输出。

---

## 视觉系统

### 配色方案
| 用途 | 色值 | 说明 |
|------|------|------|
| 背景 | `#FFD700` | 明黄，现场级冲击力 |
| 主文字/边框 | `#000000` | 纯黑，最高对比度 |
| 强调色 | `#FF0000` | 正红，重点/数字/标题前缀 |

### 字体规范
| 用途 | 字体 | 字重 | 字号 |
|------|------|------|------|
| 标题 | Montserrat | 900 | 52-96px |
| 副标题 | Inter | 400 | 20-24px |
| 正文 | Inter | 400/700 | 15-17px |
| 标签徽章 | Montserrat | 900 | 12-14px |

---

## 布局规范

### 封面（Double Border）
- 外层 7px 粗黑边框 + 内层细边框
- 主标题大号 Montserrat 900，顶部对齐
- 底部信息：PRESENTED BY / 日期 / 版本

### 目录页（2x2 / 2x3 网格）
- 2 列网格布局
- 大号红色数字（ Montserrat 900，52px+）作为视觉锚点
- 序号 → 标题 → 描述，三层结构

### 内容页
- 顶部 90px 页眉，底部 5px 黑色分割线
- 红色虚线标签徽章（tag-badge）作章节标注
- 5 个卡片纵向排列，每卡片：3px 黑色边框 + ▶ 红色前缀
- 正文 Inter，15-17px，行高 1.7

### 结尾页
- 与封面呼应，简洁有力
- 纯白底黑字黑框，金句收尾

---

## 翻页交互
- 键盘：左右箭头 / 空格键
- 触摸：左右滑动
- 右下角：圆点可点击跳转
- 底部：页码 `x / N`

---

## 安装使用

```bash
# 克隆仓库
git clone https://github.com/EEvinci/ppt-slam.git
cd ppt-slam

# 编辑内容（SLIDES 列表）
vim build.py

# 生成 HTML
python3 build.py

# 浏览器打开
open index.html

# 部署（使用 deploy 工具）
deploy /path/to/ppt-slam
```

---

## 快速上手

在 `build.py` 的 `SLIDES` 列表中添加页面：

```python
{
    'type': 'cover',
    'title': '你的标题',
    'subtitle': '副标题',
    'edition': 'PRESENTED BY 姓名 | 日期',
},
{
    'type': 'overview',
    'title': '目录标题',
    'items': [
        ('01', '章节名', '描述'),
        ('02', '章节名', '描述'),
    ],
},
{
    'type': 'section',
    'title': '01  章节标题',
    'tag': '章节标签',
    'cards': [
        ('卡片标题', '卡片正文内容，5-7句话，含具体案例。'),
        ('卡片标题', '卡片正文内容。'),
    ],
},
{
    'type': 'end',
    'title': '标题',
    'subtitle': '副标题',
    'edition': 'PRESENTED BY 姓名',
},
```

---

## CSS 核心片段

```css
/* 容器 */
.slide {
    width: 1280px;
    min-height: 720px;
    background: #FFD700;
    color: #000;
    display: flex;
    flex-direction: column;
}

/* 卡片 */
.card {
    border: 3px solid #000;
    padding: 12px 18px;
}
.card-title {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 15px;
    text-transform: uppercase;
}
.card-title::before {
    content: '▶ ';
    color: #FF0000;
}

/* 标签徽章 */
.tag-badge {
    border: 3px solid #FF0000;
    color: #FF0000;
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 5px 16px;
}
```

---

## 铁律

- ❌ CSS 中禁止使用 Python `%` 格式化（会导致 `%%`，页面全白）
- ✅ CSS 用纯字符串 + 拼接
- ❌ 首屏不用 JS 加 active，直接写 `class="s active"`
- ❌ 不要圆角、阴影、渐变——回归信息本质

---

## 目录结构

```
ppt-slam/
├── build.py          # 生成脚本
├── index.html        # 输出文件
├── README.md        # 本文件
└── assets/          # 资源目录（如有）
```
