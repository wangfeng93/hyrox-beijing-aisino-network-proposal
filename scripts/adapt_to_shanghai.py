from pathlib import Path

ROOT = Path('/home/ubuntu/hyrox-shanghai-proposal')
path = ROOT / 'index.html'
text = path.read_text(encoding='utf-8')


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'Expected exactly one occurrence, found {count}: {old[:120]}')
    text = text.replace(old, new, 1)


# Document metadata and Shanghai visual identity.
replace_once(
    '<meta name="description" content="航天信息基于 HYROX 客户访谈形成的北京赛事网络保障合作企划审阅版。" />',
    '<meta name="description" content="航天信息面向众安保险 HYROX 上海站形成的赛事网络业务可用性保障合作企划。" />'
)
replace_once(
    '<title>HYROX 北京赛事 × 航天信息｜访谈后网络方案 V2</title>',
    '<title>众安保险 HYROX 上海站 × 航天信息｜赛事网络保障方案</title>'
)
replace_once('url("assets/beijing-oval.jpg") center/cover no-repeat', 'url("assets/shanghai/hyrox-shanghai-official.jpg") 58% center/cover no-repeat')
replace_once(
    '<li><a href="#insights">访谈洞察</a></li>',
    '<li><a href="#insights">上海基线</a></li>'
)

# Hero.
old_hero = '<section class="hero"><div class="hero-bg"></div><div class="hero-grid"></div><div class="container"><div class="hero-content"><div class="hero-badge"><span class="live-dot"></span> 访谈后方案 V2 · 内部审阅稿</div><h1>BEIJING<span class="outline">BUSINESS READY</span><span class="cn">HYROX 北京赛事网络保障合作企划</span></h1><p class="hero-copy">以锐捷为主要网络产品体系，由航天信息把“网页能打开、IP 能连通”的网络保障，升级为对 Sports Pro、注册、大屏、直播、媒体上传和赛事运营的<strong>业务可用性保障</strong>。</p><div class="hero-actions"><a class="pill-btn primary" href="#topology">体验访谈后动态拓扑</a><a class="pill-btn" href="#insights">查看关键认知</a></div></div><div class="event-strip"><div class="event-cell"><span>Event</span><strong>Ulike HYROX Beijing</strong></div><div class="event-cell"><span>Date</span><strong>2026.09.10 — 09.13</strong></div><div class="event-cell"><span>Venue</span><strong>北京冰丝带（国家速滑馆）</strong></div><div class="event-cell"><span>Positioning</span><strong>从网络可达，走向业务可用</strong></div></div></div><div class="hero-credit">场馆图片来源：<a href="https://populous.com/showcases/national-speed-skating-oval" target="_blank" rel="noopener">Populous</a></div></section>'
new_hero = '<section class="hero"><div class="hero-bg"></div><div class="hero-grid"></div><div class="container"><div class="hero-content"><div class="hero-badge"><span class="live-dot"></span> 上海站概念方案 V1 · 调研校核稿</div><h1>SHANGHAI<span class="outline">BUSINESS READY</span><span class="cn">众安保险 HYROX 上海站网络保障合作企划</span></h1><p class="hero-copy">以锐捷为主要网络产品体系，由航天信息围绕上海世博展览馆 3 号馆，把“网络可达”升级为对注册、计时、大屏、直播、媒体交付和赛事运营的<strong>业务可用性保障</strong>。</p><div class="hero-actions"><a class="pill-btn primary" href="#topology">体验上海站动态拓扑</a><a class="pill-btn" href="#insights">查看上海设计基线</a></div></div><div class="event-strip"><div class="event-cell"><span>Event</span><strong>ZhongAn HYROX Shanghai</strong></div><div class="event-cell"><span>Date</span><strong>2026.10.31 — 11.01</strong></div><div class="event-cell"><span>Venue</span><strong>上海世博展览馆 3 号馆</strong></div><div class="event-cell"><span>Positioning</span><strong>先验证资源，再承诺业务可用</strong></div></div></div><div class="hero-credit">赛事图片来源：<a href="https://hyrox.com/event/hyrox-shanghai-1031/" target="_blank" rel="noopener">HYROX 官方上海站页面</a></div></section>'
replace_once(old_hero, new_hero)

