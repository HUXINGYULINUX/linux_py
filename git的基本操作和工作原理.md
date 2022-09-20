# git的基本操作和工作原理

### 一、git的工作原理

![Git工作原理及基础操作](https://picx.zhimg.com/v2-5ef4d3b19c4fae1c887f44e43ac46c62_1440w.jpg?source=172ae18b)

- Workspace：工作区
- Index：暂存区
- Repository：仓库区
- Remote：远程仓库

### 二、Git的原理

- 保证数据的完整性

  保证通过网络下载的文件跟服务器上一样：Git利用哈希算法的特性，对服务器和本地同一个文件进行哈希，得到的结果一致则表示文件没有丢失或损坏。

- Git版本保存机制

  Git每次提交，都会对当前全部文件制作一个快照，并保存这个快照的索引。若相比较上个版本有改变的文件，在快照中则保存完整的文件，若没有改变则保留一个指向文件的链接即可

- Git提交机制

  每次提交都会产生一个区块，各提交区块之间则由父子关系链接成一条链路

- Git分支管理机制

  对于git而言，创建一个分支，只需要新增一个指针

### 三、git的主要操作

#### （1）LINUX：

- cd+路径：进入某个文件夹
- pwd：显示当前文件路径
- ls-all：看到当前目录下的所有文件

#### （2）提交到暂存区

- Git init: 把当前目录变成git可以管理的仓库
- Git add + 文件名：把文件添加到暂存区
- Git commit -m + 注释：告诉Git把文件提交到仓库
- Git status：查看是否有文件未提交

#### （3）版本回退

- Git diff + 文件名：查看文件的改动
- Git log：显示从近到远的三次提交日志
- Git Checkout + 文件名：用于add后还没commit之前
- Git reset —hard HEAD^：退回上一个版本
- Git reset —hard 版本号（从git log 或git reflow里获取）

#### （4）撤销修改

- Git checkout — 文件名：丢弃工作区的修改

#### （5）删除文件

- Git rm + 文件名/直接在工作区目录下删除文件
- 如果想撤销删除文件：git checkout —文件名

#### （6）提交到Git远程仓库

- Git remote add origin + git仓库地址（从网页版复制粘贴然后添加.git即可）：将本地仓库和远程仓库关联
- Git push -u origin master：把本地库的内容推送到远程仓库

#### （7）克隆远程库的内容到本地

- Git alone git仓库地址

#### （8）创建/合并分支

- Git checkout -b dev：创建并切换分支
- Git branch：查看所有分支，当前分支会添加一个星号
- Git branch dev：创建分支
- Gti checkout dev：切换分支
- Git merge dev：合并指定分支到当前分支上
- Git branch -d dev：删除dev分支

#### （9）从远程库上更新代码

- Git pull：如果本地工作区上针对最新的远程库代码版本有更新，使用pull不会覆盖这个更新

### 四、工作区与暂存区的区别

#### （1）工作区

- 即在电脑上看到的目录

#### （2）版本库

- 即.git，存了很多东西，最重要的即为版本库，还有Git自动创建的分支master，以及指向master的一个指针HEAD

### 五、远程仓库

- 需要注册Github账号，然后在网页版上创建repository，这个新创建的仓库目前是空的，可以做的操作有：

  （1）关联一个本地的仓库，然后把本地仓库的内容推送到Git的仓库

  （2）从别的仓库引入代码

### 六、分支使用策略

- master应该是非常稳定的，一般情况下在dev上干活，需要线上发布，或者dev代码稳定后合并到master上来
- 修复bug的时候，每个bug都可以创建一个临时分支来修复，修复完成后合并分支，然后将临时分支删除
- 如果在dev上的工作还没有完成，又需要紧急修复另一个404bug：
  - 可以使用git stash把当前工作现场隐藏起来（文件暂存）
  - 解决完紧急bug之后切换回dev分支，使用git stash list查看暂存内容
  - Git stash apply/git stash pop, 后者恢复的同时会把stash的内容也删除了

### 七、在Github内建立自己的库

- 在浏览器中打开Github网页[Github](www.github.com)

- 点击右上角Sign Up注册一个新账号

  ![image-20220920153026518](C:\Users\胡兴涛\AppData\Roaming\Typora\typora-user-images\image-20220920153026518.png)

- 注册完成后在主页 右上角点+号，选择New repository新建一个库

  ![image-20220920153222204](C:\Users\胡兴涛\AppData\Roaming\Typora\typora-user-images\image-20220920153222204.png)

  ![image-20220920153250575](C:\Users\胡兴涛\AppData\Roaming\Typora\typora-user-images\image-20220920153250575.png)

- 在Repository name填写一个库名

  ![image-20220920153316417](C:\Users\胡兴涛\AppData\Roaming\Typora\typora-user-images\image-20220920153316417.png)

- 最后点击Create repository，就成功创建我们的库

  ![image-20220920153351837](C:\Users\胡兴涛\AppData\Roaming\Typora\typora-user-images\image-20220920153351837.png)