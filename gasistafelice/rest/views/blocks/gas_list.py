from django.utils.translation import ugettext as _, ugettext_lazy as _lazy
from django.core import urlresolvers

from gasistafelice.rest.views.blocks.base import BlockWithList, ResourceBlockAction
from gasistafelice.auth import CREATE
from gasistafelice.gas.models import GAS

#------------------------------------------------------------------------------#
#                                                                              #
#------------------------------------------------------------------------------#

class Block(BlockWithList):
    """Render GAS list block with the ability to create a new GAS"""

    BLOCK_NAME = "gas_list"
    BLOCK_DESCRIPTION = _("GAS")
    BLOCK_VALID_RESOURCE_TYPES = ["site", "supplier", "user"] 

    def _get_resource_list(self, request):
        return request.resource.gas_list

    def _get_user_actions(self, request):

        user_actions = []

        if request.user.has_perm(CREATE, obj=GAS):
            user_actions.append( 
                ResourceBlockAction( 
                    block_name = self.BLOCK_NAME,
                    resource = request.resource,
                    name=CREATE, verbose_name=_("Add GAS"), 
                    url=urlresolvers.reverse('admin:gas_gas_add')
                )
            )

        return user_actions
        
    def _get_add_form_class(self):
        raise NotImplementedError("The add form page in use now is the admin interface page.")

    #------------------------------------------------------------------------------#    
    #                                                                              #     
    #------------------------------------------------------------------------------#

# Unuseful code below        

# TODO fero CHECK
#        elif args == "new_note":
#            return self.add_new_note(request, resource_type, resource_id)
#        elif args == "remove_note":
#            return self.remove_note(request, resource_type, resource_id)

#    #------------------------------------------------------------------------------#    
#    #                                                                              #     
#    #------------------------------------------------------------------------------#
#            
#    def remove_note(self, request, resource_type, resource_id):
#        
#        resource = request.resource
#        
#        note_id = request.REQUEST.get('note_id')
#        
#        note = Comment.objects.get(id=note_id)
#        note.delete()
#
#        return HttpResponse('<div id="response" resource_type="%s" resource_id="%s" class="success">ok</div>' % (resource.resource_type, resource.id))
        