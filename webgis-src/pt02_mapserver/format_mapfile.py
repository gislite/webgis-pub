
from pathlib import Path
import mappyfile

inws = Path('.')

for wfile in inws.rglob('rmf*.map'):
    outfile = wfile.parent / wfile.name.split('_')[-1]
    mf = mappyfile.load(open(wfile))
    # mappyfile.write(mf, str(outfile))
    # uu = mappyfile.dump(mf)
    # print(uu)
    # mappyfile.save(, str(outfile))
    with open(outfile, 'w') as fo:
        mappyfile.dump(mf, fo)
        # fo.write(uu)

