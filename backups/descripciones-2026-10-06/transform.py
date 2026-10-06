import os,re,json
names={}
for line in open('names.tsv'):
    i,n=line.rstrip('\n').split('\t',1); names[i]=n
DEMO='&#128073; Ver la invitaci&oacute;n en vivo'
ENT_OLD=re.compile(r'(se entrega en )4 a 7( d&iacute;as h&aacute;biles desde que recibimos toda la info completa\.)')
ENT_NEW=r'\g<1>4 a 5\g<2><br />Incluye <strong>3 rondas de cambios</strong> para que quede exactamente como la imagin&aacute;s.'
DUR=re.compile(r'Tu invitaci&oacute;n estar&aacute; online (?:hasta 15 d&iacute;as despu&eacute;s del evento \(o m&aacute;s, si lo necesit&aacute;s\)\.|hasta 1 a&ntilde;o despu&eacute;s del evento(?:&nbsp;|\.)|por un a&ntilde;o\.)')
DUR_NEW='Tu invitaci&oacute;n queda online durante <strong>1 a&ntilde;o</strong> despu&eacute;s del evento.'
POL='<hr />\n<h3>Pol&iacute;tica</h3>\n<p>Te pedimos que revises bien todo antes de confirmar tu compra.<br />No se realizan devoluciones una vez iniciado el proceso.</p>\n'
EXTRAS='<p>&#10024; Sumale <strong>Pases Individuales</strong> con el nombre de cada invitado o una <strong>Trivia</strong> sobre ustedes. Los encontr&aacute;s en <a href="https://tienda.invitarteonline.com.ar/extras/">Extras</a>.</p>\n'
os.makedirs('new',exist_ok=True); log={}
for f in sorted(os.listdir('orig')):
    pid=f[:-5]; h=o=open('orig/'+f).read(); ch=[]
    is_inv=bool(re.search(r'Invitaci[oó]n (P[aá]gina Web|Web|Digital Interactiva|Inteligente)',names[pid]))
    if 'invitac&oacute;n' in h: h=h.replace('invitac&oacute;n','invitaci&oacute;n'); ch.append('typo invitacón')
    if 'Galeria' in h: h=h.replace('Galeria','Galer&iacute;a'); ch.append('typo Galería')
    links=list(re.finditer(r'(<a [^>]*href="(https://invitarteonline\.com\.ar/[^"]*)"[^>]*>)(.*?)(</a>)',h,re.S))
    if len(links)==1:
        m=links[0]; h=h[:m.start()]+m.group(1)+DEMO+m.group(4)+h[m.end():]; ch.append('demo unificada')
    elif len(links)>1:
        for m in reversed(links):
            kind='Premium' if 'premium' in (m.group(2)+m.group(3)).lower() else 'Cl&aacute;sica'
            h=h[:m.start()]+m.group(1)+'&#128073; Ver demo '+kind+m.group(4)+h[m.end():]
        ch.append('demos Clásica/Premium diferenciadas')
    if is_inv and ENT_OLD.search(h): h=ENT_OLD.sub(ENT_NEW,h); ch.append('entrega 4-5 + 3 rondas')
    if is_inv and DUR.search(h): h=DUR.sub(DUR_NEW,h); ch.append('duración 1 año')
    n=0
    h,n=re.subn(r'(<strong[^>]*>)Versi&oacute;n Premium(</strong>)',r'\1Versi&oacute;n Premium &#11088; la m&aacute;s elegida\2',h,count=1)
    if n: ch.append('Premium más elegida')
    if is_inv and 'Pol&iacute;tica' not in h and 'Preguntas frecuentes' in h:
        i=h.index('<h3'+h.split('Preguntas frecuentes')[0].rsplit('<h3',1)[1]) if False else h.rfind('<h3',0,h.index('Preguntas frecuentes'))
        h=h[:i]+POL+h[i:]; ch.append('política agregada')
    if is_inv and 'Entrega</h3>' in h and 'Pases Individuales' not in h:
        i=h.index('Entrega</h3>'); j=h.index('</p>',i)+4
        h=h[:j]+'\n'+EXTRAS+h[j:]; ch.append('extras sugeridos')
    if h!=o:
        open('new/'+f,'w').write(h); log[pid]=ch
json.dump(log,open('log.json','w'),ensure_ascii=False,indent=0)
import collections; c=collections.Counter(x for v in log.values() for x in v)
print(len(log)); print(c)
