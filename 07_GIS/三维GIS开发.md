---
tags:
  - 三维GIS
创建时间: 2026-03-02T09:50:00
课程: 三维GIS开发
课程类型: 选择性必修
阶段: 大三下
老师: 段新桥
开始日期: 2026-03-02
结束日期: 2026-03-02
---
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
## 2.2 