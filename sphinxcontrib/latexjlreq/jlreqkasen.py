#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class jlreqkasen(nodes.General, nodes.Element, nodes.Inline):
    pass


def visit_kasen(self, node):
    self.body.append(self.starttag(node, 'span', '', style='text-decoration: underline;'))
    self.body.append(node['base'])
    self.body.append('</span>')
    raise nodes.SkipNode


def visit_jlreqkasen(self, node):
    self.body.append('\\kasen{' + node['base'])
    self.body.append('}')
    raise nodes.SkipNode


def jlreqkasen_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for kasentag."""
    text = utils.unescape(text)
    node = jlreqkasen(rawtext, base=text, text=text)
    set_role_source_info(inliner, lineno, node)
    return [node], []


def setup(app):
    app.add_role('kasen', jlreqkasen_role)
    app.add_node(jlreqkasen, html=(visit_kasen, None), latex=(visit_jlreqkasen, None))
