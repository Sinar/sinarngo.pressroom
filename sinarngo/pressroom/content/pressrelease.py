from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent

from sinarngo.pressroom import MessageFactory as _


# Interface class; used to define content-type schema.

class IPressRelease(form.Schema, IImageScaleTraversable):
    """
    Press Release
    """
    title = schema.TextLine(title=u'Headline', 
                         )

    subtitle = schema.TextLine(title=u'Subheadline', 
                         required=False)

    description = schema.Text(title=u'Description',
                                  description=u'Brief description '
                                  'of Press Release. Used in listings.',
                                  required=False,
                                  )

    location = schema.TextLine(title=u'Location', 
                         description=u'eg. Town, Country',
                         )

    press_release = RichText(
                title=_(u"Press release content"),
                required=False,
            ) 
