---
tags:
  - 408_计算机学科专业基础
创建时间: 2026-01-11T16:00:00
考试科目: "408"
课程: C语言
阶段: 零基础
老师: 泥鳅
开始日期: 2026-01-11
结束日期:
---
---
[[2026-01-16]]
# 1. 配置C语言开发环境
##  1.1 简单回顾第一份代码的执行过程

```C
#include<stdio.h>
int main(){
	printf("hello world\n");
	
	return 0;
}
```

	1.打开 VS Code
	2.创建项目 - 解决方案
	3.找到源文件文件夹往其中去添加一个文件
	4.C++ 是 C 的超集
	5.调试的过程 = 编译 + 运行
---
# 2. 程序员视角中的计算机
## 2.1 计算机是什么？
	计算机是模拟人类的思考和运算的过程的机器。
	算盘
	算盘计算 1 + 2 = ？（只需要用到算盘）
	算盘计算 1 + 2 + 3 - 4 = ？（不仅需要用到算盘，还要用到草稿纸）
	计算机将算盘替换为CPU（中央处理器），将草稿纸替换为存储器。
	即：计算机 = CPU + 存储器
---
## 2.3 理解一份C代码

```C
#include<stdio.h>

int main() {
	int i = 1;
	i = i + 2;
	i = i + 3;
	i = i - 4;
	printf("i = %d\n", i);
	
	return 0;
}
```

	#include<stdio.h>
	#开头的指令叫做预处理指令

	int main(){ ... } 函数的定义
		· 定义：将一个概念的所有信息都描述清楚。
		· int（返回值）：类似于数学中函数的因变量。
		· main（函数名）：函数名是用户自己设计的（标识符），名字为main的函数比较特殊，它是整个程序的入口。
		· ()（参数）：类似于数学中函数的自变量。
		· {}（函数体）：函数运行过程中，需要执行的指令。

		int 是一个关键字（C语言语法规定的），它描述的是一种整数的数据类型。
		main函数的返回值是一个整数。
		()说明main函数的参数是空的。

		int i = 1; 分号说明一个表达式的结束。
		定义了一个名字叫做i的变量，变量的类型是整数，变量一创建里面的数值就是1。
		变量就是在存储器里面找了一块位置,给它起了个名字。

		i = i + 2; 先计算 i + 2 ，再赋值给变量i。
		“ = ” 是赋值的意思。

		return 0; 返回一个整数0。
---
## 2.4 内存模型
	1.信息
		信息是对不确定性的消除。 —— 香农

		bit（比特）：一位bit就是0或者1。

			抛硬币
				正面 ——> 0
				反面 ——> 1
			红绿灯
				红灯 ——> 00
				黄灯 ——> 01
				绿灯 ——> 10
				保留 ——> 11
				
$$n位bit可以描述2^{n}种可能性$$

		机器数：一串二进制数。
		真值：人类所能理解的信息。
		编码：把真值映射成机器数的过程。
---

	2.进制
		· 二进制：逢2进1。
			0 1 10 11 100 101 110 ...
		· 十进制：逢10进1。
			0 1 2 3 4 5 6 7 8 9 10
---

	3.进制转换
		· 二进制怎样转换为十进制？
			加权求和法：二进制数的每一位乘以对应的 2 的幂次（权重），然后求和。

$$
\begin{gather}
\text公式：{十进制数} = \sum_{i=0}^{n} b_i \times 2^i\\
\text其中  b_i  是二进制数的第 i 位（从右向左，从 0 开始编号）
\end{gather}
$$
				步骤：
					1. 从二进制数最右边开始（最低位），给每位编号，从 0 开始。
					2. 每位数字乘以2^{位索引}。
					3. 将所有乘积相加。

$$\text例：1101_{2} = 1 * 2^{3} + 1 * 2^{2} + 0 * 2^{1} + 1 * 2^{0} = 13_{10}$$

		· 十进制如何转换成二进制？
			除2取余法：将一个十进制整数不断除以2，记录每次除法的余数（0或1），直到商为0为止，然后将所得余数倒序排列即为转换所得的二进制数。
			步骤：
				1. 将十进制整数除以2，记录商和余数。
				2. 用商继续除以2，再记录余数。
				3. 重复直到商为0。
				4. 将余数从下往上（逆序）排列。

$$
\begin{align*}
&\text{例：十进制29转二进制} \\
&\begin{aligned}
\text{计算过程：}
29 &\div 2 = 14 \cdots 1 \\
14 &\div 2 = 7  \cdots 0 \\
7  &\div 2 = 3  \cdots 1 \\
3  &\div 2 = 1  \cdots 1 \\
1  &\div 2 = 0  \cdots 1 \\
\end{aligned} \\
&\text{余数序列（从下往上读）：} 11101 \\
&\begin{aligned}
\text{验证}：
11101_2 &= 1 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 \\
       &= 16 + 8 + 4 + 0 + 1 \\
       &= 29_{10}
\end{aligned}
\end{align*}
$$
- [0] 进制转换的具体方法参见：[[二进制与十进制相互转换方法]]
---

	4.八进制和十六进制
		· 八进制

$$
\begin{gather}
\text8 = 2^{3}\\
\text1234_{8} = 1 * 8^{3} + 2 * 8^{2} + 3 * 8^{1} + 4 * 8^{0} = (001|010|011|100)_{2} 
\end{gather}
$$
		· 十六进制

$$
\begin{gather}
\text16 = 2^{4}\\
\text1234_{16} = 1 * 16^{3} + 2 * 16^{2} + 3 * 16^{1} + 4 * 16^{0} = (0001|0010|0011|0100)_{2}\\
\end{gather}
$$
$$
\begin{gather}
\text十进制：0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16\\
\text十六进制：0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|10\\
\end{gather}
$$
	5.内存
		内存的最小单位是byte（字节），1 byte = 8 bit = 8位二进制数 = 2位十六进制数。
		数据的单位是byte（字节），所有数据都是以byte（字节）为单位放进内存中的。
		每一个byte都有一个独立的十六进制数字编码用来描述不同数据所在的位置，我们将其称为地址。

```
000000C61AF0FCC4  00
000000C61AF0FCC4（地址：16位十六进制数 = 64位二进制数 = 64 bit）
00（数据：2位16进制数 = 8位二进制数 = 8 bit）
```
---
# 3. 基础语法
## 3.1 空白字符
### 3.1.1 空格 换行（Enter） 制表符（TAB）

	空白字符只起到分隔的作用，不充当语法成分。
---
## 3.2 注释

```c
//单行注释

/*
多行
注释
*/
```

	注释的使用场景：
		· 用来解释代码，说明变量的作用，或者是运算的作用。
		· 用来测试代码，面对可能出错的代码，我们不会直接删除，而是将其改成注释，方便后续恢复原状。
---
## 3.3 关键字和标识符
	关键字：由C语言语法规定的一些单词，它们有着固定的含义和用途。
	
	C语言是大小写敏感的：
		int 是关键字
		Int 不是关键字

```c
#include<stdio.h>
int /* int：用于声明函数返回整型值 */ main(){
	int i = 1;// int：用于声明整型变量
	
	return 0;//return：将函数执行结果返回给调用者
}
```

- [0] C语言常用的32个关键字参见：[[C语言常用的32个关键字]]
---

	标识符：用户自定义的单词，一般用来给变量或者是函数起名字。

	规范：
		· 标识符不能和关键字重复。
		· 大小写敏感。
		· 标识符由数字、字母和下划线组成。
		· 标识符开头不能是数字。

		int 不是标识符
		Int 是标识符
		3xy 不是标识符（原因：“3xy”以数字开头了。）
		xy3 是标识符
---
[[2026-01-17]]
# 4. 常量、变量和数据类型
## 4.1 字面值常量和符号常量
	1.数据对象
		· 常量 —— 不可修改
			- 字面值常量
				一写出来，就知道它的含义。
				例如：
					整数 1234
					浮点数 3.14
					字符 'a'（界定符是英文单引号）
					字符串 "hello world"（界定符是英文双引号）
				字面值常量特别容易混淆，因此我们引入一种新的常量来规避此种现象。

```c
#include<stdio.h>
int main(){
	//圆周率为3 半径也是3
	printf("R = %d,A = %d\n",3,3 * 3 * 3);
	
	return 0;
}
```

			- 符号常量
				使用宏定义来实现符号常量。
				宏的作用是在预处理阶段做文本替换。
				
				预处理只做了文本替换，不会执行编译检查。
				所以，为了规避宏定义带来的问题，我们需要加括号。
				
				代码生成的流程（简化版）：
					*.cpp（预处理） --> *.i （编译） --> *.exe（可执行文件）

- [0] 代码生成的完整流程详见：[[计算机组成原理]]

```c
#include<stdio.h>
// 使用宏定义来实现符号常量
// 宏的作用是在预处理阶段做文本替换
#define R 3
#define PIE 3
int main(){
	//圆周率为3 半径也是3
	printf("R = %d,A = %d\n",R,PIE * R * R);
	
	return 0;
}
```

			- 小结
				字面值常量：1234、3.14、'a'、"hello world"
				符号常量：#define R 3
					注意空格，还需要注意末尾没有分号。
---
## 4.2 变量的概念、定义和初始化
		· 变量 —— 可以修改
			变量是一片可以存放数据的有名字关联的内存区域。

			要素：
				- 名字 --> 满足标识符的规范
				- 内存区域的大小 --> 通过数据类型来描述
				- 人类理解的真值如何和机器数对应起来 --> 需要设计一个合理的映射/编码规则 --> 通过数据类型来描述

```c
#include<stdio.h>
int main(){
	// 数据类型 变量名字
	int i;
	printf("sizeof(i) = %d\n",sizeof(i));
	double d1,d2; // 定义了两个变量d1和d2
	printf("sizeof(d1) = %d,sizeof(d2) = %d,sizeof(double) = %d\n",sizeof(d1),sizeof(d2),sizeof(double));
	// 数据类型决定变量在内存空间中所占的字节数量，也就是说：数据类型决定内存大小。
	// 数据类型还决定机器数和真值之间的编码规则。
	
	return 0;
}
```

			变量的初始化和赋值
				初始化：在创建变量的时候就赋予了一个初始值。
				赋值：用新的值去取代原来内存里面的内容。

				初始化和赋值都使用了 '=' 运算符。
				当 '=' 在定义语句中，我们将其称为初始化。
				当 '=' 出现在其他位置，我们将其称为赋值。

				在C语言中，同一个符号在不同的位置有着不同的含义。

```c
#include<stdio.h>
int main(){
	//初始化的代码
	int i = 3; //定义一个变量i然后设置初值为3 | 当 '=' 在定义语句中，我们将其称为初始化
	i = 4; //用4来取代i原来的内容 | 当 '=' 出现在其他位置，我们将其称为赋值
	i = i + 1; //先计算i + 1，再用计算所得结果取代原来的内容
	
	return 0;
}
```
---
## 4.3 数据类型概览
	· 数据类型
		基本数据类型
			整数
				有符号整数
					char 同时也是字符类型 （C语言中，字符的本质是整数）
					short
					int
					long / long long
				无符号整数
					unsigned char
					unsigned short
					unsigned int
					unsigned long / unsigned long long
			浮点数
				单精度浮点数 float
				双精度浮点数 double
---
## 4.4 不同类型的整形字面值
	整数类型
		有符号整数
			包含：负数 0 正数

			char —— 1byte
			short —— 2byte
			int  —— 4byte
			long —— 4byte
			long long —— 8byte

			在不同的平台上面，int和long的大小会发生变化	

		无符号整数
			只有0和正数

		整形字面值的写法

```c
#include<stdio.h>
int main(){
	printf("1234 = %d\n",1234); //1234是十进制
	printf("01234 = %d\n",01234); //0开始的整形字面值是八进制的
	printf("0x1234 = %d\n",0x1234); //0x开始的整形字面值是十六进制的
}
```

		整数的数据范围：

$$
int \ ——> \ 4Byte \ ——> \ 32Bit \ ——> \ 2^{32} \ 种可能性 
\begin{cases}
0 & \text1种 \\
正数 & \text2^{31} - 1种 \\
负数 & \text2^{31}种 \\
\end{cases}
$$
		推广到其他的数据类型，结论类似：

$$
大小为n个Bit的有符号整数 \ ——> \ 2^{n} \ 种可能性 
\begin{cases}
0 & \text1种 \\
正数 & \text2^{n-1} - 1种 \\
负数 & \text2^{n-1}种 \\
\end{cases}
$$
---
## 4.5 整数溢出问题
	溢出问题：正数在做运算的时候，算出来的结果变成了负数。

```c
#include<stdio.h>
int main(){
	int i = 0x7fffffff 
	// 0111|1111|1111|1111|1111|1111|1111|1111 --> 最大正数
	i = i + 1;
	printf("i = %d\n",i);
	
	return 0
}
```

```c
结果：i = -2147483648
```
- [0] 整数溢出问题的具体原因详见：[[计算机组成原理]]
---
## 4.6 无符号整数
	无符号整数类型
		只能描述非负数

$$
\begin{gather}
\text unsigned \ char \ —— \ 1 \ byte \ 范围:0 \sim \ 2^{8}-1 \\
\text unsigned \ short \ —— \ 2 \ byte \ 范围:0 \sim \ 2^{16}-1 \\
\text unsigned \ int \ —— \ 4 \ byte \ 范围:0 \sim \ 2^{32}-1 \\
\text unsigned \ long \ —— \ 4 \ byte \ 范围:0 \sim \ 2^{32}-1 \\
\text unsigned \ long long \ —— \ 8 \ byte \ 范围:0 \sim \ 2^{64}-1 \\
\end{gather}
$$
```c
#include<stdio.h>
int main(){
	unsigned int u = 0xffffffff;
	u = u + 1;
	printf("u = %u\n",u);
	
	return 0;
}
```

```c
结果：u = 0
```

- [0] 输出结果表明：不管是有符号整数还是无符号整数能够表示的数据范围都是有限的，都会发生溢出问题。

- [1] 进一步推广可得到以下结论：无论什么数据类型，都是有范围的，都会发生溢出问题。
---
## 4.7 浮点数
	浮点数类型
		带小数的数据
			float -- 4byte
			double -- 8byte

```c
#include<stdio.h>
int main(){
	float f = 3.14159;
	printf("f = %f\n",f);
	
	return 0;
}
```

```c
结果：f = 3.141590
```

```c
#include<stdio.h>
int main(){
	float f = 3.14159;
	printf("f = %.10f\n",f);
	
	return 0;
}
```

```c
结果：f = 3.1415901184
```

		整数与浮点数的区别：
			整数是精确的。
			浮点数是近似值，有误差，因此浮点数是不能够去比较相等的，两个浮点数之间总会有一些偏差值。

```c
#include<stdio.h>
int main(){
	float f = 3.14159;
	printf("f = %.10f\n",f);
	double d = 3.14159;
	printf("d = %.10f\n",d);
	
	return 0;
}
```

```c
结果：
	f = 3.1415901184
	d = 3.1415900000
```

- [0] 输出结果表明：double的精度比float高。

- [1] double的有效数字是15位，float的有效数字是6位。
---

		浮点数的精度丢失问题：
			两个浮点数，如果绝对值相差很大，可能会出现精度丢失的问题。

```c
#include<stdio.h>
int main(){
	float a = 1.2345e10; // e10 = * 10^10
	float b = a + 20;
	printf("a = %f,b = %f\n",a,b);
	
	return 0;
}
```

```c
结果：a = 12344999936.000000,b = 12344999936.000000
```

- [0] 输出结果表明：当两个浮点数的绝对值相差过大，会出现精度丢失的问题。该现象产生的原因为：a与b二者相差20，20相对于1.2345e10来说显得过于小了，所以在做加减法运算时，20在移位的过程中由于小于精度而被忽略掉了，所以加法的信息也就没有了。

- [1] 总结：当两个浮点数的绝对值相差过大时，用float进行加减法运算是不行的。此问题的本质是由于float的精度不够高，因此我们可以换用double将精度提高。

```c
#include<stdio.h>
int main(){
	double a = 1.2345e10; // e10 = * 10^10
	double b = a + 20;
	printf("a = %f,b = %f\n",a,b);
	
	return 0;
}
```

```c
结果：a = 12345000000.000000,b = 12345000020.000000
```
---
## 4.8 字符和ASCII编码
	· 字符类型
		可以打印在屏幕上面的字符数据。
		字母、符号、数字之类。

		C语言种用char来表示字符类型。

```c
#include<stdio.h>
int main(){
	char ch;
	//显示字母
	ch = 'a';
	printf("ch = %c\n",ch);
	
	return 0;
}
```

```c
结果：ch = a
```

```c
#include<stdio.h>
int main(){
	char ch;
	//显示数字
	ch = '0'; //字符只能显示一位数字
	printf("ch = %c\n",ch);
	
	return 0;
}
```

```c
结果：ch = 0
```

```c
#include<stdio.h>
int main(){
	char ch;
	//显示逗号
	ch = ',';
	printf("ch = %c\n",ch);
	
	return 0;
}
```

```c
结果：ch = ,
```

```c
#include<stdio.h>
int main(){
	char ch;
	//换行\n
	ch = '\n';
	printf("ch = %c\n",ch);
	
	return 0;
}
```

```c
结果：ch = 

```

