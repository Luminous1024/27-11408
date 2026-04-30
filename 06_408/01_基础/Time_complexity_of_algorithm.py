import matplotlib.pyplot as plt
import numpy as np
import math

# ================= 1. 解决中文乱码 =================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Heiti SC', 'WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False

# ================= 2. 准备数据 =================
n_values = np.arange(0, 101)

y_factorial = np.array([math.factorial(n) for n in n_values], dtype=float)
y_exp2     = 2.0 ** n_values
y_n2       = n_values ** 2
y_n        = n_values.astype(float)
y_log2     = np.where(n_values > 0, np.log2(n_values), 0.0)
y_one      = np.ones_like(n_values, dtype=float)

# ================= 3. 绘图 =================
plt.figure(figsize=(12, 7))

plt.plot(n_values, y_factorial, label=r'$n!$')
plt.plot(n_values, y_exp2,     label=r'$2^n$')
plt.plot(n_values, y_n2,       label=r'$n^2$')
plt.plot(n_values, y_n,        label=r'$n$')
plt.plot(n_values, y_log2,     label=r'$\log_2 n$')
plt.plot(n_values, y_one,      linestyle='--', label=r'$1$')

# ================= 4. 曲线旁标注（坐标已固定，不改动）=================
plt.text(3.20, 30.0, r'$n!$', fontsize=10, va='center')
plt.text(4.80, 50.0, r'$2^n$', fontsize=10, va='center')
plt.text(7.40, 70.0, r'$n^2$', fontsize=10, va='center')
plt.text(95, min(y_n[95], 95), r'$n$', fontsize=10, va='center')
plt.text(95, min(y_log2[95], 95), r'$\log_2 n$', fontsize=10, va='center')
plt.text(95, min(y_one[95], 95), r'$1$', fontsize=10, va='center')

# ================= 5. 坐标轴与标题（已按要求修改）=================
plt.xlim(0, 100)
plt.ylim(0, 100)

plt.xlabel('n')
plt.ylabel('T(n)（时间开销）')          # ← 修改为 T(n)（时间开销）
plt.title('算法的时间复杂度')            # ← 修改为 算法的时间复杂度
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', fontsize=8)
plt.tight_layout()

# ================= 6. 保存与显示 =================
plt.savefig('growth_0_100_with_labels.png', dpi=150)
plt.show()