## Readme Information

1. **开源准则** 本文内容遵循开源准则，仅供学习和参考之用。对于任何基于本文项目或教程进行实际操作所产生的后果，作者概不负责。
2. **学习用途** 本文旨在对 Anki Vector 进行学习和研究，无任何商业用途。文中引用或参考了其他项目的内容，会尽可能标明出处，并在 **Reference** 中详细列举，欢迎指出文档错误。
3. **官方优先** 针对任何与 Anki Vector 相关的问题或疑问，请优先参考 Anki 官方发布的文档、版本及代码。

## Introduction

**Anki Vector** 是一款2018年10月推出的一款桌面机器人，直至今日(2025) 在各类新一代桌面机器人的身上都能看到其"影子"，但可惜它的母公司已经关闭，后续没有更多更好的更新和优化。但是，这不妨碍它是一款非常优秀的桌面机器人。

本文将包括以下几个部分的操作笔记 (包含当前已经完成和未来预想开发）：

- 已完成：
  - **Anki Vector 重置与启动**
    1. 适用于更换不同主机的场景（主机作为 Vector 的控制大脑，可以是电脑、手机或树莓派等）。
    2. Vector 在切换不同主机时适配性较弱，信号连接偶尔不稳定。
    3. 不同主机会分配不同的 Wire-Pod IP 地址，重置机器人后，Vector 的 Robot IP 地址也会发生变化，记得重新配置。
  - **Anki Vector 必要通信**
    1. 确保主机与 Vector 之间的通信正常，包括网络连接和认证文件的配置。
  - **Anki Vector 示例驱动**
    1. 通过官方或自定义例程（示例代码）驱动 Vector，实现具体功能。
- 待完成：
  - **Anki Vector** 语音交互（植入 AGI？）
  - **Anki Vector**  与多机多模态交互和多机智能控制
    - Anki Vector <--> Kinova gen3 
    - Anki Vector  <--> ...<-->...<-->...  ( keep it secret )
    - ![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjFjM2NiYzUwNmZiOWQzNDU5NjkxOWEzYjkzNmVmODhfUHFIUnByT20zcHY0REo4dWFkQ0hVRjg2MFd2N1hobFhfVG9rZW46SlZpbmJ5M01Vb0ZBWHF4R1RDNGNlYkpzbnlVXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

| 更新时间   | 更新内容     |
| ---------- | ------------ |
| 2025.01.08 | 入门操作笔记 |

## 入门

- 按照https://github.com/kercre123/wirepod-vector-python-sdk进行配置相关库
- 精简教程: https://keriganc.com/sdkdocs/install-windows.html 
- 如果是重新更换主机, 一定要记得reset robot。

### **Anki Vector 重置启动**

#### Reset robot

1. 如果Vector机器人更换了主机, 一定要对机器人进行更新配置:
   1. 将Vector 放置在充电仓，点击背部按钮两下，上-下运动爪子，转动履带，可以调整设置到 `RESET`，再按一下背部按钮即可。

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=MDljM2E3NDk1NTUzMzQ5ZGE0ZmI2NzE3NGYzNzMwMWVfc0xwVGdaeDN6NWlSMGs0Ukt3MnVFeFFYSGhsdjhvcHpfVG9rZW46TjlCMGIyc1NXb0ZBbW94MVY0dmMxMkVpbmRoXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

#### Bluetooth

1. 通过https://wpsetup.keriganc.com/html/main.html 网页，搜索蓝牙信号，对Vector机器人进行蓝牙连接，对其网络，地区进行设定。机器人显示应如下图所示。

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=YzcxMWZhZjlmYjQyZTZhY2U4MTFjNzc4Nzc1YTgzNDRfNTZrMFFUT0ptSU9lZlpZU3lxRkRRSm92ZFJZSUdlaTVfVG9rZW46SE42TGJOUUd5b3ZEekp4RE1jQmNZa0FDbkdlXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

> 由于我已经配置好了，忘了截图，此处引用两个视频：
>
> https://www.youtube.com/watch?v=aWmPzsmMXzM
>
> https://www.youtube.com/watch?v=8Hun_F3WGF8

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmIyMzkyOWY5YjY0ZDA0ZTJlYWZhMmY1NTk4OWEyYWNfem9Id2c1V0o5Y3plcDRScWs1cVlPS3dyWXZvRG5hR3JfVG9rZW46SE4xdWJHb0RjbzRCMlZ4OVgyamNucmxGbnV6XzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

- 右上角可见`Vector name` ，`Vector name` 是自动生成的，更换控制的主机会刷新，例如此处便是：Vector-P2W3。`Vector name`可以记录下来，在后面的 **Anki Vector** **例程驱动** 会用到
- `Vector serial number`也可以在此处记录一下，但`serial number`是固定的。
- 可以配置地区，温度单位和距离单位

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=YjFjNGJmZWFjMjA2ZmY2OTE2NmM1ZDFiNjU0NGMwZDRfZDQzOUk5SFMxWnl5ZTN6UUZ2Yk1wN0dmbXNrcnVTYmtfVG9rZW46QldBamJjY0pwb2hDQ0N4eEJvOGNma2l4bmpnXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

### **Anki Vector 必要通信**

- 由于**Anki Vector 研发团队**Digital Dream labs 服务器于已停用, 目前稳定可用的是使用开源的第三方服务Wire-Pod ([官方讯息](https://www.reddit.com/r/AnkiVector/comments/1agu0uj/information_for_new_vector_owners_in_2024/))
- **通信结构：**
  - **主机（开发者端） <--> Wire-Pod <--> Anki Vector**

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=MzU4ZDcwZTE0ODQ5YmQwN2Q4MmRmZDY3YWQwZjdlMmFfWTA3Y0Q1YmRHNzFHTVNWcGppYWFmOUFXekZTNlduSXVfVG9rZW46SExUTGJiQUNlb0o2d2h4QmN1RmNZRFIzbnplXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

#### Wire-Pod

- 获取最新版本的Wire-Pod：https://github.com/kercre123/WirePod/releases/tag/v1.2.13

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=NmYyOTA1MGU1MGY2MGFiY2U3Y2E3N2Q3ZGQ0MjhiYzZfU29Ua3V5NHRXZFFkRlJoemhXOTBtcWwyMmZYUTlPS3BfVG9rZW46VHhrOWJueElZb3padXB4OUZIT2MzYVBzbjNmXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

当前，我的环境是 `windows11`，因此我选择下载了 `WirePodInstaller-v1.2.13.exe`

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=MTQzZWEzNzNlNjY0MzFlOTI0NDcwMGQwMmZjYzRjYWVfMDVibVAyOVJ1VExNeGwwaFFib0UyQkw1dzhxd2JtMDRfVG9rZW46RHNTMWJQa1Zzb2M2NW54b1YzdWNWdWtobkFkXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

如果由于网络问题，无法正常驱动`WirePodInstaller-v1.2.13.exe` 的话，理论上可以在网站中下载wire-pod-win-amd64.zip，解压放到相应文件夹中，驱动即可。

正常下载驱动成功后，既可正常使用 Wire-Pod。理论上此时， Wire-Pod会缩放在 `Hide`栏中，点击 `Web Interface`，跳转进入网页端，即可出现下图所示界面。

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=MDdkNmYwYTY1ZWM3ZTBlMzJhMmNmZmZjNTg3NTUxNTBfMWdYTFNPYjN4V2lNR2FxSmUzd1NjU1FYaGU4eFVReXZfVG9rZW46TFl5VWJGYUpxb2lFeTV4NVRlYmNzZ3ZpbkZlXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=MjA5OWIxYjZmOTQwMzRmNWFjNTdiZGRjYzk0YTQzNDFfQ1VDMmxiYWs2aXVvN3BDS0hnNlZHS3RZYURsQ0dKWkdfVG9rZW46SU5pRGJsMkZ3b1h1VEZ4ZFd5cGNWUmNJbjNkXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

如果是出现这个界面：

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2UwMzNkMDFkNDg3MDM3MDVjNDhiZGJlMjUwZGI2MTBfRnlTOThCNjQ2M041bFJ4enNWeW9EZXdkdHduOVZoYWdfVG9rZW46SUhvVmJqbU1pb3lYMkl4dzRVQ2NqRVZ4bjZiXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

点击下面的`Submit Settings`即可。

由下图蓝色长方形框中可见，我们已经连接到一个 Vector 机器人。

此处，我们还可以看见我们的 `Wire-Pod IP Address`, 是`192.168.1.95:8080`。（这个 IP 地址是根据不同主机不同，8080是默认接口；这个地址在后面的 **Anki Vector** **例程驱动** 会用到）

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=NzBkZWY5ODc1ZDQ2ODk3ODljYWU3MmViZDE5OTZjZjRfUXgwTHJzcGRUUWVZU1Q4SlN2TW5QemwxYzBFZTFtU1FfVG9rZW46TTRjY2JjWjBrb0l0NzN4YkhPTWN0T2ZubmdnXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

点击鼠标指示的小机器人头像，便可以进入到已经写好的预设功能页面。

在此处，可以进行一些已经预设好的交互功能。例如：

- 打开相机实时画面 ： Control -> Camera Feed -> Begin Camera Stream
- 实时控制 Vector 移动，转动脑袋和挥动夹爪： Control -> Behavior Control -> Assume -> keyboard control (WASD for wheels, R-lift up, F-lift down, T-head up, G-head down)
- 进行简单的语音输出（英语）：Control -> Behavior Control -> Assume -> Say Text -> " hello world"

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=NTBkYjQ1ZThmNDQzMTIzNzk0NTRhNDViNjk2YmEyZjRfNkxxZnQ0Tlp4cklibjVLT0tVM3BkYUhZek5WU0FIZEZfVG9rZW46TncxOWI5Q2Fjb00zSmp4aERHM2M0NHBPbnhlXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

### **Anki Vector** **例程驱动**

此部分,主要引用的仓库是:https://github.com/anki/vector-python-sdk

#### **anki_vector.configure**

1. 首先，我们需要先监测我们的当前主机设备到Wire-Pod再到Vector机器人通信是否连接正常。

- (Windows PowerShell) 驱动程序： `py -m anki_vector.configure`
- `anki_vector.configure` 主要验证通信是否正确，并会在`C:\Users\<username>\.anki_vector` 中生成一个 `.cert` 文件和一个 `sdk_config.ini` 配置文件。

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=NzAyNTk5NmQ0ZmNjZmNhZGE0YjYwNTQ5YjI1NGYwZDhfNGc2THBLZnk0cXpLdUFLaXl5MDVPcWppa21oWW1pTkNfVG9rZW46Rklra2J3dmdFbzF1enR4NUpHSGNqclJabkFmXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

1. 在运行`anki_vector.configure`根据要求，输入Vector相关信息（根据前面的步骤，均可获取），如下：

```Python
Vector name=Vector-P2W3
Vector robot ip=192.168.1.130 
Computer Wire-Pod ip=192.168.1.95:8080
Vector serial number=00601e1f
```

- 重复提示一遍：
  - Vector name：可以在 **`Anki Vector 重置启动`**中 **`Bluetooth`**步骤中的右上角看见并记录。例如：**`Vector-P2W3`**
  - Vector robot ip ：将Vector 放置在充电仓，点击背部按钮两下，上-下运动爪子，可以找到 robot ip。
  - Computer Wire-Pod ip：Wire-Pod 驱动后，打开的网页链接（在` `**`Anki Vector 必要通信`**中 **`Wire-Pod`** 有提及。
  - Vector serial number：可以在 **`Anki Vector 重置启动`**中 **`Bluetooth`**步骤中的右上角看见并记录。

1. 下图是完整的成功的驱动配置截图（仅供参考）：

![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=YTViYTFjODIyYWJmMGRjYzdjMjVjNDMxMTZjNThiYjRfN1NJSlJzUTU5dHRkczJTM3lSeE43Rk9aOE1ySkRyS1FfVG9rZW46WjJodGJ5S1FXb0gwZmZ4RzlnVWNsY2VPbnJmXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

#### Py 01_hello_world.py

- cd进入代码文件夹下，文件相对位置一般处于：`\Vector\examples\tutorials`
- (Windows PowerShell) 驱动程序：py 01_hello_world.py 
  - 可以听到 Vector 发出声音

下面是所有tutorials例程测试结果：

| py   01_hello_world.py                | 说“helloworld”                                               |
| ------------------------------------- | ------------------------------------------------------------ |
| py   02_drive_square.py               | 沿正方形走一圈                                               |
| py 03_motors.py                       | 完成抬头抬臂走动等动作                                       |
| py 04_animation.py                    | 眼睛咪笑和左右摇摆挥臂表示高兴                               |
| py 05_drive_on_off_charger.py         | 自动找到充电桩，倒退进去后再驶出来，注意充电桩不能离太远，最好放在视线范围内 |
| py 06_face_image.py                   | 脸上播放一张图片，默认为vector图片，也可以自己加图片，放到C:\Users\hp\Desktop\Vector\examples\face_images，但图片必须为184×96 |
| py   07_dock_with_cube.py             | 贴近方块，注意方块不要放太远，最好在vector视线范围内         |
| py 09_eye_color.py                    | Vector眼睛变紫色5秒                                          |
| py 10_play_audio.py                   | 播放一段音效                                                 |
| py   11_drive_to_cliff_and_back_up.py | 直走直到碰到“悬崖”，即桌子边缘等，会停下倒退                 |
| py   16_face_follower.py              | Vector会跟随操作者的脸转动                                   |
| py dock_pick.py                       | Vector靠近方块，然后举起方块往前走                           |
| py 24_final_demo.py                   | Vector找到方块，在距离方块一段距离的时候，做出高兴表情（与py04动作一样），然后变换眼睛颜色，然后贴近方块，举起方块往前走。 |

### 配置遇到问题

1. `py -m anki_vector.configure` 遇到` cert does not exist`
   1. `Vector` 和 `Wire-Pod` 之间的认证不成功？
   2.  追溯问题：

   3. 运行和分析` py -m anki_vector.configure `！
      - C:\Users\Mike\AppData\Roaming\Python\Python39\site-packages\anki_vector\configure\__main__.py
      - 错误步骤：
        - ```Python
          def get_cert(serial=None):
              print("\n\nEnter the IP address and webserver port of your wire-pod instance (ex. 192.168.1.50:8080) (:8080 is the default port)\nLeave this blank and press enter if you want this script to attempt to automatically connect to your wire-pod instance via escapepod.local.")
              podip = input("Enter wire-pod ip: ")
              if podip == "":
                  podip = "escapepod.local:8080"
              serial = get_serial(serial)
              print("\nDownloading Vector certificate from wire-pod...", end="") # 1
              sys.stdout.flush()
              r = requests.get('http://{}/session-certs/{}'.format(podip, serial))
              # status_code 没有返回
              if r.status_code != 200:
                  print(colored(" ERROR", "red")) # 1
          ```
   4. 在 http://192.168.1.95:8080/session-certs/00601e1f 没有证书！
      - ![img](https://gao8483f74.feishu.cn/space/api/box/stream/download/asynccode/?code=NzdiYzI5NGMxYWIwYTFiZTQwNzY4NjgzZGFlYjk0ZGZfa3FidklyMXBZdkllUHB3ZDc5T1dKb0d2MHBUZ2lNZDBfVG9rZW46Wkk5dmJyVlUxb2RmOU14S3dHTWNYVWVSbmFoXzE3MzYzMzQ3NDk6MTczNjMzODM0OV9WNA)

      - 是不是获取的本地：C:\Users\Mike\AppData\Roaming\wire-pod\session-certs 数据？
   5. wire-pod有问题？没有生成证书？
      - 但为什么网页端app又可以用？
      - http://192.168.1.95:8080/sdkapp/settings.html?serial=00601e1f 正常使用
   6. Vector会feedback 给wire-pod它的配置, 所以如果更换了控制Vector的主机,一定要重置Vector! 重置后,即可正常连接, ` py -m anki_vector.configure ` 也可以正常生成 `.cert` 文件和 `sdk_config.ini` 配置文件

## Reference

- https://www.reddit.com/r/AnkiVector/comments/1agu0uj/information_for_new_vector_owners_in_2024/
- https://github.com/kercre123/wirepod-vector-python-sdk
- https://github.com/kercre123/wire-pod
- https://github.com/GooeyPancake/victor
- https://keriganc.com/sdkdocs/index.html