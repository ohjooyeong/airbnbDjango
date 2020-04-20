
from django import template
from lists import models as list_models

register = template.Library()

@register.simple_tag(takes_context=True) #takes_context는 context object으로 call해준다
def on_favs(context, room):
    user = context.request.user
    the_list = list_models.List.objects.get_or_none(
        user=user,
        name="My Favorite Houses"
    )
    if the_list is not None:
        return room in the_list.rooms.all()
    return False