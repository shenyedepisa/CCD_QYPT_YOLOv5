import os
import shutil


def warning():
    pathImg = os.path.abspath('images')
    labelsDir = os.listdir('labels')
    labelsPath = os.path.abspath('labels')
    l1Dir = os.listdir('labels3')
    l1Path = os.path.abspath('labels3')
    pathnewImg = os.path.abspath('NewImg')
    pathNew = os.path.abspath('newLabel')
    pathNew1 = os.path.abspath('newLabel3')
    if not os.path.exists(pathnewImg):
        os.mkdir(pathnewImg)
    if not os.path.exists(pathNew):
        os.mkdir(pathNew)
    if not os.path.exists(pathNew1):
        os.mkdir(pathNew1)

    i = 0
    with open('warn.txt', 'w') as f1:
        f1.write('id    标注数    检出数\n')
        for file in labelsDir:
            print(file)
            print(l1Dir[i])
            count = len(open('{}\{}'.format(labelsPath, file), 'r').readlines())
            count1 = len(open('{}\{}'.format(l1Path, l1Dir[i]), 'r').readlines())
            if count1 > count:
                f1.write(file + '    ' + str(count) + '    ' + str(count1) + '\n')
                idjpg = '\\' + file[0:-4] + '.jpg'
                path1 = pathImg + idjpg
                path2 = pathnewImg + idjpg
                path3 = labelsPath + '\\' + file
                path4 = l1Path + '\\' + l1Dir[i]
                path5 = pathNew + '\\' + file
                path6 = pathNew1 + '\\' + l1Dir[i]
                shutil.copy(path1, path2)
                shutil.copy(path3, path5)
                shutil.copy(path4, path6)
            i += 1


if __name__ == '__main__':
    warning()
