# kjyw 快捷运维


## 项目简介
- 快捷运维 kjyw，运维脚本工具库，项目基于shell开发
- 简单 高效 快捷！
- 实现快速安装nginx、mysql、php、redis、nagios运维经常使用的脚本等等... 
- Linux下很多操作命令，都可以通用化，脚本化。
- 脚本化后，可以结合一些自动化工具，批量部署，比如可以用ansible来批量执行脚本，就可以批量部署服务器业务。
- 这里面的脚本是运维经常使用的脚本，方便大家使用！
- 相关使用文档：https://bbs.aqzt.com/forum-39-1.html

## 为什么要做快捷运维？
- 相信大家都知道，运维是一项非常重要且时效性要求很高的工作，项目和程序发布，升级，更新都少不了运维的操作，
- 因此运维也是个少不了加班的职业。我喜欢运维，但我也不希望经常加班太多，
- 于是我就思考如何能优化我的运维工作，提高效率，本来要几个小时的工作任务，能否在几分钟之内完成呢？

## 使用快捷运维脚本的好处
- 工作任务可以快速完成，提高效率，减少加班，这样就有更多的时间陪家人，或做其他事情啦！
- 可以和自动化工具结合，批量部署业务，如果有3-5台服务器，直接SSH远程编译安装，
- 如果几十台服务器，上百台服务器，上千台服务器都要安装某个应用呢？
- 可以用快捷运维脚本结合自动化工具（比如：ansible），批量推送执行脚本即可。
- 知名CEO说过：“在这个纷繁复杂的世界上，决策比别人快，很可能就赢了”，做正确决策比别人快，你就赢了。
- 在部署运维需求的时候，部署效果一样的情况下，你比其他人部署快，你就比其他人更优秀。

## 使用场景
- 【举个例子】
- 某天，某人，因某业务，有redis部署需求，需要批量部署一组redis服务，端口从8001到8009，
- 简单，马上开始部署，编译redis，拷贝redis执行文件，配置文件，8001端口，启动，再拷贝redis执行文件，修改配置文件，8002…………
- 半小时后部署好了，完成！
- 有没有更好的方法，可以提高效率，快速完成呢？
- 如果用脚本部署，只需要1分钟搞定，主要是编译redis时间，大大提高效率，快捷，快捷，快捷啊！
- 第一步 编译redis
- curl -s https://git.oschina.net/aqztcom/kjyw/raw/master/redis/install.sh | sh
- 第二步 拷贝redis执行文件，修改配置文件，并启动
- curl -s https://git.oschina.net/aqztcom/kjyw/raw/master/redis/redis_port.sh | sh -s  install 8001 8009
- 完成！
- ![image](https://git.oschina.net/aqztcom/kjyw/raw/master/images/redis1.gif)
- 批量关闭redis端口 8001到8009
- curl -s https://git.oschina.net/aqztcom/kjyw/raw/master/redis/redis_port.sh  | sh -s  stop 8001 8009
- ![image](https://git.oschina.net/aqztcom/kjyw/raw/master/images/redis2.gif)
- 批量启动redis端口 8001到8009
- curl -s https://git.oschina.net/aqztcom/kjyw/raw/master/redis/redis_port.sh  | sh -s  start 8001 8009 
- ![image](https://git.oschina.net/aqztcom/kjyw/raw/master/images/redis3.gif)
- 快捷运维还有其他运维经常使用的脚本，方便使用，提高效率！


## 适合使用快捷运维脚本的职业
- 运维工程师  （方便运维工程师搭建业务生产环境，最好先测试脚本，在用于生产环境）
- 开发工程师  （方便开发工程师搭建开发环境）
- 测试工程师  （方便测试工程师搭建测试环境）




- 运维就是踩坑，踩坑的最高境界就是：踩遍所有的坑，让别人无坑可踩！
- 做事的宗旨是：一条命令的事，一个脚本的事！
