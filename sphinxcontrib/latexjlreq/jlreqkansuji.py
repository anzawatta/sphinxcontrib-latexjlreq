#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title, set_role_source_info


class kansuji(nodes.General, nodes.Element, nodes.Inline):
    pass


def visit_kansuji(self, node):

    self.body.append(node['base'])
    raise nodes.SkipNode


def visit_latexkansuji(self, node):

    self.body.append('\kansuji ')
    self.body.append(node['base'])
    raise nodes.SkipNode


def kansuji_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """Role for kansujitag."""
    text = utils.unescape(text)
    node = kansuji(rawtext, base=text, text=text)
    set_role_source_info(inliner, lineno, node)
    return [node], []

def setup(app):
    app.add_node(kansuji, html=(visit_kansuji, None), latex=(visit_latexkansuji, None))
    app.add_role('kansuji', kansuji_role)
