from pathlib import Path
import re,html,shutil
out=Path(__file__).resolve().parent
root=out.parents[1]; source=root/'projects/dealer-portal/案例.md'
template=root.parent/'portfolio website/case-study'
# template.css is a saved style source; preview can rebuild without the sibling website.
def inline(t):return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',html.escape(t))
def figure(line,hero=False):
 fields=line.strip('［］').split('｜');_,_,path,purpose,caption,alt,fit,boundary=fields
 src=source.parent/path; dest=out/'media'/src.name;dest.parent.mkdir(exist_ok=True);shutil.copy2(src,dest)
 return f'<figure class="review-figure {"hero-figure" if hero else ""}"><button class="image-open" aria-label="放大圖片：{html.escape(alt)}"><img src="media/{dest.name}" alt="{html.escape(alt)}" loading="{"eager" if hero else "lazy"}"></button><figcaption>{inline(caption)} <span>點圖放大</span></figcaption><details><summary>素材核對事項</summary><p>{inline(boundary)}</p></details></figure>'
chunks=re.split(r'^## ',source.read_text(),flags=re.M)[1:]; rendered=[];nav=[]
for i,ch in enumerate(chunks,1):
 heading,body=ch.split('\n',1);nav.append(f'<a href="#section-{i}">{html.escape(heading.split("｜")[-1])}</a>')
 lines=[l for l in body.strip().splitlines() if l.strip()]
 if i==1:
  title=next(l[4:] for l in lines if l.startswith('### '))
  rendered.append(f'<header id="section-1" class="case-header article-width"><div class="header-copy"><p class="eyebrow">DEALER PORTAL / 中文審閱稿</p><h1 class="type-display">E-Bike Service Tool</h1><p class="type-subtitle">{title}</p></div><span class="glass status-badge"><span class="status-dot"></span>2025 年 3 月上線</span></header><div class="hero-width">'+figure(next(l for l in lines if l.startswith('［Media')),True)+'</div><article class="article-body">');continue
 content=[];inlist=False
 for l in lines:
  if inlist and not l.startswith('- '):content.append('</ul>');inlist=False
  if l.startswith('［Media'):content.append(figure(l))
  elif l.startswith('### '):content.append(f'<h3>{inline(l[4:])}</h3>')
  elif l.startswith('#### '):content.append(f'<h4>{inline(l[5:])}</h4>')
  elif l.startswith('- '):
   if not inlist:content.append('<ul class="review-list">');inlist=True
   content.append('<li>'+inline(l[2:])+'</li>')
  else:content.append('<p>'+inline(l)+'</p>')
 if inlist:content.append('</ul>')
 rendered.append(f'<section id="section-{i}" class="article-width article-section"><p class="eyebrow">{html.escape(heading)}</p>'+''.join(content)+'</section>')
page='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dealer Portal｜中文圖文審閱</title><link rel="stylesheet" href="template.css"><link rel="stylesheet" href="preview.css"><body><div class="case-shell"><div class="review-bar"><span>中文圖文審閱 · 未定稿</span><button id="theme" aria-pressed="false">切換深色</button></div><main class="case-scroll"><nav aria-label="章節導覽">'''+''.join(nav)+'''</nav>'''+''.join(rendered)+'''</article><footer class="case-footer article-width"><p>內容來源：中文案例稿 · 沿用既有 case-study 版型 · 僅供本機審閱</p><a href="#section-1">回到頂部 ↑</a></footer></main></div><dialog id="lightbox" aria-label="圖片放大檢視"><button id="close-image" autofocus>關閉 ✕</button><img alt=""><p></p></dialog><script src="preview.js"></script></body></html>'''
(out/'index.html').write_text(page)
print('Built',out/'index.html')
