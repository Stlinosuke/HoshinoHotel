from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


# 居中样式
class CenterInlineProcessor(InlineProcessor):
    def __init__(self, pattern, md):
        super().__init__(pattern, md)  # 调用父类初始化

    def handleMatch(self, m, data):
        el = etree.Element('p')  # 创建一个 HTML <p> 元素
        el.set('align', 'center')  # 设置居中对齐
        content = m.group(0)[2:-2]  # 去掉首尾的 `|-` 和 `-|` 标记，只取内容
        el.text = None  # 清空默认文本内容，改用子元素
        for line in content.split('\n'):
            el.append(etree.Element('span'))  # 创建一个子元素 span
            el[-1].text = line  # 添加文本内容
            el.append(etree.Element('br'))  # 添加换行符
        el.remove(el[-1])  # 移除最后多余的换行
        return el, m.start(0), m.end(0)  # 返回 HTML 元素和匹配范围


class CenterExtension(Extension):
    """
    文本排版扩展
    匹配：|-居中内容-|
    输出：<p align="center">居中内容</p>
    """

    def extendMarkdown(self, md):
        # 居中的匹配正则
        CENTER_PATTERN = r'\|-(?:(?!\|-|-\|)[^\|-]|\n)*-\|'  # 匹配 |-内容-| 格式
        md.inlinePatterns.register(CenterInlineProcessor(CENTER_PATTERN, md), 'center', 180)


def makeExtension(**kwargs):
    return CenterExtension(**kwargs)