# Shanghai-specific baseline facts.
old_insights = '<section class="section paper" id="insights"><div class="container"><div class="insight-head reveal"><blockquote class="insight-quote">访谈之后，问题定义更清晰：真正的风险不是“偶尔网慢”，而是关键业务出问题时，<em>无法快速判断故障发生在哪一段。</em></blockquote><div class="insight-side"><span class="pill confirmed">今日访谈信息</span><p>客户已明确业务现象、运行规模和核心风险。以下数据用于方案方向判断，最终仍需在需求基线、北京冰丝带现网勘察和业务联调中确认。</p><p><strong>设计原则：</strong>现象可以确认，根因必须验证；网络健康必须和真实业务 API、推流与大屏刷新状态一起判断。</p></div></div><div class="fact-grid reveal"><article class="fact"><strong>FRA</strong><h3>海外业务系统</h3><p>Sports Pro、注册与总部系统位于德国法兰克福。</p><span class="source">访谈口径 · 待基线确认</span></article><article class="fact"><strong>≈4K</strong><h3>运动员 / 日</h3><p>北京站预计每日约 4,000 名运动员。</p><span class="source">访谈口径 · 待基线确认</span></article><article class="fact"><strong>14–16</strong><h3>注册台位</h3><p>iPad 扫码并绑定芯片，全天连续运行。</p><span class="source">访谈口径 · 待基线确认</span></article><article class="fact"><strong>10+</strong><h3>国内直播平台</h3><p>多平台并行，断流后恢复成本高。</p><span class="source">访谈口径 · 待基线确认</span></article><article class="fact"><strong>12–14H</strong><h3>单日连续直播</h3><p>北京站可能连续运行四天。</p><span class="source">访谈口径 · 待基线确认</span></article><article class="fact"><strong>2–3K</strong><h3>工作人员</h3><p>叠加手机、赛事设备与临时设施。</p><span class="source">访谈口径 · 待基线确认</span></article></div></div></section>'
new_insights = '<section class="section paper" id="insights"><div class="container"><div class="insight-head reveal"><blockquote class="insight-quote">上海版第一原则：先确认业务、场馆和运营商资源，再把服务能力写入基线；<em>北京经验只复用方法，不复用数字。</em></blockquote><div class="insight-side"><span class="pill confirmed">网上调研 + 用户材料</span><p>赛事日期、地点和 3 号馆公开工程条件已经核验。人员、注册工位、直播、终端并发、链路和临电仍需在业务基线、现场勘察和端到端联调中确认。</p><p><strong>设计原则：</strong>注册、计时和大屏优先形成境内本地闭环；网络健康必须和真实 API、推流、成绩同步与大屏刷新状态一起判断。</p></div></div><div class="fact-grid reveal"><article class="fact"><strong>10/31</strong><h3>两日正赛启动</h3><p>2026.10.31—11.01，最终运行窗口以联合排期为准。</p><span class="source">HYROX 官方赛事页</span></article><article class="fact"><strong>H3</strong><h3>3 号馆</h3><p>上海世博展览馆，南门地址为国展路 1099 号。</p><span class="source">赛事与场馆官网</span></article><article class="fact"><strong>17K</strong><h3>平方米展厅</h3><p>会展空间；赛道与功能分区以最终图纸为准。</p><span class="source">场馆官网技术页</span></article><article class="fact"><strong>9M</strong><h3>公开净高</h3><p>9 根柱、18 米柱距，搭建后需再次进行 RF 复测。</p><span class="source">场馆官网技术页</span></article><article class="fact"><strong>8×1K</strong><h3>HYROX 标准赛制</h3><p>8 段 1 公里跑与 8 个功能训练站交替完成。</p><span class="source">HYROX 官方赛制</span></article><article class="fact"><strong>TBC</strong><h3>规模与流量模型</h3><p>人员、台位、直播、终端和峰值并发均待书面确认。</p><span class="source">上海站专项基线</span></article></div></div></section>'
replace_once(old_insights, new_insights)

