rm -rf diybot.sh &&rm -rf user.sh&&rm -rf userbot.sh
echo -e "======================== 1. 部署自定义jbot-diy机器人 ========================\n"
if [ -d "/jd" ]; then root=/jd; else root=/ql; fi; if [ -f $root/self.sh ]; then rm -f $root/self.sh; fi; cd $root; wget https://raw.githubusercontent.com/msechen/JD_Diy/main/shell/self.sh; bash self.sh

echo -e "======================== 2. 部署[user.py]监控机器人 ========================\n"
if [ -d "/jd" ]; then root=/jd; else root=/ql; fi; if [ -f $root/user.sh ]; then rm -f $root/user.sh; fi; cd $root; wget https://raw.githubusercontent.com/msechen/JD_Diy/main/shell/user.sh; bash user.sh
