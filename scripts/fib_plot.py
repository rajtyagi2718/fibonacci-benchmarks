import matplotlib.pyplot as plt

from fib.fib import fibs


names = list(fibs.keys())


tableau20 = [(r / 255, g / 255, b / 255) for r,g,b in (
    (31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
    (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229))]    

colors = {'recursive' : 0,
          'memoized' : 4,
          'iterative' : 6,
          'closed' : 8,
          'recursive++' : 1,
          'memoized++' : 5,
          'iterative++' : 7,
}
for name, i in colors.items():
    colors[name] = tableau20[i]


time_stops = {'recursive' : 5,
              'memoized' : 11,
              'iterative' : 13,
              'closed' : 11,
              'recursive++' : 9,
              'memoized++' : 17,
              'iterative++' : 16,
}

mem_stops = {'recursive' : 6,
             'memoized' : 8,
             'iterative' : 17,
             'closed' : 11,
             'recursive++' : 9,
             'memoized++' : 16,
             'iterative++' : 16,
}


def data(file):
    nums = {}
    data = {}
    try:
        with open(file, 'r') as f:
            for line in f:
                name, n, time = line.split()
                nums[name] = nums.get(name, []) + [n]
                data[name] = data.get(name, []) + [float(time)]    
    except FileNotFoundError:
        print('%s file not found.' % file)
    return nums, data

def trim(nums, data, stops):
    for name, stop in stops.items():
        del nums[name][stops[name]:] 
        del data[name][stops[name]:] 

def plot(title, nums, data, yoffset):
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=9.5)
    plt.figure(figsize=(10, 5))
    ax = plt.subplot(111)    
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)    
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)  
    ax.tick_params(axis=u'both', which=u'both',length=0)
    plt.title(title, fontsize=16)

    for name in names:
        plt.plot(nums[name], data[name], color=colors[name],
                 linestyle='-', marker='o')
        plt.annotate(name, (nums[name][-1], data[name][-1] + yoffset),
                     color=colors[name], fontsize=9.5)

    plt.grid(axis='y')
    plt.show()


def plot_times():
    print("plotting execution time")
    nums, times = data('data/time_data.txt')
    trim(nums, times, time_stops)
    plot('Execution time of nth Fibionacci algorithms (\u03BCs)',
         nums, times, 15)

def plot_mems():
    print("plotting memory allocation")
    nums, mems = data('data/mem_data.txt')
    trim(nums, mems, mem_stops)
    for name in names:
        mems[name] = [x / 1000 for x in mems[name]]
    plot('Memory allocation of nth Fibionacci algorithms (KiB)', 
         nums, mems, 1)


if __name__ == '__main__':
    plot_times()
    plot_mems()
