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
__, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
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
