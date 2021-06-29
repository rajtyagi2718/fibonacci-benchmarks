import matplotlib.pyplot as plt
from fib_time import nums, times

"""
try:
    with open('data.txt', 'r') as f:
        
except FileNotFoundError:
    print('data.txt file not found.')
"""

tableau20 = [(r / 255, g / 255, b / 255) for r,g,b in (
    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229))]    

names = list(nums.keys())
colors = {name:color for name,color in 
          zip(names, (tableau20[i] for  i in (0, 4, 6, 8, 1, 5)))}
  
plt.figure(figsize=(8, 6))
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)  
ax.tick_params(axis=u'both', which=u'both',length=0)

plt.title('Execution time of nth Fibionacci algorithms (\u03BCs)', fontsize=14)

for name in names:
    plt.plot([str(x) for x in nums[name]], times[name], color=colors[name],
             linestyle='-', marker='o')
    plt.annotate(name, (str(nums[name][-1]), times[name][-1] + 10),
                 color=colors[name])
plt.grid(axis='y')
plt.show()
