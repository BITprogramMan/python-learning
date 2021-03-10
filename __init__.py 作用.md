## Python __init__.py 作用详解

[TOC]

+ **\__init__.py**该文件的作用就是相当于把自身整个文件夹当作一个包来管理，每当有外部import的时候，就会自动执行里面的函数

### \__init__.py的作用

#### 标识该目录是一个python的模块包（module package）

如果你是使用python的相关IDE来进行开发，那么如果目录中存在该文件，该目录就会被识别为 module package 。

#### 简化模块导入操作

假设我们的模块包的目录结构如下：

```python
.
└── mypackage
    ├── subpackage_1
    │   ├── test11.py
    │   └── test12.py
    ├── subpackage_2
    │   ├── test21.py
    │   └── test22.py
    └── subpackage_3
        ├── test31.py
        └── test32.py
```

如果我们使用最直接的导入方式，将整个文件拷贝到工程目录下，然后直接导入：

```python
from mypackage.subpackage_1 import test11
from mypackage.subpackage_1 import test12
from mypackage.subpackage_2 import test21
from mypackage.subpackage_2 import test22
from mypackage.subpackage_3 import test31
from mypackage.subpackage_3 import test32
```

这样的话，看起来就会很麻烦，查找的时候也会麻烦，此时`__init__.py`就起到了简化的作用。

实际上，如果目录中包含了 __init__.py 时，当用 import 导入该目录时，会执行 __init__.py 里面的代码。我们在mypackage目录下增加一个 __ init __.py 文件来做一个实验:

```python
.
└── mypackage
    ├── __init__.py
    ├── subpackage_1
    │   ├── test11.py
    │   └── test12.py
    ├── subpackage_2
    │   ├── test21.py
    │   └── test22.py
    └── subpackage_3
        ├── test31.py
        └── test32.py
 

#####__init.py__####
print("You have imported mypackage")
```

```
import mypackage
You have imported mypackage
```

如果\__init__.py文件内容为以下：

```
from subpackage_1 import test11
```

则会报错：

```
import mypackage
#################
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/taopeng/Workspace/Test/mypackage/__init__.py", line 2, in <module>
    from subpackage_1 import test11
ImportError: No module named 'subpackage_1'
```

原来，在我们执行import时，当前目录是不会变的（就算是执行子目录的文件），还是需要完整的包名。

```
from mypackage.subpackage_1 import test11
```

综上，我们可以在init.py 指定默认需要导入的模块

#### 偷懒的导入方法

有时候我们在做导入时会偷懒，将包中的所有内容导入

```
from mypackage import *
```

这是怎么实现的呢？ \_\__all__变量就是干这个工作的。\_\__all__ 关联了一个模块列表，当执行 `from xx import *` 时，就会导入列表中的模块。我们将 \_\__init__.py 修改为 :

```
__all__ = ['subpackage_1', 'subpackage_2']
```

```
>>> from mypackage import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'subpackage_1', 'subpackage_2']
>>> 
>>> dir(subpackage_1)
['__doc__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

该例子中的导入等价于:from mypackage import subpackage_1, subpackage_2。因此，导入操作会继续查找 subpackage_1 和 subpackage_2 中的 \__init__.py 并执行。（但是此时不会执行 import *）。

我们在 subpackage_1 下添加 \__init__.py 文件:

```
__all__ = ['test11', 'test12']
# 默认只导入test11
from mypackage.subpackage_1 import test11
```

```
>>> from mypackage import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'subpackage_1', 'subpackage_2']
>>> 
>>> dir(subpackage_1)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'test11']
```

```
>>> from mypackage.subpackage_1 import *
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'test11', 'test12']
```


