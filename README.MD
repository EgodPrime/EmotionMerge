# EMOTION MERGE

> QQ表情融合

<img src="https://github.com/SingleBone/EmotionMerge/edit/main/imgs/show.png" style="zoom:80%;" />

## 环境需求

* Python3(3.8已测)
* PIL
* PyQt5

### 安装示例

```bash
# install python3.8 by your self
pip install PyQt5
pip install pillow
```

> Python3中Pillow就是PIL

## 使用

### 转换GIF为PNG

> QQ表情原图像可从百度获取，其原始格式为gif，需先转换为png

```bash
python3 gif2png.py
```

### 运行程序

```bash
python3 main.py
```

## 缺陷

部分图像中的表情不一定在正中间，融合时会看到明显的错位

如果加入自定义表情，尽量选择正方形png图片，且表情在正中间
