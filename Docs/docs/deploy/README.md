# 环境说明

判题机需部署在Linux环境下！

我使用的环境是：

+ 前端： Ubuntu 18.10 + Nginx
+ 后端： Ubuntu 18.10 + Python 3.7
+ 判题服务器： Ubuntu 18.10 + Python 3.7 
+ 判题机： Ubuntu 18.10 + Python 3.7 （必须Linux系统）
+ 爬虫部分： Ubuntu 18.10 + Python 3.7

整个OJ对系统要求不高。1G内存 1核的机器足以。但是部分题目需要大内存，所以推荐使用2G内存 1核的服务器。

## 准备部署

接下来所有操作，均在Ubuntu系统下进行，如果是其他系统，请自行百度对应的命令行语句

首先我们把代码clone下来，或者直接在Github上[下载](https://github.com/Linzecong/LPOJ/archive/master.zip)下来。
首先我们将代码解压到一个文件夹中（就用LPOJ作为名字吧！）

```
mkdir LPOJ
cd LPOJ
git clone https://github.com/Linzecong/LPOJ.git
```

然后你就成功的把所有所需的文件下载下来了，接下来开始部署，具体看后面的教程。

## Docker 一键部署

现在支持Docker-compose一键部署了。每个模块都有自己的Dockerfile。
但我更推荐使用Docker-compose一键完成所有部署！
image使用的腾讯云提供的镜像，默认使用latest

1. 安装必要的依赖
```
sudo apt-get update
sudo apt-get install -y git
sudo apt install docker.io -y
sudo apt install docker-compose -y
sudo apt-get install openssh-server -y
sftp yourusername@localhost # 验证是否安装成功！
```
2. 开始安装
```
git clone https://github.com/Linzecong/LPOJ.git && cd LPOJ
# 如有需要，修改docker-compose.yml中的数据库密码（DB_PASSWORD，MYSQL_ROOT_PASSWORD）
# 必须修改docker-compose.yml中的BACKEND_PATH,SFTP_USER,SFTP_PASSWORD为你的LPOJ/Backend文件夹的绝对路径和服务器的用户名密码
sudo docker-compose up -d
```
根据网速和配置情况，大约10到20分钟就可以自动搭建完成，全程无需人工干预。

等命令执行完成，然后运行 **docker ps -a** 当看到所有的容器的状态均为 Up 就代表 OJ 已经启动成功。

> 安装成功后，先通过IP:8080访问OJ，注册一个用户
> 
> 然后进入 IP:8000/admin 以用户名admin 密码admin 登录后台（请及时修改后台密码）
> 
> 修改User表中，你注册的超级用户的type为3，使得你注册的用户变为超级管理员

3. 更新OJ

如要更新OJ只需在LPOJ目录下执行如下步骤
```
sudo docker-compose stop
sudo docker-compose pull
sudo docker-compose up -d --scale judger=3
```

**容易运行时产生的数据会保存在对应的文件夹中，如数据库文件，题目数据等**

**容易运行时产生的数据会保存在对应的文件夹中，如数据库文件，题目数据等**

## 一般安装

如果你想用传统的方法，感受自己一步步搭起一个OJ的快感，你可以阅读后面的教程。
但是相信我，你会回来用一键部署的。


