from pathlib import Path


inws = Path('webgis-src')
outws = Path('xx_rst')
if outws.exists():
    pass
else:
    outws.mkdir()

for wfile in inws.rglob('*'):
    if wfile.name == 'index.rst':
        dst = outws / 'index.rst'

        cnts = open(wfile).readlines()
        with open(dst,'w') as fo:
            for cnt in cnts:
                cnt_strip = cnt.strip()
                if cnt_strip.startswith('part') and cnt_strip.endswith('part'):
                    sig = cnt_strip.split('/')[0].split('_')[-1]
                    print(sig)
                    fo.write(f'   {sig}\n')
                else:
                    fo.write(cnt)

    elif wfile.name == 'part.rst':
        dst = outws / (wfile.parent.name.split('_')[-1] + '.rst')

        cnts = open(wfile).readlines()
        with open(dst,'w') as fo:
            for cnt in cnts:
                cnt_strip = cnt.strip()
                if cnt_strip.startswith('ch') and cnt_strip.endswith('chapter'):
                    sig = cnt_strip.split('/')[0].split('_')[-1]
                    # print(sig)
                    fo.write(f'   {sig}\n')
                else:
                    fo.write(cnt)
    elif wfile.name == 'chapter.rst':
        dst = outws / ( wfile.parent.name.split('_')[-1] + '.rst')
        cnts = open(wfile).readlines()
        with open(dst,'w') as fo:
            for cnt in cnts:
                cnt_strip = cnt.strip()
                if cnt_strip.startswith('sec') and cnt_strip.endswith('section'):
                    sig = wfile.parent.name.split('_')[-1] + '-' + cnt_strip.split('/')[0].split('_')[-1]
                    # print(sig)
                    fo.write(f'   {sig}\n')
                else:
                    fo.write(cnt)

    elif wfile.name == 'section.rst':
        dst = outws / (wfile.parent.parent.name.split('_')[-1] + '-' + wfile.parent.name.split('_')[-1] + '.rst')

        dst.write_text(wfile.read_text())
    elif wfile.is_file():
        dst = outws / wfile.name
        dst.write_bytes(wfile.read_bytes())
    else:
        pass
