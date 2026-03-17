---
tags:
  - GIS
  - 三维GIS
创建时间: 2026-03-02T09:50:00
课程: 三维GIS开发
课程类型: 选择性必修
阶段: 大三下
老师: 段新桥
开始日期: 2026-03-02
结束日期:
---
[[2026-03-02]]
# 3D GIS Programing Essentials

	IBM深蓝 —— 国际象棋 —— AlphaGo围棋 —— AlphaFold分子药物

## 1. AI挑战下的三维GIS与编程

### 1.1 学科知识体系

#### 1.1.1 术语体系

#### 1.1.2 知识网络/图谱

$$
\text {开发/编程}
\begin{cases}
\text {前端}
\begin{cases}
\text{交互方式} \\
\text{UI} \\
\text{适配} \\
\text{配色} \\
\text{样式} \\
\end{cases} \\
\text {后端} \\
\end{cases}
$$
#### 1.1.3 知识对齐

$$
\text{Aligenment}
\begin{cases}
\text{AI} \\
\text{已有科学与技术} \\
\text{人的价值何在？} \\
\end{cases}
$$
---
### 1.2 三维挑战

#### 1.2.1

>[!note]
>三维相对二维平面，有意义的距离从来不是直线距离：非欧氏距离&非欧氏空间

#### 1.2.2 弯曲
$$
\begin{gather}
\text{线曲率} \ \kappa(s) = \lim_{\Delta s \to 0} \left\| \frac{\boldsymbol{T}(s+\Delta s) - \boldsymbol{T}(s)}{\Delta s} \right\| = \left\| \frac{d\boldsymbol{T}}{ds} \right\| \\
\text{面曲率} \ K(P) = \lim_{S \to P} \frac{\mathcal{A}(\boldsymbol{n}(S))}{\mathcal{A}(S)}
\end{gather}
$$

	平面三角形内角和 = PI
	球面三角形内角和 > PI
	双曲面三角形内角和 < PI

#### 1.2.3 距离

$$
\text{向量的内积 a · b} \\
$$
#### 1.2.4 角度
	长度之比，无量纲

$$
\begin{gather}
\alpha = \frac{l}{r} \\
\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}|\,|\mathbf{b}|}
\end{gather}
$$
---
## 2. 三维GIS编程导论
### 2.1 三维GIS的研究对象
#### 2.1.1 自然资源管理

>[!timeline]
>2018年3月，组建自然资源部
>2019年3月，省市县自然资源管理机构改革
>看齐USGS，即：
>自然资源**调查、登记、确权、规划**  
>代替国务院形式所有人职权  
>以国土空间规划为主体，“一张蓝图干到底”
>2022年2月，**实景三维**中国建设与**数字经济**；
>2024年4月，智慧城市与地形级地理场景；

#### 2.1.2 地球环境
	地球是个椭球体（至少是三维的）
	地形是起伏不平的
	地球环境变化的主体：地球流体（大气与海洋）

>[!note]
>**一些基本事实：**
>地形对地球表层系统的水热动量的再分配起到支配性作用；
>大气层密度标高*8.5km*，*20km* 厚度包括了*99%* 的质量；
>大洋平均深度*4km*，各大洋最深处都约在*9km* ;

>[!note]
>**实际上的地球表层流体：**
>地球流体（大气与海洋）
>碰到硬边界就会变形：*绕道*，*抬升*，*停滞*

#### 2.1.3 城市环境
---
### 2.2 三维空间数据与面向对象的现代软件工程
#### 2.2.1 空间数据模型

>[!note]
>**矢量与栅格**
>**矢量：** 点、线、面、体、组合体
>由基本元素( *simplex* )按规则构成复杂形体( *combinatory  topology* )，**点定义几何**( *geomertry* )，**连接关系** ( *connectivity* ) 称为 **拓扑** ( *topology* )。
>**栅格：** 二维&三维
>二维栅格即影像，三维栅格是二维影像在竖直方向上的堆叠。
>海量空间数据必须借助计算机的自动处理。

---
[[2026-03-04]]
## 3. 程序系统的基本原理和算法库
	三维 —— 凸多边形 —— 非平坦、非欧氏空间
	距离度量 —— 图最短路径(Dijkstra)
### 3.1 程序系统的基本原理

$$
\begin{gather}
\text{A = L × L} \\
\text{V = L × L × L} \\
\text 角度ε  = \frac{Δε}{Δl}
\end{gather}
$$

#### 3.1.1 形式语言与自动机

![[74ffbd8b94935c53cdcdc682f2b1b8a0.jpg]]

#### 3.1.2 程序入口(entry point)

>[!note]
>1.程序编译后形成文件(PE/OFF)
>2.文件格式的程序是**进程**( *process* )在磁盘上的**映像**( *image* )
>3.程序一旦装载( *loader* )并运行，形成**操作系统**的进程，即将获得系统资源，理论上可以做任何事。
>
>“给我一个进程入口，我可以创造一个世界。”
>**Python，R，Julia，Go，Rust**

#### 3.1.3 运行时(runtime)

>[!note]
>1.一个基本的Windows程序通常包含代码和UI( *User Interface* )两大部分
>2.源代码编辑后，由RC( *resource compiler* )编译器将这两部分整合成一个EXE文件( **可执行程序** )。
>3.EXE文件装载后，放在内存中，CPU的指令寄存器( *IP* )指向程序入口
>4.UI资源指菜单、对话框、位图、图标等，需要在一个 **.rc**文件中描述它们，也就是说，**UI界面都是WIndows“画”出来的**。
>5.这和网页设计中拖一个按钮并编写事件没什么两样。

