# Git commands

This documents contain multiple useful git commands in different situation.

## 

### Basic commands

* 从一个分支cherry-pick多个commit到其他分支

  `git cherry-pick commitid`

* 复制多个coｍmit, add .. between ids

  `git cherry-pick commitid1..commitid10`

* generate new ssh-key

  `ssh-keygen -C "jiaojiaoye@zhejianglab.com" `

* start ssh key in the background

  `ssh-add {path-to-key}` 

* display the diff between stash and master branch

  `git diff stash@{0} master`

* merge branch to another

  `git merge`

### checkout

* switch to a remote branch

```
git fetch origin branch

git checkout –track origin/xyz
```

### reset

* **git reset** 命令用于回退版本，可以指定退回某一次提交的版本。

  `git reset [--soft | --mixed | --hard] [HEAD]`

* **--mixed** 为默认，可以不用带该参数，用于重置暂存区的文件与上一次的提交(commit)保持一致，工作区文件内容保持不变。

  `git reset  [HEAD] `

* **--soft** 参数用于回退到某个版本, 回退上上上一个版本:  

  `git reset --soft HEAD~3` 

* **--hard** 参数撤销工作区中所有未提交的修改内容，将暂存区与工作区都回到上一次版本，并删除之前的所有信息提交 ( **注意：**谨慎使用 –hard 参数，它会删除回退点之前的所有信息。)：

  `git reset --hard HEAD`

> **HEAD 说明：**
>
> - HEAD 表示当前版本, HEAD~0 表示当前版本
> - HEAD^ 上一个版本, HEAD~1 上一个版本
> - HEAD^^ 上上一个版本, HEAD^2 上上一个版本
> - HEAD^^^ 上上上一个版本, HEAD^3 上上上一个版本
>



### 合并处理冲突

在看到冲突以后，你可以选择以下两种方式：

- 决定不合并。这时，唯一要做的就是重置index到HEAD节点。git merge --abort用于这种情况。
- **解决冲突。Git会标记冲突的地方，解决完冲突的地方后，使用****git add****加入到index中，然后使用****git commit****产生合并节点。**

你可以用以下工具来解决冲突:

- 使用合并工具。git mergetool将会调用一个可视化的合并工具来处理冲突合并。
- 查看差异。git diff将会显示三路差异（三路合并中所采用的三路比较算法）。

- 查看每个分支的差异。git log --merge -p 将会显示HEAD版本和MERGE_HEAD版本的差异。
- 查看合并前的版本。git show :1:文件名显示共同祖先的版本，git show :2:文件名显示当前分支的HEAD版本，git show :3:文件名显示对方分支的MERGE_HEAD版本。

[git merge 原理算法文章](https://blog.csdn.net/u012937029/article/details/77161584)

### 修改已提交的commit的用户名邮箱

第一步：前往需要修改的版本 

​	1. 使用 git log 获取需要修改的版本id 

​	2. 使用 git reset –soft [版本号] 前往版本 

第二步：修改信息 

​	1. 使用 git commit --amend --author='用户名 <邮箱>'修改 

​	2. 在打开的文件中保存一下就可以了 

第三步：提交代码 

​	使用 `git push`。