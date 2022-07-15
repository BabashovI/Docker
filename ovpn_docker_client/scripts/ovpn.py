import os
import subprocess
import glob

path = 'conf_files/*.ovpn'


def change_opvn(path):
    for filename in glob.glob(os.path.join(path)):
        result = subprocess.run(
            ['grep', 'uname', filename], stdout=subprocess.PIPE)
        if result.returncode == 1:
            if 'OpenVPN_UDP' in filename:
                subprocess.run(
                    ['sed', '-i', 's/auth-user-pass/auth-user-pass files\/uname_sc9/', filename])
            elif 'OpenVPN_global' in filename:
                subprocess.run(
                    ['sed', '-i', 's/auth-user-pass/auth-user-pass files\/uname_oci/', filename])


def hosts_alias_files():
    sao = subprocess.run(
        ['grep', 'sao', '/etc/hosts'], stdout=subprocess.PIPE)
    if sao.returncode == 1:
        subprocess.run(['cat files/sao >> /etc/hosts'], shell=True)

    subprocess.run(['cp files/aliases  /etc/profile.d/alias.sh'], shell=True)


def screenrc():
    # sed -i '/47l/c #comented' /etc/screenrc
    # termcap xterm|xterms|xs ti=\E7\E[?47l
    # terminfo xterm|xterms|xs ti=\E7\E[?47l
    # sed -i "/47l$/d" /etc/screenrc
    screenrc_conf = '/etc/screenrc'
    subprocess.run(['sed', '-i', '/47l$/d', screenrc_conf])


class test():
    def __init__(self):
        pass


change_opvn(path)
hosts_alias_files()
screenrc()
