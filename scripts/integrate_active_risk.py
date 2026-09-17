from pathlib import Path
import re

ROOT = Path('/home/ubuntu/hyrox-shanghai-proposal')
SOURCE = Path('/home/ubuntu/upload/HYROX-法兰克福连接风险与策略切换-动态演示-合作标识更新.html')
DEMO = ROOT / 'active-risk-demo.html'
INDEX = ROOT / 'index.html'


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


# Build a permanent, standalone copy of the user-provided simulator and add an embed mode.
demo = SOURCE.read_text(encoding='utf-8')
demo = demo.replace('<!doctype html>', '<!DOCTYPE html>', 1)
demo = re.sub(r'<button(?![^>]*\\btype=)', '<button type="button"', demo)
demo = demo.replace('<aside class="side">', '<aside class="side" aria-label="策略判定与参数控制">', 1)
demo = demo.replace('</div><nav><a href="#demo">', '</div><nav aria-label="演示页面导航"><a href="#demo">', 1)
demo = demo.replace('<p style="padding:20px">', '<p class="noscript-note">')
embed_css = '''
.noscript-note{padding:20px}
body.embed{background:transparent;padding:0}
body.embed .top,body.embed .intro,body.embed .explain,body.embed .boundaries,body.embed .refs{display:none}
body.embed .console,body.embed .lower{width:100%;max-width:none}
body.embed .console{border-radius:14px;margin:0}
body.embed .lower{margin-top:14px}
body.embed main{padding:0}
@media(max-width:570px){body.embed .console{border-radius:10px}}
'''
demo = replace_once(demo, '</style>', embed_css + '</style>', 'demo CSS insertion')
demo = replace_once(
    demo,
    "'use strict';",
    "'use strict';\nif(new URLSearchParams(location.search).get('embed')==='1'||location.hash==='#embed')document.body.classList.add('embed');",
    'embed mode script',
)
DEMO.write_text(demo, encoding='utf-8')

index = INDEX.read_text(encoding='utf-8')

index = replace_once(
    index,
    '上海站概念方案 V1 · 调研校核稿',
    '上海站概念方案 V2 · 主动风险检查增强版',
    'version badge',
)
index = replace_once(
    index,
    '<li><a href="#topology">动态拓扑</a></li><li><a href="#strategy">应用策略</a></li>',
    '<li><a href="#topology">动态拓扑</a></li><li><a href="#active-risk">主动检查</a></li><li><a href="#strategy">应用策略</a></li>',
    'navigation',
)

# Add styles for the historical boundary and embedded proactive-risk module.
style_anchor = '.diagnostic-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:49px}'
style_insert = '''.history-boundary{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:34px}.history-card{padding:22px;border-radius:17px;border:1px solid #d8d5cb;background:#fff}.history-card strong{display:block;font-size:13px;color:var(--blue)}.history-card p{margin:8px 0 0;color:#616a6d;font-size:12px}.history-card.shanghai{background:#101415;border-color:#31424f;color:#fff}.history-card.shanghai strong{color:var(--yellow)}.history-card.shanghai p{color:#b7c0c3}.risk-section{background:linear-gradient(180deg,#0b0f12,#10161b);overflow:hidden}.risk-head{display:grid;grid-template-columns:1.08fr .92fr;gap:50px;align-items:end}.risk-summary{margin:0;color:#aeb9bf;font-size:14px}.risk-pillars{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:34px}.risk-pillar{padding:18px;border:1px solid rgba(255,255,255,.12);border-radius:15px;background:#141b20}.risk-pillar b{display:block;color:var(--yellow);font-size:11px}.risk-pillar span{display:block;margin-top:7px;color:#9eabb2;font-size:10px}.risk-demo-shell{margin-top:28px;padding:10px;border:1px solid rgba(105,185,240,.28);border-radius:20px;background:#080c0f;box-shadow:0 24px 70px rgba(0,0,0,.28)}.risk-frame{display:block;width:100%;min-height:1080px;border:0;border-radius:13px;background:#090c0e}.risk-actions{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:16px;color:#84939b;font-size:10px}.risk-link{display:inline-flex;align-items:center;justify-content:center;min-height:40px;padding:0 15px;border-radius:999px;border:1px solid rgba(246,215,25,.45);color:var(--yellow);text-decoration:none;font-weight:900}.risk-link:hover{background:var(--yellow);color:#080808}.risk-note{margin-top:18px;padding:18px 20px;border-left:4px solid var(--orange);background:rgba(255,157,40,.08);color:#d8c5aa;font-size:12px}.risk-note strong{color:#ffbd6b}'''
index = replace_once(index, style_anchor, style_insert + style_anchor, 'risk styles')

