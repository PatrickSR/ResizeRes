## ResizeRes
Automatic Generate Android Resource Image Size

（自动生成Android图片资源）


## Background
在csdn无意看到的
[《自动生成Android不同分辨率下的图片》](http://blog.csdn.net/offbye/article/details/50012605)
大致看了一下觉得挺不错的

但是估计作者是在windows下面开发Android，所以没遇到像Mac下面存在.DS_Store 的情况导致运行失败。

然后我就直接copy出来自己维护了

同时原作者是用Python2.x来运行的,然后我改了3.x,因为在我的电脑通常拿py3.5来运行的

##Feature
自动把xxhdpi目录的图片生成xhdpi/hdpi/mdpi

然而之后只需叫美工切一张size的图：xxhdpi

##Usage

>Tips:
>	
>	Python 版本需要 3.5	
>	
>	需要安装PIL模块
>		安装方法：pip install PIL
>
>	需要压缩的图片记得放在xxhdpi目录下
>

###```python Resize.py [Project Path]/src/main/res```

然后就没然后了..