>[!note]
>1.Windows程序可以调用的函数可以分为C libs和Windows API两种，都可称为runtime libraries，简称运行时(库)。
>2.LIBC.LIB是C Runtimes的静态连接版，MSVCRT.LIB是C Runtimes的动态连接版。
>3.GDI32.DLL、USER32.DLL和KERNEL32.DLL提供基础WIndows功能API的三大函数库。
>4.应用程序也可以编写自己的静态DLL/动态DLL，对外提供功能接口
>
>可见，运行时是提供**软件功能复用**的一种形式。

#### 3.1.4 消息驱动(message driven architecture)

>[!note]
>1.Windows程序的运行靠外部事件驱动，逻辑如下：
>程序循环取消息；
>事件发生，Windows收集事件，产生消息，投递消息；
>程序从消息队列取到消息，做出相应的处理。
>2.那么每一个Windows程序都有一个取消息的无限循环。

>[!definition]
>**消息结构定义如下：**

```c
typedef struct tagMsg{
	HWND hWnd; // 窗口句柄
	UINT message; // 消息ID
	WPARAM wParam; // 短参数
	LPARAM lParam; // 参数
	DWORD time; // 时刻
	POINT pt; // 位置
}MSG;
```

>[!definition]
>窗口过程( **window function** )响应发给自己的消息，函数定义如下：

```c
LRESULT CALLBACK WndProc(HWND hWnd,UINT message,WPARAM wParam,LPARAM lParam)
{
	switch(message){
		case WM_LBUTTONDOWN: // 鼠标左键按下了
			...
		case WM_MOUSEMOVE: // 窗口在移动
			...
		case WM_DESTROY: // 窗口销毁了
		
		PostQuitMessage(0);
		
		default: // 没有特殊的或用户交互，交予默认过程处置
			return DefWindowProc(hWnd,message,wParam,lParam);
	}
	
	return (0); // 无论如何，一定要返回！！！
}
```

>[!note]
>**Windows应用程序的消息机制：**

![[936a0255bdccc52feb47f963c1be1250.jpg]]

>[!note]
>**Windows程序系统的原理要点：**
>1.Windows收集所有的消息，当一个程序( 进程，*process* )运行时，Windows为之建立相应的消息队列；
>2.应用程序从*Entry Point* 取得系统权限，建立窗口和窗口过程后，执行一个死循环( 消息循环 )：取消息并将消息分发至( 子 )窗口或线程；
>3.窗口或线程函数对消息作出反应；
>4.*GetMessage* 与*Entry Point* 是系统关键；**若消息队列为空，进程休眠，让出CPU时间**。

>[!note]
>**Windows程序本意是有图形界面的，但也存在许多变形：**
>1.控制台程序(console)：即所谓的命令行窗口程序
>2.窗口程序
>3.WinForms程序：.NET/WPF等高级语言界面程序
>**无论是哪种形式，程序原理是相似相同的。**
>4.*控制台程序下也可以使用窗口界面。*

#### 3.1.5 Linux，UNIX，鸿蒙与其它

>[!note]
>1.操作系统决定程序系统的结构
>2.操作系统的生态决定程序的生态
>3.手机与智能设备主要是类Linux系统

#### 3.1.6 软件复用、通信与接口

>[!note]
>**1.IPC/RPC：** 进程间通信/远程通信
>**2.COM/CORBA：** 
>二进制标准
>**接口**编程( *IInterface / IDispatch / IFeature / IFeatureClass ...* )
>接口好比插座，仅描述功能规范，不提供实现( *abstract class* )
>**3.Web Service/SOAP**
>**4.UDDI**  

- [1] 封装越来越高级
---
### 3.2 编程模式

>[!note]
>1.程序 = 算法 + 数据结构 —— N.Wirth
>2.但是用户(程序)也需要和计算机自身打交道
>3.用户友好界面(UI)编程：苹果，Windows，手机
>4.AI编程(Agent Programing)：prompt Engineering
>
>所以一直存在两种编程模式：
>关注输入输出的**系统程序**和关注数据处理的**算法程序**

---
### 3.3 Python与算法库

#### 3.3.1 现代软件工程

>[!note]
>1.C++是操作系统级的代码，是**编译型**底层代码。
>2.当面临快速的任务需求时，看中的**原型系统**的效率。
>项目任务的快速迭代
>脚本语言与**解释型**语言，边试错，边开发
>3.交互式语言
>变量可不声明就使用
>可以交互式，也可以程序式 >*python a.py*
>*Python.exe*在宿主机上构建了自己的“语言世界”

>[!note]
>1.面向对象
>2.强格式
>如缩进严格。好处是语法清晰。
>3.弱类型
>类型转换与声明灵活自由
>4.万金油式语言
>比如ArcGIS可以引入Python
>5.明显缺点：
>解释型，速度慢
>并行较弱(Gil)
>丰富的三方库，存在不小的功能重叠

#### 3.3.2 算法库

>[!note]
>**1.Python Package Index：** https://pypi.org
>**2.Pypi相当于实现了C++时代梦寐以求的** *UDDI* **注册中心**

