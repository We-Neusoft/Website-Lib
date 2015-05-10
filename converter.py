#coding=utf-8

# 计算文件大小，使用相应的单位
def file_size(num):
    if not num:
        return num

    for x in ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if num < 1024.0:
            return '%3.2f %s' % (num, x)
        num /= 1024.0

def link_speed(num):
    result = {}

    bits = num
    for x in ['bps', 'Kbps', 'Mbps', 'Gbps']:
        if bits < 1000.0:
            result.update({'bitrate': ('%3.2f%s' % (bits, x)).replace('.00', '')})
            break
        bits /= 1000.0

    bytes = num / 8.0
    for x in ['B/s', 'KB/s', 'MB/s', 'GB/s']:
        if bytes < 1024.0:
            result.update({'byterate': ('%3.2f%s' % (bytes, x)).replace('.00', '')})
            break
        bytes /= 1024.0

    return result