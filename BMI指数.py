'''height=float(input("your height："))
weight=float(input("your weight："))
bmi=weight/(height*height)
print("your bmi="+str(bmi))
if bmi<18.5:
    print("过轻")
if bmi>=18.5 and bmi<22.9:
    print("正常")
if bmi>=22.9 and bmi<29.9:
    print("过重")
if bmi>=29.9:
    print("肥胖")'''
height,weight=eval(input("请输入身高和体重："))
bmi=weight/pow(height,2)
print("BMI指数为：{:.2f}".format(bmi))
who,nat="",""
if bmi<18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    who,nat="正常","正常"
elif 24<=bmi<25:
    who,nat="正常","偏胖"
elif 25<=bmi<28:
    who,nat="偏胖","偏胖"
elif 28<=bmi<30:
    who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("BMI指标为：国际'{0}',国内'{1}'".format(who,nat))