console 支持的命令

info
use exploits/discuz/dz67_cookie_rce
set NAME VALUE
run
show [options | advanced]

session 支持的执行方式

session = Session()
session.run('exploits/discuz/dz67_cookie_rce', { 'URL': 'http://www.baidu.com' })


