#!/usr/bin/env python3
"""Generate the static gallery site (index.html) from data.json."""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
items = json.load(open(os.path.join(BASE, 'data.json')))

def card(it):
    src = (f'<a class="src" href="{it["src"]}" target="_blank" rel="noopener">原作者页 ↗</a>'
           if it['src'] else '<span class="src mine-tag">本站定制</span>')
    dl = f'<a class="dl" href="{it["file"]}" download>下载 PNG</a>'
    return f'''<div class="card" data-model="{it["model"]}" data-mine="{1 if it["mine"] else 0}">
  <img loading="lazy" src="{it["thumb"]}" alt="{it["title"]}">
  <div class="info">
    <div class="title">{it["title"]}</div>
    <div class="meta"><span class="badge">{it["model"]}</span><span class="author">{it["author"]}</span></div>
    <div class="row">{dl}{src}</div>
  </div>
</div>'''

mine_cards = '\n'.join(card(i) for i in items if i['mine'])
comm_cards = '\n'.join(card(i) for i in items if not i['mine'])

mine_section = f'''<section>
<h2>⭐ 本站定制 <span class="n">壁纸移植真人物 · 剪纸白边 · 无文字</span></h2>
<p class="desc">按官方 Base / Premium 模板逐像素校验，两种配置各取所需。</p>
<div class="grid">{mine_cards}</div>
</section>''' if mine_cards else ''
mine_filter = '<button data-f="mine">本站定制</button>' if mine_cards else ''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>特斯拉数字车衣 · 皮肤收藏馆</title>
<style>
:root{{--bg:#0e0f13;--card:#17181d;--line:#26272e;--txt:#e8e9ec;--dim:#9a9ba3;--red:#e82127;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--txt);font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;padding:0 0 60px}}
header{{max-width:1100px;margin:0 auto;padding:44px 20px 10px}}
h1{{font-size:30px;letter-spacing:1px}}
.sub{{color:var(--dim);margin-top:8px;font-size:14px;line-height:1.7}}
.filters{{max-width:1100px;margin:18px auto 0;padding:0 20px;display:flex;gap:10px;flex-wrap:wrap}}
.filters button{{background:var(--card);border:1px solid var(--line);color:var(--txt);border-radius:20px;padding:8px 18px;font-size:14px;cursor:pointer}}
.filters button.on{{background:var(--red);border-color:var(--red);color:#fff}}
section{{max-width:1100px;margin:34px auto 0;padding:0 20px}}
h2{{font-size:20px;margin-bottom:4px}}
h2 .n{{color:var(--dim);font-size:13px;font-weight:normal;margin-left:8px}}
.desc{{color:var(--dim);font-size:13px;margin-bottom:16px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;transition:transform .15s}}
.card:hover{{transform:translateY(-3px)}}
.card img{{width:100%;aspect-ratio:1;display:block;background:#26262b}}
.card.hide{{display:none}}
.info{{padding:14px}}
.title{{font-size:15px;font-weight:600;margin-bottom:8px}}
.meta{{display:flex;align-items:center;gap:8px;margin-bottom:12px;flex-wrap:wrap}}
.badge{{font-size:11px;background:#23242b;border:1px solid var(--line);border-radius:6px;padding:3px 8px;color:#c9cad1}}
.author{{font-size:12px;color:var(--dim)}}
.row{{display:flex;gap:10px;align-items:center}}
.dl{{flex:1;text-align:center;background:var(--red);color:#fff;text-decoration:none;border-radius:8px;padding:9px 0;font-size:14px;font-weight:600}}
.dl:hover{{filter:brightness(1.1)}}
.src{{font-size:12px;color:var(--dim);text-decoration:none}}
.src:hover{{color:var(--txt);text-decoration:underline}}
.mine-tag{{font-size:12px;color:#7ee2a8}}
.guide{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;line-height:2;font-size:14px;color:#c9cad1}}
.guide b{{color:var(--txt)}}
.guide code{{background:#23242b;padding:2px 8px;border-radius:6px;font-size:13px}}
footer{{max-width:1100px;margin:40px auto 0;padding:0 20px;color:var(--dim);font-size:12px;line-height:2}}
footer a{{color:var(--dim)}}
</style>
</head>
<body>
<header>
<h1>🚗 特斯拉数字车衣 · 皮肤收藏馆</h1>
<p class="sub">精选网络免费车衣皮肤，均为 1024×1024 PNG（&lt;1MB），可直接用于特斯拉 Toybox → Paint Shop。<br>点击「下载 PNG」保存，然后按下方教程装到车上。</p>
</header>
<div class="filters" id="filters">
<button class="on" data-f="all">全部</button>
<button data-f="new">Model Y (2025+)</button>
<button data-f="old">老款 Model Y</button>
{mine_filter}
</div>
{mine_section}
<section>
<h2>🌐 社区精选 <span class="n">来自 tesla-wrap.com 免费画廊</span></h2>
<p class="desc">设计版权归原作者所有，仅供个人学习交流；点击「原作者页」查看出处。</p>
<div class="grid">{comm_cards}</div>
</section>
<section>
<h2>📥 安装教程</h2>
<div class="guide">
<b>1.</b> 下载喜欢的 PNG（1024×1024，&lt;1MB 均已符合要求）<br>
<b>2.</b> U 盘格式化为 <code>exFAT</code> / <code>FAT32</code>，根目录新建文件夹 <code>Wraps</code>（大小写敏感），把 PNG 放进去<br>
<b>3.</b> 车机系统升级到支持 Paint Shop 的版本，插入 U 盘<br>
<b>4.</b> 车机进入 <b>Toybox 玩具箱 → Paint Shop → Wraps</b> 标签页，选择皮肤应用<br>
<b>5.</b> 注意按车型选对模板：<code>Model Y (2025+)</code> 为新款（Juniper），<code>Model Y</code> / <code>Model Y L</code> 为老款
</div>
</section>
<footer>
皮肤来源：<a href="https://www.tesla-wrap.com" target="_blank" rel="noopener">tesla-wrap.com</a> 社区免费画廊（已标注原作者） · 模板：特斯拉官方 GitHub 车衣模板<br>
本站仅做收藏整理，不拥有第三方设计版权；如原作者有异议请联系删除。个人使用请遵守相关 IP 规定。
</footer>
<script>
const btns=[...document.querySelectorAll('#filters button')];
const cards=[...document.querySelectorAll('.card')];
function matchFilter(f,m){{
  if(f==='all')return true;
  if(f==='mine')return false;
  if(f==='new')return m.indexOf('2025+')!==-1;
  if(f==='old')return m.indexOf('Model Y')!==-1&&m.indexOf('2025+')===-1;
  return true;
}}
btns.forEach(b=>b.addEventListener('click',()=>{{
  btns.forEach(x=>x.classList.remove('on'));b.classList.add('on');
  const f=b.dataset.f;
  cards.forEach(c=>{{
    const show = f==='mine' ? c.dataset.mine==='1' : matchFilter(f,c.dataset.model);
    c.classList.toggle('hide',!show);
  }});
}}));
</script>
</body>
</html>'''

open(os.path.join(BASE, 'index.html'), 'w').write(html)
print('index.html written,', len(items), 'items')
