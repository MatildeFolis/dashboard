import os,re,html
os.makedirs('final',exist_ok=True); tot=0
keep={'&amp;','&lt;','&gt;','&quot;','&nbsp;'}
for f in sorted(os.listdir('new')):
    h=open('new/'+f).read()
    h=re.sub(r' data-(start|end)="\d+"','',h)
    h=re.sub(r'&#?\w+;',lambda m: m.group(0) if m.group(0) in keep else html.unescape(m.group(0)),h)
    open('final/'+f,'w').write(h); tot+=len(h)
print(tot, tot//len(os.listdir('new')))