```c
#include<stdio.h>
int main(){
	char ch;
	//回车\r —— 将光标从右边移到左边
	ch = '\r';
	printf("abc%cxyz",ch);
	
	return 0;
}
```

```c
结果：xyz
```

```c
#include<stdio.h>
int main(){
	char ch;
	//退格\b —— 光标往左退一格
	ch = '\b';
	printf("abc%cxyz",ch);
	
	return 0;
}
```

```c
结果：abxyz
```

```c
#include<stdio.h>
int main(){
	char ch;
	//制表符\t
	ch = '\t';
	printf("abc%cxyz",ch);
	
	return 0;
}
```

```c
结果：abc xyz
```

```c
#include<stdio.h>
int main(){
	char ch;
	//反斜杠\\
	ch = '\\';
	printf("abc%cxyz",ch);
	
	return 0;
}
```

```c
结果：abc\xyz
```

	· char类型和整数的关系

```c
#include<stdio.h>
int main(){
	char ch;
	ch = 'a'; //'a' 和 数值97是等价的
	printf("ch = %d\n",ch);
	
	return 0;
}
```

```c
结果：ch = 97
```

```c
#include<stdio.h>
int main(){
	char ch1;
	ch1 = 97;
	printf("ch1 = %c\n",ch1);
	
	return 0;
}
```

```c
结果：ch1 = a
```

- [0] 输出结果表明：在内存中，任意两个数据当其数值为'a'和97时，这两个数据是等价的，输出结果的表现形式取决于打印时的解释方式（用占位符%d还是用占位符%c）。具体过程如下图所示。

$$
\text 97 \ ——> \
\begin{cases}
\%d & 97 \\
\%c & a \\
\end{cases}
$$

- [1] 因此可得到以下结论：字符的底层都是整数。
---

	· 编码规则：记录各种各样的数值与字符之间的对应关系 --> ASCII

	ASCII码
		128种对应规则 —— 0 ~ 127

		常用的ASCII码：
			0 —— NUL（null） —— 空
			10 —— LF（line feed —— new line） —— 换行
			48 ~ 57 —— 数字 0 ~ 9
			65 ~ 90 —— 大写字母 A ~ Z
			97 ~ 122 —— 小写字母 a ~ z

- [0] '0'等价于48而不是0

- [1] '3' - '1' 等价于 3 - 1

- [2] 相同含义的大写字母与小写字母之间相差32

- [0] 完整版ASCII码表格详见：[[ASCII码表(完整版)]]
---
## 4.9 字面值常量的默认类型
	一个整数字面值常量优先是int类型。
	int放不下，就是unsigned int，然后是long long。

	任何浮点数字面值常量都是double类型。

```c
#include<stdio.h>
int main(){
	float f = 1 / 2;
	printf("f = %f\n",f);
	
	return 0;
}
```

```c
结果： 0.000000
```

```c
#include<stdio.h>
int main(){
	float f = 1.0 / 2;
	printf("f = %f\n",f);
	
	return 0;
}
```

```c
结果： 0.500000
```

```c
#include<stdio.h>
int main(){
	long long ll;
	ll = 131072 * 131072;
	printf("ll = %lld\n",ll);
	
	return 0;
}
```

```c
结果：ll = 0
```

- [0] 输出结果和预想结果不同的原因：131072本身是一个int类型，131072也是一个int类型。int类型 * int类型 = int类型。二者相乘等于2^34超出了int类型能够表达的范围导致溢出了。所以在赋值给ll之前已经有一部分信息丢掉了。就算后面补救赋值给了一个long long类型信息已经不完整了导致输出结果和预想结果不同。解决办法如下：

```c
#include<stdio.h>
int main(){
	long long ll;
	ll = (long long)131072 * 131072; //(long long) + 表达式 —— 做类型转换
	printf("ll = %lld\n",ll);
	
	return 0;
}
```

```c
结果：ll = 1719869184
```
---
[[2026-01-18]]
# 5. 专题A 输入和输出
## 5.1 缓冲区
	目前需要了解的缓冲区：
		stdin —— 标准输入缓冲区
			用来处理标准输入缓冲区中的数据的函数有：
				scanf getchar fgets
		stdout —— 标准输出缓冲区
			用来处理标准输出缓冲区中的数据的函数有：
				printf puts
---
## 5.2 scanf( )的基本使用
	scanf()
		scanf()（格式化输入）：从标准输入缓冲区拷贝数据到自己的内存。

```c
#include<stdio.h>
int main(){
	int i; //用来存放从stdin过来的数据
	int ret = scanf("%d",&i); //%d是一个控制符，用来说将要接收的数据的类型是整数；&i是将数据存入i的地址当中,&符号的作用是取地址，不可省略。
	printf("ret = %d,i = %d\n",ret,i);
	
	return 0;
}
```

```c
在Visual Studio中点击编译，此时在输出窗口中会有一条报错信息："error C4996"提示我们scanf是不安全的。
```

- [0] 使用scanf( )时可能会报错，其原因是scanf是不安全的。我们希望将这个报错忽略掉，因此进行以下操作：

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i; //用来存放从stdin过来的数据
	int ret = scanf("%d",&i); //%d是一个控制符，用来说将要接收的数据的类型是整数；&i是将数据存入i的地址当中,&符号的作用是取地址，不可省略。
	printf("ret = %d,i = %d\n",ret,i);
	
	return 0;
}
```

```c
输入：1234
结果：ret = 1,i = 1234
```

		使用scanf()的步骤如下：
			1. 准备变量 —— 数据的目的地
			2. scanf()的两类参数：
				- 第一类参数：字符串 —— 用来描述数据的格式
				- 第二类参数：& + 变量名 —— 用来说明存放数据的地址（记得使用'&'运算符）
			3. scanf()的返回值是读取成功的变量个数
				- 如果返回值和'%'个数相等 —— 读取成功
				- 如果返回值小于'%'个数 —— 有数据读取失败
				- 如果返回值为-1，我们认为是特殊情况，我们将这种特殊情况称为EOF

- [0] 若想深入了解EOF请参见：[[深入了解EOF]]
---

	stdin的性质
		先进先出 —— 本质上是一个字符队列

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i;
	float f;
	scanf("%d%f",&i,&f);
	printf("i = %d,f = %f\n",i,f);
	
	return 0;
}
```

- [0] 使用scanf( )时，其参数中的%d、%f、%lf会忽略缓冲区里面的前置空白字符（换行、空格、制表符）

- [1] 因此我们使用scanf( )时，不需要考虑输入内容当中有多少个空格，控制字符可以连着写

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	char ch;
	scanf("%c",&ch);
	printf("ch = %c\n",ch);
	
	return 0;
}
```

- [2] 使用scanf( )时，其参数中的%c不会忽略前面的空白字符

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i;
	char ch;
	scanf("%d%c",&i,&ch);
	printf("i = %d,ch = %c\n",i,ch);
	
	return 0;
}
```

```c
输入：1234 a
结果：i = 1234,ch = 
```

- [3] 我们希望改变scanf( )中参数%c的性质，让它能够忽略前面的空白字符，因此可以进行如下操作：

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i;
	char ch;
	scanf("%d %c",&i,&ch); //%c前面的空格，可以让%c忽略前面的空白
	printf("i = %d,ch = %c\n",i,ch);
	
	return 0;
}
```

- [4] 一般的使用场景：绝大多数情况下scanf( )的格式字符串里面，只有%控制符，偶尔会在%c前面加空格
---
## 5.3 getchar( )
	getchar()从stdin（标准输入缓冲区）获取并返回下一个字符，如果到达文件尾返回EOF。
	getchar()等价于scanf(%c)，也不会忽略空白字符

```c
#include<stdio.h>
int main(){
	char ch1,ch2;
	ch1 = getchar();
	ch2 = getchar();
	printf("ch1 = %c,ch2 = %c\n",ch1,ch2);
	
	return 0;
}
```

```c
输入：a b
结果：ch1 = a,ch2 =  
```
---
## 5.4 printf( )
	stdout是一种行缓冲，当数据中有换行符的时候，就会刷到屏幕上面 ——> 我们写的代码输出语句要以换行结尾

	printf() —— 格式化输出

	先修知识 —— 占位符
		%c 字符
		%d 十进制
		%o 八进制
		%x 十六进制
		%f 浮点数
		%u 无符号整数
		%lld long long
		%ld long
		%s 字符串

```c
#include<stdio.h>
int main(){
	char name[] = "CaiXukun"; //C语言中用字符数组来存储字符串
	int age = 30;
	char address[] = "USA";
	printf("I am %s,I am %d years old.I live in %s\n",name,age,address);
	
	return 0;
}
```

	设置数据的宽度

```c
#include<stdio.h>
int main(){
	char name1[] = "CaiXukun",name2[] = "WuYifan"; //C语言中用字符数组来存储字符串
	int age1 = 30,age2 = 33;
	char address1[] = "USA",address2[] = "Canada";
	printf("I am %8s,I am %d years old.I live in %s\n",name1,age1,address1); //%8s：保证数据宽度不小于8个字符并且右对齐
	printf("I am %8s,I am %d years old.I live in %s\n",name2,age2,address2);
	
	return 0;
}
```

```c
#include<stdio.h>
int main(){
	char name1[] = "CaiXukun",name2[] = "WuYifan"; //C语言中用字符数组来存储字符串
	int age1 = 30,age2 = 33;
	char address1[] = "USA",address2[] = "Canada";
	printf("I am %-8s,I am %d years old.I live in %s\n",name1,age1,address1); //-%8s：保证数据宽度不小于8个字符并且左对齐
	printf("I am %-8s,I am %d years old.I live in %s\n",name2,age2,address2);
	
	return 0;
}
```

```c
#include<stdio.h>
int main(){
	char name1[] = "CaiXukun",name2[] = "WuYifan"; //C语言中用字符数组来存储字符串
	int age1 = 30,age2 = 33;
	char address1[] = "USA",address2[] = "Canada";
	printf("I am %-8s,I am %03d years old.I live in %s\n",name1,age1,address1); //%03d保证数据宽度不小于3，并且当数据宽度小于3时在前面补0
	printf("I am %-8s,I am %03d years old.I live in %s\n",name2,age2,address2);
	
	return 0;
}
```

- [0] %和d/s/c/f之间可以添加整数，用来描述最小宽度

- [1] 整数前面加负号，可以实现左对齐

- [2] 整数前面加0，可以让不足最小宽度的数据填充0
---

	设置浮点数的宽度

```c
#include<stdio.h>
int main(){
	double d = 3.1415926535;
	printf("d = %.15lf\n",d);
	
	return 0;
}
```

	puts() —— 打印一行
		puts(str) 等价于 printf("%s\n",str)

```c
#include<stdio.h>
int main(){
	char str[] = "hello";
	puts(str);
	
	return 0;
}
```
---
[[2026-01-25]]
# 6. 运算符和表达式
	运算符
		算术运算符
		关系运算符
		逻辑运算符
		赋值运算符
		位运算符
		其他：条件运算符 逗号运算符
---
## 6.1 算术运算符
	+ - * / %
	整数支持：+ - * / %
	浮点数支持：+ - * / （不支持%）

```c
#include<stdio.h>
int main(){
	int a = 10,b = 5;
	printf("a + b = %d\n",a + b);
	printf("a - b = %d\n",a - b);
	printf("a * b = %d\n",a * b);
	printf("a / b = %d\n",a / b);
	printf("a %% b = %d\n",a % b); //printf()想显示%要写%%
	
	return 0;
}
```

```c
结果：
a + b = 15
a - b = 5
a * b = 50
a / b = 2
a % b = 0
```

- [0] '%'（取余运算符）的操作数必须是整数

```c
#include<stdio.h>
int main(){
	int a = 1,b = 2,c = 3;
	//优先级：* / % 高于 + -
	//相同优先级按照从左往右的顺序
	printf("output = %d\n",a + b * c);
	
	return 0;
}
```

```c
结果：output = 7
```

- [1] 优先级：* / % 高于 + -
- [2] 相同优先级按照从左往右的顺序 —— 结合性
---
## 6.2 关系运算符
	C语言当中如何描述真和假

$$
\left.
\begin{array}{l@{\quad}l}
\text{数据的机器数是0} & \text{—— 假} \\
\text{数据的机器数不是0} & \text{—— 真}
\end{array}
\right\}
\text{ ——> if 结构}
$$

```c
#include<stdio.h>
int main(){
	int condition = 1;
	if(condition){
		printf("true!\n");
	}
	else{
		printf("false!\n");
	}
	
	return 0;
}
```

```c
结果：true!
```

	关系运算符
		判断相等关系
			判断相等 ==
			判断不相等 !=
		判断大小关系
			小于 <
			小于等于 <=
			大于 >
			大于等于 >=

```c
#include<stdio.h>
int main(){
	int a = 10,b = 5;
	printf("a == b is %d\n",a == b);
	printf("a != b is %d\n",a != b);
	
	return 0;
}
```

```c
结果：
a == b is 0
a != b is 1
```

- [0] 满足条件，关系运算符的返回值为1；不满足条件，关系运算符的返回值为0。

```c
#include<stdio.h>
int main(){
	int a = 1,b = 2,c = 3;
	printf("a < b < c is %d\n",a < b < c);
	//a < b < c不是看b是否在a与c中间，而是先执行a < b，再执行b < c
	
	return 0;
}
```

```c
结果：a < b < c is 1
```

- [1] a < b < c不是看b是否在a与c中间，而是先执行a < b，再执行b < c

```c
#include<stdio.h>
int main(){
	int a = 1,b = 2,c = 1;
	printf("a == b < c is %d\n",a == b < c);
	//'<'的优先级高于'=='，所以要先做<运算，再做==运算
	
	return 0;
}
```

```c
结果：a == b < c is 0
```

- [3] 判断大小的运算符的优先级高于判断相等的运算符，相同优先级按照从左往右的顺序 —— 结合性
---
[[2026-01-26]]
## 6.3 逻辑运算符
	对布尔表达式（返回真或假的表达式）做运算

	逻辑与（&&） 逻辑或（||） 逻辑非（！）

	逻辑与 双目 L && R

<table class="table-center">
<tr>
<th>L</th>
<th>R</th>
<th>N</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>

	逻辑或 双目 L || R

<table class="table-center">
<tr>
<th>L</th>
<th>R</th>
<th>N</th>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>1</td>
<td>0</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>1</td>
<td>1</td>
</tr>
<tr>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</table>

	逻辑非 单目

$$
\begin{cases}
\ ! \ 0 & —— \ \ \ 1 \\
\ ! \ 1 & —— \ \ \ 0 \\
\end{cases}
$$

	判断某一年是不是闰年
		闰年的规则：
			· 年份能被4整除并且不能被100整除 —— 闰年
			· 年份能被400整除 —— 闰年
		year % 4 == 0 && year % 100 != 0 || year % 400 == 0

- [0] !（逻辑非） > &&（逻辑与） > ||（逻辑或）

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int year;
	scanf("%d",&year);
	if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
		printf("%d is a leap year!\n",year);
	}
	else{
		printf("%d is not a leap year!\n",year);
	}
	
	return 0;
}
```

```c
输入：2026
结果：2026 is not a leap year!
```
---
## 6.4 优先级和表达式树
	C语言运算符的优先级
		单目运算符 > 算数运算符(* / % 高于 + -) > 关系运算符(< <= > >= 高于 == !=) > 逻辑运算符(&& 高于 ||)

- [0] 完整版C语言运算符的优先级汇总表详见[[C语言运算符优先级]]
---

	表达式树
		将表达式看作一个倒着长的树结构
			树：优先级最低的作为根

```c
year % 4 == 0 && year % 100 != 0 || year % 400 == 0
```

```mermaid
graph TD
    A["||"] --> B["&&"]
    A["||"] --> C["=="]
    B["&&"] --> D["=="]
    B["&&"] --> E["!="]
    C["=="] --> F["%"]
    C["=="] --> G["0"]
    D["=="] --> H["%"]
    D["=="] --> I["0"]
    E["!="] --> J["%"]
    E["!="] --> K["0"]
    F["%"] --> L["year"]
    F["%"] --> M["400"]
    H["%"] --> N["year"]
    H["%"] --> O["4"]
    J["%"] --> P["year"]
    J["%"] --> Q["100"]
```
---
## 6.5 短路操作
	短路操作
		当逻辑与(&&)的左操作数为假时，可以不用执行右操作数
		当逻辑或(||)的左操作数为真时，可以不用执行右操作数

```c
#include<stdio.h>
int main(){
	int i = 1;
	int j = 1;
	i == j || (j = 2);
	printf("j = %d\n",j);
	
	return 0;
}
```

```c
结果：j = 1
```

- [0] 总结：当表达式中存在&&或者||时，表达式应该先执行左边的操作数，看是否触发短路，再考虑是否执行右边的操作数。
---
## 6.6 赋值运算符
	赋值运算符 L = R
		赋值运算符优先级比较低
		可以将赋值运算符'='看作一个向左指向的箭头'⬅'，其实质为把R的值(可以是临时数据)放入L的内存空间里面。因此，我们需要对L提出一些要求：

$$
\text L(左值)
\begin{cases}
① & L必须代表一片内存空间 \\
② & 该空间可以被修改 \\
\end{cases}
$$

