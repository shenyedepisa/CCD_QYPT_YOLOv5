import csv
import os
import shutil


def statistics(name):
    imgDir = os.listdir(name)
    imgPath = os.path.abspath('{}'.format(name))
    originPath = os.path.abspath('{}_origin'.format(name))
    addictPath = os.path.abspath('{}_addict'.format(name))
    labelsDir = os.listdir('labels')
    labelsPath = os.path.abspath('labels')
    labelOriginPath = os.path.abspath('labels_origin'.format(name))
    labelAddictPath = os.path.abspath('labels_addict'.format(name))
    if not os.path.exists(originPath):
        os.mkdir(originPath)
    if not os.path.exists(addictPath):
        os.mkdir(addictPath)
    if not os.path.exists(labelOriginPath):
        os.mkdir(labelOriginPath)
    if not os.path.exists(labelAddictPath):
        os.mkdir(labelAddictPath)
    for label in imgDir:
        path1 = imgPath + '\\' + label
        path2 = addictPath + '\\' + label
        path3 = originPath + '\\' + label
        if label[12] == '_':
            shutil.copy(path1, path2)
        else:
            shutil.copy(path1, path3)
    for label in labelsDir:
        path1 = labelsPath + '\\' + label
        path2 = labelAddictPath + '\\' + label
        path3 = labelOriginPath + '\\' + label
        if label[12] == '_':
            shutil.copy(path1, path2)
        else:
            shutil.copy(path1, path3)


if __name__ == '__main__':
    dirName = input("文件名: ")
    statistics(dirName)