# Risk model introduction.
replace_once('六类业务风险，<br>不把<span class="yellow">推测写成结论</span>', '六类关键风险，<br>不把<span class="yellow">北京数字写成上海结论</span>')
replace_once('每张卡片区分“已确认现象”和“待验证根因”。点击卡片可跳转至动态拓扑，查看对应场景。', '以下是上海站必须验证的业务风险模型，不代表问题已经发生。点击卡片可跳转至动态拓扑，查看对应设计场景。')

cards = [
(
'<article class="diag-card" data-scenario="api" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 海外业务</span><span class="diag-index">01</span></div><h3>Sports Pro / 注册 / 总部系统访问不稳</h3><p class="symptom">普通网页正常时，真实业务仍可能出现请求失败，总部团队无法稳定获取运动员数据。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>运营中断、数据不可见、临时寻找其他网络。</p></div><div class="diag-box pending-box"><b>待验证根因</b><p>VPN / 跨境路径质量、API 响应或其他端到端环节。</p></div></div><div class="diag-action">合规跨境专线 + 多路径备份 + 真实 API 持续探测 + 自动择优。</div></article>',
'<article class="diag-card" data-scenario="api" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 国际协同</span><span class="diag-index">01</span></div><h3>Sports Pro 与海外协同边界尚未冻结</h3><p class="symptom">系统部署地域、接口、性能阈值和离线能力仍待系统方书面确认；普通网页可达不能代表真实业务可用。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>注册、成绩同步或总部协同在关键时刻不可用。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>接口依赖、合规路径、端到端响应、本地缓存与补传机制。</p></div></div><div class="diag-action">境内关键业务闭环 + 合规跨境服务 + 真实 API 探测 + 可演练的降级流程。</div></article>'
),
(
'<article class="diag-card" data-scenario="screen" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 现场大屏</span><span class="diag-index">02</span></div><h3>芯片已采集，但赛场大屏未刷新</h3><p class="symptom">后台已经出现记录，现场显示却不同步；问题可能发生在采集、链路、接口或应用任一段。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>损害运动员、观众体验与赛事专业形象。</p></div><div class="diag-box pending-box"><b>待验证根因</b><p>最大问题不是已有根因，而是当前无法定位故障段。</p></div></div><div class="diag-action">把“芯片→后台→API→大屏”作为完整业务链分段监控并设置 P0 告警。</div></article>',
'<article class="diag-card" data-scenario="screen" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 计时与大屏</span><span class="diag-index">02</span></div><h3>成绩采集到现场显示需要分段可观测</h3><p class="symptom">计时系统、后台、接口和大屏来自不同责任方，任何一段异常都可能表现为“屏幕不刷新”。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>成绩展示延迟，影响运动员、观众体验与赛事专业形象。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>接口、刷新机制、离线显示、补传对账和各方责任边界。</p></div></div><div class="diag-action">把“采集→后台→API→大屏”作为完整业务链监控，并验证断网降级。</div></article>'
),
(
'<article class="diag-card" data-scenario="live" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 长时直播</span><span class="diag-index">03</span></div><h3>十多个平台的直播卡顿与断流风险</h3><p class="symptom">单日可能连续直播 12–14 小时，北京站可能连续四天；断流会触发多个直播间重建。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>线上观众体验、品牌曝光和舆情风险同步放大。</p></div><div class="diag-box pending-box"><b>待验证根因</b><p>出口抖动、上行竞争、无线质量或非关键流量抢占。</p></div></div><div class="diag-action">有线优先、直播独立策略、最低上行保障、多运营商出口与推流质量监测。</div></article>',
'<article class="diag-card" data-scenario="live" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 直播制作</span><span class="diag-index">03</span></div><h3>直播平台、时长和码率尚待制作方确认</h3><p class="symptom">只有冻结节目单、平台清单、主备推流和目标码率，才能计算真实上行与冗余能力。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>推流卡顿或中断会同时影响线上体验、品牌曝光和内容交付。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>场馆上行、物理路由、制作网络、CDN 边界与国际媒体需求。</p></div></div><div class="diag-action">有线主用、异运营商备份、直播独立策略、最低上行保障与真实推流监测。</div></article>'
),
(
'<article class="diag-card" data-scenario="media" tabindex="0"><div class="diag-top"><span class="pill confirmed">P1 · 媒体生产</span><span class="diag-index">04</span></div><h3>多团队上传图片 / 视频时占满网络</h3><p class="symptom">即使接入网线，一个团队的大文件上传仍可能影响其他媒体人员正常工作。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>素材不能及时交付，公共资源被少数大流量终端占用。</p></div><div class="diag-box pending-box"><b>当前判断</b><p>并非只有带宽问题，更可能缺少应用级调度与并发控制。</p></div></div><div class="diag-action">媒体独立识别、每终端 / 应用上限、最低保障和生产上传与办公隔离。</div></article>',
'<article class="diag-card" data-scenario="media" tabindex="0"><div class="diag-top"><span class="pill pending">P1 · 媒体生产</span><span class="diag-index">04</span></div><h3>大文件并发上传可能挤占关键上行</h3><p class="symptom">媒体工位、交付时限和素材规模尚未冻结；公共出口若缺少调度，突发上传会影响其他业务。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>素材不能及时交付，直播、办公或其他团队的可用带宽下降。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>媒体数量、并发模型、平台目的地、现场存储和交付窗口。</p></div></div><div class="diag-action">媒体生产独立分区、每终端 / 应用上限、最低保障和本地暂存。</div></article>'
),
(
'<article class="diag-card" data-scenario="checkin" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 运动员注册</span><span class="diag-index">05</span></div><h3>14–16 个注册台对连续连接高度敏感</h3><p class="symptom">单台流量不大，但连接一旦中断，全部注册台会同时停滞并迅速形成现场聚集。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>注册效率下降、排队扩大、运动员体验受损。</p></div><div class="diag-box pending-box"><b>当前判断</b><p>核心要求是 API 响应和会话连续性，不是单纯追求大带宽。</p></div></div><div class="diag-action">注册独立 SSID / VLAN、高优先级与最低保障、跨境冗余、真实扫码绑定监测。</div></article>',
'<article class="diag-card" data-scenario="checkin" tabindex="0"><div class="diag-top"><span class="pill p0">P0 · 运动员注册</span><span class="diag-index">05</span></div><h3>注册工位数量未定，连续性指标不能缺位</h3><p class="symptom">注册工位、扫码绑定流程和终端清单仍待确认；单台流量不大，但集中中断会迅速形成现场排队。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>注册效率下降、排队扩大，进而影响分组与现场运行节奏。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>接口响应、会话连续、本地缓存、离线登记和恢复后补传。</p></div></div><div class="diag-action">注册独立 SSID / VLAN、高优先级、最低保障与真实扫码绑定演练。</div></article>'
),
(
'<article class="diag-card" data-scenario="wifi" tabindex="0"><div class="diag-top"><span class="pill confirmed">P1 · 高密无线</span><span class="diag-index">06</span></div><h3>空场正常，不代表赛事高峰稳定</h3><p class="symptom">2,000–3,000 名工作人员、手机、赛事设备和临时设施叠加，直播区域还可能受到建筑遮挡。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>高峰信号下降、抖动、漫游失败，移动终端体验失控。</p></div><div class="diag-box pending-box"><b>待验证根因</b><p>同频干扰、反射、遮挡、密度及 AP 位置需要 RF 实测。</p></div></div><div class="diag-action">每站重新 RF 勘测，以位置、方向、功率、信道和必要的吊装 / 立杆解决问题。</div></article>',
'<article class="diag-card" data-scenario="wifi" tabindex="0"><div class="diag-top"><span class="pill pending">P1 · 高密无线</span><span class="diag-index">06</span></div><h3>17,000 平方米会展空间会在搭建后改变 RF 环境</h3><p class="symptom">9 根立柱、临时构筑物、人群与金属设备会改变覆盖、反射和干扰；空场结果不能代表赛事高峰。</p><div class="diag-flow"><div class="diag-box"><b>业务影响</b><p>高峰信号下降、重传增加、漫游失败，移动终端体验失控。</p></div><div class="diag-box pending-box"><b>待验证事项</b><p>观众密度、频谱、AP 位置、安装审批、信道复用与蜂窝应急能力。</p></div></div><div class="diag-action">执行空场勘察、搭建后复测和高峰压测，再冻结 AP 数量、位置、功率与信道。</div></article>'
)
]
for old, new in cards:
    replace_once(old, new)

