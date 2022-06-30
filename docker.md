# Docker

Docker 是一个开源的应用容器引擎，基于 [Go 语言](https://www.runoob.com/go/go-tutorial.html)   并遵从 Apache2.0 协议开源。

Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

Docker 从 17.03 版本之后分为 CE（Community Edition: 社区版） 和 EE（Enterprise Edition: 企业版），我们用社区版就可以了。

优点：

1、快速，一致地交付您的应用程序

2、响应式部署和扩展

3、在同一硬件上运行更多工作负载





### 镜像使用

1、列出本地主机上的镜像列表

`docker images `

2、 启动镜像，进入容器。如果使用版本为15.10的ubuntu系统镜像来运行容器时，命令如下：

`docker run -t -i ubuntu:15.10 /bin/bash `

参数说明：

- **-i**: 交互式操作。
- **-t**: 终端。
- **ubuntu:15.10**: 这是指用 ubuntu 15.10 版本镜像为基础来启动容器。
- **/bin/bash**：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。



3、删除镜像

镜像删除使用 **docker rmi** 命令，比如我们删除 hello-world 镜像：

`docker rmi hello-world`

4、创建镜像

当我们从 docker 镜像仓库中下载的镜像不能满足我们的需求时，我们可以通过以下两种方式对镜像进行更改。

- 1、从已经创建的容器中更新镜像，并且提交这个镜像
- 2、使用 Dockerfile 指令来创建一个新的镜像



(1)、编辑Dockerfile

```
runoob@runoob:~$ cat Dockerfile 
FROM    centos:6.7
MAINTAINER      Fisher "fisher@sudops.com"

RUN     /bin/echo 'root:123456' |chpasswd
RUN     useradd runoob
RUN     /bin/echo 'runoob:123456' |chpasswd
RUN     /bin/echo -e "LANG=\"en_US.UTF-8\"" >/etc/default/local
EXPOSE  22
EXPOSE  80
CMD     /usr/sbin/sshd -D
```

(2)、制作镜像

```
docker build -t runoob/centos:6.7 .
Sending build context to Docker daemon 17.92 kB
Step 1 : FROM centos:6.7
 ---&gt; d95b5ca17cc3
Step 2 : MAINTAINER Fisher "fisher@sudops.com"
 ---&gt; Using cache
 ---&gt; 0c92299c6f03
Step 3 : RUN /bin/echo 'root:123456' |chpasswd
 ---&gt; Using cache
 ---&gt; 0397ce2fbd0a
Step 4 : RUN useradd runoob
......
```



### 容器使用

１、以下命令使用  ubuntu 镜像启动一个容器，参数为以命令行模式进入该容器：

`$ docker run -it ubuntu /bin/bash`

2、　启动已停止运行的容器

查看所有的容器命令如下：

```
$ docker ps -a
```

使用 docker start 启动一个已停止的容器：

`$ docker start b750bbbcfd88 `

3、停止一个容器

停止容器的命令如下：

`$ docker stop <容器 ID>`

4、进入容器

在使用 **-d** 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入：

- **docker attach**
- **docker exec**：推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。

**attach 命令**

下面演示了使用 docker attach 命令。

```
$ docker attach 1e560fca3906 
```

5、导出和导入容器

**导出容器**

如果要导出本地某个容器，可以使用 **docker export** 命令。