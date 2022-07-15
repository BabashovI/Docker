#!/bin/sh
#add required lines
#cat ../files/sao >>/etc/hosts
#cat ../files/aliases >>~/.bashrc
#creat net folder and fs node file
mkdir /dev/net
mknod /dev/net/tun c 10 200
#
python3 /vpn/scripts/ovpn.py
