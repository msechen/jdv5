# 申明

- 本项目未采用任何开源协议，项目为私有，不属于开源项目，仅供学习使用，拒绝任何人在其他项目中使用本项目中的任何代码。

- 本项目发布的内容仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。

- 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。

- `evine`对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。

- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, `evine`对于由此引起的任何隐私泄漏或其他后果概不负责。

- 请勿将本项目的任何内容用于商业或非法目的，否则后果自负。

- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。

- 您必须在下载后的24小时内从计算机或手机中完全删除以上内容。

- 任何以任何方式查看此项目的人或直接或间接使用本项目的任何脚本的使用者都应仔细阅读此声明。`evine`保留随时更改或补充此免责声明的权利。一旦使用并复制了任何相关脚本或本项目的规则，则视为您已接受此免责声明。


安装方式一 \
1、wget https://raw.githubusercontent.com/msechen/jdv5/main/docker-compose.yml \
2、修改docker-compose.yml映射目录的绝对路径及相关参数 \
3、docker-compose up -d 

安装方式二 \
 docker run -dit \
  -v /jdtrainv4bot/config:/jd/config \
  -v /jdtrainv4bot/log:/jd/log \
  -v /jdtrainv4bot/own:/jd/own \
  -v /jdtrainv4bot/diy:/jd/jbot/diy \
  -v /jdtrainv4bot/scripts:/jd/scripts \
	-p 5678:5678 \
  -e ENABLE_HANGUP=false \
  -e ENABLE_WEB_PANEL=true \
  -e ENABLE_WEB_TTYD=false \
  -e ENABLE_TG_BOT=true \
	--name jdtrainv4bot \
	--hostname jdtrainv4bot \
	--restart always \
	abcdjd/jdtrain:v4-bot 
  
  面板:http://ip:5678 \
  账号密码:admin/adminadmin  
