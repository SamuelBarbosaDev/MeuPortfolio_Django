import os
import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone


FORMA_DE_CONTATO_CHOICE = (
    ('Em', 'E-mail'),
    ('Tf', 'Telefone'),
    ('Wp', 'Whatsapp'),
    ('Tg', 'Telegram'),
)

QUAL_O_SEU_ORÇAMENTO_CHOICE = (
    ('0-1', '0 - 1.000'),
    ('1-5', '1.000 - 5.000'),
    ('5-a', '5.000 - acima'),
)

REDES_SOCIAIS = (
    ('twitter', 'twitter'),
    ('instagram', 'instagram'),
    ('whatsapp', 'whatsapp'),
    ('telegram', 'telegram'),
    ('behance', 'behance'),
    ('twitch', 'twitch'),
    ('github', 'github'),
    ('linkedin', 'linkedin'),
    ('reddit', 'reddit'),
    ('diagram-2-fill', 'diagram-2-fill'),
)


class FormularioDeContato(models.Model):
    nome = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        blank=True,
        null=True,
    )

    telefone = models.CharField(
        max_length=11,
    )

    forma_de_contato_preferencial = models.CharField(
        max_length=20,
        choices=FORMA_DE_CONTATO_CHOICE,
    )

    tipo_de_projeto = models.CharField(
        max_length=30,
    )

    qual_o_seu_orçamento = models.CharField(
        max_length=20,
        choices=QUAL_O_SEU_ORÇAMENTO_CHOICE,
        blank=True,
        null=True,
    )

    descrição_do_projeto = models.TextField(
        max_length=5000,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    @admin.display(
        boolean=True,
        ordering='data_de_criação',
        description='Data de criação',
    )
    def foi_publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_de_criação <= now

    def __str__(self):
        return self.nome


class PortfólioCategoria(models.Model):
    categoria = models.CharField(
        max_length=100,
        default='categoria',
    )

    def __str__(self) -> str:
        return self.categoria


class Portfólio(models.Model):
    titulo = models.CharField(
        max_length=50,
        default='titulo',
    )

    categoria = models.ForeignKey(
        PortfólioCategoria,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    frase = models.CharField(
        max_length=100,
        default=' ',
    )

    nome_do_cliente = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    update_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True,
    )

    url_do_projeto = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    descrição = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )

    depoimento_do_cliente = models.TextField(
        max_length=5000,
        blank=True,
        null=True,
    )
    imagem_do_cliente = models.FileField(
        default='default/images/depoimentos_imagem.png',
        upload_to='portfólio/images/',
    )
    capa_do_projeto = models.FileField(
        upload_to='portfólio/images/',
        default='default/images/Em-Breve.jpg',
    )
    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    @admin.display(
        boolean=True,
        ordering='data_de_criação',
        description='Data de criação',
    )
    def foi_publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_de_criação <= now

    def has_image(self, image):
        # print('-'*100, '\n has_image funcionou')

        return (image != None) and (image != '') and (image !=
                                                      'default/images/depoimentos_imagem.png') and (image !=
                                                                                                    'default/images/Em-Breve.jpg')

    def delete(self):
        if self.has_image(self.imagem_do_cliente):
            if os.path.isfile(self.imagem_do_cliente.path):
                os.remove(self.imagem_do_cliente.path)

        if self.has_image(self.capa_do_projeto):
            if os.path.isfile(self.capa_do_projeto.path):
                os.remove(self.capa_do_projeto.path)

        super().delete()
        print('-'*100, '\n delete funcionou')

    def __str__(self):
        return self.titulo


class PortfólioImagem(models.Model):
    add_imagem = models.ForeignKey(
        Portfólio,
        default=None,
        on_delete=models.CASCADE,
    )
    images = models.FileField(
        upload_to='portfólio/images/',
        blank=True,
        null=True,
    )

    def has_image(self):
        print('-'*100, '\n has_image 2', f"{self.images}")
        return self.images != None and self.images != ''

    def remove_image(self):
        if self.has_image():
            if os.path.isfile(self.images.path):
                os.remove(self.images.path)

        self.images = None

    def delete(self):
        self.remove_image()
        super().delete()
        print('-'*100, '\n delete funcionou 2')

    def __str__(self):
        return self.add_imagem.titulo


