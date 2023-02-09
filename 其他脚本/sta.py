import csv
import os
import shutil


def statistics(name):
    labelsDir = os.listdir(name + "/labels")
    txtDir = os.listdir(name + "/txt")
    countNum = 0

    with open('./{}/labels.csv'.format(name), 'w', encoding='utf-8_sig') as f1:
        for label in labelsDir:
            # oldDir = os.path.join(labelsDir, label)
            # print(label)
            labelLen = open("{}/labels/{}".format(name, label), 'r', encoding='utf-8')
            count = labelLen.readlines()
            # print(len(count))
            f1.write(label + "," + str(len(count)) + "\n")

    with open('./{}/txtResult.csv'.format(name), 'w', encoding='utf-8_sig') as f2:
        for txt in txtDir:
            num = 0
            countNum += 1
            # print(txt)
            txtResult = open("{}/txt/{}".format(name, txt), 'r', encoding='utf-8')
            count = txtResult.readlines()
            for sentence in count:
                for word in sentence:
                    if word == '密':
                        num += 1
                        # print(word)

            f2.write("".join(txt) + "," + str(num) + "\n")
    return countNum


def final(name, lenNum):
    pathImages = os.path.abspath('{}\\images'.format(name))
    pathOrigin = os.path.abspath('{}\\origin'.format(name))
    pathImg = os.path.abspath('{}\\newImg'.format(name))
    if not os.path.exists(pathImg):
        os.mkdir(pathImg)
    pathRefer = os.path.abspath('{}\\newRefer'.format(name))
    if not os.path.exists(pathRefer):
        os.mkdir(pathRefer)
    f1 = open('./{}/Result.csv'.format(name), 'w', encoding='utf-8_sig', newline='')
    csvF1 = csv.writer(f1)
    f2 = open('./{}/labels.csv'.format(name), 'r', encoding='utf-8_sig')
    csvF2 = csv.reader(f2)
    f3 = open('./{}/txtResult.csv'.format(name), 'r', encoding='utf-8_sig')
    csvF3 = csv.reader(f3)
    f4 = open('./{}/warning.csv'.format(name), 'w', encoding='utf-8_sig', newline='')
    csvF4 = csv.writer(f4)
    csvF1.writerow(["id", "密字数量", "检出数量"])
    csvF4.writerow(["id", "标注数量", "检出数量"])
    it2 = iter(csvF2)
    it3 = iter(csvF3)
    total = 0
    fact = 0
    loss = 0

    for i in range(lenNum):
        t1 = next(it2)
        t2 = next(it3)
        id = t1[0]
        mark = t1[1]
        det = t2[1]
        total += max(int(mark), int(det))
        # total += int(mark)
        fact += int(det)
        csvF1.writerow([id, max(int(mark), int(det)), det])
        if int(mark) > int(det):
            loss += 1
        if int(mark) < int(det):
            csvF4.writerow([id, mark, det])
            idjpg = "\\" + id[0:-4] + ".jpg"
            path1 = pathImages + idjpg
            path2 = pathOrigin + idjpg
            path3 = pathRefer + idjpg
            path4 = pathImg + idjpg
            shutil.copy(path1, path3)
            shutil.copy(path2, path4)
    with open('./{}/accuracy.txt'.format(name), 'w', encoding='utf-8_sig') as f5:
        f5.write("图片总数 {}, 其中 {} 张图片存在漏检\n".format(lenNum, loss))
        f5.write("密字数量总计:   {}\n检出密字总计: {}\n检出率:    {}\n".format(total, fact, fact / total))
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    os.remove('./{}/labels.csv'.format(name))
    os.remove('./{}/txtResult.csv'.format(name))


if __name__ == '__main__':
    dirName = input("文件名: ")
    n = statistics(dirName)
    final(dirName, n)