>[!note]
>**GIS相关包：**
>1.CGAL —— 主要是C++，学院派计算几何算法库
>2。ITK/VTK —— Kitware维护的图像图形库
>3.Shapely —— 著名的GEOS库的Python版本
>4.Cartopy —— 制图
>5.Bassmap，Flona，GeoPandas —— 集成的地图可视化
>6.pycairo，pyproj，OGR，GDAL，pyshp —— 坐标，投影，GIS数据
>7.PIL，SPy —— 遥感影像与光谱
>8.libigl —— 轻量级网格处理库，支持变形、参数化等几何操作
>9.Open3D —— 3D数据处理库，专注于点云和网格的可视化、重建及深度学习
>10.laspy —— 读写LAS/LAZ点云格式的Python库，基于NumPy
>11.PDAL/XArray —— PDAL点云处理（类似GDAL），XArray多维数组分析，常结合用于点云栅格化
>12.whitebox —— WhiteboxTools的Python接口，提供水文分析、激光雷达处理等丰富地理空间工具

#### 3.3.3 包的安装

>[!note]
>1.pip xxxxx.whl
>2.pip国内源配置：
>pip.ini
>[global] index-url = https://pypi.tuna.tsinghua.edu.cn/simple
>uv使用
>Poetry使用
>conda配置

---
### 3.4 Python/PyTorch语言要素
#### 3.4.1 简单数据类型

>[!definition]
>**代数的概念：** 集合之上的**运算**，及数的集合一起，称为**代数**( *algebra* )。

##### 3.4.1.1 整数与小数

>[!note]
>1.单个的数构成一个**集合**的元素。
>2.集合之上可以定义**运算**，运算决定数和集合的性质；称为**代数**( *algebra* )。

```text
实验：
	a = 10
	type(a);id(a)
	a = 10 + 0.1
	type(a);id(a)
	a = 0o12;a
	a = 0xafd;a
	a = 0b01;a
```

>[!note]
>**强制转换：**
>1.int(x,base = 10)：x是小鼠或字符串，base是进制。
>2.float(x)：x是数与字符串。
>3.str(x)：x是数

##### 3.4.1.2 字符串

>[!note]
>1.a = 'abc'; b = "abc"; c = '''abc'''; d = """abc"""
>2.type(a)
>3.字符串前加：
>r —— 不转义
>u —— UNICODE编码
>f —— 接受参数的字符串格式化 
>4.字符串的**加/乘**运算：
>s = 'good' * 3

![[Pasted image 20260304104034.png]]

#### 3.4.2 结构数据类型
##### 3.4.2.1 list：列表

>[!definition]
>**列表：** 可动态增删改的混合元素集合。

>[!note]
>1. l = []
>2. l.append(a)
>3. l.extend(l1)
>4. 列表通常比数组灵活，却又可以当数组用
>
>人工智能经典语言<span style = "color:skyblue;">LISP</span>以列表为语言基础

##### 3.4.2.2 tuple：元组

>[!definition]
>**元组：** 基本固定的列表。

>[!note]
>1.l = (1,2)
>2.x = 2,3;x
>3.x,y = 2,3;x;y;
>4.x,y = y,x;x;y;

##### 3.4.2.3 dict：字典

>[!definition]
>**字典：** 字典是动态的**键 — 值对**集合，其位置索引仅是象征性。

>[!note]
>dict = {'a' : 1,'b' : 131,'c' : 666}\
>dict = [ 'c' ]

##### 3.4.2.4 set：集合

>[!definition]
>**集合：** **无重复**元素。

>[!note]
>1.dict = {'a','bbc','cx'}
>2.for s in dict:
>3.集合支持**交/差/对称查**运算

#### 3.4.4 序列内涵 ( *list comprehension* )

>[!note]
>1.[i ** 2 for i in range(1,100)]
>**字典也可以内涵：**
>2.{k:v for k,v in zip(keys,values)}
>**内涵还可以加条件：**
>3.[i ** 2 for i in range(1,1000) if i % 2 == 1]

#### 3.4.5 PyTorch语言要素

>[!note]
>1.PyTorch以张量(tensor)为基本要素，但此张量不是狭义的数学概念，更多地是数组/矩阵的兼容概念。
>2.以数组和矩阵的概念看张量，Numpy中的数据类型在PyTorch中都找得到对应。
>3.数组和矩阵最重要的是讲究维度对齐。
>
>这对后面的神经网络与深度学习的数学模型设计至关重要。
>向量默认都是列序。

>[!important]
>**矩阵相乘(点乘)的行列要求：**

$$
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}
\end{pmatrix}
\begin{pmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
b_{31} & b_{32}
\end{pmatrix}
=
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} & a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} \\
a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31} & a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32}
\end{pmatrix}
$$

---
### 3.5 图形库
#### 3.5.1 OpenGL

![[3aa4907461dd1cc17bb6ee7e2dd50a99.jpg]]

#### 3.5.2 DirectX

![[4611b198d4025fb307066451ceba2330.jpg]]

#### 3.5.3 Osg/OsgEarth

![[ebd7e96bed7e9a6b36cc611adc8f6e2a.jpg]]

#### 3.5.4 OpenInventor

![[d27e91665c44ef36b9f9b80432aeead6.jpg]]

#### 3.5.5 VTK/Paraview/PyVista/panel/Trame

![[207dcd69ff71616d97c39a22515a0884.jpg]]

#### 3.5.6 总结

![[b6b7cba9ed369913696c1ff67e7b1000.jpg]]

#### 3.5.7 实例与练习
##### 3.5.7.1 *Pyvista* 读取空间数据并展示

![[Pasted image 20260304111537.png]]

```python
import pyvista as pv # 导入pyvista库  
  
mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk') # 读取模型文件  
mesh.plot() # 显示网格
```

