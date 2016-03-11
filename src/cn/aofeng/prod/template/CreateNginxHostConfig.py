#coding:utf8

''' 用途：在nginx_conf_dir目录下生成Host信息。
参数说明：
{0} - 主机域名
{1} - 主机端口'''
import sys
import os

#nginx_conf_dir = "/home/share/local/nginx-1.9.2/conf/conf.d"
nginx_conf_dir = "/home/nieyong"
template = '''server {{
    listen      80;
    server_name dev.nieyong.local;
    access_log  /home/share/local/nginx-1.9.2/logs/{hostDomain}_access.log;
    error_log   /home/share/local/nginx-1.9.2/logs/{hostDomain}_error.log;
    proxy_read_timeout 600;
    proxy_send_timeout 600;
    location / {{
        proxy_pass http://127.0.0.1:{hostPort}/;
        proxy_set_header Host               $host;
        proxy_set_header X-Real-IP          $remote_addr;
        proxy_set_header X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header Via                "nginx";
    }}
}}'''

def createHost(hostDomainName, hostPort):
    arr = template.splitlines()
    os.chdir(nginx_conf_dir)
    fo = open(hostDomainName, "w")
    try:
        for line in arr:
            fo.write( line.format(hostDomain=hostDomainName, hostPort=hostPort) )
            fo.write("\n")
    finally:
        fo.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''错误的参数！
        使用方法：python CreateNginxHost.py 主机域名 主机端口
        例：python CreateNginxHost.py dev.nieyong.local 8080'''
        sys.exit(1)
    createHost(sys.argv[1], sys.argv[2])
