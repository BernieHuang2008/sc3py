# sc3py

convert `Scratch 3.0 Script` to `Python Code`!

Compiler Scratch to Python, 
Create more possibilities.

![Screenshot](https://github.com/earthno1/scratch2py/assets/88757735/08d1622c-16b5-4e8c-880f-9a7bf111468c)

# 如何运行 / Quick Start
1. 把`.sb3`的后缀名改为`.zip`，并解压
2. 从压缩包里找到`projects.json`，放到[sc3py/compiler/source/](https://github.com/BernieHuang2008/sc3py/tree/main/sc3py/compiler/source)文件夹下
3. 直接运行[sc3py/compiler/compiler.py](https://github.com/BernieHuang2008/sc3py/blob/main/sc3py/compiler/compiler.py)
4. 查看结果：打开[sc3py/compiler/result/main.py](https://github.com/BernieHuang2008/sc3py/blob/main/sc3py/compiler/result/main.py)文件，查看编译后的代码。该文件夹中的scgame是为了保证不出红线（syntax error）而写的临时库，一点用都没有，`main.py`是目前的唯一成果。