##### 3.5.7.2 *VTK* 读取空间数据并展示

![[Pasted image 20260304111445.png]]

```python
import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集  
  
r = vtk.vtkPolyDataReader() # 构建一个多边形数据集读取器  
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk') # 设置读取文件名  
r.Update() # 更新读取器，读取模型文件  
  
pd = vtk.vtkPolyData() # 构建一个多边形数据集  
pd.ShallowCopy(r.GetOutput()) # 从读取器r获取输出并浅拷贝到多边形数据集pd  
  
actor = vtk.vtkActor() # 构建一个演员  
m = vtk.vtkPolyDataMapper() # 构建一个多边形数据集映射器  
m.SetInputData(pd) # 为映射器m添加多边形数据集pd  
actor.SetMapper(m) # 为演员actor设置映射器m  
  
ren = vtk.vtkRenderer() # 构建一个渲染器  
ren.AddActor(actor) # 为渲染器ren添加演员actor  
  
# 创建渲染窗口  
rw = vtk.vtkRenderWindow() # 构建一个渲染窗口  
rw.AddRenderer(ren)  # 为渲染窗口rw添加渲染器ren  
rw.SetWindowName("Klein Bottle - VTK Visualization") # 设置渲染窗口标题  
  
# 创建渲染窗口交互器，用于处理用户与3D模型的交互  
ri = vtk.vtkRenderWindowInteractor()  # 实例化交互器对象  
ri.SetRenderWindow(rw)  # 将交互器与渲染窗口关联  
ri.Render()  # 触发初始渲染  
  
ri.Start()  # 启动交互循环，开始接收用户输入事件
```

##### 3.5.7.3 *gdal* / *xarray* 读取 *netcdf* / *hdf*

---
[[2026-03-09]]
## 4. 三维文件格式和组合拓扑
### 4.1 三维文件格式
#### 4.1.1 组合拓扑( *combinatory topology* )

>[!note]
>**空间对象的抽象：**
>*0* 维对象点
>*1* 维对象线由*0* 维点界定
>*2* 维面/多边形对象由*1* 维线界定
>*3* 维体由*2* 维面界定
>*k* 维对象由( *k - 1* )维对象组成其**边界**即组合拓扑。

>[!caution]
>1.文件是数据组织格式的工业交换标准。
>2.文件是数学法则的具体化。

>[!important]
>**边界**是某种*奇点* ( singularity )，即连接性质发生突变的空间位置。
>*e.g.*
>*1.* 线的两边*端点* 就是线的**边界**，这两个*端点* 即为*奇点*。
>*2.* *三维* 的**球体**投影到*二维* 的**平面**上可能会遇到的问题 —— 详见[[]]
>
>通过*求边界、粘连* 等操作，可以得到操作几何形状的一个 “**代数**” ( algebra )

#### 4.1.2 表结构与组合拓扑

>[!note]
>**顶点表：** 顶点索引与坐标($x,y,z$)；*list of vertices of tuple* ($x,y,z$);
>**边表：** 边索引与顶点集；*list of edges of vertices* ;
>**面表：** 面索引与边集；*list of facets of edges* ;
>体表：体索引与面集；*list of volumes of facets* ;
>组( group )；
>多体( multi - volume )；

![[1b69328adcc54a85a31e7df4ebb24966.jpg]]

##### 4.1.2.1 顶点表

>[!note]
>**储存顶点的坐标，是图形的几何；**
>**顶点表由其索引来引用**，即顶点在表中的顺序号。
>
>**好处：**
>1.减少数据冗余，提高数据访问效率；
>2.保持拓扑关系，即从逻辑上保证不同的边 / 面结构中访问的是同一个点。

>[!caution]
>在很多图形系统中，如果两个点分别定义，即使它们坐标相同，它们也是拓扑不相同的点。

##### 4.1.2.2  边表

>[!note]
>**存储两个端点所使用顶点的索引：**
>1.不同的顺序代表不同的边定向( *orientation* )。
>2.有时为方便访问，会使用双端队列( *queue* )存储对边，成为*DCEL* ( *double - connected edge list* )或*Halfedge* 结构。

##### 4.1.2.3 面表

>[!note]
>**储存（三个）端点所使用顶点的索引：**
>1.不同的顶点顺序代表不同的面定向( *orientation* )
>2.为避免图形结构中出现不常见的”非流形“ ”假流形“ ”伪流形“，组合拓扑还需要在边表 / 面表结构中增加更多的约束，比如：
>*1) 一个顶点至少要由两条边邻接；*
>*2) 一条边至多能由两个面邻接。*

![[c9824a14d32b568901f350a6e58ba5d3.jpg]]

>[!note]
>1.边界是**空间奇异**( *singularity* )，是拓扑突变；
>2.边界具有不同的维度；
>3.边界是不同维度对象的连接关节；
>4.非流形是边界连接的不顺畅，具有特殊的空间意义。

##### 4.1.2.4 练习

###### 4.1.2.4.1 **VTK** 读取空间数据并展示

	DataFrame
		columns x,y,z,v
	变量名：df['x']

![[Pasted image 20260309120204.png]]

