#coding=utf-8
from django.conf import settings

from netaddr import IPAddress, IPNetwork
from zlib import crc32

from converter import link_speed

ip_network = [
    IPNetwork('127.0.0.1/32'),
    IPNetwork('172.18.0.0/16'), IPNetwork('172.19.0.0/17'), IPNetwork('172.21.0.0/17'), IPNetwork('172.21.128.0/17'),
    IPNetwork('172.22.0.0/16'), IPNetwork('172.23.0.0/16'), IPNetwork('172.24.0.0/16'),
    IPNetwork('192.168.24.0/24'), IPNetwork('192.168.102.0/24'),
    IPNetwork('219.216.128.0/24'), IPNetwork('219.216.129.0/27'),
]
ip_name = [
    ('localhost', '本地'),
    ('wireless', '校园无线网'), ('apartment', '校园有线网'), ('unicom', '联通有线网'), ('x', 'X'),
    ('classroom', '校园有线网'), ('faculty', '校园有线网'), ('server_172', '服务器网络'),
    ('administration', '校园有线网'), ('server_192', '服务器网络'),
    ('server_128', '服务器网络'), ('server_129', '服务器网络'),
]
ip_speed = [
    10000000000,
    2000000, 100000000, 20000000, 1000000000,
    100000000, 100000000, 1000000000,
    100000000, 1000000000,
    1000000000, 1000000000,
]

def get_ip(request):
    return IPAddress(request.META['REMOTE_ADDR'])

def get_geo(request):
    ip_address = get_ip(request)

    for network, name in zip(ip_network, ip_name):
        if ip_address in network:
            return name
    return ('', '')

def get_speed(request):
    ip_address = get_ip(request)

    for network, speed in zip(ip_network, ip_speed):
        if ip_address in network:
            return link_speed(speed)