replace_once(
    '<strong>根因边界：</strong>无线干扰、AP 部署、线路质量、出口拥塞、单点故障和流量管理都属于当前假设。北京最终设计前，需要通过频谱测试、真实业务 API 探测、长时推流、抓包和端到端监控验证。',
    '<strong>上海边界：</strong>北京访谈中的运动员规模、注册台数量、直播平台与时长、工作人员数量均不构成上海容量依据。上海最终设计必须通过业务清单、场馆资源核查、空场与搭建后 RF 测试、真实 API 探测、推流压测和端到端联调验证。'
)

# Topology wording and data labels.
replace_once('切换八种访谈场景，查看法兰克福业务路径、国内直播出口、双旁路、锐捷承载与网络健康运营平台如何协同判断和恢复。', '切换八种设计场景，查看海外业务协同、国内直播出口、备份路径、锐捷承载与网络健康运营平台如何协同判断和恢复。')
replace_once('HYROX 北京赛事网络健康架构 · 逻辑演示', 'HYROX 上海赛事网络健康架构 · 逻辑演示')
replace_once('<text class="node-title" x="180" y="66">德国法兰克福</text><text class="node-sub" x="180" y="89">Sports Pro / 注册 / 总部系统</text>', '<text class="node-title" x="180" y="66">海外赛事系统</text><text class="node-sub" x="180" y="89">Sports Pro / 国际协同 · 待确认</text>')
replace_once('<text class="node-sub" x="1030" y="89">十多个平台 · 长时上行</text>', '<text class="node-sub" x="1030" y="89">平台 / 码率 / 时长 · 待确认</text>')
replace_once('<text class="node-title" x="250" y="232">合规跨境专线</text><text class="node-sub" x="250" y="253">主用 / 持续质量探测</text>', '<text class="node-title" x="250" y="232">合规跨境连接</text><text class="node-sub" x="250" y="253">设计主用 / 待资源核查</text>')
replace_once('<text class="node-title" x="430" y="232">旁路软件路由 A</text><text class="node-sub" x="430" y="253">备份路径 01</text>', '<text class="node-title" x="430" y="232">备份路径 A</text><text class="node-sub" x="430" y="253">异故障域 / 待资源核查</text>')
replace_once('<text class="node-title" x="680" y="232">旁路软件路由 B</text><text class="node-sub" x="680" y="253">备份路径 02</text>', '<text class="node-title" x="680" y="232">备份路径 B</text><text class="node-sub" x="680" y="253">异故障域 / 待资源核查</text>')
replace_once('<text class="node-sub" x="150" y="682">14–16 台 · API 连续性</text>', '<text class="node-sub" x="150" y="682">工位 / 并发 · 待确认</text>')
replace_once('<text class="node-sub" x="695" y="700">12–14 小时 / 日</text>', '<text class="node-sub" x="695" y="700">平台 / 时长 · 待确认</text>')
replace_once('<span>跨境专线</span><b>当前优选</b>', '<span>合规跨境连接</span><b>设计主用</b>')
replace_once('<span>旁路路由 A</span><b>热备</b>', '<span>备份路径 A</span><b>设计热备</b>')
replace_once('<span>旁路路由 B</span><b>热备</b>', '<span>备份路径 B</span><b>设计热备</b>')
replace_once('<span>国内多运营商</span><b>当前优选</b>', '<span>国内多运营商</span><b>设计主用</b>')
old_normal_text = '跨境专线与国内多运营商出口满足策略阈值；Sports Pro API、推流和大屏业务链同步处于可用状态。'
new_normal_text = '设计链路满足策略阈值；Sports Pro 接口、推流、注册和大屏业务链同步处于可用状态。'
if text.count(old_normal_text) != 2:
    raise RuntimeError(f'Expected two normal-state descriptions, found {text.count(old_normal_text)}')
