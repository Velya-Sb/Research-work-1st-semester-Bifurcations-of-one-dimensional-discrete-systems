import matplotlib.pyplot as plt
xvals = [[], [], []]
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
        xvals[2].append(2 - r)
        if(abs(xnew - xss) < 0.001):
            break
    r += 0.001
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax.plot(xvals[1], xvals[2],'.', markersize = 1.2, color = 'white', linewidth=0.1)
ax.tick_params(axis='both', colors = 'white')
ax.set_yticks([0, 0.5, 1, 1.5, 2])
ax.set_yticklabels(['2', '1.5', '1', '0.5', '0'])
#ax.set_xticks([1, 1.5, 2])
#ax.set_yticklabels(['2', '1.5', '1'])
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.set_xlabel('X')
ax.set_ylabel('r')
plt.show()
