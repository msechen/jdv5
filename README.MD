<h1 align="center">
  本项目jdtrain v5安装使用
</h1>

docker-compose（适合支持docker-compose的环境）安装方式一 \
1、wget https://raw.githubusercontent.com/msechen/jdv5/main/docker-compose.yml \
2、修改docker-compose.yml映射目录的绝对路径及相关参数 \
3、docker-compose up -d 

docker（通用）安装方式二 \
1、新建映射用到的目录，下面/jdtrainv4bot/config、/jdtrainv4bot/log、/jdtrainv4bot/own、/jdtrainv4bot/diy、/jdtrainv4bot/scripts替换你新建的目录 \
2、执行以下命令 \
docker run -dit \ \
  -v /jdtrainv4bot/config:/jd/config \ \
  -v /jdtrainv4bot/log:/jd/log \ \
  -v /jdtrainv4bot/own:/jd/own \ \
  -v /jdtrainv4bot/diy:/jd/jbot/diy \ \
  -v /jdtrainv4bot/scripts:/jd/scripts \ \
	-p 5678:5678 \ \
  -e ENABLE_HANGUP=false \ \
  -e ENABLE_WEB_PANEL=true \ \
  -e ENABLE_WEB_TTYD=false \ \
  -e ENABLE_TG_BOT=true  \ \
	--name jdtrainv4bot \ \
	--hostname jdtrainv4bot \ \
	--restart always \ \
	abcdjd/jdtrain:v4-bot 
  
  面板:http://ip:5678 \
  账号密码:admin/adminadmin  
  
 
2022-4-19 新增单车头、ck分段运行脚本功能
用法：
1. jtask jd_opencard desi 1 4 6    1是车头4-6是分段
2. jtask jd_opencard desi 4 6        4-6是分段运行
