# import的用法

+ \__init__ .py在早期的python版本中必须存在，在python3.5（大约）之后可以没有，但是推荐使用。
+ import导入的路径必须存在于sys.path中
+ 导入自己写的文件，如果是非运行入口文件（运行入口文件可以使用绝对导入），则需要相对导入。

```
from . import module_name。导入和自己同目录下的模块。
from .package_name import module_name。导入和自己同目录的包的模块。
from .. import module_name。导入上级目录的模块。
from ..package_name import module_name。导入位于上级目录下的包的模块。
当然还可以有更多的.，每多一个点就多往上一层目录
```

+ 运行入口文件也可以使用相对导入。

```python
--Tree
  --m1.py
  --m2.py
  --branch
    --m3.py
    --m4.py
# m1.py
from .Branch import m3
m3.printSelf()

# m2.py
def printSelf():
	print('In m2')
	
# m3.py
from . import m4
def printSelf():
	print('In m3')
# m4.py
def printSelf():
	print('In m4')

```

+ 在Tree目录下直接运行 `python m1.py`会报错，因为`m1.py`中的 **.** 是根据\_\_name\_\__来确定的，直接运行 \_\_name\_\_的值是\_\_main\_\_，正确的做法是进入到Tree所在的目录，，使用`python -m Tree.m1`来运行。

> 执行指令中的-m是为了让Python预先import你要的package或module给你，然后再执行script。即不把m1.py当作运行入口文件，而是也把它当作被导入的模块，这就和非运行入口文件有一样的表现了。

+ 注意，在Tree目录下运行python -m m1是不可以的，会报 ImportError: attempted relative import with no known parent package的错误。因为m1.py中的from .Branch import m3中的. ，解释器并不知道是哪一个package。使用python -m Tree.m1，解释器就知道.对应的是Tree这个package。