```python
import pandas as pan # 导入pandas库，用于读取CSV文件  
import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集  
import numpy as np # 导入numpy库，用于数组操作  
  
df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv') # 读取CSV文件  
x = df['x'] # 从DataFrame中提取x列  
y = df['y'] # 从DataFrame中提取y列  
z = df['z'] # 从DataFrame中提取z列  
#print(x,len(x)) # 输出x列和其长度  
  
pts = vtk.vtkPoints() # 构建点集  
for i in range(len(x)): # 对len(x)进行遍历  
    pts.InsertNextPoint(x[i],y[i],z[i])  
    #pts.InsertNextPoint(i,np.array([x[i],y[i],z[i]]))  
print(pts.GetNumberOfPoints()) # 输出点集的点数  
  
vtx = vtk.vtkCellArray() # 构建顶点集  
#for i in range(len(x)): #存在风险：i可能会超出范围  
for i in range(pts.GetNumberOfPoints()): # 使用点集的点数更安全  
    v = vtk.vtkVertex() # 构建一个顶点  
    v.GetPointIds().SetId(0,i) # 为顶点v添加一个点索引i  
    vtx.InsertNextCell(v) # 为顶点集vtx添加一个顶点v  
  
pd = vtk.vtkPolyData() # 构建一个多边形数据集  
pd.SetPoints(pts) # 为多边形数据集pd添加点集pts  
pd.SetVerts(vtx) # 为多边形数据集pd添加顶点集vtx  
  
w = vtk.vtkPolyDataWriter() # 构建一个多边形数据集写入器  
w.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.vtk') # 设置写入文件名  
w.SetInputData(pd) # 为写入器w添加多边形数据集pd  
w.Write() # 写入文件
```

###### 4.1.2.4.2 **Pyvista** 读取空间数据并展示

![[Pasted image 20260309120447.png]]

```python
import pandas as pan # 导入pandas库，用于读取CSV文件  
import pyvista as pv # 导入pyvista库，用于可视化网格  
import numpy as np # 导入numpy库，用于数组操作  
  
df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv') # 读取CSV文件  
x = df['x'] # 从DataFrame中提取x列  
y = df['y'] # 从DataFrame中提取y列  
z = df['z'] # 从DataFrame中提取z列  
cords = np.array([x,y,z]).T # 将x、y、z列转换为点坐标数组  
  
#使用pyvista与使用vtk时的区别：  
# 1. pyvista直接使用点坐标构建网格，而vtk需要先构建点集和顶点集  
# 2. pyvista的plot()方法可以直接显示网格，而vtk需要通过渲染器、渲染窗口和交互器来显示  
# 3. 数据类型上，pyvista使用numpy数组，而vtk使用vtkPoints对象  
  
points = pv.PolyData(cords) # 从点坐标数组构建PolyData对象  
points.plot() # 显示网格
```

---
[[2026-03-11]]
### 4.2 散点格式与可视化

>[!summary]
>**总结：**
>**1.** 散点是0维空间对象的抽象，不与其它的点或高维对象相关联，因而点( *表* )就是**几何**；
>**2.** 而由点构线 / 线构面 / 面构体的组合关系形成高维对象时，无一不涉及到组合与空间关系，因而几何单元( *cell* )就是**拓扑**；
>**3.** 通俗意义上的拓扑就是空间关系，但组合拓扑是一个维度的邻接关系( *incidence* )，是细粒度的“空间关系”，更宏观的空间关系如“包含”、“相切”、“方位”可以由几何体的组合拓扑计算。

---
### 4.3 折线与曲线

#### 4.3.1 定义与格式

>[!definition]
>**线段：** 由0维点组成边界形成的1维空间对象；
>**折线** ( 多义线，*polyline* )：多个点有序连成线段的集合；
>**简单曲线** ( *Jordan Curve* )：没有自相交的曲线；
>**♦操作4：** 使用Paraview打开*data/structure_from_asc_points.vtk* 研究其形状；
>**♦操作5：** 使用Editplus或Nodepad打开*data/structure_from_asc_points.vtk* 研究其多义线数据的存储结构。

![[05616a46a80b1318fb7e42829c8de3f4.jpg]]

##### 4.3.1.1 练习

###### 4.3.1.1.1 基于 **GeoPandas** 的 *Shapefile数据读取* 与 *VTK/PyVista可视化*

![[Pasted image 20260311105658.png]]

![[Pasted image 20260311105714.png]]

![[Pasted image 20260311111104.png]]

![[Pasted image 20260311111749.png]]

![[Pasted image 20260311112335.png]]

![[Pasted image 20260311112446.png]]

![[Pasted image 20260311112642.png]]

![[Pasted image 20260311112852.png]]



