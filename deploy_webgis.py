'''
Deploy  WebGIS site.
'''
from fabric import Connection

from cfg import mach

site_ws = '/home/gislite/coding/book-webgis/webgis_pub'

def main():

    print("{}@{}".format(mach['u'], mach['h']))
    rcon = Connection("{}@{}".format(mach['u'], mach['h']), port=mach['k'], connect_kwargs={"password": mach['p']})

    # c.run('pip3 install markdown')
    # c.run('pip3 install mappyfile')
    # c.run('pip3 install openpyxl')
    # c.run('pip3 install bs4')
    # c.run('pip3 install docutils')
    # c.run('pip3 install jinja2')
    # c.run('pip3 install pyyaml')

    with rcon.cd(site_ws):
        rcon.run('hostname')

    rcon.run('sudo chown -R bk {}/owg'.format(site_ws))
    # c.run('sudo chown -R bk {}/geodata'.format(site_ws))
    # c.run('sudo chown -R bk {}/data'.format(site_ws))

    with rcon.cd(site_ws):
        try:
            rcon.run('rm -f templates/99_gislite_GISLite/2*')
        except:
            pass
        try:
            rcon.run('rm -f templates/99_gislite_GISLite/3*')
            rcon.run('rm -f templates/99_gislite_GISLite/4*')
        except:
            pass
        rcon.run('git reset --hard')
        rcon.run('git clean -df')
        rcon.run('git pull')
    # with c.cd('/home/bk/coding/site_webgis/static/f2elib'):
    #     c.run('git pull')


    with rcon.cd(site_ws):
        rcon.run('python3 build_mapfile2.py')
        # c.run('python3 build_gislite.py')
        rcon.run('/xpy/bin/python3 build_site.py')

    '''
    sudo chown -R www-data.www-data owg
    sudo chown -R www-data.www-data geodata
    sudo chown -R www-data.www-data data
    '''
    rcon.run('sudo chown -R www-data.www-data {}/owg'.format(site_ws))
    # c.run('sudo chown -R www-data.www-data {}/geodata'.format(site_ws))
    # c.run('sudo chown -R www-data.www-data {}/data'.format(site_ws))


if __name__ == '__main__':
    main()
