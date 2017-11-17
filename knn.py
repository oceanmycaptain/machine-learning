import numpy as np
from sklearn import neighbors
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import  classification_report
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

'''数据的读入'''
data = []
labels = []
with open('data\\1.txt') as ifile:
    for line in ifile:
        tokens = line.strip().split(' ')
        #print(tokens[:2])
        data.append([float(tk) for tk in tokens[:2]])
        labels.append(tokens[2])
x = np.array(data)
#将x的数据集用数组表示出来
labels = np.array(labels)
y = np.zeros(labels.shape)

#将数据的fat和thin转变成0和1
y[labels=='fat'] = 1

'''拆分训练数据与测试数据'''
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
#x：所要划分的样本特征。y：所要划分的样本结果。test_size：样本占比，如果是整数就是样本的数量。
#帮我们随机挑选训练集和测试集，这样我们的每次输出的结果不一样的原因就在这里了
#print(x_train,x_test,y_test,y_train)

'''创建网格以方便绘制'''
h = 0.01
x_min,x_max = x[:,0].min()-0.1,x[:,0].max()+0.1
y_min,y_max = x[:,1].min()-1,x[:,1].max()+1
xx,yy = np.meshgrid(np.arange(x_min,x_max,h),
                    np.arange(y_min,y_max,h))

'''训练KNN分类器'''
clf = neighbors.KNeighborsClassifier(algorithm='kd_tree')
#这一步可以用来设置我们的三种算法:"brute","kd_tree","ball_tree",如果不知道也可以用"auto"让KNeighborsClassifier自动选择
clf.fit(x_train,y_train)

#测试结果的打印
answer = clf.predict(x)
print(x)
print(answer)
print(y)
print(np.mean(answer==y))

'''准确率与召回率'''
precision,recall,thresholds = precision_recall_curve(y_train,clf.predict(x_train))
answer = clf.predict(x)
print(classification_report(y,answer,target_names=['thin','fat']))

'''将整个测试空间的分类结果用不同颜色区分开'''
answer = clf.predict_proba(np.c_[xx.ravel(),yy.ravel()])[:,1]
z = answer.reshape(xx.shape)
plt.contourf(xx,yy,z,alpha = 0.8,cmap = plt.cm.gray)
#该处的cmap用来调整我们的颜色'http://blog.csdn.net/haoji007/article/details/52063168'该处可以看看cmap的用法

'''绘制训练样本'''
plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap=plt.cm.cool)
plt.xlabel('身高')
plt.ylabel('体重')
plt.show()
#每次跑时候的得到的结果都不一样，可能是和每次他选择的训练集和测试集不一样，导致模型训练准确度不一样。
#但是怎么说还是到达不了，我看的博客的博主的0.94的准确性，最多的是0.88很奇怪。