import os


def oneline():
    labelsDir = os.listdir('labels')
    labelsPath = os.path.abspath('labels')
    print(labelsPath)
    with open('not_one_line.txt', 'w') as f1:
        for label in labelsDir:
            count = len(open('{}\{}'.format(labelsPath, label), 'r').readlines())
            if count != 1:
                f1.write(label + '    ' + str(count) + '\n')


if __name__ == '__main__':
    oneline()
