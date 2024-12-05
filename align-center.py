from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

# utils/markdown_ext.py
class CenterInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('p')
        el.set('align', 'center')
        return el, m.start(0), m.end(0)


class CenterExtension(Extension):
    """
    删除文本
    匹配：~~删除~~
    输出：<del>删除</del>
    """

    def extendMarkdown(self, md):
        CENTER_PATTERN = r'|*(.*?)*|'  # like ~~del~~
        md.inlinePatterns.register(CenterInlineProcessor(CENTER_PATTERN, md), 'center', 175)
