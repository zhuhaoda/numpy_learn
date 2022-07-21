###########author：All.Z 朱浩达 7.19################
"""
此代码为自学时瞎敲的，如果你用numpy的时候突然大脑宕机，可以拿来查一查代码咋写。

为啥要用nupmy呢？众所周知，在进行复杂的数据结构分析与神经网络计算时，
python本身的解释器实在是太拉了，可能会遇到频率瓶颈。
而numpy的底层使用c来写的，在计算时将代码解释成C语言的格式，
并且其内部优化了计算方法，占用内存更小，
所以对于提高计算速度有显著作用。
如果在git上看到这段项目，麻烦给卑微小朱一个star吧，犒劳一下在萨拉热窝（实验室别称）被蚊子叮脸的我（doge）。

使用NumPy，开发人员可以执行以下操作：

数组的算数和逻辑运算。

傅立叶变换和用于图形操作的例程。

与线性代数有关的操作。 NumPy 拥有线性代数和随机数生成的内置函数。
"""

import numpy as np

if __name__ == '__main__':

    mat=np.array([[1,2,3],[2,3,4]],ndmin=4)
    # print(mat)
    # print(mat.shape)

    dt=np.dtype([('age',np.int8)])
    a=np.array([(10),(20)],dtype=dt)
    # print(a['age'])
    dt1=np.dtype([('name','S20'),('age','i2')])
    # print(dt1)

    #TODO:reshape
    mat1=np.array([[1,2,3],[2,3,4]]).reshape(3,2)
    # print(mat1)

    mat2=np.arange(24).reshape(4,6)
    # print(mat2)

    #TODO:返回字节长度

    mat3=np.array([1,2,3,4,5],dtype=np.float32)
    # print(mat3.itemsize)
    """返回4个字节"""

    #TODO:空与0与1（doge）
    mat=np.empty([3,3],dtype=float)
    # print(mat)
    """与array相似，也可以自定义dtype数据类型"""
    mat=np.zeros([4,4])
    # print(mat)
    mat=np.ones([5,5])
    # print(mat)
    mat=np.ones(4)
    # print(mat)

    #TODO:转化原有数据
    x=[1,2,3,4,50]
    y=[(1,2,3),(4,5)]
    c='fuck you'

    mat=np.asarray(x,dtype=float)
    # print(mat)

    mat=np.asarray(y)
    # print(mat)

    # mat5=np.frombuffer(c,dtype='S1')
    # print (mat5)
    """tnnd，报错了不知道为啥"""

    #TODO:等间隔数组
    mat=np.arange(10,20,2)
    # print(mat)

    """
    构造器接受下列参数：
     
    numpy.linspace(start, stop, num, endpoint, retstep, dtype)
     
    序号	参数及描述
    1.	start 序列的起始值
    2.	stop 序列的终止值，如果endpoint为true，该值包含于序列中
    3.	num 要生成的等间隔样例数量，默认为50
    4.	endpoint 序列中是否包含stop值，默认为ture
    5.	retstep 如果为true，返回样例，以及连续数字之间的步长
    6.	dtype 输出ndarray的数据类型
    """
    mat=np.linspace(1,2,5,endpoint=False,retstep=True)
    # print(mat)

    #TODO:切片
    mat=np.arange(10)
    mat1=mat[2:7]
    # print(mat1)

    #对于多维数组
    mat2=np.arange(24).reshape(4,6)
    # mat=mat2[1:]
    # print(mat2[1,1:])
    # print(mat2[...,1:])
    """...本质上代表的类似循环的存在"""

    #TODO:高级索引与切片
    mat=np.arange(12).reshape(3,4)
    pos=mat[[1,2,2],[0,1,2]]
    """是10，21，22这三个位置"""
    # print(pos)

    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    # print(x[1:4,1:3])
    # print(x[1:4,[1]])#高级索引

    #TODO:广播
    #如果两个数组的维数不相同，则元素到元素的操作是不可能的。
    # 然而，在 NumPy 中仍然可以对形状不相似的数组进行操作，因为它拥有广播功能。
    # 较小的数组会广播到较大数组的大小，以便使它们的形状可兼容。

    a=np.arange(4)
    b = np.arange(5,20,4)
    # print(a*b)

    a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
    b = np.array([1.0, 2.0, 3.0])
    # print(a+b)

    #TODO:数组转置
    a=np.arange(12).reshape(3,4)
    print(a.T)

    #TODO:高维数组展平
    print(a.flatten())
    print(a.ravel(order='F')) #按列展开

    #TODO:删除维度
    x=np.arange(9).reshape(1,3,3)
    print(x)
    y=np.squeeze(x)
    print(y)

    #TODO:相同shape数组连接
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print(np.concatenate((a,b)))
    print(np.concatenate((a,b),axis=1))

    #TODO:相同shape数组按新轴连接
    print(np.stack((a,b),0))
    print(np.stack((a,b),1))

    #TODO:相同shape数组水平堆叠（同上边按axis=1连接）
    print(np.hstack((a,b)))

    #TODO:数组分割
    a=np.arange(9)
    print(np.split(a,3))
    print(np.split(a,[2,7]))
    a=np.arange(16).reshape(4,4)
    print(np.hsplit(a,2))
    print(np.vsplit(a,2))

    #TODO:数组从新修改形状
    a=np.arange(8).reshape(2,4)
    print(a)
    print(np.resize(a,(4,2)))

    #TODO:数组添加
    a=np.arange(6).reshape(2,3)
    print(a)
    print(np.append(a,[[7,8,9]],axis=0)) #必须是同等维度的才能按特定轴添加，否则会使原数组降维

    #TODO:数组插入
    a=np.arange(6).reshape(2,3)
    print(np.insert(a,3,[1,1,1])) #未传递 Axis 参数。 在插入之前输入数组会被展开
    print(np.insert(a,2,[1,1,1],axis=0))

    #TODO:数组删除
    print(np.delete(a,2))
    print(np.delete(a,1,axis=0))

