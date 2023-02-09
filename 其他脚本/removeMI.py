import csv
import os
import shutil


def statistics(name):
    txtDir = os.listdir(name + "/txt")
    imgesPath = os.path.abspath('{}\\images'.format(name))
    cankaoPath = os.path.abspath('{}\\cankao'.format(name))
    newPath = os.path.abspath('{}\\newFeimi'.format(name))
    missPath = os.path.abspath('{}\\missImg'.format(name))
    imgPath = os.path.abspath('{}\\origin'.format(name))
    if not os.path.exists(missPath):
        os.mkdir(missPath)
    if not os.path.exists(newPath):
        os.mkdir(newPath)
    if not os.path.exists(cankaoPath):
        os.mkdir(cankaoPath)
    with open('./{}/txtResult.csv'.format(name), 'w', encoding='utf-8_sig') as f2:
        for txt in txtDir:
            num = 0
            # print(txt)
            txtResult = open("{}/txt/{}".format(name, txt), 'r', encoding='utf-8')
            count = txtResult.readlines()
            for sentence in count:
                for word in sentence:
                    if word == '密':
                        num += 1
            idjpg = "\\" + txt[0:-4] + ".jpg"
            path1 = imgPath + idjpg
            if num > 0:
                f2.write("".join(txt) + "," + str(num) + "\n")
                path2 = missPath + idjpg
                shutil.copy(path1, path2)
                path3 = imgesPath + idjpg
                path4 = cankaoPath + idjpg
                shutil.copy(path3, path4)
            else:
                path5 = newPath + idjpg
                shutil.copy(path1, path5)


if __name__ == '__main__':
    dirName = input("文件名: ")
    statistics(dirName)
