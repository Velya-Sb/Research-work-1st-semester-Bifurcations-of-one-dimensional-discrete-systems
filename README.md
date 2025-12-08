# Research-work-1st-semester-Bifurcations-of-one-dimensional-discrete-systems
#Code for logistic map:
```python
import matplotlib.pyplot as plt
xvals = [[], [], []]
beta = 0.0
endd = 4.0

while(endd > beta):
    xold = 0.5
    for i in range(1, 5000):
        xnew = (xold - xold*xold) * beta
        xold = xnew
    xss = xnew
    for i in range(1, 10000):
        xnew = ((xold - xold*xold) * beta)
        xold = xnew
        xvals[0].append(beta)
        xvals[1].append(xnew)
        xvals[2].append(4 - beta)
        if(abs(xnew - xss) < 0.001):
            break
    beta += 0.001
#plt.plot(xvals[0], xvals[1], 'black.', ms = 1)
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
#Первая версия графика
#ax.plot(xvals[0], xvals[1],'.', markersize = 1.2, color = 'white', linewidth=0.1)
#ax.tick_params(axis='both', colors = 'white')
#ax.spines['bottom'].set_color('white')
#ax.spines['top'].set_color('white')
#ax.spines['left'].set_color('white')
#ax.spines['right'].set_color('white')
#ax.xaxis.label.set_color('white')
#ax.yaxis.label.set_color('white')
#ax.set_xlabel('Beta')
#ax.set_ylabel('X')

ax.plot(xvals[1], xvals[2],'.', markersize = 1.2, color = [0.2,0.2,1], linewidth=0.1)
ax.tick_params(axis='both', colors = 'white')
ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
ax.set_yticklabels(['4', '3.5', '3', '2.5', '2', '1.5', '1', '0.5', '0'])
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel('X')
ax.set_ylabel('Beta')
plt.show()
    #plot(xvals(1:), xvals(2:), '.', 'LineWidth',.1,'MarkerSize', 1.2, 'Color', [1,1,1])
    #set(gca, 'color', 'k', 'xcolor', 'w', 'ycolor', 'w')
    #set(gcf, 'color', 'k')
```
#Code for PLL
```python
import matplotlib.pyplot as plt
from math import sin
xvals = [[], []]
alpha = 0.0
endd = 4.0
start = -3.0
while(start < 3.0):
    if(start == 0):
        continue
    alpha = 0.0
    while(endd > alpha):
        xold = start
        for i in range(1, 1000):
            xnew = xold - alpha*sin(xold)
            xold = xnew
        xss = xnew
        for i in range(1, 1000):
            xnew = xold - alpha*sin(xold)
            xold = xnew
            xvals[0].append(alpha)
            xvals[1].append(xnew)
            if(abs(xnew - xss) < 0.001):
                break
        alpha += 0.001
    start += 0.1
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax.plot(xvals[0], xvals[1],'.', markersize = 1.2, color = 'white', linewidth=0.1)
ax.tick_params(axis='both', colors = 'white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel('Alpha')
ax.set_ylabel('X')
plt.show()
```
#Code for Tent map
```python
import matplotlib.pyplot as plt
xvals = [[], []]
r = 1.0
endd = 2.0

while(endd > r):
    xold = 0.5
    for i in range(1, 1000):
        if(0 <= xold and xold <= 0.5):
            xnew = r * xold
        elif(0.5 < xold <= 1):
            xnew = r * (1 - xold)
        xold = xnew
    xss = xnew
    for i in range(1, 2000):
        if(0 <= xold and xold <= 0.5):
            xnew = r * xold
        elif(0.5 < xold <= 1):
            xnew = r * (1 - xold)
        xold = xnew
        xvals[0].append(r)
        xvals[1].append(xnew)
        if(abs(xnew - xss) < 0.001):
            break
    r += 0.001
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax.plot(xvals[0], xvals[1],'.', markersize = 1.2, color = 'white', linewidth=0.1)
ax.tick_params(axis='both', colors = 'white')
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel('r')
ax.set_ylabel('X')
plt.show()
```
