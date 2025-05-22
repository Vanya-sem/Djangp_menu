from django import template
from menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag()
def draw_menu(menu_url):
    menu_items = MenuItem.objects.filter(url=menu_url).select_related('parent')
    return mark_safe(_draw_menu(menu_items))


#Во избежание могучего экранирования Джанго, решил сделать вот так
def _draw_menu(menu_items):
    menu_html = '<ul class="tree">'
    for item in menu_items:
        menu_html += '<li><div class="sticky>"</div>'
        if item.url:
            menu_html += f'<a href=/{item.url}>{item.name}</a>'
        elif item.named_url:
            menu_html += f'<a href="/{item.named_url}">{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += _draw_menu(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html

