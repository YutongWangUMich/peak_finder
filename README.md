# Peak Finder

To use: 
1. copy `isotonic_regression_l1_total_order.py` and `peak_finder.py` into your folder
2. do `from peak_finder import peak_finder`
3. OPTION 1, do `peak_finder(y,n_peaks)` where `y` is the signal where you want to find peaks, and `n_peaks` is the desired of the number of peaks
3. OPTION 2, do `peak_finder_auto(y)` where `y` is the signal where you want to find peaks. Peak is automatically selected. There is an option parameter `sensitivity = 0.05` that must be between `0` and `1`. Larger `sensitivity` means that the algorithm will detect more peaks.


Return values:
`S,x,opt = peak_finder(y,n_peaks)`
1. `S` indices of the peaks
2. `x` an approximation to `y` with only peaks at `S`
3. `opt = np.sum(np.abs(x-y))`



```python
from peak_finder import peak_finder, peak_finder_auto
from toy_examples import sin_waves, mountains_and_plateau
import numpy as np
import matplotlib.pyplot as plt
import time
```


```python
y_examples = [sin_waves(n_peaks=1),sin_waves(n_peaks=2),sin_waves(n_peaks=3), mountains_and_plateau()]
y_names = ["1peak", "2peaks","3peaks", "plateau"]
n_peaks_true = [1,2,3,3]
```

## Automatically detect the number of peaks


```python
S_all = []
x_all = []
opt_all = []
start = time.time()

for i,y in enumerate(y_examples):
    S,x,opt = peak_finder_auto(y)
    S_all.append(S)
    x_all.append(x)
    opt_all.append(opt)
end = time.time()
run_time = (end-start)
```


```python
fig, axes = plt.subplots(2, 2)
axes = axes.flatten()
for i,y in enumerate(y_examples):
    x = x_all[i]
    S = S_all[i]
    ax = axes[i]
    ax.plot(y, label='original',linewidth=0.5,zorder=2)
    ax.plot(x, label="smoothed",linewidth=5,zorder=-1,alpha=0.4)


    for j in S:
        ax.axvline(x=j,color='black', linestyle="--", label='peaks')
    if i == 0:
        ax.legend()
fig.suptitle(f"Auto-mode, run time (sec) = {np.round(run_time,2)}")

```




    Text(0.5, 0.98, 'Auto-mode, run time (sec) = 4.53')




    
![png](README_files/README_5_1.png)
    


## Setting the number of peaks manually speed things up


```python
S_all = []
x_all = []
opt_all = []
start = time.time()

for i,y in enumerate(y_examples):
    n_peaks = n_peaks_true[i]
    S,x,opt = peak_finder(y,n_peaks)
    S_all.append(S)
    x_all.append(x)
    opt_all.append(opt)
end = time.time()
run_time = (end-start)
```


```python
fig, axes = plt.subplots(2, 2)
axes = axes.flatten()
for i,y in enumerate(y_examples):
    x = x_all[i]
    S = S_all[i]
    ax = axes[i]
    ax.plot(y, label='original',linewidth=0.5,zorder=2)
    ax.plot(x, label="smoothed",linewidth=5,zorder=-1,alpha=0.4)


    for j in S:
        ax.axvline(x=j,color='black', linestyle="--", label='peaks')
    if i == 0:
        ax.legend()
fig.suptitle(f"Manual-mode, run time (sec) = {np.round(run_time,2)}")
```




    Text(0.5, 0.98, 'Manual-mode, run time (sec) = 1.18')




    
![png](README_files/README_8_1.png)
    

