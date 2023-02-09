import cv2
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add noisy for images')
    parser.add_argument('-s', '--src', type=str, default='../dataset/d/images', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='../dataset/d_label', help='destination path')
    args = parser.parse_args()
    print(args.src)
    print(args.dst)

    if not os.path.exists(args.src):
        print('source path not exists')
        exit(0)
    if not os.path.exists(args.dst):
        os.mkdir(args.dst)
    
    my_path = args.src
    result_path = args.dst
    
    listdir = os.listdir(my_path)
    for file_path in listdir:
        img_path = os.path.join(my_path, file_path)
        orig_image = cv2.imread(img_path)
        image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)
        txt_path = img_path.replace('images', 'labels').replace('.jpg', '.txt')
        with open(txt_path, 'r') as txtfile:
            labelbox = txtfile.readline()
            centerx = float(labelbox.split(' ')[1]) * orig_image.shape[1]
            centery = float(labelbox.split(' ')[2]) * orig_image.shape[0]
            width = float(labelbox.split(' ')[3]) * orig_image.shape[1]
            height = float(labelbox.split(' ')[4]) * orig_image.shape[0]
            xmin = int(centerx - width/2)
            xmax = int(centerx + width/2)
            ymin = int(centery - height/2)
            ymax = int(centery + height/2)
            cv2.rectangle(orig_image, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
            # cv2.circle(orig_image, (int(centerx), int(centery)), int(width/1.5), (0, 0, 255), 2)
        cv2.imwrite(os.path.join(result_path, file_path), orig_image)
        print(file_path)
