# !/usr/bin/env python
# -*- coding:utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages

setup(
    # 指定项目名称，我们在后期打包时，这就是打包的包名称，当然打包时的名称可能还会包含下面的版本号哟~
    name='MarkdownEx',
    # 指定版本号
    version='1.0.0',
    # 这是对当前项目的一个描述
    description='Custom markdown extension for mkdocs Material',
    # 作者是谁，指的是此项目开发的人，这里就写你自己的名字即可
    author='Stlinosuke',
    # 作者的邮箱
    author_email='lhwdsj123@foxmail.com',
    # 写上项目的地址，比如你开源的地址开源写博客地址，也开源写GitHub地址，自定义的官网地址等等。
    url='https://Stlinosuke.github.io',
    # 指定包名，即你需要打包的包名称，要实际在你本地存在哟，它会将指定包名下的所有"*.py"文件进行打包哟，但不会递归去拷贝所有的子包内容。
    # 综上所述，我们如果想要把一个包的所有"*.py"文件进行打包，应该在packages列表写下所有包的层级关系哟~这样就开源将指定包路径的所有".py"文件进行打包!
    # 比如对于包devops，其包含2个子文件夹dev和ops，里面分别有需要打包的.py，那么就这么写
    # packages=['devops', "devops.dev", "devops.ops"],
    # packages= find_packages(exclude=['test']),
    py_modules=['MarkdownEx.textcolor','MarkdownEx.centeralign','MarkdownEx.leftalign','MarkdownEx.rightalign','MarkdownEx.marktext','MarkdownEx.delins'],
    license='MIT',
    zip_safe=False)
