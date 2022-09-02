from adm.models import *
from django.shortcuts import render, get_object_or_404
from adm.forms import ContatoFormulario
from django.core.paginator import Paginator


def portfólio(request):
    try:
        template_name = 'adm/portfólio.html'
        # --------------
        portfólio_condição = request.GET.get('categoria')
        categorias = 2
        if portfólio_condição:
            categorias = PortfólioCategoria.objects.filter(categoria__icontains=portfólio_condição).values()[0]['id']
            portfólio_todas_as_informações_do_backend = Portfólio.objects.filter(categoria__id=categorias).order_by(
            '-data_de_criação')
        else:
            portfólio_todas_as_informações_do_backend = Portfólio.objects.all().order_by('-data_de_criação')

        portfólio_paginator = Paginator(portfólio_todas_as_informações_do_backend, 13)
        portfólio_page = request.GET.get('page')
        portfólio_projeto = portfólio_paginator.get_page(portfólio_page)
        portfólio_categorias = PortfólioCategoria.objects.all()
        # --------------
        contato_todas_as_informações_do_backend = Contato.objects.all().order_by(
            '-data_de_criação')
        contato_informação_mais_recente_do_backend = contato_todas_as_informações_do_backend[
            0]
        contato_redes_sociais = ContatoRedeSocial.objects.filter(
            add_redeSocial=contato_informação_mais_recente_do_backend)
        # --------------
        site_todas_as_informações_do_backend = Site.objects.all().order_by('-data_de_criação')
        site_informação_mais_recente_do_backend = site_todas_as_informações_do_backend[0]

    except IndexError:
        contato_informação_mais_recente_do_backend = None
        contato_redes_sociais = None
        # --------------
        site_informação_mais_recente_do_backend = None

    context = {
        'ativo_p': 'active',
        'portfólio_projeto': portfólio_projeto,
        'portfólio_categorias': portfólio_categorias,
        'portfólio_condição':portfólio_condição,
        'contato': contato_informação_mais_recente_do_backend,
        'contato_redes_sociais': contato_redes_sociais,
        'site': site_informação_mais_recente_do_backend,
    }

    return render(request, template_name=template_name, context=context)


def contato(request):
    try:
        template_name = 'adm/contato.html'
        # --------------
        contato_todas_as_informações_do_backend = Contato.objects.all().order_by(
            '-data_de_criação')
        contato_informação_mais_recente_do_backend = contato_todas_as_informações_do_backend[
            0]
        contato_redes_sociais = ContatoRedeSocial.objects.filter(
            add_redeSocial=contato_informação_mais_recente_do_backend)
        # --------------
        site_todas_as_informações_do_backend = Site.objects.all().order_by('-data_de_criação')
        site_informação_mais_recente_do_backend = site_todas_as_informações_do_backend[0]

    except IndexError:
        contato_informação_mais_recente_do_backend = None
        contato_redes_sociais = None
        # --------------
        site_informação_mais_recente_do_backend = None

    if request.method == "GET":
        form = ContatoFormulario()
    else:
        form = ContatoFormulario(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ContatoFormulario()

    context = {
        'ativo_c': 'active',
        'form': form,
        'contato': contato_informação_mais_recente_do_backend,
        'contato_redes_sociais': contato_redes_sociais,
        'site': site_informação_mais_recente_do_backend,
    }

    return render(request, template_name=template_name, context=context)


def sobre(request):
    template_name = 'adm/sobre.html'
    try:
        # --------------
        sobre_todas_as_informações_do_backend = Sobre.objects.all().order_by('-data_de_criação')
        sobre_informação_mais_recente_do_backend = sobre_todas_as_informações_do_backend[0]
        sobre_habilidades = SobreHabilidade.objects.filter(
            add_habilidade=sobre_informação_mais_recente_do_backend)
        # --------------
        contato_todas_as_informações_do_backend = Contato.objects.all().order_by(
            '-data_de_criação')
        contato_informação_mais_recente_do_backend = contato_todas_as_informações_do_backend[
            0]
        contato_redes_sociais = ContatoRedeSocial.objects.filter(
            add_redeSocial=contato_informação_mais_recente_do_backend)
        # --------------
        portfólio_todas_as_informações_do_backend = Portfólio.objects.all().order_by(
            '-data_de_criação')
        portfólio_paginator = Paginator(
            portfólio_todas_as_informações_do_backend, 3)
        portfólio_page = request.GET.get('page')
        portfólio_projeto = portfólio_paginator.get_page(portfólio_page)
        # --------------
        site_todas_as_informações_do_backend = Site.objects.all().order_by('-data_de_criação')
        site_informação_mais_recente_do_backend = site_todas_as_informações_do_backend[0]

    except IndexError:
        sobre_informação_mais_recente_do_backend = None
        sobre_habilidades = None
        sobre_depoimentos = None
        # --------------
        contato_informação_mais_recente_do_backend = None
        contato_redes_sociais = None
        # --------------
        portfólio_todas_as_informações_do_backend = Portfólio.objects.all().order_by(
            '-data_de_criação')
        portfólio_paginator = Paginator(
            portfólio_todas_as_informações_do_backend, 3)
        portfólio_page = request.GET.get('page')
        portfólio_projeto = portfólio_paginator.get_page(portfólio_page)
        # --------------
        site_informação_mais_recente_do_backend = None

    context = {
        'ativo_s': 'active',
        'sobre': sobre_informação_mais_recente_do_backend,
        'sobre_habilidades': sobre_habilidades,
        'contato': contato_informação_mais_recente_do_backend,
        'contato_redes_sociais': contato_redes_sociais,
        'portfólio_projeto': portfólio_projeto,
        'portfólio_todas_as_informações_do_backend': portfólio_todas_as_informações_do_backend,
        'site': site_informação_mais_recente_do_backend,
    }

    return render(request, template_name=template_name, context=context)


def projeto(request, id):
    try:
        template_name = 'adm/projeto.html'
        # --------------
        portfólio_projetos = get_object_or_404(Portfólio, pk=id)
        portfólio_imagens = PortfólioImagem.objects.filter(
            add_imagem=portfólio_projetos)
        # --------------
        contato_todas_as_informações_do_backend = Contato.objects.all().order_by(
            '-data_de_criação')
        contato_informação_mais_recente_do_backend = contato_todas_as_informações_do_backend[
            0]
        contato_redes_sociais = ContatoRedeSocial.objects.filter(
            add_redeSocial=contato_informação_mais_recente_do_backend)
        # --------------
        site_todas_as_informações_do_backend = Site.objects.all().order_by('-data_de_criação')
        site_informação_mais_recente_do_backend = site_todas_as_informações_do_backend[0]

    except IndexError:
        contato_informação_mais_recente_do_backend = None
        contato_redes_sociais = None
        # --------------
        site_informação_mais_recente_do_backend = None

    context = {
        'portfólio_projetos': portfólio_projetos,
        'portfólio_imagens': portfólio_imagens,
        'contato': contato_informação_mais_recente_do_backend,
        'contato_redes_sociais': contato_redes_sociais,
        'site': site_informação_mais_recente_do_backend,
    }

    return render(request, template_name=template_name, context=context)
