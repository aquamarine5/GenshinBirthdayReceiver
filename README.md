# GenshinBirthdayReceiver
*本人UID：140309417，欢迎加好友玩~*  
作者是住校学生，一周回一次，看到新活动是和生日有关的就想做一个自动领名片的程序，因为那些通常有效期只有1天，说干就干开Fiddler和VSCode写了两三分钟就通了，放Github Actions里面了  
## 如何使用？
- Fork本仓库，去Setting/Secrets添加COOKIE和UID两个secrets
- 去Action打开Fork Repo的Action权限
- 去Python Application的Action点击Run workflow即可

<details>
<summary>👀 查看更加详细的教程</summary>
  
  
### 1. 点击右上角的 Fork 按钮
- 等待刷新并自动跳转至新页面


  
### 2. 前往 [Mihoyo 米游社](https://bbs.mihoyo.com/ys) 获取Cookie
- 按`F12`，打开`开发者工具`，找到`Network`并点击
- 按`F5`刷新页面，按下图复制`Cookie`

![cookie](https://i.loli.net/2020/10/28/TMKC6lsnk4w5A8i.png)
### 3.添加Secrets
- 回到自己Fork的Github页面，依次点击`Settings`->`Secrets`->`Actions`->`New repository secret`
- 添加一个名为***COOKIE***（必须全大写）的Secrets，内容为刚才复制的Cookies
- 再添加一个名为***UID***的Secrets，内容为原神用户Uid

![1649507038_1_.png](https://s2.loli.net/2022/04/09/EYVaXvuBFx9gH1J.png)
### 4.再次点击上方的Action
- 点击绿色按钮  ***I understand my workflows, go ahead and enable them***
![1649506736.png](https://s2.loli.net/2022/04/09/ZapToF4lhjEIKxu.png)  
- 点击左侧的GenshinBirthdayScheduleTasks
- 在 *This workflow has a workflow_dispatch event trigger.* 右侧点击**Run workflow**，branch默认为`main`即可
![image.png](https://s2.loli.net/2022/04/09/PvIwmryp7YQZsn1.png)
- 至此 部署完毕。


</details>

## 关于脚本：
- `--forced-indexed` 会强制尝试获取当前生日列表并领取，如果没有此标识会优先获取生日日历判断今天是不是角色的生日
- `--use-locals` 会使用Repo下的[calendar.json](calendar.json)进行查找日历，没有则默认从服务器获取
## 使用须知！
- 米游社可能会封号，不知道会不会
- 新活动，没准后期会改api，如果有记得踢我一脚（issue or pr please）
## ps:
- 今日（3/3）七七生日B站竟然不是送椰奶
- 明天（3/4）是我生日今天下午却要返校（气）
- 申鹤生日（3/10）成功用Actions离线领取了生日相册
