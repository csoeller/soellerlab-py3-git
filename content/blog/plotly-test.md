Title: A plotly and jupyter notebook test
Date: 2017-11-30 22:03
Status: draft
Slug: blog/plotly-test
Tags: python, pelican, jupyter


```python
import plotly
print plotly.__version__            # version 1.9.4 required
plotly.offline.init_notebook_mode() # run at the start of every notebook
```

>     2.0.8



```python
plotly.offline.iplot({
"data": [{
    "x": [1, 2, 3],
    "y": [4, 2, 5]
}],
"layout": {
    "title": "hello world"
}
}, image='svg')
```


```python
%matplotlib inline

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.rcParams['figure.figsize'] = (12.0, 8.0)
```


```python
f1 = plt.figure(1)
plt.plot(np.arange(100),np.sin(np.arange(100)*2*3.14/20))
```



>      [<matplotlib.lines.Line2D at 0x1112b02d0>] 




![png](/images/blog/plotly-test_3_1.png)



```python
plotly.offline.iplot_mpl(f1)
```



```python

```