text = text.replace(old_normal_text, new_normal_text)
replace_once('动画用于说明访谈后方案逻辑，不代表北京站已实测参数。路径、阈值和动作需在现场勘察与真实业务联调后确认。', '动画用于说明上海站设计逻辑，不代表现场已部署或实测。路径、阈值和动作需在 3 号馆勘察、运营商资源核查与真实业务联调后确认。')

# Strategy and six-layer system.
replace_once('以下策略方向需在北京需求基线中与各业务负责人确认。', '以下策略方向需在上海站需求基线中与各业务负责人确认。')
replace_once('<h3>Sports Pro / 注册后台</h3><p>重点保障法兰克福 API 的连续响应，而不是只验证普通网页可达。</p>', '<h3>Sports Pro / 国际协同</h3><p>在系统部署地域与接口确认后，保障真实业务连续响应，而不是只验证普通网页可达。</p>')
replace_once('<div><b>路径</b><span>跨境专线优选，多路径备份</span></div>', '<div><b>路径</b><span>合规连接优选，异故障域备份</span></div>')
replace_once('每站重新频谱与覆盖勘测；关键终端、AP 回传和大屏采用专业抗干扰有线链路。', '围绕 3 号馆执行空场勘察、搭建后复测和高峰压测；关键终端、AP 回传与大屏采用有线优先。')
replace_once('合规跨境专线、不同运营商国内出口与两组旁路软件路由协同。', '合规跨境服务、异运营商有线出口与经实测的应急路径协同，并核验真实故障域。')
replace_once('按注册、大屏、直播、媒体、办公和商业制定路由、QoS、最低保障与上限。', '按注册、计时、大屏、直播、媒体、办公、POS / IoT 与观众接入制定隔离、路由和 QoS。')
replace_once('具体型号和数量在冰丝带勘察、RF 实测及需求基线确认后确定。', '具体型号和数量在 3 号馆受控图纸、双轮 RF 实测、终端清单及运营商资源确认后确定。')

