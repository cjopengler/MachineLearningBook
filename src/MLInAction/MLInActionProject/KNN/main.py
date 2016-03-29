# coding:utf-8

import knn
import classifyPerson as cp

def main():
    print 'Main Begin******************'

    group, labels = knn.createDataSet()

    print group,'\n',labels

    predict = [1, 0.9]
    label = knn.classify0(predict, group, labels, 3)

    print predict,' lable is: ', label

    cp.predict()


    print 'Main End********************'

if __name__ == '__main__':
    main()