'''
Deploy  WebGIS site.
'''
from fabric import Connection

from cfg import mach, mach_gislite

site_ws = '/home/gislite/github/webgis-pub'


def deploy():
    rcon = Connection("{}@{}".format(mach['u'], mach['h']), port=mach['k'], connect_kwargs={"password": mach['p']})
    rcon.run('sudo rsync -av /home/gislite/github/webgis-pub/_build/ /owg && sudo chown -R www-data.www-data /owg')



def gislite_build_site():
    print("{}@{}".format(mach_gislite['u'], mach_gislite['h']))
    rcon = Connection("{}@{}".format(
        mach_gislite['u'],
        mach_gislite['h']),
        port=mach_gislite['k'],
        connect_kwargs={"password": mach_gislite['p']}
    )

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
        # rcon.run('git reset --hard')
        # rcon.run('git clean -df')
        # rcon.run('git pull')
    # with c.cd('/home/bk/coding/site_webgis/static/f2elib'):
    #     c.run('git pull')

    with rcon.cd(site_ws):
        rcon.run('bash build.sh')


if __name__ == '__main__':

    print('=' * 80)
    gislite_build_site()
    deploy()
    print('QED')