# Standardization, delivery, venue facts and CTA.
replace_once('从北京一站，沉淀<span class="yellow">中国区赛事网络标准</span>', '从上海一站，验证并迭代<span class="yellow">中国区赛事网络标准</span>')
replace_once('北京站验证后的能力沉淀为可复制项目资产。', '上海站验证后的能力进入可复制项目资产，并以每站复测结果持续更新。')
replace_once('<p>验证线路、机房、光纤、供电、频谱、遮挡和安装条件。</p>', '<p>核验光纤、弱电间、货梯转运、临电、供电、频谱、遮挡、吊点与安装审批。</p>')
replace_once('<h3>四日赛时保障</h3><p>作战室监控、告警分级、自动动作、备件与专家升级。</p>', '<h3>两日赛时保障</h3><p>按联合排期组织作战室监控、告警分级、备件、专家升级与夜间窗口。</p>')

old_reference = '<section class="section paper" id="reference"><div class="container"><div class="eyebrow">Reference sample · Shenzhen</div><h2 class="heading">深圳资料仍只做参考，<br>北京参数必须<span class="blue">重新勘察与验证</span></h2><p class="lead">深圳图纸可帮助识别同类赛事的业务类型和点位复杂度，但北京站参数必须以冰丝带现场及访谈后业务基线为准。</p><div class="reference-grid reveal"><figure class="reference-image"><span class="reference-label">深圳参考 · 非北京最终点位</span><img id="shenzhenImage" src="assets/shenzhen-reference-layout.webp" alt="HYROX 深圳赛事布局参考图" /></figure><div class="reference-panel"><div class="ref-stat"><strong>28</strong><span>深圳图纸需求单元，仅作复杂度参考</span></div><div class="ref-stat"><strong>350M</strong><span>深圳图纸标注带宽静态加总</span></div><div class="ref-stat"><strong>21</strong><span>深圳参考样本中的仅无线单元</span></div><div class="ref-stat"><strong>15</strong><span>运动站与赞助商分散无线点位</span></div><div class="ref-warning"><strong>重要边界：</strong>以上数字不是北京站设备清单，也不能直接等同于北京出口规格。最终容量还必须叠加海外 API、直播平台、长时上行、媒体并发和 2,000–3,000 名工作人员等真实业务条件。</div></div></div></div></section>'
new_reference = '<section class="section paper" id="reference"><div class="container"><div class="eyebrow">Venue facts · Hall 3</div><h2 class="heading">公开条件用于立项，<br>工程参数必须<span class="blue">现场确认</span></h2><p class="lead">3 号馆是二层会展空间。公开资料可帮助识别柱网、净高、承重和转运约束，但网络、供电、吊点与最终搭建仍须以当期受控图纸、订单、审批和现场复核为准。</p><div class="reference-grid reveal"><figure class="reference-image"><span class="reference-label">上海世博展览馆 · 环境示意</span><img id="venueImage" src="assets/shanghai/sweecc-exterior.webp" alt="上海世博展览馆外部环境示意" /></figure><div class="reference-panel"><div class="ref-stat"><strong>17K㎡</strong><span>3 号馆公开面积；功能分区待最终图纸确认</span></div><div class="ref-stat"><strong>9M</strong><span>官网公开净高；最大搭建高度标为暂定</span></div><div class="ref-stat"><strong>9 / 18M</strong><span>9 根柱、18 米柱距；影响覆盖与布线路由</span></div><div class="ref-stat"><strong>8</strong><span>4 部 5 吨及 4 部 3 吨货梯；无直接货物入口</span></div><div class="ref-warning"><strong>重要边界：</strong>场馆仅公开“电话 / 网络可申请”和供电制式，未公开确认赛事日带宽、Wi-Fi 覆盖、光纤路由、双路由、SLA 或可用电量。所有工程承诺须在资源核查、正式订单和联合测试后冻结。</div></div></div></div></section>'
replace_once(old_reference, new_reference)

