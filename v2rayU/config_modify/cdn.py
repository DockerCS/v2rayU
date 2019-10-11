#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

from .tls import TLSModifier
from ..util_core.v2ray import restart
from ..util_core.selector import GroupSelector
from ..util_core.writer import StreamWriter, GroupWriter
from ..util_core.utils import StreamType, ColorStr, get_ip

class CDNModifier:
    def __init__(self, group_tag='A', group_index=-1, domain=''):
        self.domain = domain
        self.group_tag = group_tag
        self.group_index = group_index
        if domain:
            StreamWriter(self.group_tag, self.group_index, StreamType.WS).write()

        self.gw = GroupWriter(group_tag, group_index)

    def openHttp(self):
        '''
        cloudflare cdn proxy 80 port
        '''
        self.gw.write_port("80")
        self.gw.write_domain(self.domain)

    def closeHttp(self):
        self.gw.write_domain()

    def openHttps(self):
        '''
        cloudflare cdn proxy 443 port
        '''
        self.gw.write_port("443")
        TLSModifier(self.group_tag, self.group_index, self.domain).turn_on()

@restart()
def modify():
    gs = GroupSelector(_("modify cdn"))
    group = gs.group

    if group == None:
        pass
    else:
        print("")
        print(_("1.80 port + ws"))
        print(_("2.443 port + ws"))
        print(_("3.close cdn(80 port)"))
        choice = input(_("please select: "))
        if not choice:
            return
        if not choice in ("1", "2", "3"):
            print(_("input error, please input again"))
            return

        if choice == '3':
            if group.port != "80":
                print(ColorStr.yellow(_("only support 80 port cdn close!")))
                return
            CDNModifier(group.tag, group.index).closeHttp()
            return True

        domain = input(_("please input run cdn mode domain: "))
        if not domain:
            print(ColorStr.yellow(_("domain is empty!")))
            return
        try:
            input_ip = socket.gethostbyname(domain)
        except Exception:
            print(_("domain check error!!!"))
            print("")
            return

        if choice == '2':
            local_ip = get_ip()
            print(_("local vps ip address: ") + local_ip + "\n")

            if input_ip != local_ip:
                print(_("domain can't analysis to local ip!!!"))
                print(_("must be close cdn proxy!"))
                print("")
                return

        cm = CDNModifier(group.tag, group.index, domain)

        if choice == '1':
            cm.openHttp()
        elif choice == '2':
            cm.openHttps()

        return True