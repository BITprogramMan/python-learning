一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。

而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。

这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。

```python
class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print 'hello', name
    def foo2(self, name):
        print 'hello', name
    @classmethod
    def foo3(cls, name):
        print 'hello', name
```

首先定义一个类A，类A中有三个函数，foo1为静态函数，用@staticmethod装饰器装饰，这种方法与类有某种关系但不需要使用到实例或者类来参与。如下两种方法都可以正常输出，也就是说既可以作为类的方法使用，也可以作为类的实例的方法使用。

```python
a = A()
a.foo1('mamq') # 输出: hello mamq
A.foo1('mamq')# 输出: hello mamq
```

foo2为正常的函数，是类的实例的函数，只能通过a调用。foo3为类函数，cls作为第一个参数用来表示类本身. 在类方法中用到，类方法是只与类本身有关而与实例无关的方法。如下两种方法都可以正常输出。

```python
a.foo3('mamq') # 输出: hello mamq
A.foo3('mamq') # 输出: hello mamq
```

但是通过例子发现staticmethod与classmethod的使用方法和输出结果相同，再看看这两种方法的区别。

> 既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
> 从它们的使用上来看,
> @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
> @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。
> 如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
> 而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。

也就是说在classmethod中可以调用类中定义的其他方法、类的属性，但staticmethod只能通过A.a调用类的属性，但无法通过在该函数内部调用A.foo2()。修改上面的代码加以说明：

```python
class A(object):
    a = 'a'
    @staticmethod
    def foo1(name):
        print 'hello', name
        print A.a # 正常
        print A.foo2('mamq') # 报错: unbound method foo2() must be called with A instance as first argument (got str instance instead)
    def foo2(self, name):
        print 'hello', name
    @classmethod
    def foo3(cls, name):
        print 'hello', name
        print A.a
        print cls().foo2(name)
```