old_cta = '<section class="cta"><div class="container cta-grid"><div><div class="eyebrow" style="color:#090909">Next step</div><h2>从“北京冰丝带”业务链与 RF 联合勘察开始。</h2></div><div><p>建议 HYROX、航天信息、冰丝带场馆、运营商、Sports Pro、计时 / 大屏及直播团队共同完成现场勘察和真实业务联调。会后由航天信息提交详细设计、锐捷产品物料、探针清单、测试用例与四日赛时 Runbook。</p></div></div></section>'
new_cta = '<section class="cta"><div class="container cta-grid"><div><div class="eyebrow" style="color:#090909">Next step</div><h2>从“上海世博展览馆 3 号馆”的业务清单、资源核查与双轮 RF 勘察开始。</h2></div><div><p>建议 HYROX、航天信息、场馆、运营商、Sports Pro、计时 / 大屏及制作团队共同完成现场勘察和真实业务联调。会后由航天信息提交详细设计、锐捷产品物料、业务探针清单、测试用例及按联合排期编制的两日赛时 Runbook。</p></div></div></section>'
replace_once(old_cta, new_cta)

old_footer = '<footer><div class="container footer-grid"><div><div class="footer-title">HYROX 北京赛事网络保障合作企划 · 访谈后 V2 审阅版</div><div>方案策划与制作：航天信息（Aisino）</div><div>主要网络产品体系：锐捷网络（Ruijie Networks）</div><div>© 2026 航天信息。用于 HYROX 北京赛事网络合作沟通。</div></div><div class="sources"><a href="https://hyrox.com/event/hyrox-beijing-0912/" target="_blank">HYROX 北京官方赛事页</a><a href="https://populous.com/showcases/national-speed-skating-oval" target="_blank">场馆图片来源</a><a href="https://www.ruijie.com.cn/" target="_blank">锐捷官网</a></div></div></footer>'
new_footer = '<footer><div class="container footer-grid"><div><div class="footer-title">众安保险 HYROX 上海站网络保障合作企划 · 上海站概念方案 V1</div><div>方案策划与制作：航天信息（Aisino）</div><div>主要网络产品体系：锐捷网络（Ruijie Networks）</div><div>© 2026 航天信息。用于 HYROX 上海赛事网络合作沟通。</div></div><div class="sources"><a href="https://hyrox.com/event/hyrox-shanghai-1031/" target="_blank">HYROX 上海官方赛事页</a><a href="https://sweecc.dlg-expo.com/MouldV/ExhibitionHallInfo?WenMenuId=127" target="_blank">3 号馆官方技术数据</a><a href="https://sweecc.dlg-expo.com/MouldV/DownloadCenter?WenMenuId=132" target="_blank">场馆图纸下载</a><a href="https://www.ruijie.com.cn/" target="_blank">锐捷官网</a></div></div></footer>'
replace_once(old_footer, new_footer)

