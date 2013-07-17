from five import grok
from plone.directives import dexterity, form
from sinarngo.pressroom.content.pressrelease import IPressRelease

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IPressRelease)
    grok.require('zope2.View')
    grok.template('pressrelease_view')
    grok.name('view')

