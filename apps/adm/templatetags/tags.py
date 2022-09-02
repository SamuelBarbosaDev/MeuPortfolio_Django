from django import template

register = template.Library()

@register.simple_tag
def default_images(condição):
    if condição == 1:
        img = '/static/img/default/images/hero.webp'

    if condição == 2:
        img = '/static/img/default/images/foto_de_perfil.svg'
        
    if condição == 3:
        img = '/static/img/default/images/2.jpg'
    
    if condição == 4:
        img = '/static/img/default/images/depoimentos_imagem.png'
        
    return img 