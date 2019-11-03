import csv
import os
import xml.etree.ElementTree as ET

root_path = "/home/abin/my_works/github_works/faster_rcnn/datasets/annotations"
files = os.listdir(root_path)
train_file = open('/home/abin/my_works/github_works/faster_rcnn/datasets/train.csv', 'w')
csvwriter = csv.writer(train_file)

for file_name in files:
    annotation_file = root_path + "/" + file_name
    xml_doc = ET.parse(annotation_file).getroot()
    image_name = xml_doc.find('filename').text
    for object in xml_doc.findall('object'):
        image_sample = [image_name]
        cell_type = object.find('name').text
        image_sample.append(cell_type)
        xmin = object[4][0].text
        image_sample.append(xmin)
        xmax = object[4][2].text
        image_sample.append(xmax)
        ymin = object[4][1].text
        image_sample.append(ymin)
        ymax = object[4][3].text
        image_sample.append(ymax)
#        print(image_sample)
        csvwriter.writerow(image_sample)
train_file.close()