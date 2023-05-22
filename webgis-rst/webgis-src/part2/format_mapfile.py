
from pathlib import Path
import mappyfile

inws = Path('.')

for wfile in inws.rglob('rmf*.map'):
    outfile = wfile.parent / wfile.split('_')[-1]
    mf = mappyfile.load(wfile)
    mappyfile.write(mf, outfile)
