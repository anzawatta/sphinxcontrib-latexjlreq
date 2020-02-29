sphinxcontrib-latexjlreq
========================

This is a sphinx extension to use latex comands for jlreq class.

- ruby
- kenten
- kansuji
- kasen

Setting
=======

Install
-------

.. code:: none

   > pip install git+https://github.com/anzawatta/sphinxcontrib-latexjlreq.git

Configure Sphinx
----------------

To enable this extension, add ``sphinxcontrib.latexjlreq`` module to extensions option at `conf.py`.

.. code:: python

   extensions = [
      'sphinxcontrib.latexjlreq',
   ]


Usage
=====

ruby
----

.. code:: none

   ごん :ruby:`狐<ぎつね>` という

.. image:: sample/ruby.jpg

Output ``\ruby[g]{}`` to .tex file.

To enable this role, add `pxrubrica <https://github.com/zr-tex8r/PXrubrica>`_ package at `latex.tex_t` .

This role was inspired by `sphinxcontrib-textstyle <https://bitbucket.org/r_rudi/sphinxcontrib-textstyle>`_ .

kenten
------

.. code:: none

   :kenten:`しだ` の一ぱい

.. image:: sample/kenten.jpg

Output ``\kenten[s]{}`` to .tex file.

To enable this role, add `pxrubrica <https://github.com/zr-tex8r/PXrubrica>`_ package at `latex.tex_t` .

kansuji
-------

.. code:: none

   :kansuji:`1232` （昭和 :kansuji:`7` ）年に

.. image:: sample/kansuji.jpg

Output ``\kansuji`` to .tex file.

kasen
-----

.. code:: none

   :kasen:`とんがらし` をむしりとって

.. image:: sample/kasen.jpg

Output ``\kasen{}`` to .tex file.

To enable this role, add `plext` package at `latex.tex_t` .

These roles could export html tag.


Repository
==========
https://github.com/anzawatta/sphinxcontrib-latexjlreq
