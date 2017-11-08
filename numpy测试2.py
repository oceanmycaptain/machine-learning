import numpy as np

# x = np.array([[1,2,3],[4,5,6]])
# y = np.array([[6,23],[-1,7],[8,9]])
# print(np.ones(3))
# print(np.dot(x,np.ones(3)))

# print(x.dot(y))
# from numpy.linalg import inv,qr
# x =np.random.randn(5,5)
# #print(x)
# mat =x.T.dot(x)#这个是什么意思，完全看不懂‘T’是咋回事？该‘T’指的x的转置（可百度详解）。
# #print(mat)
# #print(x)
# #print(mat.dot(mat))#需要多多了解矩阵之间的相乘。
# samples = np.random.normal(size=(4,4))
#print(samples)

# nsteps = 1000
# draws = np.random.randint(0,2,size=nsteps)
# steps = np.where(draws > 0 ,1,-1)
# walk = steps.cumsum()
# #print(walk)
# print(walk.min())
# print(walk.max())

# nwalks = 5000
# nsteps = 1000
# draws = np.random.randint(0,2,size=(nwalks,nsteps))
# steps = np.where(draws>0,1,-1)
# walks = steps.cumsum(1)
# print(walks.max())
# print(walks.min())
# hits30 = (np.abs(walks)>= 30).any(1)
# print(hits30)
# print(hits30.sum())

# x = np.array([[1,2],[3,4]])
# print(np.sum(x,axis=0))

# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([[7,8,9],[10,11,12]])
# a = np.concatenate([arr1,arr2])
# print(a)

# arr = np.arange(3)
# print(arr.repeat([2,3,4]))

# arr = np.random.randn(2,2)
# print(arr)
# print(arr.repeat([2,3],axis=1))#axis的值代表的轴的方向

# arr = [[0.7157,-0.6387],[0.3626,0.849]]
# print(np.tile(arr,2))#默认是复制行数2次。
#print(np.tile(arr,(4,3)))#行复制4次，列复制3次，即代表这样的意义。

# arr = np.arange(10)*100
# inds = [7,1,2,6]
#print(arr[inds])
#print(arr.take(inds))

# inds = [2,0,2,1]
# arr =np.random.randn(2,4)
# print(arr)
# print(arr.take(inds,axis=1))

# arr = np.arange(5)
# print(arr)
# print(arr*4)

# arr = np.random.randn(4,3)
# print(arr)
# print(arr.mean(0))#此时是取我们的各个平均值，数字'0'自然是取列的平均，‘1’就是行的平均值
# demeaned = arr - arr.mean(0)
# print(demeaned)

# arr = np.random.randn(4,3)
# print(arr)
# row_means = arr.mean(1)
# print(row_means)
# a = row_means.reshape((4,1))
# print(a)
# demeaned = arr - a
# print(demeaned.mean(1))

# arr =np.random.randn(3,4,5)
# depth_means = arr.mean(2)
# print(depth_means)
# demeaned = arr - depth_means[:,:,np.newaxis]
# print(demeaned.mean(2))

# arr = np.zeros((4,3))
# arr[:] = 5
#print(arr)

# arr = np.zeros((4,3))
# col = np.array([1.28,-0.42,0.44,1.6])
# arr[:] = col[:,np.newaxis]
# arr[:2] = [[-1.37],[0.509]]
# print(arr)

# arr = np.arange(10)
# a = np.add.reduce(arr)
# b =arr.sum()
# print(b)

# arr = np.random.randn(5,5)
# arr[::2].sort(1)
# print(arr)
# print(arr[:,:-1])#此时除掉了数组的最后一列
# print(arr[:,1:])#此时除掉了最后一列
# a0 = np.logical_and.reduce(arr[:,:-1]<arr[:,1:],axis=0)#判断列数的是否可序
# a1 = np.logical_and.reduce(arr[:,:-1]<arr[:,1:],axis=1)#判断行数的是否可序
# print(a0)
# print(a1)


