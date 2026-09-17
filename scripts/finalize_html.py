from pathlib import Path
import re

path = Path('/home/ubuntu/hyrox-shanghai-proposal/index.html')
text = path.read_text(encoding='utf-8')

text = text.replace('<!doctype html>', '<!DOCTYPE html>')
text = re.sub(r'<meta([^>]*)\s*/>', r'<meta\1>', text)
text = re.sub(r'<img([^>]*)\s*/>', r'<img\1>', text)
text = text.replace('<button class=', '<button type="button" class=')

css_anchor = '.smallcaps{font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:950}'
css_replacement = css_anchor + '.accent-yellow{color:var(--yellow)}.accent-red{color:#ff646d}.status-heading{margin-top:8px!important}.flush-top{padding-top:0!important}.cta-eyebrow{color:#090909!important}'
if text.count(css_anchor) != 1:
    raise RuntimeError('CSS anchor missing or duplicated')
text = text.replace(css_anchor, css_replacement, 1)

replacements = {
    '<div class="smallcaps" style="color:var(--yellow)">Route & business state</div>': '<div class="smallcaps accent-yellow">Route &amp; business state</div>',
    '<h3 style="margin-top:8px">路径与业务状态</h3>': '<h3 class="status-heading">路径与业务状态</h3>',
    '<section class="section paper" id="solution" style="padding-top:0">': '<section class="section paper flush-top" id="solution">',
    '<div class="smallcaps" style="color:#ff646d">Primary product ecosystem</div>': '<div class="smallcaps accent-red">Primary product ecosystem</div>',
    '<section class="section dark2" id="proof" style="padding-top:0">': '<section class="section dark2 flush-top" id="proof">',
    '<div class="eyebrow" style="color:#090909">Next step</div>': '<div class="eyebrow cta-eyebrow">Next step</div>',
    'P0 · TIMING & DISPLAY': 'P0 · TIMING &amp; DISPLAY',
    'REDUNDANCY & QOS': 'REDUNDANCY &amp; QOS',
    'Delivery & assurance': 'Delivery &amp; assurance',
    '<button type="button" class="scenario-btn" data-scenario="routeFault">旁路 A 故障</button>': '<button type="button" class="scenario-btn" data-scenario="routeFault">备份路径 A 故障</button>',
    '需要同时观察数据采集、海外后台、接口调用和现场刷新。': '需要同时观察数据采集、业务后台、接口调用和现场刷新。',
    '<h3>压测与演练</h3><p>验证长时直播、并发上传、注册高峰、旁路故障和无线高密。</p>': '<h3>压测与演练</h3><p>按节目单验证持续推流、并发上传、注册高峰、路径故障和无线高密。</p>',
    '<b>海外 API 与注册</b>': '<b>国际协同与注册</b>',
    '<span>真实平台长时推流、上行保障、并发上传公平性</span>': '<span>按节目单推流、上行保障、并发上传公平性</span>',
    '查看原始网络结构图': '查看参考网络结构图（非上海定稿）',
    "'用户原始网络结构图'": "'参考网络结构图（非上海定稿）'"
}
for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'Expected one occurrence, found {count}: {old}')
    text = text.replace(old, new, 1)

# Internal identifier only; align it with visible Shanghai copy.
text = text.replace('frankfurt', 'overseas')

path.write_text(text, encoding='utf-8')
print(f'Finalized {path}')