index = replace_once(
    index,
    '.insight-head,.topology-wrap,.replicate-grid,.aisino-grid,.cta-grid,.reference-grid{grid-template-columns:1fr}',
    '.insight-head,.topology-wrap,.replicate-grid,.aisino-grid,.cta-grid,.reference-grid,.risk-head{grid-template-columns:1fr}.risk-pillars{grid-template-columns:repeat(3,1fr)}',
    'tablet layout',
)
index = replace_once(
    index,
    '.fact-grid,.diagnostic-grid,.policy-grid,.solution-grid,.case-grid,.cap-grid,.acceptance{grid-template-columns:1fr}',
    '.fact-grid,.diagnostic-grid,.policy-grid,.solution-grid,.case-grid,.cap-grid,.acceptance,.history-boundary,.risk-pillars{grid-template-columns:1fr}.risk-frame{min-height:1880px}.risk-actions{align-items:flex-start;flex-direction:column}',
    'mobile layout',
)

insight_anchor = '<div class="fact-grid reveal">'
history_block = '''<div class="history-boundary reveal"><article class="history-card"><strong>北京站 · 已知事实</strong><p>北京站未安排直播，采用专线技术方案，赛事期间未发生故障。该结果证明专线方案可作为可靠方法参考，但不应被描述为发生过直播或链路故障。</p></article><article class="history-card shanghai"><strong>上海站 · 规划假设</strong><p>上海站先按“有直播”设计和规划，预留独立制作网络、国内多运营商上行、最低带宽、主备推流与真实码流监测；平台、时长和码率仍需制作方确认。</p></article></div>'''
index = replace_once(index, insight_anchor, history_block + insight_anchor, 'history boundary cards')

index = replace_once(
    index,
    '人员、注册工位、直播、终端并发、链路和临电仍需在业务基线、现场勘察和端到端联调中确认。',
    '人员、注册工位、终端并发、链路和临电仍需在业务基线、现场勘察和端到端联调中确认；直播按上海规划假设先行纳入设计。',
    'insight scope',
)
index = replace_once(
    index,
    '以下是上海站必须验证的业务风险模型，不代表问题已经发生。点击卡片可跳转至动态拓扑，查看对应设计场景。',
    '以下是上海站必须验证的业务风险模型，不代表北京站或上海站已经发生问题。北京站无直播、采用专线且未发生故障；上海站则先按有直播规划。点击卡片可跳转至动态拓扑，查看对应设计场景。',
    'diagnostic intro',
)
index = replace_once(
    index,
    '<strong>上海边界：</strong>北京访谈中的运动员规模、注册台数量、直播平台与时长、工作人员数量均不构成上海容量依据。上海最终设计必须通过业务清单、场馆资源核查、空场与搭建后 RF 测试、真实 API 探测、推流压测和端到端联调验证。',
    '<strong>北京事实与上海边界：</strong>北京站未安排直播，采用专线技术且未发生故障；北京站人员、注册台和工作人员规模仍不构成上海容量依据。上海先按有直播设计，最终平台、时长、码率、主备推流及上行容量必须通过业务清单、资源核查、真实推流压测和端到端联调冻结。',
    'diagnostic boundary',
)

index = replace_once(
    index,
    '切换八种设计场景，查看海外业务协同、国内直播出口、备份路径、锐捷承载与网络健康运营平台如何协同判断和恢复。',
    '切换八种设计场景，查看法兰克福业务协同、上海直播出口、备份路径、锐捷承载与网络健康运营平台如何协同判断和恢复；后续主动检查模块将进一步演示连续探测与策略切换。',
    'topology intro',
)
index = replace_once(index, '>海外赛事系统</text>', '>法兰克福业务服务</text>', 'overseas node title')
index = replace_once(index, '>Sports Pro / 国际协同 · 待确认</text>', '>Sports Pro / 指定业务 API · 待确认</text>', 'overseas node subtitle')
index = replace_once(index, '>合规跨境连接</text>', '>专线 / 合规主路径</text>', 'primary path node')
index = replace_once(index, '<span>合规跨境连接</span>', '<span>专线 / 合规主路径</span>', 'primary path status')
index = replace_once(
    index,
    '<div class="policy-step"><span>3</span><div>连续越过阈值后自动切换，降低抖动</div></div><div class="policy-step"><span>4</span><div>统一记录发现、定位、处置和恢复过程</div></div>',
    '<div class="policy-step"><span>3</span><div>连续越阈且备路通过连通、业务与容量准入后切换</div></div><div class="policy-step"><span>4</span><div>切换后继续验证新路径业务，并完整记录恢复过程</div></div>',
    'topology policy steps',
)

