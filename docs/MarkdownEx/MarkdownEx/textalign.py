
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re

class CenterInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('p')
        el.set('align', 'center')
        el.text = m.group(2)
        return el, m.start(0), m.end(0)


class CenterExtension(Extension):
    """
    文本排版
    匹配：|*居左文本；|*居中文本*|；居右文本*|
    输出：<del>删除</del>
    """

    def extendMarkdown(self, md):
        CENTER_PATTERN = r'^(\|\*)(.*?)(\*\|)$'  # like |*center*|
        md.inlinePatterns.register(CenterInlineProcessor(CENTER_PATTERN, md), 'center', 175)
    
'''

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

class DelInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('del')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class DelExtension(Extension):
    """
    删除文本
    匹配：~~删除~~
    输出：<del>删除</del>
    """

    def extendMarkdown(self, md):
        DEL_PATTERN = r'~(.*?)~'  # like ~~del~~
        md.inlinePatterns.register(DelInlineProcessor(DEL_PATTERN, md), 'del', 175)
'''

def makeExtension(**kwargs):
    return CenterExtension(**kwargs)