```c
#include<stdio.h>
int main(){
	int i = 1; //这个等于号不是赋值，它是初始化
	i = 3 + 4; //合理
	3 + 4 = i; //不合理
	i = i + 1; //合理 i出现在左边表示访问i的地址；i出现在右边表示获取i的值
	i += 1; //等价于 i = i + 1;
	++i; //等价于 i = i + 1;
	
	return 0;
}
```

	赋值运算符的结合性 —— 从右往左

```c
#include<stdio.h>
int main(){
	int x,y;
	x = y = 1;
	printf("x = %d,y = %d\n",x,y);
	
	return 0;
}
```

```c
结果：x = 1,y = 1
```
---
## 6.7 三目运算符
	条件运算符 3目 A ? B : C
		检查A的真假，若A为真则返回B，若A为假则返回C

```c
#include<stdio.h>
int main(){
	int a = 10,b = 5;
	int max = a > b ? a : b;
	printf("max = %d\n",max);
	
	return 0;
}
```

```c
结果：max = 10
```

```c
#include<stdio.h>
int main(){
	int a = 10,b = 5,c = 15;
	int max = (a > b ? a : b) > c ? (a > b ? a : b) : c;
	printf("max = %d\n",max);
	
	return 0;
}
```

```c
结果：max = 15
```
---
## 6.8 逗号运算符
	逗号运算符的优先级是最低的
	A,B ——> 先执行A再执行B最后返回B
	和A;B;很像

	场景：变量i，要求先改变i的值，再判断i是否合适

	if(i = i + 1,i == 3){
	}

- [2] 注意：函数参数里面的','不是逗号运算符，C语言没有规定参数的处理顺序。
---
## 6.9 自增自减运算符
	++ 单目 自增 ——> 操作数必须是左值
	-- 单目 自减 ——> 操作数必须是左值

	++i 前缀自增 内存内容：4 返回结果：4 ——> 先自增再返回
	i++ 后缀自增 内存内容：4 返回结果：3 ——> 先返回再自增

```c
#include<stdio.h>
int main(){
	int i = 3;
	int j;
	j = ++i; //前缀自增：先自增(++)再返回
	printf("i = %d,j = %d\n",i,j)
	
	return 0;
}
```

```c
结果：i = 4,j = 4
```

```c
#include<stdio.h>
int main(){
	int i = 3;
	int j;
	j = i++; //前缀自增：先自增(++)再返回
	printf("i = %d,j = %d\n",i,j)
	
	return 0;
}
```

```c
结果：i = 4,j = 3
```
---
[[2026-01-27]]
## 6.10 运算符总结

```c
5 > 3 && 8 < 4 - !0
```

```mermaid
graph TD
    A["&&"] --> B["&gt;"]
    A["&&"] --> C["<"]
    B["&gt;"] --> D["5"]
    B["&gt;"] --> E["3"]
    C["<"] --> F["8"]
    C["<"] --> G["&minus;"]
    G["&minus;"] --> H["4"]
    G["&minus;"] --> I["!"]
    I["!"] --> J["0"]
```

```
先算 5 > 3 --> 1

!0 --> 1
4 - 1 --> 3
8 < 3 --> 0

最后 1 && 0 --> 0
```

- [0] 1.需要按照优先级整理表达式树
- [1] 2.几个特殊运算符 && || , 规定了执行顺序
---
# 7. 选择结构
## 7.1 选择结构描述

	先修知识 —— 顺序结构

```mermaid
flowchart TD
    Start([开始]) --> Input[/输入数据/]
    Input --> Process1[处理步骤1]
    Process1 --> Process2[处理步骤2]
    Process2 --> Output[/输出结果/]
    Output --> End([结束])
```

	选择结构

```mermaid
flowchart TD
    Start([开始]) --> Condition{条件判断}
    Condition -->|真| ProcessA[执行操作A]
    Condition -->|假| ProcessB[执行操作B]
    ProcessA --> End([结束])
    ProcessB --> End
```

- [0] C语言中选择结构靠if和switch两种方式实现
---
## 7.2 单分支if
	if(表达式){
		语句块
	}

	语句块可以是：
		一个语句
		{多个语句}

```mermaid
flowchart TD
    A([开始]) --> B[操作1]
    B --> C{条件判断?}
    C -->|真| D[执行语句块]
    D[执行语句块] --> F([结束])
    C -->|假| F([结束])
```
```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i;
	scanf("%d",&i);
	if(i == 1){
		printf("i is 1!\n");
	} //编程要求：我们自己写的代码，不能省略花括号。
	
	return 0;
}
```

```c
输入：1
结果：i is 1!
```
---
## 7.3 双分支if
	if(表达式){
		语句块1
	}
	else{
		语句块2
	}

```mermaid
flowchart TD
    A([开始]) --> B{条件判断?}
    B -->|真| C[执行语句块1]
    B -->|假| D[执行语句块2]
    C --> E([结束])
    D --> E([结束])
```

```c
#include<stdio.h>
int main(){
	int a = 10,b = 5;
	if(a > b){
		printf("max = a,a is %d\n",a)
	}
	else{
		printf("max = b,b is %d\n",b);
	}
	
	return 0;
}
```

```c
结果：max = a,a is 10
```

```c
#include<stdio.h>
int main(){
	int a = 10,b = 15,c = 20;
	if(a > b){
		if(a > c){
			printf("max = a,a is %d\n",a);
		}
		else{
			printf("max = c,c is %d\n",c);
		}
	}
	else{
		if(b > c){
			printf("max = b,b is %d\n",b);
		}
		else{
			printf("max = c,c is %d\n",c);
		}
	}
	
	return 0;
}
```

```c
结果：max = c,c is 20
```
---
## 7.4 多分支if
	只需要在else的语句里面嵌套使用if，就可以实现更多分支的if了。

```mermaid
flowchart TD
    Start([开始]) --> Condition1{条件判断1?}
    Condition1 -->|真| Process1[执行语句块1]
    Condition1 -->|假| Condition2{条件判断2?}
    Condition2 -->|真| Process2[执行语句块2]
    Condition2 -->|假| Default[执行语句块3]
    Process1 --> End([结束])
    Process2 --> End([结束])
    Default --> End([结束])
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int height;
	scanf("%d",&height);
	if(height < 160){
		printf("He is short!\n");
	}
	else if(height <= 178){
		printf("He is middle-sized!\n")
	}
	else{
		printf("He is tall!\n");
	}
	
	return 0;
}
```

```c
输入：180
结果：He is tall!
```
---
[[2026-01-29]]
## 7.5 else就近匹配
	不加花括号可能会出现的问题

```c
#include<stdio.h>
int main(){
	int i = 0;
	if(i > 1)
		if(i < 10)
			printf("i is between 1 amd 10\n");
	else{
		printf("i is less than 1\n");
	}
	
	return 0;
}
```

```c
结果：
```

- [0] if和else是就近匹配的

```c
#include<stdio.h>
int main(){
	int i = 0;
	if(i > 1){
		if(i < 10){
			printf("i is between 1 and 10\n");
		}
	}
	else{
		printf("i is less than 1\n");
	}
	
	return 0;
}
```

```c
结果：i is less than 1
```

- [1] C语言中，缩进不代表匹配规则
---
## 7.6 switch
	用于处理固定的多分支。

	switch(表达式){
		case 值1:
			...
		case 值2:
			...

		...

		default:
			...
	}

```c
#include<stdio.h>
int main(){
	int i = 4;
	switch(i){
		case 1:
			printf("1\n");
		case 2:
			printf("2\n");
		case 3:
			printf("3\n");
		default:
			printf("default!\n");
	}
	
	return 0;
}
```

```c
结果：default!
```

```c
#include<stdio.h>
int main(){
	int i = 3;
	switch(i){
		case 1:
			printf("1\n");
		case 2:
			printf("2\n");
		case 3:
			printf("3\n");
		default:
			printf("default!\n");
	}
	
	return 0;
}
```

```c
结果：
i = 3
default!
```

	switch当中的break
		switch语句块的代码遇到break会立刻跳出语句块

```c
#include<stdio.h>
int main(){
	int i = 3;
	switch(i){
		case 1:
			printf("1\n");
			break;
		case 2:
			printf("2\n");
			break;
		case 3:
			printf("3\n");
			break;
		default:
			printf("default!\n");
			break;
	}
	
	return 0;
}
```

```c
结果：3
```

	场景题：给出年份和月份，求这个月有多少天？

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int year,month;
	scanf("%d%d",&year,&month);
	int days_of_the_month;
	switch(month){
		case 1: case 3: case 5:
		case 7: case 8: case 10:
		case 12:
			days_of_the_month = 31;
			printf("Days of the month are %d\n",days_of_the_month);
			break;
		case 4: case 6: case 9:
		case 11:
			days_of_the_month = 30;
			printf("Days of the month are %d\n",days_of_the_month);
			break;
		case 2:
			days_of_the_month = 28 + (year % 400 == 0 || year % 4 == 0 && year % 100 != 0);
			printf("Days of the month are %d\n",days_of_the_month);
			break;
		default:
			printf("error!\n");
	}
	
	return 0;
}
```

```c
输入：2026 1
结果：Days of the month are 31
```
---
# 8. 循环结构
## 8.1 goto和循环
	实现函数内部的跳转 ——> 重复做一些事情 ——> 循环结构

```c
#include<stdio.h>
int main(){
	int i = 1;
	int total = 0;
label:
	total += i;
	++i;
	if(i <= 100){
		goto label;
	}
	printf("total is %d\n",total);
	
	return 0;
}
```

```c
结果：total is 5050
```

	如何用goto实现循环：
		先写标签，再写goto —— 实现循环
		goto语句应该放在if结构里面，否则会产生死循环（死循环需要用任务管理器排查）

	goto实现循环的问题：
		goto有害 —— Dijkstra
			代码的可读性下降
			性能问题（破坏了局部性）
		我们一般情况下使用goto，就算是用goto，也不会用它来实现循环。
		goto的使用场景是做快速跳转 —— 可以用goto离开多重循环。

		前向goto：标签在goto前面 —— 实现循环
		后向goto：标签在goto后面 —— 快速跳转
---
[[2026-02-01]]
## 8.2 while循环
	while循环
		while(表达式 —— 入口条件){
			语句块 —— 循环体
		}

		语句块可以是：
			一个语句
			{多个语句}

```mermaid
flowchart TD
    Start([开始]) --> Init[初始化循环变量]
    Init --> Condition{循环条件?}
    Condition -->|真| LoopBody[执行循环体]
    LoopBody --> Update[更新循环变量]
    Update --> Condition
    Condition -->|假| Exit[退出循环]
    Exit --> End([结束])
```

```c
#include<stdio.h>
int main(){
	int i = 1;
	int total = 0;
	while(i <= 100){ //先写循环体，再写入口条件
		total += i;
		++i;
	}
	printf("Total is %d\n",total);
	
	return 0;
}
```

```c
结果：Total is 5050
```
---
## 8.3 翻转整数
	输入一个整数，然后输出翻转之后的结果：
	1234 ——> 4321

- [0] 本题解题思路详见[[8.3 翻转整数解题思路]]

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int number;
	scanf("%d",&number);
	int input = number;
	int output = 0;
	while(input > 0){
		output *= 10;
		output += input % 10;
		input /= 10;
	}
	printf("output is %d\n",output);
	
	return 0;
}
```

```c
输入：1234
结果：output is 4321
```

	使用循环解决问题的思路：
		1.代码中肯定存在重复的行为

		2.先想循环体，把问题的中间状态列一个表格，观察各数据的变化，设计合理的变量

		3.入口条件，重点关注最后一次循环体（边界问题）
---
## 8.4 小写转大写
	输入一行字符串，将其中的小写字母转成大写字母：
	hello world! ——> HELLO WORLD!

- [0] 本题需要用到我们之前学过的知识[[ASCII码表(完整版)]]

- [1] 本题解题思路详见[[8.4 小写转大写解题思路]]

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	char ch;
	while(scanf("%c",&ch) , ch != '\n'){
		if(ch >= 'a' && ch <= 'z'){
			ch -= 32; //将小写字母 转换成 大写字母
		}
		printf("%c",ch);
	}
	printf("\n");
	
	return 0;
}
```

```c
输入：hello world!
结果：HELLO WORLD!
```

	使用循环解决问题的思路：
		1.代码中肯定存在重复的行为

		2.先想循环体，把问题的中间状态列一个表格，观察各数据的变化，设计合理的变量

		3.入口条件，重点关注最后一次循环体（边界问题）
---
## 8.5 for循环
	背景：使用while执行一个100次的循环，代码如下：

```c
#include<stdio.h>
int main(){
	int i = 0;
	while(i < 100){
		循环体
		++1;
	}
}
```

	当我们使用while循环时，需要在主业务(循环体)之外进行一些额外操作(用于控制此循环)：
		1.初始化一个循环变量
		2.设置入口条件
		3.在循环体末尾对循环变量进行迭代
---

	这些额外操作(用于控制此循环)与主业务(循环体)的逻辑是毫无关联的，但在书写代码时却与主业务(循环体)的代码混在一起。为了解决这个问题，我们提出了for循环。
	for循环希望将这些额外操作(用于控制此循环)的代码和主业务(循环体)的代码分离，使代码结构更加清晰，方便程序员阅读。
---

	for(初始化;入口条件;循环变量迭代){
		语句块 —— 循环体
	}

```mermaid
flowchart TD
    Start([开始]) --> Init[初始化]
    Init --> Condition{循环条件?}
    Condition -->|真| LoopBody[执行循环体]
    LoopBody --> Update[更新循环变量]
    Update --> Condition
    Condition -->|假| Exit[退出循环]
    Exit --> End([结束])
```

```c
#include<stdio.h>
int main(){
	int total;
	for(i = 1;i <= 100;++1){
		total += i;
	}
	printf("Total is %d\n",total);
	
	return 0;
}
```

```c
结果：Total is 5050
```
---
## 8.6 do while循环
	do while循环
		do{
			语句块 —— 循环体
		}
		while(条件);
	先执行语句块，再检查条件

```mermaid
flowchart TD
    Start([开始]) --> Init[初始化循环变量]
    Init --> LoopBody[执行循环体]
    LoopBody --> Update[更新循环变量]
    Update --> Condition{循环条件?}
    Condition -->|真| LoopBody
    Condition -->|假| Exit[退出循环]
    Exit --> End([结束])
```

```c
#include<stdio.h>
int main(){
	int total = 0;
	int i = 1;
	do{
		total += i;
		++1;
	}while(i <= 100);
	printf("Total is %d\n",total);
	
	return 0;
}
```

```c
结果：Total is 5050
```
---
[[2026-02-06]]
## 8.7 continue
	continue关键字
		continue用在循环体里面
		程序运行的时候遇到continue，就会跳过本次循环体，直接开始下一次循环体
---

	场景题：对2，4，6，8，···，100进行求和

```c
#include<stdio.h>
int main(){
	int i = 1;
	int total = 0;
	while(i <= 100){
		if(i % 2 != 0){
			++i; //在continue之前记得对循环变量进行迭代！！！
			continue;
		}
		else{
			total += i;
			++i;
		}
	}
	printf("Total is %d\n",total);
	
	return 0;
}
```

```c
结果：Total is 2550
```

- [0] 在while循环中使用continue需注意要在continue之前对循环变量进行迭代！！！

```c
#include<stdio.h>
int main(){
	int total = 0;
	for(i = 1;i <= 100;++i){
		if(i % 2 != 0){
			continue;
		}
		else{
			total += i;
		}
	}
	printf("Total is %d\n",total);
	
	return 0;
}
```

```c
结果：Total is 2550
```
---
## 8.8 break
	break关键字
		break之前在选择结构switch里面出现过，现在讲的是一种新用法。
		break与continue一样只能出现在循环体里面。
		当程序运行到break的时候，程序会跳出单层循环。
		break的此种用法一般用于提前终止循环或循环次数未知的循环。
---

	场景题：1 + 2 + 3 + ··· + n > 200 (n∈N)，使此不等式成立的n的最小值是多少？（n为多少时，1 + 2 + 3 + ··· + n 第一次大于200？）

```c
#include<stdio.h>
int main(){
	while(1){
		//死循环 + 循环体里面break --> 循环次数未知的循环
		total += i;
		if(total > 200){
			break; //跳出循环结构
		}
		++i;
	}
	printf("Total is %d,i is %d\n",total,i);
	
	return 0;
}
```

```c
结果：Total is 210,i is 20
```
---
# 9. 专题B 枚举
	枚举思想
		面对一个问题的时候，直接将问题的所有可能性全部列出来，一个一个地检查是否符合题目的要求 --> 暴力解法 --> 存在重复操作 --> 循环
## 9.1 水仙花数
	“水仙花数”是指一个三位数，其各位数字的立方和等于该数本身。例如，153是一个水仙花数。请编写程序，找出所有的三位水仙花数。

```c
#include<stdio.h>
int main(){
	for(int i = 1;i <= 9;++i){
		for(int j = 0;j <= 9;++j){
			for(int k = 0;k <= 9;++k){
				if(100 * i + 10 * j + k == i * i * i + j * j * j + k * k * k){
					printf("%d\n",100 * i + 10 * j + k);
				}
			}
		}
	}
	
	return 0;
}
```

```c
结果：
153
370
371
407
```
---
## 9.2 找完数
	完数是指除本身以外的因子之和等于其本身的数。
	任给一个自然数n，求n以内的所有完数。如果找不到，则输出"No"

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int n;
	printf("Please enter a natural number:");
	scanf("%d",&n);
	int Is_Empty = 1; //记录完数个数是否为0
	for(int i = 1;i <= n;++i){
		// i用来遍历所有小于等于n的自然数
		int total = 0;
		for(int j = 1;j < i;++j){
			// j用来遍历所有比i小的数，把i的约数找出来
			if(i % j == 0){
				// 如果整除，则j是i的一个约数
				total += j;
			}
			else{
				continue;
			}
		}
		if(total == i){
			// 满足完数条件
			Is_Empty = 0; // 只要有一个完数，就不打印No
			printf("%d is a perfect number!\n",i);
		}
		else{
			continue;
		}
	}
	if(Is_Empty == 1){
		printf("There are no perfect numbers within the natural number n!\n");
	}
	
	return 0;
}
```

