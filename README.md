# 适用于rt-thread的milkv-duo系列bsp

编译后内核烧录文件位于install/BOARD目录

# 注意事项

* 1. 
要使用sdio请更新`driver/sdhci`子模块。

* 2. 
`boot.emmc`前添加了一个`mbr.img`分区表数据块，无法用原版fip.bin启动。

# usb烧录emmc版镜像

* 1. 对原始ROOTFS镜像文件处理成cimg (可选)

```
python3 image_tool/raw2cimg.py rootfs_ext4.emmc install/milkv-duos-emmc partition_emmc.xml
```
参数说明: 输入文件 输出目录 分区信息xml文件

`注意`: `输入文件名`须和XML中设置的文件名一致

* 2. 替换原版fip.bin

修改了uboot环境变量BOOT_PART_OFFSET的值为0x40

cv18xx-rv: 拷贝`cv18xx_risc-v\resource\fip\modified\fip.bin`到你的安装目录(如`install\milkv-duos-emmc`)

* 3. 拷贝partition_emmc.xml到你的安装目录


* 4. 烧录

参见: https://milkv.io/zh/docs/duo/getting-started/duos


* 备注：ROOTFS镜像不是每次必须烧录的文件

* :
```
.\usb_dl.exe -s linux -c cv181x -i .\install\milkv-duos-emmc
```
