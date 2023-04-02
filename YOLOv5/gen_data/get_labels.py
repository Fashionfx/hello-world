import xml.dom.minidom as xmldom
import os
# annotation_path = os.getcwd() + "\Annotations"
annotation_path='h:/Repository/Gastric-cancer-image-recognition-system/YOLOv5/Annotations'
annotation_names=[os.path.join(annotation_path,i) for i in os.listdir(annotation_path)]
print(annotation_path)
labels = list()
for names in annotation_names:
    xmlfilepath = names
    domobj = xmldom.parse(xmlfilepath)
    elementobj = domobj.documentElement
    subElementObj = elementobj.getElementsByTagName("object")
    for s in subElementObj:
        label=s.getElementsByTagName("name")[0].firstChild.data
        #print(label)
        if label not in labels:
            labels.append(label)
print(labels)