```c
Please enter a natural number:1024
结果：
6 is a perfect number!
28 is a perfect number!
496 is a perfect number!
```
---
## 9.3 检查一个数是否为质数
	输入一个正整数，检查该数是否为质数。如果该数是质数，则输出Yes；如果该数不是质数，则输出No。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int n;
	printf("Please enter a positive integer:");
	scanf("%d",&n);
	int Is_Prime = 1;
	for(int i = 2;i < n;++i){
		if(n % i == 0){
			Is_Prime = 0;
			break;
		}
	}
	if(Is_Prime == 1){
		printf("Yes\n");
	}
	else{
		printf("No\n");
	}
	
	return 0;
}
```

```c
Please enter a positive integer:31
结果：Yes
```
---

	算法是否有优化空间？
	当前算法为：从2检查到n - 1 --> 有没有办法少检查几次？

- [0] 假如一个数n不是质数，那么它可以用a * b（a,b ≠ 1 且 a,b ≠ n）来表示，并且a,b不可能同时大于$\sqrt{n}$ ，也就是说，假如一个数n不是质数，那么它至少有一个约数小于等于$\sqrt{n}$
- [1] 因此，我们只需要从2检查到$\sqrt{n}$就可以了

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int n;
	printf("Please enter a positive integer:");
	scanf("%d",&n);
	int Is_Prime = 1;
	for(int i = 2;i * i <= n;++i){
		if(n % i == 0){
			Is_Prime = 0;
			break;
		}
	}
	if(Is_Prime == 1){
		printf("Yes\n");
	}
	else{
		printf("No\n");
	}
	
	return 0;
}
```

```c
Please enter a positive integer:31
结果：Yes
```
---
# 10. 函数的基本原理
## 10.1 函数简介
	正式学习函数之前，我们需要对函数建立两个直觉：
		- 函数大概有什么用？
			● 传入参数 --> 执行函数体里面的指令 --> 返回结果
			● 把函数看成是程序的组件：
				■ 可以把函数看成是小的子程序
				■ 可以把程序看成是不同的函数组合起来
		- 使用函数有什么好处？
			● 减少重复代码的冗余
---

	场景题：现有3组数据，每组数据里面有3个整数，请你判断每组数据中的3个整数能否作为三角形的三边边长。三组数据如下：

	第一组数据：1,2,3
	第二组数据：2,3,4
	第三组数据：4,5,6

	解题思路：根据三角形任意两边之和大于第三边的性质对每组数据进行判断。
---
>**Version 1** : 声明每组数据时直接进行初始化，再对每组数据进行判断。

```c
#include<stdio.h>
int main(){
	int a1 = 1,b1 = 2,c1 = 3;
	int a2 = 2,b2 = 3,c2 = 4;
	int a3 = 4,b3 = 5,c3 = 6;
	
	if(a1 + b1 > c1 && a1 + c1 > b1 && b1 + c1 > a1){
		printf("The three integers in the first set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	if(a2 + b2 > c2 && a2 + c2 > b2 && b2 + c2 > a2){
		printf("The three integers in the second set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the second set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	if(a3 + b3 > c3 && a3 + c3 > b3 && b3 + c3 > a3){
		printf("The three integers in the third set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the third set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	return 0;
}
```

```c
结果：
The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.
The three integers in the second set of data can serve as the lengths of the three sides of a triangle.
The three integers in the third set of data can serve as the lengths of the three sides of a triangle.
```
---
>**Version 2** : 先声明每组数据，然后通过 **scanf( )** 对每组数据进行赋值，最后对每组数据进行判断。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int a1,b1,c1;
	printf("Please enter the first set of data:");
	scanf("%d%d%d",&a1,&b1,&c1);
	
	int a2,b2,c2;
	printf("Please enter the second set of data:");
	scanf("%d%d%d",&a2,&b2,&c2);
	
	int a3,b3,c3;
	printf("Please enter the third set of data:");
	scanf("%d%d%d",&a3,&b3,&c3);
	
	if(a1 + b1 > c1 && a1 + c1 > b1 && b1 + c1 > a1){
		printf("The three integers in the first set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	if(a2 + b2 > c2 && a2 + c2 > b2 && b2 + c2 > a2){
		printf("The three integers in the second set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the second set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	if(a3 + b3 > c3 && a3 + c3 > b3 && b3 + c3 > a3){
		printf("The three integers in the third set of data can serve as the lengths of the three sides of a triangle.\n");
	}
	else{
		printf("The three integers in the third set of data cannot serve as the lengths of the three sides of a triangle.\n");
	}
	
	return 0;
}
```

```c
Please enter the first set of data:1 2 3
Please enter the second set of data:2 3 4
Please enter the third set of data:4 5 6
结果：
The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.
The three integers in the second set of data can serve as the lengths of the three sides of a triangle.
The three integers in the third set of data can serve as the lengths of the three sides of a triangle.
```
---

	Version 1与Version 2的代码中存在大量重复冗余的片段，导致代码非常容易出错。为了降低代码出错的概率，我们应该尽量减少重复的操作。为此我们提出了函数这一概念。
---

	函数
		返回值类型 函数名(函数参数列表 --> 形参 --> 当作局部变量){
			函数体
		}
---
>**Version 3** : 将 **Version 1** 与 **Version 2** 中对每组数据进行判断的代码重新编写后集成到新定义的函数 **Is_Triangle( )** 中，对每组数据进行判断时只需调用**Is_Triangle( )** ，减少了重复操作，降低了代码出错的概率。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void Is_Triangle(char rank[], int a, int b, int c){
	if (a + b > c && a + c > b && b + c > a){
		printf("The three integers in the %s set of data can serve as the lengths of the three sides of a triangle.\n", rank);
	}
	else{
		printf("The three integers in the %s set of data cannot serve as the lengths of the three sides of a triangle.\n", rank);
	}
}

int main(){
	int a1, b1, c1;
	char r1[] = "first";
	printf("Please enter the %s set of data:", r1);
	scanf("%d%d%d", &a1, &b1, &c1);
	Is_Triangle(r1, a1, b1, c1);

	int a2, b2, c2;
	char r2[] = "second";
	printf("Please enter the %s set of data:", r2);
	scanf("%d%d%d", &a2, &b2, &c2);
	Is_Triangle(r2, a2, b2, c2);

	int a3, b3, c3;
	char r3[] = "third";
	printf("Please enter the %s set of data:", r3);
	scanf("%d%d%d", &a3, &b3, &c3);
	Is_Triangle(r3, a3, b3, c3);

	return 0;
}
```

```c
Please enter the first set of data:1 2 3
结果：
The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.
Please enter the second set of data:2 3 4
结果：
The three integers in the second set of data can serve as the lengths of the three sides of a triangle.
Please enter the third set of data:4 5 6
结果：
The three integers in the third set of data can serve as the lengths of the three sides of a triangle.
```
---
>**Version 4** : 进一步将告诉程序输入的是第几组数据这一功能也集成到**Is_Triangle( )** 中，并引入**整形变量n** 来获取要输入几组数据的信息，进而通过**for** 循环来调用**Is_Triangle( )** 对每组数据进行判断。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void Is_Triangle(){
	char rank[100];
	printf("Please enter the ranking of this set of data(e.g., first, second, third, ...):");
	scanf("%s",rank);
	int a,b,c;
	printf("Please enter the %s set of data(three integers):",rank);
	scanf("%d%d%d",&a,&b,&c);
	
	if (a + b > c && a + c > b && b + c > a){
		printf("The three integers in the %s set of data can serve as the lengths of the three sides of a triangle.\n", rank);
	}
	else{
		printf("The three integers in the %s set of data cannot serve as the lengths of the three sides of a triangle.\n", rank);
	}
}

int main(){
	int n;
	printf("Please input the number of data groups:");
	scanf("%d",&n);
	for(int i = 1;i <= n;++i){
		Is_Triangle();
	}

	return 0;
}
```

```c
Please input the number of data groups:3
Please enter the ranking of this set of data(e.g., first, second, third, ...):first
Please enter the first set of data(three integers):1 2 3
结果：
The three integers in the first set of data cannot serve as the lengths of the three sides of a triangle.
Please enter the ranking of this set of data(e.g., first, second, third, ...):second
Please enter the second set of data(three integers):2 3 4
结果：
The three integers in the second set of data can serve as the lengths of the three sides of a triangle.
Please enter the ranking of this set of data(e.g., first, second, third, ...):third
Please enter the third set of data(three integers):4 5 6
结果：
The three integers in the third set of data can serve as the lengths of the three sides of a triangle.
```

- [0] 当我们使用函数时，可以将重复冗余的操作都放进函数体中。这样做可以使代码量减少，进而降低程序出错的可能性。
---
[[2026-02-10]]
## 10.2 函数的声明和定义
	函数的声明
		通知编译器函数的一些信息，包括：
			返回值类型
			函数名
			形式参数
			分号';'

		在使用函数之前，必须有函数的声明

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void Is_Triangle(); //函数的声明
void Is_Triangle(); //声明可以多次

int main(){
	int n;
	printf("Please input the number of data groups:");
	scanf("%d",&n);
	for(int i = 1;i <= n;++i){
		Is_Triangle();
	}

	return 0;
}

void Is_Triangle(){
	char rank[100];
	printf("Please enter the ranking of this set of data(e.g., first, second, third, ...):");
	scanf("%s",rank);
	int a,b,c;
	printf("Please enter the %s set of data(three integers):",rank);
	scanf("%d%d%d",&a,&b,&c);
	
	if (a + b > c && a + c > b && b + c > a){
		printf("The three integers in the %s set of data can serve as the lengths of the three sides of a triangle.\n", rank);
	}
	else{
		printf("The three integers in the %s set of data cannot serve as the lengths of the three sides of a triangle.\n", rank);
	}
}
```
---

	函数的定义
		函数的定义就是把一个函数的所有信息全部描述出来，包括：
			返回值类型
			函数名
			形式参数
			函数体{}

		函数的定义会自带一次声明。
		函数的定义在一个程序中只能有一次！
---
- [0] 一个函数的定义在程序中只能有一次；一个函数的声明在程序中可以有多次。
---
## 10.3 函数运行过程
	函数调用
		函数调用语句之前，必须要先有函数声明。

		调用函数时，先写函数的名字，再写一对圆括号，在圆括号里面写传入的参数（实际参数 —— 实参）

		主调方：调用函数的一方
		被调方：被调用的函数

		流程：主调方先准备实参，然后传入给被调方，调用被调函数，被调方执行函数体，返回之后讲返回值给主调方。
---

	调试函数调用过程

```mermaid
flowchart TD
    Start["开始执行程序"] --> A[main开始]
    
    A --> B["定义变量 n<br>int n;"]
    B --> C["输出提示信息<br>printf(&quot;Please input...&quot;)"]
    C --> D["读取输入 n<br>scanf(&quot;%d&quot;, &n)"]
    D --> E["for 循环开始<br>i = 1"]
    
    E --> Condition{i <= n?}
    
    Condition -- 是 --> F["调用 Is_Triangle() 函数"]
    
    F --> G[IsTriangle开始执行]
    G --> H["定义局部变量<br>char rank[100];<br>int a, b, c;"]
    H --> I["输出排名提示<br>printf(&quot;Please enter the ranking...&quot;)"]
    I --> J["读取 rank<br>scanf(&quot;%s&quot;, rank)"]
    J --> K["输出数据输入提示<br>printf(&quot;Please enter the %s...&quot;, rank)"]
    K --> L["读取 a, b, c<br>scanf(&quot;%d%d%d&quot;, &a, &b, &c)"]
    L --> M["判断三角形条件<br>a+b>c && a+c>b && b+c>a"]
    
    M -- 条件成立 --> N["输出可以构成三角形<br>printf(&quot;The three integers...&quot;)"]
    M -- 条件不成立 --> O["输出不能构成三角形<br>printf(&quot;The three integers...&quot;)"]
    
    N --> P[IsTriangle执行结束]
    O --> P
    
    P --> Q["返回到 main 调用处<br>控制权交还给 main"]
    Q --> R["i++ (i 增加 1)"]
    R --> Condition
    
    Condition -- 否 --> S["跳出循环"]
    S --> T["return 0;<br>程序结束"]
    
    style Start fill:#e1f5e1
    style A fill:#e1f5e1
    style F fill:#bbdefb
    style G fill:#bbdefb
    style P fill:#ffccbc
    style T fill:#ffccbc
```
- [0] 1.调试函数的时候要使用F11而不是F10
- [1] 2.主调函数去调用被调函数的时候，指令位置会跳转到被调函数，等被调函数返回之后，再回到主调方

>总结：
>顺序结构：指令一行一行从上往下走
>选择结构：出现指令跳转的情况
>循环结构：出现指令走回头路的情况
>函数调用：出现指令临时跳转到被调函数，被调方返回之后，再回到主调方的情况
---
## 10.4 函数运行的内存原理

```c
#include<stdio.h>

void func1(){
	
}

void func2(){
	func1();
}

int main(){
	func1();
	func2();
	
	return 0;
}
```

- [1] 调试函数调用的过程会发现：存在这样一个现象 —— 后调用的函数先返回。此现象的详细说明详见 —— [[函数调用的详细过程]]

- [0] 在指令的运行过程中，内存发生了什么变化？详见 —— [[内存布局]] + [[函数调用的内存原理]]

>总结：
>根据先修知识[[内存布局]]我们了解到 —— 函数调用影响的是栈区
>栈区的特征 —— 后进先出 **(Last in,first out.)**
>
>根据先修知识[[函数调用的内存原理]]我们了解到 —— 在函数调用的过程中，内存的变化如下：
>每次调用函数，会开辟一个栈帧
>栈帧会压入栈区；
>每次函数返回，会弹出一个栈帧 —— 被弹出的这个栈帧就会被销毁掉
---
## 10.5 作用域
	作用域用来描述变量的有效范围

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int a = 1;
void func(){
	int b = 2;
}
int main(){
	int c = 3;
	{
		int d = 4;
		// 在第11行这个位置，a b c d谁是有效的谁是无效的？答：除了b其他都有效。
	}
	
	// 在第14行这个位置，a b c d谁是有效的谁是无效的？答：除了b和d其他都有效。
	return 0;
}
```

- [0] 通过在**不同位置分别对a b c d进行赋值操作**，然后对代码进行编译，我们会发现：存在这样一个**现象** —— **不同位置的变量的有效范围是有区别的。**

- [1] 变量的作用域是以 —— **花括号'{}'** 作为边界的。

- [2] 我们将**花括号'{}'** 内部的变量称为 —— **内部变量**；我们将**花括号'{}'** 外部的变量称为 —— **外部变量**。

- [3] 外部变量在内部**依然可以生效**；内部变量在外部**不生效**。

- [4] C语言**不支持函数嵌套定义**

- [5] 函数**外部**的叫做**全局变量**；函数**内部**的叫做**局部变量**。
---
[[2026-02-11]]

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int a = 1;
void func(){
	int b = 2;
}
int main(){
	int c = 3;
	{
		int d = 4;
		int a = 2;
		a = 3;
		
	}
	
	return 0;
}
```

- [0] 在**main函数**前面打上一个**断点**后对程序进行调试，会发现指令在**进入main函数之前** **变量a的值为1**。指令在**进入main函数之后** 走到**int a = 2;** 这一行时，**变量a的值为2**；走到**a = 3;** 这一行时，**变量a的值为3**。指令**离开main函数之后**，**变量a的值又变回1了**。

>总结：
>在内部作用域里面，可以初始化一个和外部变量重名的变量 —— 起到隐藏的效果
>隐藏的含义：当程序运行到内部作用域的时候，外部变量就被藏起来了。
>
>❗注意：在C语言中，如果存在一个已被初始化的全局变量 `a`，而在某个函数内部**没有**定义同名的局部变量 `a`，就直接对变量 `a` 做各种运算，那么这里的 `a` 指的就是全局变量 `a`，所有运算都会直接作用于该全局变量，从而改变它的值。
---
## 10.6 生存期
	变量的生存期关注的是进程启动的时候，变量申请内存和释放内存的时机。
	变量在申请内存之后才能够使用；变量在释放内存后就不能够使用了。
	生存期与作用域的区别
		作用域：在写代码的时候考虑的。
		生存期：在程序运行的时候考虑的。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int a = 1;
void func(){
	int a = 2;
}
int main(){
	int a = 3;
	func();
	
	return 0;
}
```

>总结：
>**全局变量**的**生存期**：**程序一启动**就**有效**；**程序终止**时**失效**。**与函数的调用与返回无关**。
>因此**全局变量**储存在内存的 **"数据段"** 中 **("数据段"的概念详见[[内存布局]])**。
>**局部变量**的**生存期**：所有的**局部变量**都储存在**栈帧**中 **("栈帧"的概念详见[[函数调用的内存原理]])**。**函数调用**时**分配内存**；**函数返回**时**释放内存**。
>因此**栈帧的大小**由**局部变量的大小**决定的。
---
## 10.7 值传递

>引例：对变量a和变量b做值交换的操作，代码如下：

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
void swap(int a,int b){
	int temp = a;
	a = b;
	b = temp;
	printf("swap,a = %d,b = %d\n",a,b);
}
int main(){
	int a = 10,b = 5;
	swap(a,b);
	printf("main,a = %d,b = %d\n",a,b);
	
	return 0;
}
```

```c
结果：
swap,a = 5,b = 10
main,a = 10,b = 5
```

- [0] 通过**输出结果**我们可以得知：在**swap函数**中**成功**实现了对变量a和变量b做值交换的操作，而在**main函数**中**失败**了。这牵扯到了C语言中函数的一个非常重要的**机制** —— **[[值传递]](型参与实参的关系)**

- [1] **函数调用的过程**就是把**主调方的实参**传递给**被调方的形参**，**传递的方式**为**值传递**。

- [2] 在C语言中，**函数的形参**  **等价于** **函数内部的局部变量** **——** **函数的形参是储存到对应函数的栈帧中的**。**值传递的过程**可以简单理解为用 **实参值** 来 **初始化** **形参** **(将实参的值复制粘贴给形参)**。

- [3] **在main函数中失败的原因：** 值交换这一操作的代码都集成到**swap函数**中了，而**swap函数**所实现的值交换仅仅是对**swap函数**的**形参(sawp函数内部的局部变量)** 进行值交换，**main函数内部的局部变量a、b**并没有发生任何改变。因此在**main函数**中失败了。
---
[[2026-02-14]]
# 11. 数组
## 11.1 数组的概念和定义
	数组

	场景：
		如果需要5个变量？ —— int a1,a2,a3,a4,a5;
		如果需要10个变量？ —— int a1,a2,···,a10;
		如果需要100个变量？ —— int a1,a2,···,a100;

	由于程序业务的要求，我们现在需要很多个变量，原来用来描述单一数据的数据类型已经无法满足我们的需求了。因此我们提出了 —— 聚合数据结构(把单一的数据组合在一起)

	数组就是一种典型的聚合数据结构。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[5];
	
	return 0;
}
```

- [0] 当我声明了一个整形数组arr[5] (int arr[5])时，内存中发生了什么呢？ —— 详见[[C语言数组声明详解：int arr[5] ]]
- [1] 数组的性质 —— 详见[[数组的性质]]
---

	数组的定义
		元素的数据类型 数组名[数组长度(必须是"正·常·整数")];

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	// 数组的长度必须大于0 && 数组的长度是一个整数
	int arr[LEN]; // 数组的元素类型为int，数组名为arr，数组长度为5。
	// 下面是不推荐的写法（不推荐的原因：数组长度不应该是变量）
	// int len = 5;
	// int arr[len];
	
	return 0;
}
```
---
## 11.2 数组的初始化
	数组的初始化就是在定义数组时，就给数组的元素设置好值 —— 数组的初始化

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[LEN] = {1,2,3,4,5};
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	// 初始化列表元素个数小于数组长度时，剩余元素自动赋值为0。
	// 注意：初始化列表元素个数不允许大于数组长度！！！
	int arr[LEN] = {1,2,3};
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	// 数组长度是可以自动推断的。
	// 注意：只有初始化列表存在的情况下才可以省略数组长度！！！
	int arr[] = {1,2,3};
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	// 申请一个长度为1024的数组，内容全是0
	int arr[1024] = {0};
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[5] = {1,2,3,4,5}; // 定义语句里面，"="是初始化符号。
	int arr[5];
	arr[5] = {1,2,3,4,5}; // 在定义语句之外，"="是赋值的意思，赋值不能使用初始化列表。
	
	return 0;
}
```
---
[[2026-02-15]]
## 11.3 访问数组元素

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[5] = {1,2,3,4,5};
	// 下标运算符'[]'
	// arr[0] arr[1] ··· arr[4] // 范围是 0 ~ N - 1
	/* arr[0]是一个元素 —— 可以当成一个变量：
		1.arr[0]里面有值
		2.编译器给arr[0]分配了内存空间
	*/
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[5] = {1,2,3,4,5}; // 定义语句里面'[]'用来规定数组的长度，这时'[]'称为数组定义运算符。
	for(int i = 0;i < 5;++i){
		// 非定义语句里面'[]'用来根据下标访问元素。
		printf("arr[%d] = %d\n",i,arr[i]);
	}
	printf("-------------------------\n");
	arr[3] = 1024;
	for(int i = 0;i < 5;++i){
		printf("arr[%d] = %d\n",i,arr[i]);
	}
	
	return 0;
}
```
---
## 11.4 数组元素的内存布局和越界问题

