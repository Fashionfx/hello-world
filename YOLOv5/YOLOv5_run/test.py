import os
file = "H:\Repository\yolov5-master\yolov5-master\data\VOC.yaml"
file = str(file)  # convert to str()
print(file)
with open('H:/Repository/yolov5-master/yolov5-master/data/VOC.yml',"r",encoding="UTF-8") as f:
    print("open sucss")
if os.path.isfile(file) or not file:  # exists
    print("YES!!!")
else:
    print("NO")