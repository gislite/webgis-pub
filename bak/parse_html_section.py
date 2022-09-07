from bs4 import BeautifulSoup

from pprint import pprint


def dictify(ul, fo):
    print('=' * 10)
    result = {}

    the_finds = ul.find_all('div', class_="section", recursive=False)
    # print(the_finds)

    for the_find in the_finds:
        print('-' * 10)

        print(the_find)
        # the_find.replacewith('aa')
        # print(the_find.contents)
        tt = the_find.contents
        from pprint import pprint


        tt= ''.join([ str(x) for x in tt])
        print('>' * 40)
        pprint(tt)
        the_find.replaceWith(tt)
        print('<' * 40)

    fo.write(str(ul))


def dictify2(ul, fo):
    print('=' * 10)
    result = {}

    # the_finds = ul.find_all('a', class_="headerlink", recursive=True)
    the_finds = ul.select('a[class="headerlink"]')
    # print(the_finds)

    # soup.select('td[class="bar"]')

    for the_find in the_finds:
        print('\033[33m')
        print('-' * 10)
        print(the_find)
        print('\033[0m' )
        # the_find.replacewith('aa')
        # print(the_find.contents)

        the_find.replaceWith('')


    fo.write(str(ul))

def method_name(inhtml, outfile):

    soup = BeautifulSoup(open(inhtml).read(), features="html.parser")
    bd = soup.find('div', class_='body')
    with open(outfile, 'w') as fo:
        dictify(bd, fo)
    with open(outfile, 'w') as fo:
        dictify2(bd, fo)
    cnts = open(outfile).read()
    with open(outfile, 'w') as fo:
        fo.write(cnts.replace('&lt;', '<').replace('&gt;', '>').replace('¶', '').replace('&amp;gt;', '>'))



inhtml = 'book_pygis/_build/html/ch02_k802_gdal/sec3_reading_data/section.html'
outfile = 'xx_out.html'
method_name(inhtml, outfile)

outfile2 = 'xx_out2.html'
method_name(outfile, outfile2)

method_name(outfile2, outfile)

# pprint(dictify(bd), width=1)
