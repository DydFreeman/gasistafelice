"""Receive signals and notify users"""

from django.db import models
from django.utils.translation import ugettext as _

from gasistafelice.gas.models import GAS
from gasistafelice.gas import signals as gas_signals

#class GASOrderNotifications(models.Model):
#
#    gas = models.ForeignKey(GAS)
#    order_mailing_list = models.EmailField()
#    
#-------------------------------------------------------------------------------

def notify_gmo_product_erased(sender, **kwargs):

    gmo = sender
    msg = _("Product %(product)s: has been erased from order %(order)s") % {
            'product' : gmo.product,
            'order' : gmo.order,
    }

    gmo.gasmember.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

def notify_gmo_price_update(sender, **kwargs):

    gmo = sender
    old_price = gmo.ordered_price
    new_price = gmo.ordered_product.order_price
    msg = _("Product %(product)s: updated price from %(old_price)s to %(new_price)s") % {
            'product' : gmo.product,
            'old_price' : old_price,
            'new_price' : new_price,
    }

    gmo.gasmember.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

def notify_gasstock_product_enabled(sender, **kwargs):

    gasstock = sender
    msg = _("Product %(product)s is now available for %(gas)s") % {
            'product' : gasstock.product,
            'gas' : gasstock.gas
    }

    for gm in gasstock.gasmembers:
        #TODO: check for user settings and see if user wants to be notified
        # via messages, mail or both
        gm.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

def notify_gasstock_product_disabled(sender, **kwargs):

    gasstock = sender
    msg = _("Product %(product)s has been disabled for %(gas)s") % {
            'product' : gasstock.product,
            'gas' : gasstock.gas
    }

    for gm in gasstock.gasmembers:
        #TODO: check for user settings and see if user wants to be notified
        # via messages, mail or both
        gm.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

def notify_order_open(sender, **kwargs):

    order = sender
    msg = _('Order related to %(pact)s has been created. Check it at <a href="%(url)s">%(url)s</a>') % {
            'pact' : order.pact,
            'url' : order.get_absolute_url()
    }

    for gm in order.gasmembers:
        #TODO: check for user settings and see if user wants to be notified
        # via messages, mail or both
        gm.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

def notify_order_state_update(sender, **kwargs):

    order = sender
    transition = kwargs['transition']

    if transition.destination == "closed":
        msg = _('Order related to %(pact)s has been closed. Check it at <a href="%(url)s">%(url)s</a>') % {
                'pact' : order.pact,
                'url' : order.get_absolute_url()
        }

        for gm in order.gasmembers:
            #TODO: check for user settings and see if user wants to be notified
            # via messages, mail or both
            gm.person.user.message_set.create(message=msg)

#-------------------------------------------------------------------------------

gas_signals.order_open.connect(notify_order_open)
gas_signals.order_state_update.connect(notify_order_state_update)
gas_signals.gmo_price_update.connect(notify_gmo_price_update)
gas_signals.gmo_product_erased.connect(notify_gmo_product_erased)
gas_signals.gasstock_product_enabled.connect(notify_gasstock_product_enabled)
gas_signals.gasstock_product_disabled.connect(notify_gasstock_product_disabled)


