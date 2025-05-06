# 数学

###### prerequisites

```
高中数学
```

### 单变量微积分

###### 变化率

> 目标： 1. 什么是导数  2. 如何计算导数?

```
所有函数都能计算导数？
NO:绝大多数可以,部分不行
```

$$
并非所有函数都有导数:\\ 
对于点/点集合的情况:\\
	1.不连续的函数点 不可导\\
	2.尖点不可导\\
	3.垂直切线不可导\\
	4.分段函数分界点\\\\
对于特殊函数:
	f(x)= x \sin{\frac{1}{x}}
$$

- Geometric Interpretation 几何意义
  - 找出 y= f(x) 在某点P (x,y)处的切线


​		如何使用计算机计算出某个点的切线?
$$
割线方程: y - y_0 = m (x-x_0) \ \ \ at  \ \  P(x,y) \\ 切线: x \rightarrow x_0 处的割线
\\ 切线的斜率 m = f'(x_0)
$$



>  切线 = PQ 当Q  无限趋于 P 处的割线( P 是固定的)

- eg: f(x)= 1/x

$$
x_0 处导数 = f'(x_0) = x_0处切线的斜率 = x_0 处 割线极限= \lim_{\Delta_X \rightarrow0} \frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\\ 
= \lim_{\Delta x \rightarrow 0 } \frac{1}{\Delta x} (\frac{1}{x_0+\Delta x} - \frac{1}{x_0}) \\ = \lim_{\Delta x \rightarrow 0 } \frac{1}{\Delta x} (\frac{x_0-x_0-\Delta x}{x_0^2+\Delta x \times x_0})\\ = \lim_{\Delta x \rightarrow 0 } \frac{1}{\Delta x} \frac{-\Delta x}{x^2 + \Delta x \times x} \\ = \lim_{\Delta x \rightarrow 0 }  \frac{-1}{x_0^2 + \Delta x \times x_0} \\ = \lim_{\Delta x \rightarrow 0 } \frac{-1}{x_0^2}\\ \\ f'(x_0) = - \frac{1}{x_0^2}
$$

- 计算 y= 1/x 任一点P处切线 与x，y轴围成的面积大小

$$
1. 求出切线 y-y_0 = k(x-x_0) [点斜式]\\
2. 求出切线与X轴、Y轴截距 A,B\\
3. 面积等于 1/2 * (A + B)\\

ans: X - 1/2\\
$$

$$
1. find \  x-intercept \\
2. find \ y-intercept \\
3. 
$$

$$
f' = \frac{df}{dx} = \frac{dy}{dx} = \frac{d}{dx} f = \frac{d}{dx} y
$$

- 计算 f(x ) = x**n 的导数

$$
\frac{d}{dx} y = \lim_{\Delta x \rightarrow 0} \frac {f(x + \Delta x ) - f(x)}{\Delta x}
\\= 
$$

多项式定理 binomia theorem 
$$
(x + \Delta x)^n = (x+\Delta x) (x+\Delta x) (x+\Delta x) .. \\ 
= x^n + n x^{n-1}x + ... \\
= x^n + n x^{n-1}x + Junk \\ 
$$

$$
导数= \lim_{\Delta x\rightarrow 0} nx^{n-1}
$$

- 拓展  求  x**3 + 5 x\*\*10 的导数

$$
导数 = \frac{d}{dx} (x^3) +  \frac{d}{dx}  (5 x^2)
$$



###### 极限

