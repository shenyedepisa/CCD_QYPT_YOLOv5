import cv2
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='add noisy for images')
    parser.add_argument('-s', '--src', type=str, default='../dataset/a', help='source path')
    parser.add_argument('-d', '--dst', type=str, default='../dataset/a_gray', help='destination path')
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
        orig_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)
        img_dst = os.path.join(result_path, file_path)
        print(img_dst, end=" ")
        if cv2.imwrite(img_dst, orig_image):
            print('done')
        else:
            print('fail')