# Scenario copy and labels in JavaScript.
replace_once("title:'网页可访问，但 Sports Pro API 异常'", "title:'网页可访问，但 Sports Pro 接口异常'")
replace_once("text:'14–16 个注册台获得独立业务策略；跨境 API 响应、扫码绑定成功和会话连续性同步监测。'", "text:'注册业务获得独立策略；接口响应、扫码绑定、会话连续性和离线补传同步监测。'")
replace_once("title:'旁路 A 故障：旁路 B 可用'", "title:'备份路径 A 故障：路径 B 保持可用'")
replace_once("text:'旁路 A 退出承载并告警，旁路 B 保持可用，避免旁路软件路由成为新的单点故障。'", "text:'备份路径 A 退出承载并告警，路径 B 保持可用；正式方案需验证各路径的物理、汇聚和供电故障域。'")
replace_once("const labels={active:'当前优选',standby:'热备',degraded:'质量下降',failed:'故障'}", "const labels={active:'设计主用',standby:'设计热备',degraded:'质量下降',failed:'故障'}")
replace_once("document.getElementById('shenzhenImage').addEventListener('click',()=>openImage('assets/shenzhen-reference-layout.webp','HYROX 深圳赛事布局参考图'));", "document.getElementById('venueImage').addEventListener('click',()=>openImage('assets/shanghai/sweecc-exterior.webp','上海世博展览馆外部环境示意'));" )

# Remaining deterministic Shanghai substitutions.
replace_once('上海站可能连续运行四天', '赛事运行窗口以联合排期为准') if '上海站可能连续运行四天' in text else None

path.write_text(text, encoding='utf-8')
print(f'Updated {path} ({len(text)} characters)')
