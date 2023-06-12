from pathlib import Path

def chuli_b():
    inws = Path('webgis-rst/webgis-src')
    outws = Path('/owg')
    if outws.exists():
        pass
    else:
        outws.mkdir()

    for wfile in inws.rglob('*'):
        if wfile.is_file():
            dst = outws / wfile.name
            dst.write_bytes(wfile.read_bytes())
        else:
            pass

if __name__ == '__main__':
    chuli_b()
