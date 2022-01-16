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

<h1 align="center">
  本项目jdtrain v5安装使用
</h1>

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
  
<h1 align="center">
  🐏 jbot三方监控bot安装
  <br>
  Author: chiupam
</h1>

# 仓库目录说明
```text
./                     # 仓库
  |-- backup                    # 备份
  |-- beta                      # 测试版
  |-- config                    # 配置目录
  |-- jbot                      # 正式版
  |-- module                    # 实例模块
  |-- other                     # 不便于分类
  |-- pys                       # python脚本
  |-- shell                     # shell脚本
  |-- requirements.txt          # 依赖文件
  `-- README.md                 # 仓库说明
```
# 版权
- 未经本人同意，仓库内所有资源文件，禁止任何公众号、自媒体、开发者进行任何形式的转载、发布、搬运。
# 声明
- 这不是一个开源项目，只是把 GitHub 当作一个代码的存储空间，本项目不接受任何开源要求。
- 仅用于学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
- 本人对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, 本人对于由此引起的任何隐私泄漏或其他后果概不负责。
- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明、所有权证明，我将在收到认证文件后删除相关脚本。
- 任何以任何方式查看此项目的人或者以直接或间接的方式使用该项目的任何脚本的使用者都应仔细阅读此声明。 本人保留随时更改或补充此免责声明的权利。一旦使用并复制或使用了任何相关脚本，则视为您已接受此免责声明。
- 您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
# 特别感谢
- 脚本的写作参考了 [SuMaiKaDe](https://github.com/SuMaiKaDe) 的 [bot](https://github.com/SuMaiKaDe/bot) 仓库
- 模块的写作参考了 lxk0301 的 jd_scripts 仓库
# 使用手册
- [Github](https://github.com/chiupam/JD_Diy/wiki/%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)
- [Gitee](https://gitee.com/chiupam/JD_Diy/wikis/%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)

  