>**知识回顾 —— 数组的性质**
>1.连续存储
>2.数据类型相同

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[5] = {1,2,3,4,5}; // 定义语句里面'[]'用来规定数组的长度，这时'[]'称为数组定义运算符。
	for(int i = 0;i < 5;++i){
		// 非定义语句里面'[]'用来根据下标访问元素。
		printf("arr[%d] = %d\n",i,arr[i]);
	}
	printf("-------------------------\n");
	arr[3] = 1024;
	for(int i = 0;i < 5;++i){
		printf("arr[%d] = %d\n",i,arr[i]);
	}
	
	return 0;
}
```

	数组元素的内存布局
		1.数组的首地址和arr[0]的首地址是一样的。
		2.arr[i]的地址 = 数组首地址 + i * sizeof(元素类型) —— 如果想要访问某个元素，不需要知道数组的长度，只需要知道数组的首地址、下标和元素类型即可。

	'[]'的原理：根据数组的首地址、下标和元素类型求出i号元素在内存中的位置，再访问元素。
	'[]'的本质：先计算地址，再访问元素。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	int arr[5] = {1,2,3,4,5};
	int a = 20;
	for(int i = 0;i < 13;++i){
		arr[i] = i + 1;
	}
	printf("a = %d\n",a);
	
	return 0;
}
```

```c
结果：a = 12
```

- [0] 我并没有对局部变量a进行除了初始化之外的任何操作，但为什么打印的时候a的值从20变为12了呢？ —— 具体原因详见[[数组元素的内存布局与越界问题]]
---
[[2026-02-16]]
## 11.5 局部数组的长度限制
	栈帧的大小限制
		只要是局部的变量，无论是单一变量还是数组，都分配在栈帧上面。与单一变量不同，数组的长度可能会很大，因此我们提出这样一个问题 —— 数组的长度有没有限制？

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
int main(){
	char arr[1200000];
	
	return 0;
}
```

- [0] 我点击调试按钮之后弹出了一条报错信息：**Stack Overflow** 这是怎么回事？默认栈帧大小是多少？该如何解决？ —— 具体原因与解决方案详见 —— [[局部数组的长度限制与栈溢出]]
---
## 11.6 数组作为函数参数
	使用函数传递数组

	知识回顾：'[]'运算符
		arr[i]的原理：先根据数组首地址、元素类型和下标i计算出地址，再根据地址去访问内存 —— 数组的长度是没用的信息。
		C语言的作者在设计数组参数的时候，决定丢弃掉长度信息。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#define LEN 5
void func(int arr[5],int length){
	// length补充数组的长度信息。
	// 在被调函数中，数组会退化成一个地址，丢失了长度信息。
	printf("func sizeof(arr) = %d\n",sizeof(arr));
	for(int i = 0;i < length;++i){
		printf("%3d",arr[i]); // '[]'不需要长度信息。
	}
	printf("\n");
}
int main(){
	// 在主调函数的位置，我们知道数组的长度信息。
	int arr[LEN] = {1,2,3,4,5};
	printf("main sizeof(arr) = %d\n",sizeof(arr));
	for(int i = 0;i < sizeof(arr) / sizeof(int);++i){
		printf("%3d",arr[i]);
	}
	printf("\n");
	func(arr,sizeof(arr) / sizeof(int)); // 数组这个整体作为实参时，不需要'[]'。
	
	return 0;
}
```

```c
结果：
main sizeof(arr) = 20
  1  2  3  4  5
func sizeof(arr) = 8
  1  2  3  4  5
```

- [0] C语言中将一个数组从主调函数传递给被调函数时，会将数组退化成指向数组第一个字节的地址
---
[[2026-02-24]]
## 11.7 二维数组的基本概念
	一维数组 —— 向量
	二维数组 —— 矩阵

```c
int arr[M][N]; // M —— 行数 N —— 列数
```


$$
\text {从计算机的角度看：二维数组也是一维数组}
\begin{cases}
\text {数组的元素类型是数组 \ —— \ “数组的数组”} \\
\text {数组的行数即数组的长度} \\
\end{cases}
$$

```c
int a[2][3]; // 长度为2的数组，数组元素是长度为3的数组
```

- [0] 数组在内存中按照行优先存储
---
## 11.8 二维数组的初始化

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	// 二维数组方式初始化
	int arr[2][3] = { {1,2,3},{4,5,6} };
	// 一维数组方式初始化
	int arr[2][3] = {1,2,3,4,5,6};
	
	// 二维数组方式初始化
	int arr[2][3] = { {1,2},{3,4} };
	// 一维数组方式初始化
	int arr[2][3] = {1,2,3,4};
	
	return 0;
}
```
---
[[2026-02-25]]
## 11.9 二维数组的访问和传递

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[2][3] = { {1,2,3},{4,5,6}};
	for(int i = 0;i < 2;++i){ // 遍历每一行
		for(int j = 0;j < 3;++j){ // 遍历每一列
			printf("%3d",arr[i][j]);
		}
		printf("\n");
	}
	
	return 0;
}
```

```c
结果：
  1  2  3
  4  5  6
```

	arr[i][j]的地址如何计算？
	arr首地址 + i * sizeof(int) * 3 + j * sizeof(int)

>[!note]
>计算二维数组元素的内存地址时，只需要知道二维数组的列数，不需要知道二位数组的行数。

- [0] 深入理解C语言中是如何计算二维数组元素的内存地址 —— 详见[[计算二维数组元素的内存地址]]

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
void func(int arr[2][3]){
	for(int i = 0;i < 2;++i){ // 遍历每一行
		for(int j = 0;j < 3;++j){ // 遍历每一列
			printf("%3d",arr[i][j]);
		}
		printf("\n");
	}
}
int main(){
	int arr[2][3] = { {1,2,3},{4,5,6}};
	for(int i = 0;i < 2;++i){ // 遍历每一行
		for(int j = 0;j < 3;++j){ // 遍历每一列
			printf("%3d",arr[i][j]);
		}
		printf("\n");
	}
	printf("-----------\n");
	func(arr);
	
	return 0;
}
```

```c
结果：
  1  2  3
  4  5  6
-----------
  1  2  3
  4  5  6
```

>[!note]
>二维数组作为参数传递时只丢失了行数的信息。

---
[[2026-02-26]]
# 12. 指针
## 12.1 地址、指针和指针变量

>知识回顾：内存模型 —— 详见[[内存布局]]

	我们想根据地址来访问内存中的数据
	指针就是地址
	指针变量是一个变量，变量的内存里面存储了一个指针

---
## 12.2 指针变量的定义和初始化
	前提：指针变量是依附于另外一个目标而存在的。所以在使用指针变量时需要先给目标申请内存，再创建指针变量。

	基类型：指针所指向的目标的数据类型。
	基类型决定了目标的大小。
	基类型 *指针变量名

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i = 10;
	int *p; // 推荐将*和变量名写在一起。
	// '&'(取地址运算符)出现在非定义语句里面时，表示取地址的意思。'&'(取地址运算符)只能作用于变量/数组的名字，不能对一个临时的结果做取地址的操作。
	p = &i; // p里面存储的地址值是i的地址 —— p指向i
	// 对指针变量赋值可以修改指针的指向
	
	int *p = &i; // 定义一个指针变量p，初始化为指向i
	
	return 0;
}
```

---
## 12.3 解引用运算符

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i = 10;
	
	int *p = &i; // 定义一个指针变量p，初始化为指向i
	
	printf("*p = %d\n",*p);
	// '*'运算符在定义语句里面，用来说明创建指针变量。
	// '*'(解引用运算符)出现非定义语句里面，表示解引用/间接访问(根据指针变量里面存储的地址值和指针变量的基类型去访问目标的内容)的意思。
	*p = 11;
	printf("i = %d\n",i);
	
	return 0;
}
```

```c
结果：
*p = 10
i = 11
```

---
[[2026-02-27]]
## 12.4 指针基本使用小结
	流程：
		1.给目标申请内存
		2.准备一个指针变量，通过初始化/赋值的方式，让指针变量去指向目标
		3.使用解引用运算符'*'去间接访问目标

	两种用途：
		1.指针的传递 —— 指针和函数配合
		2.指针的偏移 —— 指针和数组配合

---
## 12.5 指针的传递

>**知识回顾：函数的值传递机制 —— 详见[[值传递]]**

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
void swap(int a,int b){
	int temp = a;
	a = b;
	b = temp;
	printf("sawp a = %d,b = %d\n",a,b);
}
int main(){
	int a = 10,b = 5;
	swap(a,b);
	printf("main a = %d,b = %d\n",a,b);
	
	return 0;
}
```

```c
结果：
sawp a = 5,b = 10
main a = 10,b = 5
```

>[!note]
>由于**函数的值传递机制**，被调函数没有办法修改**主调函数栈帧里面的内容**。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
void swap(int *pa,int *pb){
	int temp = *pa;
	*pa = *pb;
	*pb = temp;
	printf("swap *pa = %d,*pb = %d\n",*pa,*pb);
}
int main(){
	int a = 10,b = 5;
	int *pa,*pb;
	pa = &a;
	pb = &b;
	swap(pa,pb);
	printf("main a = %d,b = %d\n",a,b);
	
	return 0;
}
```

```c
结果：
swap *pa = 5,*pb = 10
main a = 5,b = 10
```

>[!Note]
>指针的传递可以用来在被调函数中去修改主调函数栈帧中的数据。
>	1.主调方先给被修改的数据申请内存
>	2.被调方需要用数据的指针作为参数
>	3.被调方需要用解引用运算符去间接访问内存，修改内容

- [0] 若想深入理解程序运行过程中内存是如何变化的 —— 详见[[指针交换程序内存变化分析]]
---
[[2026-02-28]]
## 12.6 指针的偏移
	对指针变量做加减法（只能加减整数）
	int *p
	p和p + 1有什么关系？

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int i = 10;
	double d = 3.14;
	int *pi = &i;
	double *pd = &d;
	printf("pi = %p,pi + 1 = %p\n",pi,pi + 1); // 指针可以用%p作为占位符
	printf("pd = %p,pd + 1 = %p\n",pd,pd + 1);
	
	return 0;
}
```

```c
结果：
pi = 000000533A19FB74,pi + 1 = 000000533A19FB78
pd = 000000533A19FB98,pd + 1 = 000000533A19FBA0
```

>[!note]
>p + n的结果 = p里面存储的地址 + n * sizeof(基类型) —— 和'[]'运算符很像
>因此可以得到以下结论：我们经常会把数组当中的某个元素的地址取出来，然后**对指针变量做加减法（即指针的偏移）** 从而去访问数组中的其他元素。
>根据此结论我们建立了一个直觉 —— 指针的偏移通常会和数组联系在一起，也就是说我们会经常会通过**对指针变量做加减法（即指针的偏移）** 来访问数组中的其他元素。

---
## 12.7 指针和数组的关系

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[] = {1,2,3,4,5};
	int *p = &arr[0];
	for(int i = 0;i < 5;++i){
		printf("i = %d,p + i = %p,&arr[i] = %p\n",i,p + i,&arr[i]);
		printf("i = %d,*(p + i) = %d,arr[i] = %d\n",i,*(p + i),arr[i]);
	}
	
	return 0;
}
```

```c
结果：
i = 0,p + i = 00000091628FF638,&arr[i] = 00000091628FF638
i = 0,*(p + i) = 1,arr[i] = 1
i = 1,p + i = 00000091628FF63C,&arr[i] = 00000091628FF63C
i = 1,*(p + i) = 2,arr[i] = 2
i = 2,p + i = 00000091628FF640,&arr[i] = 00000091628FF640
i = 2,*(p + i) = 3,arr[i] = 3
i = 3,p + i = 00000091628FF644,&arr[i] = 00000091628FF644
i = 3,*(p + i) = 4,arr[i] = 4
i = 4,p + i = 00000091628FF648,&arr[i] = 00000091628FF648
i = 4,*(p + i) = 5,arr[i] = 5
```

>[!important] 指针和数组更有意思的关联

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[] = {1,2,3,4,5};
	int *p = arr;
	for(int i = 0;i < 5;++i){
		printf("i = %d,p + i = %p,&arr[i] = %p\n",i,p + i,&arr[i]);
		printf("i = %d,*(p + i) = %d,arr[i] = %d\n",i,*(p + i),arr[i]);
	}
	
	return 0;
}
```