```python
import geopandas as gpd # 导入geopandas库，用于读取SHP文件  
import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集  
import numpy as numpy # 导入numpy库，用于数组操作  
import pyvista as pv # 导入pyvista库，用于可视化  
  
df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp',encoding = 'gbk') # 读取REG.shp文件  
print(df.columns) # 打印列名  
print(df.geometry[2].exterior.coords) # 打印第3个几何对象的外部坐标  
l = len(df.geometry[2].exterior.coords) # 提取第3个几何对象的外部坐标的长度  
  
# x = [df.geometry[2].exterior.coords[i][0] for i in range(l)] # 提取x坐标  
# x = [] # 提取x坐标  
# y = [] # 提取y坐标  
# z = [] # 提取z坐标  
# for i in range(l): # 遍历所有点  
#     x.append(df.geometry[2].exterior.coords[i][0]) # 提取x坐标  
#     y.append(df.geometry[2].exterior.coords[i][1]) # 提取y坐标  
#     z.append(0) # 提取z坐标  
  
pts = vtk.vtkPoints() # 创建点对象  
pts.SetDataTypeToDouble() # 设置数据类型为双精度浮点数  
for i in range(l): # 遍历所有点  
    pts.InsertNextPoint(df.geometry[2].exterior.coords[i][0], df.geometry[2].exterior.coords[i][1], 0) # 插入点  
ca = vtk.vtkCellArray() # 创建单元数组对象  
  
# 提取所有点的索引  
# for i in range(pts.GetNumberOfPoints()): # 遍历所有点  
#     v = vtk.vtkVertex() # 创建顶点对象  
#     v.GetPointIds().SetId(0,i) # 设置顶点的点索引  
#     ca.InsertNextCell(v) # 插入单元  
# pd = vtk.vtkPolyData() # 创建多边形数据对象  
# pd.SetPoints(pts) # 设置点对象  
# pd.SetVerts(ca) # 设置单元数组对象  
#  
# pp = pv.PolyData(pd) # 创建PyVista多边形数据对象  
# pp.plot(color = 'green') # 绘制多边形数据对象  
  
# 提取所有线的索引  
# for i in range(pts.GetNumberOfPoints() - 1): # 遍历所有点  
#     ln = vtk.vtkLine() # 创建线对象  
#     ln.GetPointIds().SetId(0,i) # 设置线的点索引  
#     ln.GetPointIds().SetId(1,(i+1)) # 设置线的点索引  
#     ca.InsertNextCell(ln) # 插入单元  
# ln = vtk.vtkLine() # 创建线对象  
# ln.GetPointIds().SetId(0,(pts.GetNumberOfPoints() - 1)) # 设置线的点索引  
# ln.GetPointIds().SetId(1,0) # 设置线的点索引  
# ca.InsertNextCell(ln) # 插入单元  
#  
# pd = vtk.vtkPolyData() # 创建多边形数据对象  
# pd.SetPoints(pts) # 设置点对象  
# pd.SetLines(ca) # 设置单元数组对象  
#  
# pp = pv.PolyData(pd) # 创建PyVista多边形数据对象  
# pp.plot(color = 'green') # 绘制多边形数据对象  
  
# 提取所有线的索引  
pln = vtk.vtkPolyLineSource() # 创建折线源对象  
pln.SetPoints(pts) # 设置折线源对象的点对象  
pln.Update() # 更新折线源对象  
  
pp = pv.PolyData(pln.GetOutput()) # 创建PyVista折线数据对象  
pp.plot(color = 'red') # 绘制折线数据对象  
  
# 提取所有线的索引  
plg = vtk.vtkPolygon() # 创建多边形对象  
plg.GetPointIds().SetNumberOfIds(pts.GetNumberOfPoints()) # 设置折线点对象的点索引数量  
for i in range(pts.GetNumberOfPoints()): # 遍历所有点  
    plg.GetPointIds().SetId(i, i) # 设置折线点对象的点索引  
ca.InsertNextCell(plg) # 插入单元  
  
pd = vtk.vtkPolyData() # 创建多边形数据对象  
pd.SetPoints(pts) # 设置点对象  
pd.SetPolys(ca) # 设置单元数组对象 # 来自人的先验知识，而不是vtk的自动三角化  
  
# 进行Delaunay2D三角化  
# d2d = vtk.vtkDelaunay2D() # 创建Delaunay2D对象  
# d2d.SetInputData(pd) # 设置Delaunay2D对象的输入数据  
# d2d.Update() # 更新Delaunay2D对象  
  
# 提取所有三角形的索引  
# tri = vtk.vtkTriangleFilter() # 创建三角形过滤器对象  
# tri.SetInputData(pd) # 设置三角形过滤器对象的输入数据  
# tri.Update() # 更新三角形过滤器对象  
  
pp = pv.PolyData(pd) # 创建PyVista多边形数据对象  
pp = pp.triangulate() # 三角化多边形数据对象  
pp.plot(color = 'green') # 绘制三角化多边形数据对象  
  
# 单纯形simplex:  
# 一个单纯形是一个n维空间中的一个n-1维的子空间，它由n个点组成，这些点在n维空间中是线性独立的。  
# 例如，在二维空间中，一个三角形就是一个单纯形，它由三个点组成，这些点在二维空间中是线性独立的。  
# 在三维空间中，一个四面体就是一个单纯形，它由四个点组成，这些点在三维空间中是线性独立的。  
  
#pyvsita渲染折线源和多边形数据对象的区别:  
# 折线源对象是一个vtk对象，它可以直接渲染出来。  
# 多边形数据对象是一个vtk对象，它可以直接渲染出来。  
# 但是，折线源对象和多边形数据对象的渲染结果是不同的。  
# 折线源对象的渲染结果是一条折线，它由多个点组成，这些点之间是连续的。  
# 多边形数据对象的渲染结果是一个多边形，它由多个点组成，这些点之间是不连续的。  
  
#solid和wireframe:  
# solid: 渲染出一个实心的多边形，它由多个点组成，这些点之间是不连续的。  
# wireframe: 渲染出一个空心的多边形，它由多个点组成，这些点之间是不连续的。  
  
#共线与Delaunay三角化：  
# 共线：如果在一个n维空间中，n个点是共线的，那么这n个点就构成了一个n-1维的子空间，这个子空间就是一个单纯形。  
# Delaunay三角化：Delaunay三角化是一种三角化算法，它可以将一个平面上的点集三角化，使得每个三角形的外接圆都不包含其他点。  
  
#凸多边形和Delaunay三角化：  
# 凸多边形：如果一个多边形的所有内角都小于180度，那么这个多边形就是一个凸多边形。  
# Delaunay三角化：Delaunay三角化是一种三角化算法，它可以将一个平面上的点集三角化，使得每个三角形的外接圆都不包含其他点。  
  
#显卡能接受的多边形都是三角形，所以不能渲染出非三角形的多边形。只有通过三角化才能渲染出非三角形的多边形。
```

