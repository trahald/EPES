import matplotlib.pyplot as plt

from pylab import genfromtxt

import seaborn as sns
sns.set()
#sns.set_context('talk')
sns.set_context("notebook", font_scale=1.1, rc={"lines.linewidth": 1.5})

# Sources: http://www.randalolson.com/2014/06/28/how-to-make
#            -beautiful-data-visualizations-in-python-with-matplotlib/
# These are the "Tableau 20" colors as RGB.   
tableau20=[(31, 119, 180),  (174, 199, 232), (255, 127, 14),  (255, 187, 120),    
            (44, 160, 44),   (152, 223, 138), (214, 39, 40),   (255, 152, 150),    
            (148, 103, 189), (197, 176, 213), (140, 86, 75),   (196, 156, 148),    
            (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
            (188, 189, 34),  (219, 219, 141), (23, 190, 207),  (158, 218, 229)]
# Scale the RGB values to the [0, 1] range, which is the format matplotlib
# accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.) 

plot_data, labels, colors = [], [], []



plot_data.append(genfromtxt("coh_0.7_300.txt", skip_header=2))
labels.append(r'$\sigma$=0.7')
colors.append(tableau20[8])


plot_data.append(genfromtxt("coh_0.8_300.txt", skip_header=2))
labels.append(r'$\sigma$=0.8')
colors.append(tableau20[10])

plot_data.append(genfromtxt("coh.txt", skip_header=2))
labels.append(r'$\sigma$=0.2')
colors.append(tableau20[10])

fig = plt.figure()

nr_plots = len(plot_data)
for i in [0]:
    plt.errorbar(plot_data[i][:,0], plot_data[i][:,1], plot_data[i][:,2],
                label = labels[i], color = colors[i]
            )   
for i in [1]:
    plt.errorbar(plot_data[i][:,0]/10, plot_data[i][:,1], plot_data[i][:,2],
                label = labels[i], color = colors[i]
            ) 
for i in [2]:
    plt.errorbar(plot_data[i][:,0], plot_data[i][:,1], plot_data[i][:,2],
                label = labels[i], color = colors[i]
            ) 

plt.legend(loc="upper left")#.set_draggable(True)
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Formating:
#plt.xlim(0,1.1)
#plt.ylim(0,1.1)

#plt.xlabel(r'Edge density ($t$)')
#plt.ylabel(r'$C_{max}/N$')

plt.xlabel(r'Temporal steps')
plt.ylabel(r'Phase coherence: $r$')

plt.gcf().subplots_adjust(bottom=0.15)
plt.show()