active_risk_section = '''
<section class="section risk-section" id="active-risk"><div class="container"><div class="eyebrow">Proactive risk inspection · Shanghai to Frankfurt</div><div class="risk-head"><div><h2 class="heading">不等用户报障，<br>让主动探测与策略切换<span class="yellow">提前介入</span></h2></div><p class="risk-summary">探测机分别绑定主路 P、备用 A 与备用 B，持续验证 TCP / TLS、链路质量及获授权的只读业务结果。只有持续异常成立、候选备路连续健康且容量合格时，才允许新连接切换；切换后继续复核业务，不把“路由下发”误当成“业务恢复”。</p></div><div class="risk-pillars reveal"><div class="risk-pillar"><b>01 · 主动探测</b><span>主路与空闲备路同步检查，不等终端用户报障。</span></div><div class="risk-pillar"><b>02 · 连续确认</b><span>单轮波动不切换，连续越阈后才进入评估。</span></div><div class="risk-pillar"><b>03 · 备路准入</b><span>连通、业务结果与承载余量三项同时合格。</span></div><div class="risk-pillar"><b>04 · 防抖与回切</b><span>设置冷却与更长恢复窗口，默认恢复不抢占。</span></div><div class="risk-pillar"><b>05 · 共同异常冻结</b><span>三路同时业务异常或探针失联时告警，不盲切。</span></div></div><div class="risk-note reveal"><strong>重要说明：</strong>下方全部指标与时序均为交互模拟，不访问德国服务器、不扫描端口、不修改真实网络。示例阈值包括 RTT 450 ms、抖动 40 ms、丢包 2%、HTTPS P95 800 ms、业务成功率 98% 和备路负载 75%；正式值必须依据上海现场基线、业务容忍度、设备能力与系统方授权重新校准。</div><div class="risk-demo-shell reveal"><iframe class="risk-frame" id="riskDemoFrame" src="active-risk-demo.html#embed" title="HYROX 上海站法兰克福连接主动风险检查与策略切换交互演示" loading="lazy"></iframe></div><div class="risk-actions"><span>网页内为核心控制台；完整独立页同时保留方案逻辑、实施边界、技术参考和日志导出。</span><a class="risk-link" href="active-risk-demo.html" target="_blank" rel="noopener">打开完整主动风险检查演示</a></div></div></section>
'''
index = replace_once(index, '<section class="section paper" id="strategy">', active_risk_section + '<section class="section paper" id="strategy">', 'active risk section')

index = replace_once(
    index,
    '<h3>多平台直播</h3><p>直播使用有线优先与独立策略，避免媒体、办公和普通终端挤占上行。</p>',
    '<h3>多平台直播（上海规划假设）</h3><p>北京站未安排直播；上海先按有直播规划，使用有线优先与独立策略，避免媒体、办公和普通终端挤占上行。</p>',
    'streaming policy card',
)
index = replace_once(
    index,
    '<h3>冗余与自动恢复</h3><p>核心、出口和关键链路消除单点；预设阈值、故障脚本和自动切换。</p>',
    '<h3>冗余与主动恢复</h3><p>核心、出口和关键链路消除单点；以持续探测、连续阈值、备路准入、切换冷却和业务复核驱动恢复。</p>',
    'layer 5',
)
index = replace_once(
    index,
    '<h3>业务探针</h3><p>定义 Sports Pro API、大屏、推流和注册业务的监测方式。</p>',
    '<h3>业务探针</h3><p>定义 Sports Pro / 法兰克福业务 API、大屏、推流和注册的主动探测、授权边界与数据留痕。</p>',
    'delivery probes',
)
index = replace_once(
    index,
    '<h3>压测与演练</h3><p>按节目单验证持续推流、并发上传、注册高峰、路径故障和无线高密。</p>',
    '<h3>压测与演练</h3><p>按节目单验证持续推流、并发上传、注册高峰、三路退化、容量不足、共同异常和无线高密。</p>',
    'delivery exercises',
)
index = replace_once(
    index,
    '<div class="footer-title">众安保险 HYROX 上海站网络保障合作企划 · 上海站概念方案 V1</div>',
    '<div class="footer-title">众安保险 HYROX 上海站网络保障合作企划 · 上海站概念方案 V2</div>',
    'footer version',
)

# Add same-origin iframe height synchronization without affecting standalone behavior.
script_anchor = "const topbar=document.getElementById('topbar');"
iframe_script = "const riskFrame=document.getElementById('riskDemoFrame');function fitRiskFrame(){if(!riskFrame)return;try{const d=riskFrame.contentDocument;if(!d)return;const h=Math.max(d.body?.scrollHeight||0,d.documentElement?.scrollHeight||0);if(h)riskFrame.style.height=Math.max(900,h+4)+'px'}catch(e){}}if(riskFrame){riskFrame.addEventListener('load',()=>{fitRiskFrame();try{new ResizeObserver(fitRiskFrame).observe(riskFrame.contentDocument.body)}catch(e){}});window.addEventListener('resize',fitRiskFrame);}\n"
index = replace_once(index, script_anchor, iframe_script + script_anchor, 'iframe script')

INDEX.write_text(index, encoding='utf-8')
print(f'Wrote {DEMO}')
print(f'Updated {INDEX}')
