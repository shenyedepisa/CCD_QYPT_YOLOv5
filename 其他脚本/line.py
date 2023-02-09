import os


def lines():
    labelsDir = os.listdir('labels')
    labelsPath = os.path.abspath('labels')
    # l1Dir = os.listdir('labels1')
    # l1Path = os.path.abspath('labels1')
    # l2Dir = os.listdir('labels2')
    # l2Path = os.path.abspath('labels2')
    print(labelsPath)

    count = 0
    for label in labelsDir:
        count += len(open('{}\{}'.format(labelsPath, label), 'r').readlines())
    print('label ' + str(count))

    # count = 0
    # for label in l1Dir:
    #     count += len(open('{}\{}'.format(l1Path, label), 'r').readlines())
    # print('label1 ' + str(count))
    #
    # count = 0
    # for label in l2Dir:
    #     count += len(open('{}\{}'.format(l2Path, label), 'r').readlines())
    # print('label2 ' + str(count))


if __name__ == '__main__':
    lines()
