# 术语表


## Devices

一块可以用来运算并且拥有自己的地址空间的硬件,比如GPU和CPU。


## Eval

Tensor的一个方法,返回Tensor的值。触发任意一个图计算都需要计算出这个值。只能在一
个已经启动的会话的图中才能调用该Tensor值。


## Feed

TensorFlow的一个概念:把一个Tensor直接连接到一个会话图表中的任意节点。feed不是在
构建图的时候创建,而是在触发图的执行操作时去申请。一个feed临时替代一个带有Tensor值
的节点。把feed数据作为run()方法和eval()方法的参数来初始化运算。方法运行结束后,替换
的feed就会消失,而最初的节点定义扔然存在。可以通过tf.placeholder()把特定的节点
指定为feed节点来创建他们。


## Fetch

TensorFlow中的一个概念:为了取回运算操作的输出结果。取回的申请发生在触发执行图操作
的时候,而不是发生在建立图的时候。如果要取回一个或多个节点的Tensor值,可以通过在session
对象上调用run()方法并将待取回节点的列表作为参数来执行图标。


## Graph

把运算任务描述成一个直接的无环图形(DAG),图表中的节点代表必须要实现的一些操作。图中的边
代表数据或者可控制的依赖。GratheDef是系统中描述一个图标的协议(api),它由一个NodeDefs
集合组成。一个GraphDef可以转化为一个更容易操作的图标对象。


## IndexedSlices

在Python API中,TensorFlow仅仅在第一维上对Tensor有所体现。如果一个Tensor有K维,那么
一个IndexedSlices实例在逻辑上代表一个沿着这个Tensor第一维的(k-1)维切片的集合。切片
的索引被连续存储在一个单独的一维向量中,而对应的切片则被拼接成一个单独的K维Tensor。如果
sparsity不是受限于第一维空间,请用SparseTensor。


## Node

图中的一个元素。把启动一个特定操作的方式成为特定运算图表的一个节点,包括任何用来配置这个操作
的属性的值。对于那些多形态的操作,这些属性包括能完全决定这个节点签名的充分信息。


## Operation

在TensorFlow的运行时中,它是一种类似add或matmul或concat的运算。


## Run

在一个运行的图中执行某种操作的行为。要求图必须运行在会话中。


## Session

启动图的第一步是创建一个Session对象。


## Shape

Tensor的维度和它们的大小。

在一个已经启动的图中,它表示流动在节点之间的Tensor的属性。一些操作对shape有比较强
的要求,如果没有Shape属性则会报告错误。


## Tensor

Tensor是一种特定的多为数组。比如,一个浮点型的四维数组表示一批由[batch,height,
width,channel]组成的图片。在一个运行的图中,它是一种流动在节点之间的数据。在python
中,Tensor类表示添加到图的操作中的输入和输出。