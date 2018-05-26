## Faster_RCNN for text detection

使用Faster_RCNN做文本检测

软件支持:

* python2.7

* tesnsorflow_gpu, cython, python-opencv,  easydict,  etc.

将ICDAR2011数据集简单制作成VOC2007格式, 放入Faster_RCNN

ICDAR数据文件: https://pan.baidu.com/s/1iswBSW5UIvHcT7xq2Iur3g  密码：fjtt



将数据文件中的VGG_imagenet.npy放到Faster-RCNN_TF\data\pretrain_model文件夹下

imagenet数据文件：https://pan.baidu.com/s/1UHlD7zpJyLO_5jHC27_ojw 密码：v3um



#### VOC2007结构

* JPEGImages文件夹 :   训练图片和测试图片

* Annatations文件夹 :  xml格式的标签文件

* ImageSets文件夹 :  Action暂时不用  Layout暂时不用

 * Main存放的是图像物体识别的数据，Main里面有test.txt , train.txt, val.txt,trainval.txt.


#### 数据制作
直接将ICAR2011的训练集图片放入JPRGImages

xml.py:  用于制作.xml文件

generate_maintxt.py:  用于生成Main文件夹下的.txt文件

#### 构建Cython模块
```bash
cd $FRCN_ROOT/lib
make
```


#### 测试模型
```bash
cd $FRCN_ROOT
python ./tools/demo.py --model model_path
```


#### 训练模型
```bash
cd $FRCN_ROOT
./experiments/scripts/faster_rcnn_end2end.sh  DEVICE   DEVICE_ID  VGG16 pascal_voc
```




