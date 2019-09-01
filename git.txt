
安装：
sudo apt-get install git
查看：
git
创建版本库：
git init
使用：
git add code,txt
git commit -m ‘版本 1‘   （版本说明）
查看版本记录：
git log

（后面版本不是重新生成的，只是在前一个版本的基础上做出修改记录）
回退版本：
git reset --hard HEAD
其中HEAD表示当前最新版本，HEAD^表示当前版本的前一个版本，HEAD^^前前版本，也可以用HEAD~1表示前一个版本，HEAD~100 表示前100个版本

