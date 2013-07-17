from collective.grok import gs
from sinarngo.pressroom import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.pressroom', 
    title=_('sinarngo.pressroom import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.pressroom.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
