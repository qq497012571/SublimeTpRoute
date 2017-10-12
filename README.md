## sublime text 3的php插件
### 适用php框架Thinkphp3

### 更新日志
> 2017年10月11日

1. 支持直接路由匹配视图

2. 新增匹配方法中的参数

### 安装

1. 打开

```
Preferences->Browsswer Packages

```
2. 新建一个文件夹TpRoute
3. 项目的所有文件复制进TpRoute文件夹

### 用处介绍

解决频繁手工输入url地址来调试功能,根据插件的配置的路由规则快速打开指定方法

> 插件设置

```
设置
Preferences->Package Settings->TpRoute->Settings - User
{
	"tp_host" : "http://localhost/index.php?m={m}&a={a}&c={c}",
}
```

> {m}模块，{c}控制器，{a}方法

### 快捷键

> F9

### 效果

![image](https://github.com/qq497012571/SublimeTpRoute/blob/master/images/%E6%BC%94%E7%A4%BA1.gif)
