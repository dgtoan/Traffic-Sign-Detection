import pandas as pd

PATH =  "D:\\x64\\New folder\\images" #path đến file ảnh
data = pd.read_csv("annotation.csv")
bbox = data.bbox
category_id = data.category_id
image_name = data.file_name

#format từ coco label sang yolo
W = 1622
H = 626
bbox = [i.replace("[", "").replace("]", "").replace(" ", "").split(",") for i in bbox] # loại các dấu [ ] và dấu cách trong string để chuyển đổi về int
bbox = [list(map(int, i)) for i in bbox]                                               # chuyển về int          
bbox = [[(i[0]+i[2]/2)/W, (i[1]+i[3]/2)/H, i[2]/W, i[3]/H] for i in bbox]                  # format từ coco sang yolo

# append các thứ để có 1 list chứa các item dạng id + bbox + tên ảnh
image_name = [i.replace(".png", "") for i in image_name]
list_data = [list(i) for i in zip(category_id, bbox, image_name)]
tmp = []
for i in list_data:
    tmp.append([i[0]] + i[1] + [i[2]])
list_data = tmp

# mỗi lần chạy thì xóa hết file txt trong dir
import sys
import os
from os import listdir
test=os.listdir(PATH)
for item in test:
    if item.endswith(".txt"):
        os.remove(os.path.join(PATH, item))
        
# tạo file label       
for i in list_data:
    txt_file = file_jpg = PATH + "\\" +i[-1] + ".txt"
    f = open(txt_file, "a")
    i[1:-1] = [format(x, '.6f') for x in i[1:-1]]
    content = str(i[0]-1) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3]) + ' ' + str(i[4]) + ' ' + '\n'
    f.write(content)
    print(txt_file)
    f.close()
    
    