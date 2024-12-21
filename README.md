# dumbbell

```python
import matplotlib.pyplot as plt
from dumbbell import lollipop

x = [1, 2, 3, 4, 5]
y = [10, 50, 27, 48, 1]

fig, ax = plt.subplots()
lollipop(x=x, y=y, c=y)
plt.show()
```

![](img/quickstart.png)
