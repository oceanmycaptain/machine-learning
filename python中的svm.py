import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib as mpl
from matplotlib import colors
import matplotlib.pyplot as plt


'''导入数据'''
def iris_type(s):
    it = {b'Iris-setosa':0,b'Iris-versicolor':1,b'Iris-virginica':2}
    return it[s]

path = 'data\\iris.txt'
data = np.loadtxt(path,dtype=float,delimiter=',',converters={4:iris_type})
#在我们将数据划分时我们得注意一下，博主的在定义时'Iris-setosa'应该定义成b’Iris-setosa',不然会报keyerror。

'''将Iris划分训练集与测试集'''
x,y = np.split(data,(4,),axis=1)
x = x[:,:2]
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,train_size=0.6)
#这块数据集随机抽样来让划分训练集和测试集

'''训练svm分类器'''
#clf = svm.SVC(C=0.1,kernel='linear',decision_function_shape='ovr')
clf = svm.SVC(C=0.8,kernel='rbf',gamma=20,decision_function_shape='ovr')
clf.fit(x_train,y_train.ravel())
#kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）
#kernel='rbf'时，为高斯核，gamma值越小
#decision_function_shape='ovr'时，为one v rest,即一个类别与其他类别进行划分
#decision_function_shape='ovo'时，为one v one ，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果

'''计算svc分类器的准确度'''
print(clf.score(x_train,y_train))#精度
y_hat = clf.predict(x_train)
print('训练集的正确率:%s'%accuracy_score(y_hat,y_train))
print(clf.score(x_test,y_test,))
y_hat = clf.predict(x_test)
print('测试集的正确率:%s'%accuracy_score(y_hat,y_test))

'''绘制图像'''
x1_min,x1_max = x[:,0].min(),x[:,0].max()#第0列的范围
x2_min,x2_max = x[:,1].min(),x[:,1].max()#第1列的范围
x1,x2 = np.mgrid[x1_min:x1_max:200j,x2_min:x2_max:200j]#生成网格采样点
grid_test = np.stack((x1.flat,x2.flat),axis=1)#测试点

'''指定默认字体'''
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
#没有这一步我们的打出的汉字都成为了框框了。

'''绘制'''
cm_light = mpl.colors.ListedColormap(['#A0FFA0','#FFA0A0','#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g','r','w'])
#这里是几种颜色的显示
grid_hat = clf.predict(grid_test)#预测分类值
grid_hat = grid_hat.reshape(x1.shape)#使之与输出的形状相同
plt.pcolormesh(x1,x2,grid_hat,cmap = cm_dark)
plt.scatter(x[:,0],x[:,1],c=y,edgecolors='k',s=50,cmap=cm_dark)#样本
plt.scatter(x_test[:,0],x_test[:,1],s=120,facecolors='none',zorder = 10)#圈中测试集样本
plt.xlabel(u'花萼长度',fontsize = 13)
plt.ylabel(u'花萼宽度',fontsize = 13)
#fontsize = 13为了改变字体的大小
plt.xlim(x1_min,x1_max)
plt.ylim(x2_min,x2_max)
plt.title('鸢尾花svm二特征分类',fontsize=13)
plt.show()


