from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
import re


#居中样式
class AlignInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        if re.match(r'^(\|\-)(.*?)(\-\|)$',m.group(0)) is not None:
            el = etree.Element('p')
            el.set('align', 'center')
            el.text = m.group(2)
            return el, m.start(0), m.end(0)
        
        elif re.match(r'^(\|\-)(.*?)$',m.group(0)) is not None:
            el = etree.Element('p')
            el.set('align', 'left')
            el.text = m.group(2)
            return el, m.start(0), m.end(0)
        
        elif re.match(r'^(.*?)(\-\|)$',m.group(0)) is not None:
            el = etree.Element('p')
            el.set('align', 'right')
            el.text = m.group(1)
            return el, m.start(0), m.end(0)


class AlignExtension(Extension):
    """
    文本排版
    匹配：|-居左文本；|-居中文本-|；居右文本|
    输出：<p align='center|left|right'>Aligned Text</p>
    """

    def extendMarkdown(self, md):
            CENTER_PATTERN = r'^(\|\-)(.*?)(\-\|)$|^(\|\-)(.*?)$'  # like |-center-|
            md.inlinePatterns.register(AlignInlineProcessor(CENTER_PATTERN, md), 'center', 180)
    

def makeExtension(**kwargs):
    return AlignExtension(**kwargs)