```c
结果：
i = 0,p + i = 00000091628FF638,&arr[i] = 00000091628FF638
i = 0,*(p + i) = 1,arr[i] = 1
i = 1,p + i = 00000091628FF63C,&arr[i] = 00000091628FF63C
i = 1,*(p + i) = 2,arr[i] = 2
i = 2,p + i = 00000091628FF640,&arr[i] = 00000091628FF640
i = 2,*(p + i) = 3,arr[i] = 3
i = 3,p + i = 00000091628FF644,&arr[i] = 00000091628FF644
i = 3,*(p + i) = 4,arr[i] = 4
i = 4,p + i = 00000091628FF648,&arr[i] = 00000091628FF648
i = 4,*(p + i) = 5,arr[i] = 5
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[] = {1,2,3,4,5};
	int *p = arr;
	for(int i = 0;i < 5;++i){
		printf("i = %d,p + i = %p,&arr[i] = %p\n",i,p + i,&arr[i]);
		printf("i = %d,*(p + i) = %d,arr[i] = %d\n",i,*(p + i),arr[i]);
		printf("i = %d,p[i] = %d,*(arr + i) = %d\n",i,p[i],*(arr + i));
	}
	
	return 0;
}
```

```c
结果：
i = 0,p + i = 0000006EB40FF7B8,&arr[i] = 0000006EB40FF7B8
i = 0,*(p + i) = 1,arr[i] = 1
i = 0,p[i] = 1,*(arr + i) = 1
i = 1,p + i = 0000006EB40FF7BC,&arr[i] = 0000006EB40FF7BC
i = 1,*(p + i) = 2,arr[i] = 2
i = 1,p[i] = 2,*(arr + i) = 2
i = 2,p + i = 0000006EB40FF7C0,&arr[i] = 0000006EB40FF7C0
i = 2,*(p + i) = 3,arr[i] = 3
i = 2,p[i] = 3,*(arr + i) = 3
i = 3,p + i = 0000006EB40FF7C4,&arr[i] = 0000006EB40FF7C4
i = 3,*(p + i) = 4,arr[i] = 4
i = 3,p[i] = 4,*(arr + i) = 4
i = 4,p + i = 0000006EB40FF7C8,&arr[i] = 0000006EB40FF7C8
i = 4,*(p + i) = 5,arr[i] = 5
i = 4,p[i] = 5,*(arr + i) = 5
```

>[!note]
>1.数组不是指针，指针也不是数组
>2.数组的数组名可以赋值给一个指针变量；也可以做加减法 —— 数组的数组名可以退化成&arr[0]
>3.指针可以使用'[]'运算符
>p[i] = 等价于 (p + i) (先做偏移，后做解引用)

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[] = {1,2,3,4,5};
	int *p = arr;
	for(int i = 0;i < 5;++i){
		printf("i = %d,p + i = %p,&arr[i] = %p\n",i,p + i,&arr[i]);
		printf("i = %d,*(p + i) = %d,arr[i] = %d\n",i,*(p + i),arr[i]);
		printf("i = %d,i[p] = %d,*(arr + i) = %d\n",i,i[p],*(arr + i));
	}
	
	return 0;
}
```

```c
结果：
i = 0,p + i = 000000076BCFFAE8,&arr[i] = 000000076BCFFAE8
i = 0,*(p + i) = 1,arr[i] = 1
i = 0,i[p] = 1,*(arr + i) = 1
i = 1,p + i = 000000076BCFFAEC,&arr[i] = 000000076BCFFAEC
i = 1,*(p + i) = 2,arr[i] = 2
i = 1,i[p] = 2,*(arr + i) = 2
i = 2,p + i = 000000076BCFFAF0,&arr[i] = 000000076BCFFAF0
i = 2,*(p + i) = 3,arr[i] = 3
i = 2,i[p] = 3,*(arr + i) = 3
i = 3,p + i = 000000076BCFFAF4,&arr[i] = 000000076BCFFAF4
i = 3,*(p + i) = 4,arr[i] = 4
i = 3,i[p] = 4,*(arr + i) = 4
i = 4,p + i = 000000076BCFFAF8,&arr[i] = 000000076BCFFAF8
i = 4,*(p + i) = 5,arr[i] = 5
i = 4,i[p] = 5,*(arr + i) = 5
```

>[!note]
>数组有时候会变成指针，指针也可以对其使用'[]'运算符。
>此时我们会有一个疑问：数组是不是就是指针？指针和数组是有区别的。
>大部分场景下指针和数组是等价的，但存在例外 —— **sizeof( )**

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(){
	int arr[] = {1,2,3,4,5};
	int *p = arr;
	for(int i = 0;i < 5;++i){
		printf("i = %d,p + i = %p,&arr[i] = %p\n",i,p + i,&arr[i]);
		printf("i = %d,*(p + i) = %d,arr[i] = %d\n",i,*(p + i),arr[i]);
		printf("i = %d,i[p] = %d,*(arr + i) = %d\n",i,i[p],*(arr + i));
	}
	printf("sizeof(p) = %d,sizeof(arr) = %d\n",sizeof(p),sizeof(arr));
	
	return 0;
}
```

```c
结果：
i = 0,p + i = 00000007BD0FF818,&arr[i] = 00000007BD0FF818
i = 0,*(p + i) = 1,arr[i] = 1
i = 0,i[p] = 1,*(arr + i) = 1
i = 1,p + i = 00000007BD0FF81C,&arr[i] = 00000007BD0FF81C
i = 1,*(p + i) = 2,arr[i] = 2
i = 1,i[p] = 2,*(arr + i) = 2
i = 2,p + i = 00000007BD0FF820,&arr[i] = 00000007BD0FF820
i = 2,*(p + i) = 3,arr[i] = 3
i = 2,i[p] = 3,*(arr + i) = 3
i = 3,p + i = 00000007BD0FF824,&arr[i] = 00000007BD0FF824
i = 3,*(p + i) = 4,arr[i] = 4
i = 3,i[p] = 4,*(arr + i) = 4
i = 4,p + i = 00000007BD0FF828,&arr[i] = 00000007BD0FF828
i = 4,*(p + i) = 5,arr[i] = 5
i = 4,i[p] = 5,*(arr + i) = 5
sizeof(p) = 8,sizeof(arr) = 20
```

>[!note]
>指针和数组尽管在很多情况下起到一样的作用。比如说在偏移的时候；比如说在赋值的时候；比如说在使用'[]'运算符的时候。但是指针和数组并不是一回事，在使用**sizeof( )** 去计算二者的大小时二者的结果并不是相等的。
>指针不是数组，数组也不是指针。但是**数组可以退化成指针**，**指针也可以使用'[]'运算符**。

---
[[2026-03-02]]
## 12.8 指针的使用原则

>[!important]
>指针非常容易犯错
>原则：我们必须先确保目标的存在，再考虑指向它的指针。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int *func(){
	int arr[] = {1,2,3};
	for(int i = 0;i < 3;++i){
		printf("func arr[i] = %d\n",arr[i]);
	}
	return arr; // 数组的数组名是可以赋值/传递给主调方的，这样的话数组会退化成指针
}
int main(){
	int *p = func();
	for(int i = 0;i < 3;++i){
		printf("main p[i] = %d\n",p[i]);
	}
	
	return 0;
}
```

```c
结果：
func arr[i] = 1
func arr[i] = 2
func arr[i] = 3
main p[i] = 1
main p[i] = -858993460
main p[i] = -858993460
```

>[!Important]
>结论：函数的返回值不能返回指向自己局部变量的指针。因为在它返回时，这个局部变量已经被销毁了。

---
[[2026-03-03]]
## 12.9 堆空间和动态数组
#### 堆空间
##### 内存布局

>**知识回顾：[[内存布局]]**
>栈区：函数调用的时候申请内存函数返回的时候释放内存。
>数据段 *(用来存放全局变量)* ：程序运行的时候申请内存；程序结束的时候释放内存。
>堆区：由用户自己决定什么时候申请内存 **(malloc)** ，什么时候释放内存 **(free)**。

	malloc
		语法：
			#include<stdlib.h>
			void *malloc(size_t size);
		功能：函数指向一个大小为size的空间，如果错误发生返回NULL。

	1.添加一个#include<stdlib.h>
	2.函数名是malloc，函数参数是一个size_t类型（无符号的8字节整数 —— 描述申请空间的大小），返回值是一个void *（基类型还没有确定的指针，void *类型的指针变量在解引用和偏移之前必须先强转成其他类型） —— 描述申请空间的首地址

	free
		语法：
			#include<stdlib.h>
			void free(void *ptr);
		功能：函数释放指针ptr指向的空间，以供以后使用，指针ptr必须由先前对malloc()，calloc()，realloc()的调用返回。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int *func(){
	int *arr = (int*)malloc(3 * sizeof(int));
	arr[0] = 1;
	arr[1] = 2;
	arr[2] = 3;
	for(int i = 0;i < 3;++i){
		printf("func arr[%d] = %d\n",i,arr[i]);
	}
	return arr;
}
int main(){
	int *p = func();
	for(int i = 0;i < 3;++i){
		printf("main p[%d] = %d\n",i,p[i]);
	}
	free(p); // 避免内存泄漏
	
	return 0;
}
```

```c
结果：
func arr[0] = 1
func arr[1] = 2
func arr[2] = 3
main p[0] = 1
main p[1] = 2
main p[2] = 3
```

- [0] 若想深入理解此程序 —— 详见[[C程序内存动态分析：malloc与函数返回示例]]

>[!堆空间的用法]
>**使用堆空间的好处：** 
>1.堆空间的生存期是不受函数调用和返回的影响。
>2.堆空间的长度不需要在一开始写代码时就确定，可以在后期根据需求再进行分配，我们将其称为 —— **动态数组(实际上并不是一个数组而是一个指针)**
>
>堆空间的长度是可以 **在程序运行的时候确定的**。

---
## 12.10 野指针和空指针

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#icnlude<string.h>

int main(){
	int *p;
	p = (int*)0x12345678;
	// 这是一个野指针
	*p = 100;
	printf("*p = %d\n",*p);
	
	return 0;
}
```

>[!caution]
>此程序虽然能够编译成功，但实际上这个程序是错误的！！！
>
>**使用指针的原则：** 必须先确保目标的存在，在考虑指向它的指针。
>
>0x12345678不是任何目标的内存地址，当你运行此程序时，编译器会弹出一条**报错信息：引发了异常，写入访问权限冲突。** 也就是说，0x12345678所指向的内存空间根本就没分配，所以我们无法访问这部分内存空间。所以这种指针变量我们是无法使用的。

- [0] 我们如果创建了一个指针变量，为了**规避野指针**的问题，我们可以怎么做？

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	int *p = NULL; // NULL底层原理是0 —— 我们将p称为空指针
	int i = 101;
	p = &i;
	*p = 100;
	
	return 0;
}
```

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void func(int *pi){
	*pi = 100;
}
int main(){
	int *p = NULL;
	int i = 100;
	p = &i;
	func(p);
	
	return 0;
}
```

---
# 13. 专题C C风格字符串
## 13.1 C风格的字符串

>[!definition]
>**字符串：** 字符串是由一个或者多个字符组成的字符序列。

>[!caution]
>C语言没有原生的字符串类型。
>C语言的字符串是基于字符数组 **(char数组)** 的。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[] = "hello";
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
结果：
str = hello
```

>[!important]
>C语言的字符串 = 字符数组 + 在字符串的有效内容之后，要额外加一个ASCII码为0的终止符**('\0') ** 作为结尾 **(额外约定)**

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[5] = {'h','e','l','l','o'}; // 没有空间去放'\0'
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
结果：
str = hello烫烫烫烫烫烫烫烫烫烫烫烫烫烫烫?
```

---
[[2026-03-04]]
## 13.2 strlen
#### 和字符串相关的函数

	strlen
		语法：
			#include<string.h> // 所有和字符串相关的函数在使用前都要引入<string.h>这个头文件。
			size_t strlen(char *str);
		功能：函数返回字符串str的长度(即空值结束符之前字符数目)。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[10] = "hello"; // 数组长度 ≥ 有效长度 + 1 即可
	printf("strlen(str) = %d,sizeof(str) = %d\n",strlen(str),sizeof(str));
	return 0;
}
```

```c
结果：
strlen(str) = 5,sizeof(str) = 10
```

---
## 13.3 strcpy

	strcpy
		语法：
			#include<string.h>
			char *strcpy(char *to,const char *from)
		功能：复制字符串from中的字符到字符串to，包括空值结束符。返回值为指针to。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char to[10];
	char from[10] = "hello";
	// to = from; // 这是一个错误用法，数组是不能赋值的。
	strcpy(to,from);
	printf("to = %s\n",to)
	
	return 0;
}
```

>[!caution]
>使用 `strcpy` 存在**缓冲区溢出风险**。
>
>`strcpy(to, from);`  
>该函数仅根据源字符串的 `'\0'` 结束符决定拷贝长度，**不检查目标数组 `to` 的大小**。因此，如果源字符串的长度（包含结尾的 `'\0'`）超过目标数组的容量，就会发生越界写入，导致程序行为不可预测甚至崩溃。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char to[5];
	char from[10] = "hello";
	// to = from; // 这是一个错误用法，数组是不能赋值的。
	strcpy(to,from);
	printf("to = %s\n",to)
	
	return 0;
}
```

>[!caution]
>程序运行时报错 **Run-Time Check Failure #2 – Stack around the variable 'to' was corrupted**，这是因为 `strcpy(to, from)` 将长度为 6 字节的字符串（`"hello"` 的 5 个字符 + 结尾的 `'\0'`）复制到容量仅 5 字节的数组 `to` 中，导致数组越界。由于 `to` 是 `main` 函数的局部数组，存储在栈区，越界写入破坏了栈上其他数据（如相邻变量或返回地址），从而引发栈损毁检测错误。

---
## 13.4 strcmp

	strcmp
		语法：
			#include<string.h>
			int strcmp(const char *str1,const char *str2);
		功能：比较字符串str1 and str2，返回值如下：

| 返回值            | 解释                        |
| -------------- | ------------------------- |
| less than 0    | str1 is less than str2    |
| equal to 0     | str1 is equal to str2     |
| greater than 0 | str1 is greater than str2 |
```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<Stdlib.h>
#include<string.h>

int main(){
	char str1[] = "back";
	char str2[] = "backward";
	char str3[] = "back";
	printf("str1 vs str2 = %d\n",strcmp(str1,str2));
	printf("str2 vs str1 = %d\n",strcmp(str2,str1));
	printf("str1 vs str3 = %d\n",strcmp(str1,str3));
	
	return 0;
}
```

```c
结果：
str1 vs str2 = -1
str2 vs str1 = 1
str1 vs str3 = 0
```

---
## 13.5 strcat

	strcat
		语法：
			#include<string.h>
			char *strcat(char *str1,const *str2);
		功能：函数将字符串str2连接到str1的末端，并返回指针str1。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str1[20] = "how";
	char str2[] = "ever";
	strcat(str1,str2);
	printf("str1 = %s\n",str1);
	
	return 0;
}
```

```c
结果：
str1 = however
```

>[!caution]
>使用 `strcat` 存在**缓冲区溢出风险**。
>
>`strcat(str1, str2);`  
>该函数将字符串 `str2` 追加到 `str1` 的末尾（覆盖 `str1` 的结尾空字符，然后添加新的空字符）。**它不检查目标数组 `str1` 的大小**。因此，如果 `str1` 中原有字符串的长度与 `str2` 的长度（均不包含结尾的 `'\0'`）之和再加 1 超过 `str1` 数组的容量，就会发生越界写入，导致程序行为不可预测甚至崩溃。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str1[5] = "how";
	char str2[] = "ever";
	strcat(str1,str2);
	printf("str1 = %s\n",str1);
	
	return 0;
}
```

>[!caution]
>程序运行时报错 **Run-Time Check Failure #2 – Stack around the variable 'str1' was corrupted**，这是因为 `strcat(str1, str2)` 将字符串 `"ever"`（长度 4，加上结尾 `'\0'` 共 5 字节）追加到 `str1` 原有字符串 `"how"`（长度 3，加上结尾 `'\0'` 共 4 字节）的末尾。合并后的字符串总长度为 7（不含结尾 `'\0'`），加上结尾 `'\0'` 共需 8 字节，而 `str1` 数组的容量仅为 5 字节，导致数组越界写入。由于 `str1` 是 `main` 函数的局部数组，存储在栈区，越界写入破坏了栈上其他数据（如相邻变量或返回地址），从而引发栈损毁检测错误。

---
## 13.6 字符串输入

>**从标准输入中读取字符串**

	scanf %s —— 读取一个单词 —— 以空白字符为边界(遇到换行、空格、制表符等空白字符时都会停止输入)
	fgets —— 读取一行内容 —— 以换行为边界

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#icnlude<stdlib.h>
#include<string.h>

int main(){
	char str[20];
	scanf("%s",str); // str是一个数组，当数组作为参数进行传递时会退化成一个指针
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
输入：
hello
结果：
str = hello
```

```c
输入：
how are you
结果：
str = how
```

	fgets
		语法：
			#include<stdio.h>
			char *fgets(char *str,int num,FILE *stream);
		函数fgets()从给出的文件流中读取[num - 1]个字符并且把它们转储到str(字符串)中。fgets()在到达行末时停止，在这种情况下，str(字符串)将会被一个新行符结束。如果fgets()达到[num - 1]个字符或者遇到EOF, str(字符串)将会以null结束.fgets()成功时返回str(字符串),失败时返回NULL。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[20];
	fgets(str,20,stdin); // 从stdin中读取一行到str，最大长度是20。
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
输入：
how are you
结果：
str = how are you


```

>[!important]
>fgets读取一行内容时，不会将末尾的'\n'换行符去掉，而是会留在缓冲区中。

- [1] 若想去掉多余的换行，我们可以进行如下操作：

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[20];
	fgets(str,20,stdin); // 从stdin中读取一行到str，最大长度是20。
	int idx = strlen(str) - 1;
	if(str[idx] == '\n'){
		str[idx] = '\0';
	}
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
输入：
how are you
结果：
str = how are you

```

>[!caution]
>**scanf和fgets的安全性**
>**scanf的安全性**
>scanf的参数里面没有长度信息。
>**结论一：** scanf是不安全的，有可能会出现数组越界的问题。
>**fgets的安全性**
>fgets的参数里面有长度限制信息。
>**结论二：** fgets是安全的。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	char str[4];
	scanf("%s",str);
	printf("str = %s\n",str);
	
	return 0;
}
```

>[!caution]
>程序运行时报错 **Run-Time Check Failure #2 – Stack around the variable 'str' was corrupted**，这是因为 `scanf("%s", str)` 没有限制输入长度，当用户输入的字符串长度超过数组 `str` 的容量（4字节，最多存储3个字符加一个结尾空字符）时，就会发生缓冲区溢出，越界写入栈上的相邻内存，导致栈损毁检测错误。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<Stdlib.h>
#include<string.h>

int main(){
	char str[10];
	fgets(str,10,stdin);
	printf("str = %s\n",str);
	
	return 0;
}
```

```c
输入：
how are you
结果：
str = how are y
```

---
[[2026-03-05]]
# 14. 专题D 递归和分治
## 14.1 递归

>[!definition]
>**递归：** 设计一个函数func的函数定义，再func的函数体里面，去调用func函数本身 —— 递归

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void func(int i){
	printf("i = %d\n",i);
	// 避免无限递归触发栈溢出，我们可以设计一个递归出口。
	if(i <= 0){
		return;
	}
	else{
		func(i - 1);
	}
}
int main(){
	func(4);
}
```

```c
结果：
i = 4
i = 3
i = 2
i = 1
i = 0
```

>[!caution]
>**避免无限递归的方法：** 设计一个合理的递归出口。

---
## 14.2 爬楼梯问题

>[!question]
>**爬楼梯问题：** 假设你正在爬楼梯，总共有n阶台阶。每次你只能爬1阶 **或者** 爬2阶。
>问：你有多少种不同的方法可以爬到楼顶？ 

>[!challenge]
>我们从传统的全局视角当中，很难去找到问题的解决方案。

>[!solution]
>**局部解决：** 把一个规模大一点的问题转移成规模小一点的问题 —— 分治法( *分而治之 divide and conquer* )

>[!method]
>**数学归纳法：** 假设 num = 1,2,3,4, ... ,n - 1 都已经被解决了，在此基础上去解决 num = n的问题。

>[!principle]
>**组合计数问题 —— 加法原理** 
>台阶数num = n时爬到楼顶的方法总数 = 台阶数num = n - 1时爬到楼顶的方法总数 + 台阶数num = n - 2时爬到楼顶的方法总数

>[!derivation]
>**同理可得：** 
>$$
>\begin{gather}
>\text{设台阶数num \ = \ n时爬到楼顶的方法总数为}S_n \\
>S_{n - 1} \ = \ S_{n - 2} \ + \ S_{n - 3} \\
>S_{n - 2} \ = \ S_{n - 3} \ + \ S_{n - 4} \\
>... \\
>S_{3} \ = \ S_{2} \ + \ S_{1} \\
>\end{gather}
>$$

>[!ideology]
>当$S_{n-1}$逐步分解直到分解为$S_{3} \ = \ S_{2} \ + \ S_{1}$时，如何根据$S_{1} \ 和 \ S_{2}$求得$S_{3}$已经不再困难，我们可以非常轻松的计算出$S_{3}$。( *divide：递推 —— 将大问题转移成小问题* )
>求出$S_{3}$之后，我们可以根据$S_{2} \ 和刚刚求得的 \ S_{3} \ 进而去计算 \ S_{4}$，以此类推，最后我们可以计算出$S_{n}$。( *conquer：回归 —— 将小问题解决后进行反向推理使大问题也得到了解决* )

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int f(int n){
	// 大问题 —— 小问题 —— 递归
	if(n > 2){
		int result = f(n - 1) + f(n - 2);
		return result;
	}
	// 最小问题的解决方案
	else if(n == 2){
		return 2;
	}
	else if(n == 1){
		return 1;
	}
}
int main(){
	int n = 4;
	printf("f(%d) = %d\n",n,f(n));
	
	return 0;
}
```

```c
结果：
f(4) = 5
```

```mermaid
flowchart TD
    A["main调用f(4)"] -->|1| B["f(4)条件 n>2"]
    B -->|2| C["调用f(3)"]
    C -->|3| D["f(3)条件 n>2"]
    D -->|4| E["调用f(2)"]
    E -->|5| F["f(2)返回2"]
    F -->|6| D
    D -->|7| G["调用f(1)"]
    G -->|8| H["f(1)返回1"]
    H -->|9| D
    D -->|10| I["f(3)返回3"]
    I -->|11| B
    B -->|12| J["调用f(2)"]
    J -->|13| K["f(2)返回2"]
    K -->|14| B
    B -->|15| L["f(4)返回5"]
    L -->|16| M["main输出5"]
```

>[!process]
>**递归过程**
>*1.大问题转移成小问题 —— 递推*
>*2.找到问题的边界(最小问题) —— 回归*

---
## 14.3 汉诺塔问题

>[!question]
>**汉诺塔问题：** 现在有n个从小到大排列的圆盘，我们需要将圆盘全部移动到另一个柱子上，并遵守**以下规则**：
>1.每次只能移动一个圆盘；
>2.移动过程中，大盘不能放在小盘上面；
>3.只能移动最顶端的圆盘。

>[!challenge]
>如果我们用**枚举**的思路( *从全局的角度* )去解决`汉诺塔问题`显然是很困难的。

>[!solution]
>因此我们退而求其次选择**分治法**来解决`汉诺塔问题`。

>[!method]
>**数学归纳法：** 假设我们已经知道如何移动 n-1 个盘子，那么就可以解决 n 个盘子的移动问题。

>[!principle]
>**分治策略：** 将 n 个盘子的移动问题分解为三个子问题：
>1. 将上面的 n-1 个盘子从起始柱移动到辅助柱；
>2. 将最大的盘子从起始柱移动到目标柱；
>3. 将 n-1 个盘子从辅助柱移动到目标柱。

>[!derivation]
>**递归公式：** 设移动 n 个盘子所需的最少步数为 $T_n$，则有：
>$$
>T_n = 2T_{n-1} + 1, \quad T_1 = 1
>$$
>**通项公式推导（迭代法）：**
>$$
>\begin{aligned}
>T_n &= 2T_{n-1} + 1 \\
>&= 2(2T_{n-2} + 1) + 1 = 2^2 T_{n-2} + 2 + 1 \\
>&= 2^2(2T_{n-3} + 1) + 2 + 1 = 2^3 T_{n-3} + 2^2 + 2 + 1 \\
>&\quad \vdots \\
>&= 2^{n-1} T_1 + (2^{n-2} + 2^{n-3} + \cdots + 2 + 1)
>\end{aligned}
>$$
>代入 $T_1 = 1$，并利用等比数列求和公式 $2^{n-2} + 2^{n-3} + \cdots + 2 + 1 = 2^{n-1} - 1$，得：
>$$
>T_n = 2^{n-1} \cdot 1 + (2^{n-1} - 1) = 2^n - 1
>$$

>[!ideology]
>当 $T_{n-1}$ 逐步分解直到 $T_1$ 时，问题变得极为简单：直接移动一个盘子即可。这就是 ( *divide：递推* ) 的过程。求出 $T_1$ 后，我们可以根据 $T_1$ 计算出 $T_2$，进而得到 $T_3$，以此类推，最终得到 $T_n$。这就是 ( *conquer：回归* ) 的过程。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 汉诺塔递归函数
void hanoi(int n, char from, char buffer, char to){
	// 形参from 圆盘的初始位置
	// 形参to 圆盘的最终位置
	// 形参buffer 临时借用的位置
	
	// 大问题 —— 小问题 —— 递归
	if(n > 1){
		// 把前n - 1个圆盘从 from 移动到 buffer
		hanoi(n - 1,from,to,buffer);
		// 将第n个圆盘从 from 移动到 to
		hanoi(1,from,buffer,to);
		// 把前n - 1个圆盘从 buffer 移动到 to
		hanoi(n - 1,buffer,from,to);
	}
	else if(n == 1){
		printf("move %c to %c\n",from,to);
	}
}

int main(){
    int n = 5;
    hanoi(n, 'A', 'B', 'C');
    return 0;
}
```

```c
结果：
move A to C
move A to B
move C to B
move A to C
move B to A
move B to C
move A to C
move A to B
move C to B
move C to A
move B to A
move C to B
move A to C
move A to B
move C to B
move A to C
move B to A
move B to C
move A to C
move B to A
move C to B
move C to A
move B to A
move B to C
move A to C
move A to B
move C to B
move A to C
move B to A
move B to C
move A to C
```

根据新代码（参数顺序为 `from, buffer, to`），以 n=5 为例的递归调用树非常庞大（共 46 个节点，31 个叶子节点对应输出）。为了清晰展示整体结构，下面采用缩略树的形式，用节点范围表示完整的子树，并标注了深度优先遍历的序号。

**缩略版递归调用树**

```mermaid
flowchart TD
    A["1: hanoi(5, A, B, C)"] --> B["2..23: hanoi(4, A, C, B) (22 个节点)"]
    A --> C["24: hanoi(1, A, B, C)"]
    A --> D["25..46: hanoi(4, B, A, C) (22 个节点)"]
```

#### 节点序号说明
- **序号 1**：根调用 `hanoi(5, A, B, C)`。
- **序号 2~23**：完整的 `hanoi(4, A, C, B)` 子树，内部包含 22 个节点（递归展开后对应前 22 步调用）。
- **序号 24**：直接输出 `move A to C` 的调用 `hanoi(1, A, B, C)`。
- **序号 25~46**：完整的 `hanoi(4, B, A, C)` 子树，内部包含 22 个节点。

每个 `hanoi(4, ...)` 子树内部结构可类比 n=4 时的递归树（共 22 个节点），其展开方式与根节点类似，依次包含两个 n=3 子树和一个 n=1 调用。若需查看完整展开，可参考 n=3 的详细树结构进行类推。

#### 完整调用统计
- n=5 时，总调用次数（含叶子输出）为 46 次，其中输出语句执行 31 次，与 $2^5-1=31$ 一致。

此缩略树在保持整体结构的同时，避免了过长的节点列表，便于在 Obsidian 中呈现和理解递归的层次关系。

**完整版递归调用树**

#### 根节点：hanoi(5, A, B, C)
```mermaid
flowchart TD
    1["1: hanoi(5,A,B,C)"]
```
#### 左子树：hanoi(4, A, C, B)
```mermaid
flowchart TD
    2["2: hanoi(4,A,C,B)"]
    3["3: hanoi(3,A,B,C)"]
    4["4: hanoi(2,A,C,B)"]
    5["5: hanoi(1,A,B,C)"]
    6["6: hanoi(1,A,C,B)"]
    7["7: hanoi(1,C,A,B)"]
    8["8: hanoi(1,A,B,C)"]
    9["9: hanoi(2,B,A,C)"]
    10["10: hanoi(1,B,C,A)"]
    11["11: hanoi(1,B,A,C)"]
    12["12: hanoi(1,A,B,C)"]
    13["13: hanoi(1,A,C,B)"]
    14["14: hanoi(3,C,A,B)"]
    15["15: hanoi(2,C,B,A)"]
    16["16: hanoi(1,C,A,B)"]
    17["17: hanoi(1,C,B,A)"]
    18["18: hanoi(1,B,C,A)"]
    19["19: hanoi(1,C,A,B)"]
    20["20: hanoi(2,A,C,B)"]
    21["21: hanoi(1,A,B,C)"]
    22["22: hanoi(1,A,C,B)"]
    23["23: hanoi(1,C,A,B)"]
    2 --> 3
    3 --> 4
    4 --> 5
    4 --> 6
    4 --> 7
    3 --> 8
    3 --> 9
    9 --> 10
    9 --> 11
    9 --> 12
    2 --> 13
    2 --> 14
    14 --> 15
    15 --> 16
    15 --> 17
    15 --> 18
    14 --> 19
    14 --> 20
    20 --> 21
    20 --> 22
    20 --> 23
```
#### 中子树(中子)：hanoi(1, A, B, C)
```mermaid
flowchart TD
    24["24: hanoi(1,A,B,C)"]
```
#### 右子树：hanoi(4, B, A, C)
```mermaid
flowchart TD
    25["25: hanoi(4,B,A,C)"]
    26["26: hanoi(3,B,C,A)"]
    27["27: hanoi(2,B,A,C)"]
    28["28: hanoi(1,B,C,A)"]
    29["29: hanoi(1,B,A,C)"]
    30["30: hanoi(1,A,B,C)"]
    31["31: hanoi(1,B,C,A)"]
    32["32: hanoi(2,C,B,A)"]
    33["33: hanoi(1,C,A,B)"]
    34["34: hanoi(1,C,B,A)"]
    35["35: hanoi(1,B,C,A)"]
    36["36: hanoi(1,B,A,C)"]
    37["37: hanoi(3,A,B,C)"]
    38["38: hanoi(2,A,C,B)"]
    39["39: hanoi(1,A,B,C)"]
    40["40: hanoi(1,A,C,B)"]
    41["41: hanoi(1,C,A,B)"]
    42["42: hanoi(1,A,B,C)"]
    43["43: hanoi(2,B,A,C)"]
    44["44: hanoi(1,B,C,A)"]
    45["45: hanoi(1,B,A,C)"]
    46["46: hanoi(1,A,B,C)"]
    25 --> 26
    26 --> 27
    27 --> 28
    27 --> 29
    27 --> 30
    26 --> 31
    26 --> 32
    32 --> 33
    32 --> 34
    32 --> 35
    25 --> 36
    25 --> 37
    37 --> 38
    38 --> 39
    38 --> 40
    38 --> 41
    37 --> 42
    37 --> 43
    43 --> 44
    43 --> 45
    43 --> 46
```

>[!process]
>**递归过程**
>*1. 大问题转移成小问题 —— 递推：每次将 n 个盘子的问题转化为 n-1 个盘子的问题，直到边界 n=1。*
>*2. 找到问题的边界（最小问题）—— 回归：当 n=1 时直接移动，然后逐步返回，完成上层剩余的移动。*

---
[[2026-03-06]]
## 14.4 归并排序

>*利用分而治之的思想进行排序*

>[!question]
>现有一个**无序**的数组（即对于下标 i < j，不一定有 a[i] < a[j]），我们想通过**分而治之的思想**对数组中的元素进行**排序**。

>*解决这个问题之前让我们先解决一个前提问题：*

>[!question]
>给出两个**有序**的小数组，如何合并成一个大的**有序**数组？
>**例如：**
>```c
>int a[5] = {1,3,5,7,9};
>int b[5] = {2,4,6,8,10};
>```

>[!solution]
>准备两个变量 i 和 j 分别从左往右扫描数组 a 和 b，每次比较 i 和 j 所指的元素，将**较小者**放入结果数组中，并移动相应指针。重复此过程直到其中一个数组扫描完毕，最后将另一个数组的剩余元素直接复制到结果末尾。

>*解决了前提问题之后，让我们回到最初的问题 —— 利用* **分而治之的思想** *对* **无序** * *数组进行* **排序**

>[!ideology]
>**分治法**
>1. **划分（Divide）**：将无序大数组均分成两个无序的小数组( *divide：递推过程* ）；
>2. **解决（Conquer）**：递归地对两个小数组进行排序，使其成为有序小数组；
>3. **合并（Combine）**：将两个有序小数组**合并**成一个有序大数组( *conquer：回归过程* )。
>
>当数组长度为 0 或 1 时，数组自然有序，这是递归的**边界条件**。

>[!method]
>**数学归纳法（递归视角）**：假设我们已经知道如何对长度为$n - 1$的数组进行排序，那么可以通过“分 — 排 — 合”的步骤解决长度为$n$的数组的排序问题。但归并排序更自然的描述是：将数组一分为二，递归排序两个子数组，然后合并。

>[!principle]
>**分治策略**：将长度为 n 的数组排序问题分解为三个子问题：
>4. 将数组从中间分成左右两个子数组(规模约为$n/2$)；
>5. 递归地对左子数组进行归并排序；
>6. 递归地对右子数组进行归并排序；
>7. 将两个已排序的子数组合并成一个完整的有序数组。

>[!derivation]
>**递归公式**：设对 n 个元素进行归并排序所需的最多比较次数为 $T(n)$，则有：
>$$
>T(n) = 2T(n/2) + O(n)
>$$
>其中 $O(n)$ 为合并两个有序子数组所需的时间（线性扫描）。若忽略常数，可写为：
>$$
>T(n) = 2T(n/2) + n
>$$
>**通项公式推导（迭代法 / 主定理）**：
>假设 $n = 2^k$，则：
>$$
>\begin{aligned}
>T(n) &= 2T(n/2) + n \\
>&= 2(2T(n/4) + n/2) + n = 4T(n/4) + 2n \\
>&= 4(2T(n/8) + n/4) + 2n = 8T(n/8) + 3n \\
>&\quad \vdots \\
>&= 2^k T(1) + k \cdot n
>\end{aligned}
>$$
>其中 $T(1)=0$（一个元素无需比较），$k = \log_2 n$，因此：
>$$
>T(n) = n \log_2 n
>$$
>即归并排序的时间复杂度为 **$O(n \log n)$**。

>[!caution]
>在时间复杂度的大$O$表示法中，对数底数通常是**省略**的，因为不同底数之间仅相差一个常数因子，而常数因子在大$O$中被忽略。例如，$\log⁡_{2}n=\log⁡_{2}10⋅\log_{⁡10}n$，所以 $O(\log_{⁡2}n)$ 与 $O(\log_{⁡10}n)$是等价的，统一写作 $O(\log⁡_{}n)$。
>因此，归并排序的时间复杂度$O(n\log_{}⁡n)$中的$\log$默认可以是以$2$为底，也可以是以其他常数为底，不影响渐近阶。推导中出现了$\log_{⁡2}n$，最后写成$O(n\log n)$是标准且正确的，不需要特意加上底数$2$。

>[!ideology]
>当子数组长度降为 1 时，问题变得极为简单：单个元素自然有序。这就是( *divide：递推* )的过程。求出最小问题的解后，我们逐层返回，将两个有序子数组合并成更大的有序数组。这就是( *conquer：回归* )的过程。

#### 代码实现

以下实现使用 `while` 循环完成合并，逻辑清晰且无变量作用域错误。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 合并两个有序子数组 [left, mid] 和 [mid+1, right]
void merge(int* arr, int* temp, int left, int mid, int right) {
    // 1. 将原数组备份到 temp
    for (int i = left; i <= right; ++i) {
        temp[i] = arr[i];
    }

    // 2. 合并两个有序子数组
    int i = left;          // 左半部分起始下标
    int j = mid + 1;       // 右半部分起始下标
    int k = left;          // 写入 arr 的位置

    while (i <= mid && j <= right) {
        if (temp[i] < temp[j]) {
            arr[k++] = temp[i++];
        } else {
            arr[k++] = temp[j++];
        }
    }

    // 3. 处理剩余元素
    while (i <= mid) {
        arr[k++] = temp[i++];
    }
    while (j <= right) {
        arr[k++] = temp[j++];
    }
}

// 归并排序递归函数
void mergeSort(int* arr, int* temp, int left, int right) {
    if (left < right) {                     // 当区间长度大于1时
        int mid = (left + right) / 2;        // 划分点
        mergeSort(arr, temp, left, mid);     // 排序左半
        mergeSort(arr, temp, mid + 1, right); // 排序右半
        merge(arr, temp, left, mid, right);   // 合并两个有序半区
    }
    // left == right 时，区间只有一个元素，自然有序，不做任何操作
}

int main() {
    int arr[] = {3, 14, 15, 9, 26, 5, 35, 89, 79, 32, 38, 46};
    int temp[12];                            // 辅助数组
    mergeSort(arr, temp, 0, 11);              // 对全部12个元素排序

    printf("排序后的 arr：\n");
    for (int i = 0; i < 12; ++i) {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    return 0;
}
```

以下实现使用 `for` 循环完成合并，逻辑清晰且无变量作用域错误。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 合并功能函数merge
void merge(int *arr,int *temp,int left,int mid,int right){
	// arr[left] ~ arr[mid] 和 arr[mid + 1] ~ arr[right] 进行合并
	// 1.将arr的内容备份到temp里面
	for(int i = left;i <= right;++i){
		temp[i] = arr[i];
	}
	
	// 2.合并有序数组 —— 准备三个变量i,j,k
	// i用来访问左半边 | j用来访问右半边 | k用来存放结果
	int i,j,k;
	// 把左右两边当中比较小的那一边完全放到目标数组中
	for(int i = left,j = mid + 1,k = left;i <= mid && j <= right;++k){
		if(temp[i] < temp[j]){
			arr[k] = temp[i];
			++i;
		}
		else{
			arr[k] = temp[j];
			++j;
		}
	}
	
	// 如果左边没有放完，那就将左边剩余的数组元素放到目标数组中
	while(i <= mid){
		arr[k] = temp[i];
		++i;
		++k;
	}
	
	// 如果右边没有放完，那就将右边剩余的数组元素放到目标数组中
	while(j <= right){
		arr[k] = temp[j];
		++j;
		++k;
	}
}

//归并排序
void mergeSort(int *arr,int *temp,int left,int right){
	// 大问题 —— 小问题 —— 递归
	if(left < right){
		int mid = (left + right) / 2;
		mergeSort(arr,temp,left,mid);
		mergeSort(arr,temp,mid + 1,right);
		merge(arr,temp,left,mid,right);
	}
	
	// 找到最小问题的解决方案
}

int main(){
	int arr[] = {3,14,15,9,26,5,35,89,79,32,38,46};
	int temp[12];
	mergeSort(arr,temp,0,11);
	for(int i = 0;i < 12;++i){
		printf("arr[%d] = %d\n",i,arr[i]);
	}
	printf("--------------------\n");
	for(int i = 0;i < 12;++i){
		printf("temp[%d] = %d\n",i,temp[i]);
	}
	
	return 0;
}
```

> [!caution]
> 初学者容易在 `merge` 函数中犯变量作用域错误（如过早声明 `i, j, k` 却未初始化，或在 `for` 循环内重新定义局部变量）。上述代码分别采用了`while` 循环和`for` 循环实现，每个变量在使用前都被正确初始化。

#### 递归调用树示例

以数组 `{3,14,15,9,26,5,35,89,79,32,38,46}`( 下标 $0$ ~ $11$ )为例，归并排序的递归调用树如下( 缩进表示递归深度，每个节点表示一次 `mergeSort` 调用，其后的区间为待排序范围 )：

```
mergeSort(arr, temp, 0, 11)
├── mergeSort(arr, temp, 0, 5)                 // 左半 [0,5]
│   ├── mergeSort(arr, temp, 0, 2)              // [0,2]
│   │   ├── mergeSort(arr, temp, 0, 1)           // [0,1]
│   │   │   ├── mergeSort(arr, temp, 0, 0)       // [0,0] 叶子
│   │   │   └── mergeSort(arr, temp, 1, 1)       // [1,1] 叶子
│   │   │   └── merge(arr, temp, 0, 0, 1)         // 合并 [0,0] 和 [1,1]
│   │   └── mergeSort(arr, temp, 2, 2)           // [2,2] 叶子
│   │   └── merge(arr, temp, 0, 1, 2)             // 合并 [0,1] 和 [2,2]
│   └── mergeSort(arr, temp, 3, 5)              // [3,5]
│       ├── mergeSort(arr, temp, 3, 4)           // [3,4]
│       │   ├── mergeSort(arr, temp, 3, 3)       // [3,3] 叶子
│       │   └── mergeSort(arr, temp, 4, 4)       // [4,4] 叶子
│       │   └── merge(arr, temp, 3, 3, 4)         // 合并 [3,3] 和 [4,4]
│       └── mergeSort(arr, temp, 5, 5)           // [5,5] 叶子
│       └── merge(arr, temp, 3, 4, 5)             // 合并 [3,4] 和 [5,5]
│   └── merge(arr, temp, 0, 2, 5)                 // 合并左半 [0,2] 和 [3,5]
└── mergeSort(arr, temp, 6, 11)                 // 右半 [6,11]
    ├── mergeSort(arr, temp, 6, 8)               // [6,8]
    │   ├── mergeSort(arr, temp, 6, 7)           // [6,7]
    │   │   ├── mergeSort(arr, temp, 6, 6)       // [6,6] 叶子
    │   │   └── mergeSort(arr, temp, 7, 7)       // [7,7] 叶子
    │   │   └── merge(arr, temp, 6, 6, 7)         // 合并 [6,6] 和 [7,7]
    │   └── mergeSort(arr, temp, 8, 8)           // [8,8] 叶子
    │   └── merge(arr, temp, 6, 7, 8)             // 合并 [6,7] 和 [8,8]
    └── mergeSort(arr, temp, 9, 11)              // [9,11]
        ├── mergeSort(arr, temp, 9, 10)          // [9,10]
        │   ├── mergeSort(arr, temp, 9, 9)       // [9,9] 叶子
        │   └── mergeSort(arr, temp, 10, 10)     // [10,10] 叶子
        │   └── merge(arr, temp, 9, 9, 10)        // 合并 [9,9] 和 [10,10]
        └── mergeSort(arr, temp, 11, 11)         // [11,11] 叶子
        └── merge(arr, temp, 9, 10, 11)           // 合并 [9,10] 和 [11,11]
    └── merge(arr, temp, 6, 8, 11)                 // 合并右半 [6,8] 和 [9,11]
└── merge(arr, temp, 0, 5, 11)                     // 最终合并左右两半
```

>[!note]
>树中每个内部节点都对应一次 `merge` 操作，而叶子节点（长度为1的区间）不执行任何实际合并。整个递归过程先**递推**分解到叶子，然后逐层**回归**合并，最终得到完全有序的数组。

>[!process]
>**递归过程**
>1. **大问题转移成小问题 —— 递推**：每次将长度为 n 的数组排序问题转化为两个长度为 n/2 的子数组排序问题，不断划分直到数组长度为 1（自然有序）。
>2. **找到问题的边界（最小问题）—— 回归**：当数组长度为 1 时直接返回，然后逐层向上将两个已排序的子数组合并成更大的有序数组，最终得到原数组的有序结果。

>[!summarization]
>通过上述分治策略，归并排序实现了稳定、高效的排序，时间复杂度始终为 $O(n \log n)$，且不受输入数据初始顺序的影响。

---
# 15. 结构体和补充知识
## 15.1 结构体类型定义和变量定义

>[!review]
>**知识回顾：[[数据类型]] —— 一个对象被放在内存里面后，它的种类是什么？**
>**组成数据类型的三要素：**
>1.数据在内存中占多大的空间？
>2.以何种方式去解释内存中的每一个`bit` ？
>3.数据都支持什么类型的运算？

>[!review]
>**基本数据类型：** `int` , `double` , `float` , `char` , `···`
>**复合数据类型：** `数组` , `指针` , `···`

>[!question]
>*除此之外还有没有其他* **数据类型** *？*

>[!definition]
>**结构体：** 一种由用户自定义的复合数据类型( 可以把多个不同类型的成员打包在一起组成一个新的类型 )。
>可以将**结构体**看作一个容器，容器里面是一个个成员。

>[!question]
>如何定义一个结构体类型？

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 定义结构体类型
struct student_s{ // struct studentn_s 是结构体类型的名字
	int id;
	char name[25];
	char gender;
	float Politics;
	float English;
	float Math;
	float cs408;
}; //分号是不可省略的

int main(){
	// struct student_s stu; // 结构体类型的变量
	struct student_s stu = {2023211033,"LvZiyuan",'m',60,75,115,115};
	
	return 0;
}
```

>[!important]
>**声明**一个**结构体变量**时，系统会为该变量分配一块连续的内存空间，其占用的内存大小通常 **≥** 该结构体类型所有成员占用的内存大小之和。

---
## 15.2 对齐问题

>[!question]
>*结构体都支持什么类型的运算？*

>[!note]
>**1.sizeof：** 用字节计算右边表达式并返回字节数 —— 计算数据类型所占内存大小

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 定义结构体类型
struct student_s{ // struct studentn_s 是结构体类型的名字
	int id;
	char name[25];
	char gender;
	float Politics;
	float English;
	float Math;
	float cs408;
	// sizeof(stu) = 4 + 25 + 1 + 4 + 4 + 4 + 4 = 46
}; //分号是不可省略的

int main(){
	// struct student_s stu; // 结构体类型的变量
	struct student_s stu = {2023211033,"LvZiyuan",'m',60,75,115,115};
	printf("sizeof(stu) = %d\n",sizeof(stu));
	
	return 0;
}
```

```c
结果：
sizeof(stu) = 48
```

>[!question]
>系统分配给**结构体变量stu**的内存大小的理论值为46 $byte$，但在程序实际运过程中**sizeof(stu) = 48** $byte$，系统实际分配给**结构体变量stu**的内存大小比系统分配给**结构体变量stu**的内存大小的理论值大 $2 \ byte$，这是为什么？

>[!definition]
>**内存对齐：( Memory Alignment )** 是计算机系统为了提升内存访问效率，而对数据在内存中的存放地址所做出的一种限制。简单来说，它要求特定类型的数据只能存储在内存中某些特定的地址上（通常是该数据类型大小的整数倍地址）。
>若想深入理解 **内存对齐** 的概念 —— 详见[[内存对齐]]

---
## 15.3 常见结构体变量

### '.'运算符

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 定义结构体类型
struct student_s{ // struct studentn_s 是结构体类型的名字
	int id;
	char name[25];
	char gender;
	float Politics;
	float English;
	float Math;
	float cs408;
}; //分号是不可省略的

int main(){
	// struct student_s stu; // 结构体类型的变量
	struct student_s stu = {2023211033,"LvZiyuan",'m',60,75,115,115};
	
	// '.'运算符 —— 根据结构体去访问内部的成员
	printf("stu = %d %s %c %f %f %f %f\n",stu.id,stu.name,stu.gender,stu.Politics,stu.English,stu.Math,stu.cs408);
	
	return 0;
}
```

```c
结果：
stu = 2023211033 LvZiyuan m 60.000000 75.000000 115.000000 115.000000
```

### '='运算符

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 定义结构体类型
struct student_s{ // struct studentn_s 是结构体类型的名字
	int id;
	char name[25];
	char gender;
	float Politics;
	float English;
	float Math;
	float cs408;
}; //分号是不可省略的

int main(){
	// struct student_s stu; // 结构体类型的变量
	struct student_s stu = {2023211033,"LvZiyuan",'m',60,75,115,115};
	
	// '.'运算符 —— 根据结构体去访问内部的成员
	printf("stu = %d %s %c %f %f %f %f\n",stu.id,stu.name,stu.gender,stu.Politics,stu.English,stu.Math,stu.cs408);
	
	// '='运算符
	struct student_s stu1;
	stu1 = stu;
	printf("stu1 = %d %s %c %f %f %f %f\n",stu1.id,stu1.name,stu1.gender,stu1.Politics,stu1.English,stu1.Math,stu1.cs408);
	
	return 0;
}
```

```c
结果：
stu = 2023211033 LvZiyuan m 60.000000 75.000000 115.000000 115.000000
stu1 = 2023211033 LvZiyuan m 60.000000 75.000000 115.000000 115.000000
```

>[!caution]
>**数组**是**不能直接赋值**的，但如果**结构体变量**中的某个成员的数据类型是**数组** 的话，我们是可以把含有**数组**成员的**结构体变量**赋值给另外一个**结构体变量**的。

### '->'运算符

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

// 定义结构体类型
struct student_s{ // struct studentn_s 是结构体类型的名字
	int id;
	char name[25];
	char gender;
	float Politics;
	float English;
	float Math;
	float cs408;
}; //分号是不可省略的

int main(){
	// struct student_s stu; // 结构体类型的变量
	struct student_s stu = {2023211033,"LvZiyuan",'m',60,75,115,115};
	
	// '.'运算符 —— 根据结构体去访问内部的成员
	printf("stu = %d %s %c %f %f %f %f\n",stu.id,stu.name,stu.gender,stu.Politics,stu.English,stu.Math,stu.cs408);
	
	// '='运算符
	struct student_s stu1;
	stu1 = stu;
	printf("stu1 = %d %s %c %f %f %f %f\n",stu1.id,stu1.name,stu1.gender,stu1.Politics,stu1.English,stu1.Math,stu1.cs408);
	
	// 指针
	struct student_s *pstu = &stu; // 可能会存在一个坑！！！
	// '*'运算符的优先级低于'.'运算符
	//(*pstu).id // 这种访问方式过于复杂，因此我们引入'->'运算符
	// '->'运算符 —— 先解引用再访问结构体成员
	//引入'->'运算符后，(*pstu).id 可以改为 pstu -> id
	printf("(*pstu).id = %d,pstu -> id = %d\n",(*pstu).id,pstu -> id);
	
	return 0;
}
```

```c
结果：
stu = 2023211033 LvZiyuan m 60.000000 75.000000 115.000000 115.000000
stu1 = 2023211033 LvZiyuan m 60.000000 75.000000 115.000000 115.000000
(*pstu).id = 2023211033,pstu -> id = 2023211033
```

---
## 15.4 typedef

>[!definieion]
>**typedef(给类型起别名)：** **关键字** `typedef` 允许你从一个现有的类型中创建一个新类型。

```c
#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef int type_t; // 给int起了一个别名叫type_t
```