# 数值计算要点 1
## getA() in np
对于矩阵来说，通过getA来将数组类型变成ndarray，因为在matplot中需要的是ndarray类型。
## 绘制散点

	ax.scatter(xcord1, ycord1, s=30, c='red', marker='p')
	
其中的 marker 表示点的形状。xcord1是array，所以一维矩阵不行，必须转换成array.

## random.uniform
返回指定范围的随机浮点值[small, big)。和random.random()是返回[0.0, 1.0)的浮点值。

## 数值计算的集中类型
1. list 普通的列表，这是python自身的数据类型，不能进行矩阵运算
2. numpy.array 这是可以进行对其进行统一运算的。例如 A = array(ListA). A*3.但是，他不是矩阵，他的性质只是能够对每一个元素进行ufunc操作而已。
3. numpy.matrix 是像矩阵一样处理。所以需要matrix(ListA)或者matrix(ArrayA)
他们又是可以互相转化的使用 mat.A或者mat.getA转换成array.

## 错误: s32类型错误
这是说明在处理数据的时候，没有转换成float，而数据依然是字符串类型。