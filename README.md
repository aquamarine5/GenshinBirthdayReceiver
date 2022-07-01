# GenshinBirthdayReceiver
> ![](https://genshin-card.getloli.com/11/237006471.png)  
> *本人UID：140309417，欢迎加好友玩~*  
> 作者是住校学生，一周回一次，看到新活动是和生日有关的就想做一个自动领名片的程序，因为那些通常有效期只有1天，说干就干开Fiddler和VSCode写了两三分钟就通了，放Github Actions里面了  
## 如何使用？
- Fork本仓库，去`Setting/Secrets/Actions`添加COOKIE（米游社cookie）一个secrets
- 去Action打开Fork Repo的Action权限
- 去`GenshinBirthdayScheduleTasks`的Action点击Run workflow即可

**以下为更为详细的教程：**
### 1. 点击右上角的 Fork 按钮
- 等待刷新并自动跳转至新页面
  
### 2. 前往 [Mihoyo 米游社](https://bbs.mihoyo.com/ys) 获取Cookie
- 如果米游社还未登录，请先登录
- 按`F12`，打开`开发者工具`，找到`Network`（或`网络`）并点击
- 按`F5`刷新页面，找到名为`ys/`的页面（通常是第一个），按照下图拖到复制`Cookie`项
- **只要下图的灰框区域的内容，不需要前面的`Cookies: `**

![cookie](https://i.loli.net/2020/10/28/TMKC6lsnk4w5A8i.png)
### 3.添加Secrets
- 回到自己Fork的Github页面，依次点击`Settings`->`Secrets`->`Actions`->`New repository secret`
- 添加一个名为***COOKIE***（必须全大写）的Secrets，内容为刚才复制的Cookies

![image.png](https://s2.loli.net/2022/05/26/sjyL8KJSldBCgxr.png)  
> 在2022/5/29的新更新后，无需*UID*这一项Secret，已经fork的用户可以选择Create Pull Request拉取更新

### 4.再次点击上方的Action
- 点击绿色按钮  ***I understand my workflows, go ahead and enable them***
![1649506736.png](https://s2.loli.net/2022/04/09/ZapToF4lhjEIKxu.png)  
- 点击左侧的GenshinBirthdayScheduleTasks
- 启用GenshinBirthdayScheduleTasks
- 在 *This workflow has a workflow_dispatch event trigger.* 右侧点击**Run workflow**，branch默认为`main`即可
![image.png](https://s2.loli.net/2022/04/09/PvIwmryp7YQZsn1.png)
- **如需使用KeepActionAlive（默认Action只能够运行90days，启用KeepActionAlive后可一直使用，推荐启用），请点击左侧的KeepActionAlive，并在内启用。**
- 至此 部署完毕。
  
## 故障排除：
- Actions运行出现红叉叉时，点击左侧的`Jobs`->`build`
- 然后打开`Run GenshinBirthdayReceiver`页
  
![image.png](https://s2.loli.net/2022/05/29/LpMuSH8aEtC35ew.png)
  
### 遇到了`'message': '当前暂未登录，请登录后重试(-100)'`，怎么办？
- 请确认在Secrets正确设置了COOKIE，见[此页面](https://github.com/aquamarine5/GenshinBirthdayReceiver#3%E6%B7%BB%E5%8A%A0secrets)
### 如果遇到了其他的问题，怎么办？
- 去[Discussions](https://github.com/aquamarine5/GenshinBirthdayReceiver/discussions/new)选择**Q&A**发问题。
## Changelog:
### 2022/5/29
- 新版本无需*UID*这一Secret了，现在可以自动获取uid
## 关于脚本：
- `--forced-indexed` 会强制尝试获取当前生日列表并领取，如果没有此标识会优先获取生日日历判断今天是不是角色的生日
- `--use-locals` 会使用Repo下的[calendar.json](calendar.json)进行查找日历，没有则默认从服务器获取
## 使用须知！
- 米游社可能会封号，不知道会不会
- 新活动，没准后期会改api，如果有记得踢我一脚（issue or pr please）\
