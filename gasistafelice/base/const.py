from django.utils.translation import ugettext, ugettext_lazy as _

## role-related constants
NOBODY = 'NOBODY'
GAS_MEMBER = 'GAS_MEMBER'
GAS_REFERRER_SUPPLIER = 'GAS_REFERRER_SUPPLIER'
GAS_REFERRER_ORDER = 'GAS_REFERRER_ORDER'
GAS_REFERRER_WITHDRAWAL = 'GAS_REFERRER_WITHDRAWAL'
GAS_REFERRER_DELIVERY = 'GAS_REFERRER_DELIVERY'
GAS_REFERRER_CASH = 'GAS_REFERRER_CASH'
GAS_REFERRER_TECH = 'GAS_REFERRER_TECH'
SUPPLIER_REFERRER = 'SUPPLIER_REFERRER'

ROLES_LIST = [
(NOBODY, _('Nobody')),
(SUPPLIER_REFERRER, _('Supplier referrer')),
(GAS_MEMBER, _('GAS member')),
(GAS_REFERRER_SUPPLIER, _('GAS supplier referrer')),
(GAS_REFERRER_ORDER, _('GAS order referrer')),
(GAS_REFERRER_WITHDRAWAL, _('GAS withdrawal referrer')),
(GAS_REFERRER_DELIVERY, _('GAS delivery referrer')),
(GAS_REFERRER_CASH, _('GAS cash referrer')),
(GAS_REFERRER_TECH, _('GAS technical referrer')),
]

## permission-related constants
VIEW = 'view'
LIST = 'list'
CREATE = 'create'
EDIT = 'edit'
DELETE = 'delete'
ALL = 'all' # catchall

PERMISSIONS_LIST = [
(VIEW, _('View')),
(LIST, _('List')),
(CREATE, _('Create')),
(EDIT, _('Edit')),
(DELETE, _('Delete')),
(ALL, _('All')), # catchall
]


SUPPLIER_FLAVOUR_LIST = [
('COMPANY', _('Company')),
('COOPERATING', _('Cooperating')),
]

MU_CHOICES = [('Km', 'Km')]
ALWAYS_AVAILABLE = 1000000000

CONTACT_CHOICES = [
('PHONE', _('PHONE')),
('EMAIL', _('EMAIL')),
('FAX', _('FAX')),
]