
<!-- vim-markdown-toc GFM -->

* [v2rayU](#v2rayU)
    * [特色](#特色)
    * [功能](#功能)
    * [安装命令](#安装命令)
    * [升级命令](#升级命令)
    * [卸载命令](#卸载命令)
    * [命令行参数](#命令行参数)
    * [系统要求](#系统要求)
    * [更新日志](#更新日志)
    * [特别说明](#特别说明)
    * [感谢](#感谢)

<!-- vim-markdown-toc -->

# v2rayU
V2ray多用户管理脚本，向导式管理[新增|删除|修改]传输协议，享受V2ray的乐趣~  


## 特色
- [x] 调用v2ray官方api进行流量统计
- [x] **多用户, 多端口管理**, 混合传输协议管理不再是梦
- [x] 首次安装时产生随机端口，默认配置mkcp + 随机一种 (srtp | wechat-video | utp | dtls) header伪装;  
  安装完成显示配置信息;  **脚本跑完即可放心食用！**
- [x] 每天**北京时间**早上3点自动升级重启v2ray核心,降低v2ray因内存小被kill几率。可关闭开启此功能。
- [x] 查看配置信息显示vmess字符串(v2rayN的分享链接格式)
- [x] 生成**Telegram**的socks5/MTProto分享链接, 支持socks5 + tls组合
- [x] 支持http/2, 随机生成伪装h2 path
- [x] 开启关闭tcpFastOpen
- [x] 开启关闭动态端口
- [x] 禁止BT
- [x] 支持新版v2ray配置文件格式(v4.1+)
- [x] 支持范围端口修改
- [x] 支持程序和**命令行参数**管理控制

## 功能
- 一键 启动 / 停止 / 重启 V2ray 服务端
- 流量统计(v2ray && iptables)
- 命令行模式管理v2ray
- 支持多用户， 多端口管理
- 开启关闭动态端口
- bittorrent的禁止与放行
- 单端口, 范围端口的修改
- 开启关闭tcpFastOpen
- 快速查看服务器连接信息, 常规配置修改
- 自由更改**传输配置**：
  - 常规TCP
  - HTTP头部伪装
  - WebSocket流量
  - 常规mKCP流量
  - mKCP 伪装 FaceTime通话流量(srtp)
  - mKCP 伪装 BT下载流量(utp)
  - mKCP 伪装 微信视频通话流量(wechat-video)
  - mKCP 伪装 DTLS 1.2流量(dtls)
  - mKCP 伪装 WireGuard流量(wireguard)
  - HTTP/2的tls流量(h2)(需备域名) 
  - Socks5
  - MTProto
  - Shadowsocks
  - Quic

## 安装命令

```bash
source <(curl -sL https://raw.githubusercontent.com/DockerCS/v2rayU/master/v2rayU.sh) --zh
```

## 升级命令(保留配置文件，升级失败请全新安装)
```bash
source <(curl -sL https://raw.githubusercontent.com/DockerCS/v2rayU/master/v2rayU.sh) -k
```

## 卸载命令
```bash
source <(curl -sL https://raw.githubusercontent.com/DockerCS/v2rayU/master/v2rayU.sh) --remove
```

## 命令行参数  
所有命令行参数支持**Tab**补全  
```bash
   v2ray -h                   查看帮助
   v2ray -v                   查看版本信息
   v2ray start                启动 V2Ray
   v2ray stop                 停止 V2Ray
   v2ray restart              重启 V2Ray
   v2ray status               查看 V2Ray 运行状态
   v2ray log                  查看 V2Ray 运行日志
   v2ray update               更新 V2Ray 到最新Release版本
   v2ray update [version]     更新 V2Ray 到特定版本
   v2ray update.sh            更新 v2rayU 脚本
   v2ray update.sh [version]  更新 v2rayU 到特定版本
   v2ray add                  新增mkcp + 随机一种 (srtp | wechat-video | utp) header伪装的端口(Group)
   v2ray add [wechat|utp|srtp|dtls|wireguard|socks|mtproto|ss]     新增一种协议的组，端口随机,如 v2ray add utp 为新增utp协议
   v2ray del                  删除端口组
   v2ray info                 查看配置
   v2ray port                 修改端口
   v2ray tls                  修改tls
   v2ray tfo                  修改tcpFastOpen
   v2ray stream               修改传输协议
   v2ray stats                iptables流量统计
   v2ray clean                清理日志
```
更多命令行参数请参考 [v2rayU wiki](https://github.com/DocerCS/v2rayU/wiki)


## 系统要求

- Debian 7 
- Debian 8
- **Debian 9（推荐）** 
- Ubuntu 14 
- Ubuntu 16 
- Ubuntu 18
- CentOS 7
- Fedora 28
- Fedora 29

**不支持Centos 6**


## 特别说明

有任何问题或者新功能想法欢迎提交 Issue。

本程序遵循 GPL v3协议发布，请Fork保留源项目地址，谢谢！

由于官方统计方式的限制, v2ray core重启就会重置统计流量数据！


## 感谢
Jrohy的multi-v2ray: [https://github.com/Jrohy/multi-v2ray](https://github.com/Jrohy/multi-v2ray)

V2ray: [https://v2ray.com](https://v2ray.com)

雨落无声的v2ray.fun: [YLWS-4617](https://github.com/YLWS-4617)
