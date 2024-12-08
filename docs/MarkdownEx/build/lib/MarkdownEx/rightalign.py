from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re


#居中样式
class RightInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('p')
        el.set('align', 'right')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class RightExtension(Extension):
    """
    文本排版
    匹配：|-居左文本；|-居中文本-|；居右文本|
    输出：<del>删除</del>
    """

    def extendMarkdown(self, md):
            RIGHT_PATTERN = r'^(.*?)(\-\|)$'  # like center-|
            md.inlinePatterns.register(RightInlineProcessor(RIGHT_PATTERN, md), 'right', 180)
    

def makeExtension(**kwargs):
    return RightExtension(**kwargs)