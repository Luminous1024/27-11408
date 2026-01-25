---
tags:
  - 408_计算机学科专业基础
创建时间: 2026-01-11T16:44:00
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
				- 第二类参数：& + 变量名 —— 用来说明存放数据的地址（记得使用&运算符）
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
		*位运算符
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

- [0] %（取余运算符）的操作数必须是整数

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

><font color="#add8e6">注意：</font>$$
'<' \text{的优先级高于} '==' \text{，所以要先做<运算，再做==运算}
$$

- [3] 判断大小的运算符的优先级高于判断相等的运算符，相同优先级按照从左往右的顺序 —— 结合性
---
[[2026-01-26]]
## 6.3 逻辑运算符