>[!quote] 代码功能概述
> 这段代码主要利用 `geopandas` 读取 Shapefile 文件，提取其中的几何对象（第三个要素），然后通过 `vtk` 和 `pyvista` 库对提取的二维多边形点集进行多种形式的几何构建与可视化。包括注释部分在内，实现了以下功能：
> 
> 1. **读取 Shapefile 数据**  
>    - 使用 `geopandas.read_file()` 读取指定路径的 `REG.shp` 文件，并指定编码为 `gbk`。  
>    - 打印数据框的列名，以及第三个几何对象（索引为2）的外环坐标点列表。
> 
> 2. **提取坐标点**  
>    - 从第三个几何对象的外环中获取所有点的二维坐标（`x`, `y`），并为每个点设置 `z=0`。  
>    - 注释部分展示了分别提取 `x`, `y`, `z` 列表的代码（z 全部为 0）。
> 
> 3. **构建 VTK 点集（vtkPoints）**  
>    - 创建 `vtk.vtkPoints` 对象，设置为双精度浮点类型。  
>    - 将提取的所有点插入到 `vtkPoints` 中。
> 
> 4. **绘制点云（注释部分）**  
>    - 遍历所有点，为每个点创建 `vtk.vtkVertex` 单元。  
>    - 将这些顶点单元存入 `vtkCellArray`。  
>    - 构建 `vtkPolyData` 数据对象，设置点集和顶点单元。  
>    - 通过 `pyvista.PolyData` 包装并绘制（绿色点云）。
> 
> 5. **绘制闭合折线（两种方式）**  
>    - **手动构建线段单元**（注释部分）  
>      - 遍历相邻点对，创建 `vtk.vtkLine` 单元，并添加最后一个点到第一个点的线段，形成闭合环。  
>      - 存入 `vtkCellArray`，构建 `vtkPolyData` 并设置为线（`SetLines`）。  
>      - 通过 `pyvista` 绘制（绿色线）。  
>    - **使用 `vtkPolyLineSource` 直接生成折线**（激活部分）  
>      - 创建 `vtk.vtkPolyLineSource` 对象，设置点集。  
>      - 调用 `Update()` 后获取输出，用 `pyvista` 绘制（红色线）。
> 
> 6. **创建多边形并三角化渲染**（激活部分）  
>    - 创建 `vtk.vtkPolygon` 单元，将所有点的索引依次加入（形成多边形）。  
>    - 将该多边形单元存入 `vtkCellArray`。  
>    - 构建 `vtkPolyData`，设置点集和多边形单元（`SetPolys`）。  
>    - 使用 `pyvista.PolyData` 包装该数据，并调用 `.triangulate()` 将其三角化（因为显卡只能渲染三角形）。  
>    - 绘制三角化后的多边形（绿色填充）。  
>    - 注释部分还提到可以通过 `vtkDelaunay2D` 或 `vtkTriangleFilter` 进行三角化。
> 
> 7. **附带的概念说明**（注释中的文字）  
>    - 解释了单纯形（simplex）、共线、凸多边形、Delaunay 三角化的基本概念。  
>    - 比较了折线源与多边形数据对象的渲染区别，以及 solid 与 wireframe 渲染模式。  
>    - 说明了为什么需要将非三角形多边形三角化后才能被显卡正常渲染。
> 
> 总之，代码完整演示了从 Shapefile 读取地理数据，到使用 VTK 进行几何建模，最后通过 PyVista 实现多种可视化形式的全过程，涵盖了点、线、面的构建与显示。

>[!quiz]
>### 1. 处理 polyline.csv 数据为线和多边形输出
>通常，CSV 文件包含点坐标序列，每个线要素或多边形要素由多个点构成。处理步骤如下：
>- **读取 CSV**：使用编程语言（如 Python 的 pandas、C++ 的文件流）解析数据，确定每一行代表的点及其所属要素的 ID。
>- **构建几何**：按要素 ID 分组，将点串连成线。若需多边形，需确保首尾点闭合（必要时手动闭合）。
>- **输出格式**：可将结果保存为常见矢量格式（如 Shapefile、GeoJSON），利用库（如 GDAL、GeoPandas）直接写入；或输出为自定义文本格式。
>- **注意事项**：确认坐标系统（WGS84 或其他），属性字段（如要素名称）可一并输出。
>
>### 2. 处理商业软件特殊格式数据的思路
>遇到未知格式时，一般解决思路为：
>- **研究文档**：首先查找软件官方文档、开发者社区或格式说明，了解数据结构。
>- **利用现有工具**：尝试用该软件自身导出为通用格式（如 CSV、Shapefile），或搜索第三方转换工具。
>- **逆向分析**：若无文档，可用十六进制编辑器查看文件头，推测字节对齐、字段类型；或通过对比不同参数下的文件差异，分析数据规律。
>- **编写解析器**：根据分析结果，使用编程语言（如 Python 的 struct 模块）编写自定义解析脚本，提取几何和属性信息。
>- **验证与测试**：用已知数据测试解析结果，确保几何和属性正确。
>
>### 3. AI 加工地理信息数据特别关心的两点
>- **几何精度与拓扑一致性**：AI 生成或处理的数据可能引入位置偏差、自相交等拓扑错误，需验证几何是否符合实际地理空间规则。
>- **属性语义准确性**：地理信息通常包含丰富的语义标签（如地物类别），AI 可能误判或混淆，需确保分类、命名等属性的正确性和一致性。

