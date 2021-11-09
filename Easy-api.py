from aip import AipImageClassify
APP_ID='24943035'
API_KEY='4MAW5NSf9GReuVDsXByKRYM5'
SECRET_KEY='nU8Nemwyz1Lrzw8f7uqzKadDcP9bZ2QG'
client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)  #实现api接口的调用
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()  #读取图片

image=get_file_content('e:\\py\\api接口\\example.jpg')  #输入要识别的图片
images=client.advancedGeneral(image)  #调用库中不带参数的图像识别
options={}
#带参数调用图像识别
options["baike_num"] = 5
client.advancedGeneral(image,options)
print(images)