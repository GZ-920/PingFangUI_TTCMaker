# PingFangUI_TTCMaker

这是一个用来快捷制作iOS上的`PingFangUI.ttc`文件的脚本，运行环境为Python，可以利用Lara等工具替换/复写。

## 使用方法（以iOS设备为例）

1. App Store安装 **a-Shell**
2. 打开a-Shell，运行以下命令：
   ```bash
   cd ~/Documents
   curl -L -o make.py https://raw.githubusercontent.com/GZ-920/PingFangUI_TTCMaker/main/make.py
   curl -L -o names.json https://raw.githubusercontent.com/GZ-920/PingFangUI_TTCMaker/main/names.json
   curl -L -o hywh.ttf https://raw.githubusercontent.com/GZ-920/PingFangUI_TTCMaker/main/hywh.ttf
   ls
```

最后一行输出能看到 make.py、names.json 和 hywh.ttf 即为成功。

1. 打开 文件 app，点击“我的iPhone/iPad”，找到 a-Shell 文件夹，将你需要替换的字体文件丢入（ttf 或 otf）。
2. 打开a-Shell，运行以下命令：
   ```bash
   python3 make.py {你的字体文件名}.ttf
   ```
3. 若成功，可在a-Shell文件夹下找到 PingFangUI.ttc 文件。

## 使用Lara替换字体方法

1. 点击 设置，选择 Hybird。
2. 点击 Run Exploit，等待后出现蓝色的 Escape Sandbox，点击后出现 Initialise VFS，点击后出现白色的 Tweaks，点击它。
3. 第一个 Font Overwrite 是替换西文字体，本教程使用 Custom Overwrite 替换中文字体。点击 Custom Overwrite。
4. 在第一行“/”后面输入：
   ```
   System/Library/PrivateFrameworks/FontServices.framework/CorePrivate/PingFangUI.ttc
   ```
5. 点击蓝色的 Choose Source File。
6. 选择刚刚生成的 PingFangUI.ttc 文件。
7. 点击蓝色的 Overwrite Target。
8. 注销设备。
9. 大功告成！
