import matplotlib.pyplot as plt
from math import sin
xvals = [[], [], []]
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
            xvals[2].append(4 - alpha)
            if(abs(xnew - xss) < 0.001):
                break
        alpha += 0.001
    start += 0.1
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax.plot(xvals[1], xvals[2],'.', markersize = 1.2, color = 'white', linewidth=0.1)
ax.tick_params(axis='both', colors = 'white')
ax.set_yticks([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
ax.set_yticklabels(['4', '3.5', '3', '2.5', '2', '1.5', '1', '0.5', '0'])
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel('Alpha')
ax.set_ylabel('X')
plt.show()
