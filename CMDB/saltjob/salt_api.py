#!/usr/bin/env python
#coding:utf-8
import salt.client
client = salt.client.LocalClient()
import salt.utils.event
event = salt.utils.event.MasterEvent('/var/run/salt/master')
def overview(request):
    target = request.GET.get("target", '*')
    try:
        grains = client.cmd(target, 'grains.items')
    except:
        grains = {}
    return grains


def execute():
    return client.cmd_async(**kwargs)


def get_state(target):
    try:
        states = client.cmd(target,'state.show_top')
    except:
        states = {}
    return  states

if __name__ == "__main__":
    print get_state('*')






