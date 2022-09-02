from django.contrib import admin
from adm.models import *


# Portfólio.
class PortfólioImagemAdmin(admin.StackedInline):
    model = PortfólioImagem
    extra = 0


@admin.register(Portfólio)
class PortfólioAdmin(admin.ModelAdmin):
    inlines = [PortfólioImagemAdmin]
    list_display = ('titulo', 'categoria', 'data_de_criação')
    list_filter= ('categoria', 'data_de_criação')
    search_fields = ['titulo']


    class Meta:
        model = Portfólio

@admin.register(PortfólioCategoria)
class PortfólioCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)


# Sobre.
# -----SobreHabilidade-----


class SobreHabilidadeAdmin(admin.StackedInline):
    model = SobreHabilidade
    extra = 0


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    inlines = [SobreHabilidadeAdmin,]

    class Meta:
        model = Sobre

# Contato.
# -----SobreDepoimento-----


class ContatoRedeSocialAdmin(admin.StackedInline):
    model = ContatoRedeSocial
    extra = 0


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    inlines = [ContatoRedeSocialAdmin]

    class Meta:
        model = Contato
# ----------------------------------

# FormularioDeContato.
# -----FormularioDeContato-----


@admin.register(FormularioDeContato)
class FormularioDeContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_de_projeto', 'data_de_criação')
    search_fields = ['nome']

# FormularioDeContato.
# -----FormularioDeContato-----


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass

