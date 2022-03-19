# 问题。

1. 自己的项目不需要考虑高可用的问题。主要是可用备份就行，针对NAS之类的。方便停机迁移即可
解决小项目部署，不想用k8s这种重量级选手
解决docker swarm管理不方便的问题。
使用docker swarm + compose结合的方式来允许使用privilege模式
使用 treafik来管理统一出口
提供一个dns 服务，来管理dns
可以快速的部署小型sass，不考虑高可用。


## 机器管理，明确机器的指责

## 服务管理 
配置管理，吧配置文件，目录下发到每个机器的指定的目录下， client做
### 目录管理、
只读模式
1。 单个配置文件 （只读）
    1。 使用swarm时使用配置挂载
    1。 compose模式，吧配置复制到宿主机器上，本地挂载
1。 目录配置 （只读）
    1。 覆盖模式
        1。 compose/swarm 挂载目录
    1。 融合模式，先把镜像内的文件cp出来，在用修改的文件覆盖配置
可写模式  只有一个相同的instance

1。 备份与迁移 （可写目录只能有一个同镜像的 service同时允许），
    1。 swarm模式，通过标签来控制service运行位置。
    2。 compose模式，client来在宿主机器上启动，可以使用特权模式


### 环境变量管理


通过本管理，使用traefik来暴露服务。

分为client和服务控制端两部发