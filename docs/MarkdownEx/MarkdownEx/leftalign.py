from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re


#居中样式
class LeftInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('p')
        el.set('align', 'left')
        el.text = m.group(2)
        return el, m.start(0), m.end(0)


class LeftExtension(Extension):
    """
    文本排版
    匹配：|-居左文本；|-居中文本-|；居右文本|
    输出：<del>删除</del>
    """

    def extendMarkdown(self, md):
            LEFT_PATTERN = r'^(\|\-)(.*?)$'  # like |-center
            md.inlinePatterns.register(LeftInlineProcessor(LEFT_PATTERN, md), 'left', 180)
    

def makeExtension(**kwargs):
    return LeftExtension(**kwargs)