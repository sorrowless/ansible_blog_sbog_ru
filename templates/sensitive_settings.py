#!/usr/bin/env python
# -*- coding: utf-8 -*- #
AUTHOR = u'Stan'
SITENAME = u'OpsBlog'

TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = u'en'

# Additional menu items
MENUITEMS = (
    ('Categories', '/meta/categories.html'),
    ('Tags', '/meta/tags.html'),
    ('About', 'https://{{ mainsite_hostname }}'),
)

# Ya.Metrika
YANDEX_METRYKA = {{ ya_metrika }}

SITEURL = '{{ blog_hostname }}'