class Sobre(models.Model):
    nome = models.CharField(
        max_length=50,
        default='Qual é o seu nome?',
        blank=True,
        null=True,
    )

    profissão = models.CharField(
        max_length=50,
        default='Qual é sua profissão?',
        blank=True,
        null=True,
    )

    email = models.EmailField(
        default='Qual é o seu email?',
        blank=True,
        null=True,
    )

    telefone = models.CharField(
        default='Qual é o seu telefone?',
        max_length=11,
        blank=True,
        null=True,
    )

    hero = models.FileField(
        default='default/images/hero.webp',
        upload_to='sobre/images/',
    )

    foto_de_perfil = models.FileField(
        default='default/images/foto_de_perfil.svg',
        upload_to='sobre/images/',
    )

    background_depoimento = models.FileField(
        default='default/images/backgroud.webp',
        upload_to='sobre/images/',
    )

    frase = models.CharField(
        default='Qual é a sua frase?',
        max_length=50,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def has_image(self, image):
        return (image != None) and (image != '') and (image != 'default/images/hero.webp') and (image != 'default/images/foto_de_perfil.svg') and (image != 'default/images/backgroud.webp')

    def delete(self):
        if self.has_image(self.hero):
            if os.path.isfile(self.hero.path):
                os.remove(self.hero.path)

        if self.has_image(self.foto_de_perfil):
            if os.path.isfile(self.foto_de_perfil.path):
                os.remove(self.foto_de_perfil.path)

        if self.has_image(self.background_depoimento):
            if os.path.isfile(self.background_depoimento.path):
                os.remove(self.background_depoimento.path)

        super().delete()

    def __str__(self):
        return self.nome


class SobreHabilidade(models.Model):
    add_habilidade = models.ForeignKey(
        Sobre,
        default=None,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    habilidade = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    porcentagem = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.add_habilidade.nome


class Contato(models.Model):
    email = models.EmailField(
        blank=True,
        null=True,
    )

    telefone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
    )
    
    titulo_do_formulario = models.CharField(
        max_length=30,
        default="Fale comigo.",
        blank=True,
        null=True,
    )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def __str__(self):
        return self.email


class ContatoRedeSocial(models.Model):
    add_redeSocial = models.ForeignKey(
        Contato,
        default=None,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    rede_social = models.CharField(
        choices=REDES_SOCIAIS,
        default='diagram-2-fill',
        max_length=50,
        blank=True,
        null=True,
    )

    url = models.CharField(
        default='https://www.instagram.com/samuelbarbosa_dev/',
        max_length=500,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.add_redeSocial.email


class Site(models.Model):
    nome = models.CharField(
        max_length=50,
        default='Nome',
        blank=True,
        null=True,
    )

    frase = models.CharField(
        max_length=100,
        default='Nome',
        blank=True,
        null=True,
    )

    icon_32x32 = models.FileField(
        default='default/images/onda_icon.png',
        upload_to='site/images/',
    )

    icon_150x150 = models.FileField(
        default='default/images/onda_icon_maior.png',
        upload_to='site/images/',
    )

    footer = models.FileField(
        default='default/images/footer.webp',
        upload_to='site/images/',
    )

    # cor_do_icons_de_redes_sociais = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_secundaria_do_icons_de_redes_sociais = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_dos_icons_de_contato = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_secundaria_dos_icons_de_contato = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_dos_detalhes = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_do_botão = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    # cor_secundaria_do_botão = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     null=True,
    #     default='black',
    # )

    data_de_criação = models.DateTimeField(
        'Data de criação',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    def has_image(self, image):
        return (image != None) and (image != '') and (image != 'default/images/footer.webp') and (image != 'default/images/onda_icon.png') and (image != 'default/images/onda_icon_maior.png')

    def delete(self):
        if self.has_image(self.footer):
            if os.path.isfile(self.footer.path):
                os.remove(self.footer.path)

        if self.has_image(self.icon_32x32):
            if os.path.isfile(self.icon_32x32.path):
                os.remove(self.icon_32x32.path)

        if self.has_image(self.icon_150x150):
            if os.path.isfile(self.icon_150x150.path):
                os.remove(self.icon_150x150.path)

        super().delete()

    def __str__(self):
        return self.nome
