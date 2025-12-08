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
