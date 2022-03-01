# 根目录扩容

**具体任务**：在已安装好的系统下重新分区，扩展空间。

**环境**

* 双系统: Windows + Ubuntu 16.04



## 方案一

基本思路是，通过USB引导进入镜像系统，使用工具gparted进行磁盘重分配。具体步骤参照： 

[GParted磁碟分割工具使用](https://blog.gtwang.org/linux/gparted-gnome-partition-editor-and-live-cd-usb/3/#:~:text=GParted%20Live%20CD%2FUSB&text=%E9%81%B8%E6%93%87%E4%BE%86%E6%BA%90%E6%98%A0%E5%83%8F%E6%AA%94%E8%88%87,%E9%BB%9E%E9%81%B8%E3%80%8C%E5%AF%AB%E5%85%A5%E3%80%8D%E3%80%82&text=%E7%AD%89%E5%BE%85%E6%98%A0%E5%83%8F%E6%AA%94%E5%AF%AB%E5%85%A5%E9%81%8E%E7%A8%8B%E3%80%82&text=%E6%98%A0%E5%83%8F%E6%AA%94%E5%AF%AB%E5%85%A5%E6%88%90%E5%8A%9F%E3%80%82&text=%E5%B0%87%E8%A3%BD%E4%BD%9C%E5%A5%BD%E7%9A%84GParted,%EF%BC%88Default%20settings%EF%BC%89%E3%80%8D%E9%96%8B%E6%A9%9F%E3%80%82)



## 方案二

当Ubuntu的磁盘分区是采用lvm方式挂载，可以采用虚拟磁盘的方式直接对齐进行分区扩容。假设，空闲磁盘为`/dev/sdb`， 目标磁盘为`/dev/mapper/vg1-lv1`, 即需要进行扩充的空间为。

1 扫盘

```
# sudo su
# pvscan
# vgscan
```

2 快速分区，从空闲硬盘位置`/dev/sdb`划分出一块格式为lvm的空间。

```
# fdisk /dev/sdb

Command (m for help): n
All primary partitions are in use
Adding logical partition 8
First sector (25176064-41943039, default 25176064): 
Using default value 25176064
Last sector, +sectors or +size{K,M,G} (25176064-41943039, default 41943039): +2G
Partition 8 of type Linux and of size 2 GiB is set
Command (m for help): t
Partition number (1-8, default 8): 
Hex code (type L to list all codes): 8e
Changed type of partition 'Linux' to 'Linux LVM'

Command (m for help): w
The partition table has been altered!

```

3.创建pv

```
# pvcreate /dev/sdb
Physical volume "/dev/sdb6" successfully created.
```

4.vg 扩展

```
# vgextend vg1 /dev/sdb
  Volume group "vg1" successfully extended
```

```
# vgdisplay vg1
  --- Volume group ---
  VG Name               vg1
  System ID             
  Format                lvm2
  Metadata Areas        4
  Metadata Sequence No  26
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                1
  Open LV               1
  Max PV                0
  Cur PV                4
  Act PV                4
  VG Size               7.98 GiB
  PE Size               4.00 MiB
  Total PE              2044
  Alloc PE / Size       1152 / 4.50 GiB
  Free  PE / Size       892 / 3.48 GiB
  VG UUID               dx3XD9-rQBV-QtBu-EebN-wgjI-CQcn-36iIbm
```

5.lv扩容

```
# lvextend /dev/vg1/lv1 /dev/sdb
  Size of logical volume vg1/lv1 changed from 4.5
```

6.更新lv挂载信息

```
# resize2fs /dev/mapper/vg1-lv1  #xfs文件系统不适用，xfs文件系统需要执行xfs_growfs /dev/vg1/lv1  xfs
![Linux LVM系列（四）vg扩容和lv扩容_lvm ](http://i2.51cto.com/images/blog/201712/08/f4977ad91fc0c475ced44d60e51dc25a.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)
resize2fs 1.42.9 (28-Dec-2013)
Filesystem at /dev/mapper/vg1-lv1 is mounted on /mnt; on-line resizing required
old_desc_blocks = 1, new_desc_blocks = 1
The filesystem on /dev/mapper/vg1-lv1 is now 1702912 blocks long.

```

7.查看更新后

```
# df -hT
Filesystem          Type      Size  Used Avail Use% Mounted on
/dev/mapper/cl-root xfs       8.6G  5.3G  3.4G  62% /
devtmpfs            devtmpfs  2.4G     0  2.4G   0% /dev
tmpfs               tmpfs     2.4G     0  2.4G   0% /dev/shm
tmpfs               tmpfs     2.4G  8.7M  2.4G   1% /run
tmpfs               tmpfs     2.4G     0  2.4G   0% /sys/fs/cgroup
/dev/mapper/cl-home xfs       4.0G   33M  4.0G   1% /home
/dev/mapper/cl-var  xfs       3.0G  159M  2.8G   6% /var
/dev/sda2           xfs       497M  132M  366M  27% /boot
tmpfs               tmpfs     479M     0  479M   0% /run/user/0
/dev/mapper/vg2-lv2 ext4      3.9G   16M  3.7G   1% /data
/dev/mapper/vg1-lv1 ext4      6.4G   18M  6.1G   1% /mnt

```



**potential error**

pvcreate error: 

```
  /run/lvm/lvmetad.socket: connect failed: No such file or directory
  WARNING: Failed to connect to lvmetad. Falling back to internal scanning.
  Can't open /dev/sdb6 exclusively.  Mounted filesystem?

```

solution:

```
systemctl enable lvm2-lvmetad.service
systemctl enable lvm2-lvmetad.socket
systemctl start lvm2-lvmetad.service
systemctl start lvm2-lvmetad.socket
```



## reference

https://www.cfanz.cn/resource/detail/XrnlODooELBNl