---
[[2026-03-16]]
#### 4.3.2



---
#### 4.3.3 曲线

>[!note]
>**人工&自然曲线要素：**
>**1.** 道路
>**2.** 河流
>**3.** 等高线/等深线

>[!note]
>自然对象很少有纯粹的形状，因而不太可能由**简单函数**来描述其形状。
>那我们可以使用初等函数的组合来表示：
>一次函数，二次函数，···，n次函数
>$f \ = \ a_{0} \ + \ a_{1}x \ + \ a_{2}x^2 \ + a_{3}x^3 \ + \ ··· \ + \ a_{n}x^n$
>这里系数$a_{i}$未知
>同时，**小波变换**与**快速傅里叶变换**理论表明，可以将任意信号分解为简单函数的线性组合，但代价颇高；
>更因为**龙格库塔**现象的存在，对某些形状的逼近计算不可行。

>[!note]
>工业设计上，出现**样条逼近**的解决办法：
>Pierre Bézier，1970s，Renault工厂
>
>样条逼近有时又称**分段线性逼近**，即相邻两点间线性逼近，整体上再组合。
>样条逼近具有严密的数学解释( *Bernstein / Chebyshev* 多项式 )

>[!note]
>**径向基函数逼近** ( *Radial Basis Function* )：用一组基本形状( 函数 )去逼近目标的任意形状。
>高斯函数( gaussian )：$\varphi(x) \ = \ exp(-\frac{x^2}{2σ^2})$
>多面函数( multiquadric )：$\varphi(x) \ = \ \sqrt{1 + \frac{x^2}{\sigma^2}}$
>薄板曲面( thin - plate )：$\varphi(x) \ = \ x^2\ln{(x+1)}$
>
>所谓径向基函数，是说函数的影像随着距离( 径向! )向四周而变化，函数中的 *x* 即是距离。

>[!note]
>现在假设有 *N* 个采样点，每一个采样点对其余
>影响的权重即是点之间距离 *x* 的RBF值，每
>参量，即：
>$$\color{#adc094}{F(r) = \sum_{i=1}^{n}\omega_{i}\varphi(||r - r_{i}||)}$$
>![[Pasted image 20260317203112.png]]
>对此 *N* 个点，注意它有真值{ $y_{i}$ }
>$$ \underbrace{ \begin{bmatrix} \varphi_{11} & \varphi_{12} & \cdots & \varphi_{1N} \\ \varphi_{21} & \varphi_{22} & \cdots & \varphi_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ \varphi_{N1} & \varphi_{N2} & \cdots & \varphi_{NN} \end{bmatrix} }_{\Phi} \qquad \underbrace{ \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_N \end{bmatrix} }_{\mathbf{w}} \qquad = \qquad \underbrace{ \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_N \end{bmatrix} }_{\mathbf{y}}, \quad \text{其中} \ \varphi_{ji} = \varphi\!\left(\left\|\boldsymbol{r}_j - \boldsymbol{r}_i\right\|\right) $$
>
>这样可得到当前条件下各点的系数$\color{#c36e75}\Phi$和权重$\color{#c36e75}W$，这些参数对其它任意点也适用！

---
#### 4.3.4 样条与RBF光滑曲线

>[!note]
>在Python的scipy包中，已经具有RBF插值及实现RBF的接口。
>
>但RBF接收不了三维曲线；
>`c = RBF(x,y,z,function = 'multiquadric')`
>
>VTK提供的样条可以拟合三维曲线：
> - **vtkParametric + vtkParametricFunctionSource**  
>   - 用于定义并生成参数化的三维曲线或曲面。  
>   - `vtkParametric` 提供数学公式，`vtkParametricFunctionSource` 将其采样为几何数据。  
>   - 适合 **生成型**：通过公式生成曲线。
>
> - **vtkSplineFilter**  
>   - 用于对已有的 polyline 数据进行样条插值和平滑。  
>   - 输入是离散点或折线，输出是拟合后的光滑三维曲线。  
>   - 适合 **拟合型**：通过数据点拟合曲线。
>
> 👉 总结：  
> - **生成曲线**：`vtkParametric` + `vtkParametricFunctionSource`  
> - **拟合已有点集**：`vtkSplineFilter`  
> 三者都能得到三维曲线，但用途不同：前两个偏向数学建模，后者偏向数据拟合。
>
>$\color{#eeb074} Hermite \ / \ Bezier \ / \ Lagrange \ 曲线及用法，参见 \ vtkBezierCurve \ / \ vtkLagrangeCurve$

---
#### 4.3.5 练习

##### 4.3.5.1 练习1

![[Pasted image 20260316104234.png]]

![[Pasted image 20260316104618.png]]

##### 4.3.5.2 练习2

![[Pasted image 20260316112152.png]]

![[Pasted image 20260316111727.png]]

![[Pasted image 20260316112242.png]]

##### 4.3.5.3 练习3

![[Pasted image 20260316112509.png]]

![[Pasted image 20260316113351.png]]

![[Pasted image 20260316113623.png]]

![[Pasted image 20260316113639.png]]

---
### 4.4 三角形与曲面
