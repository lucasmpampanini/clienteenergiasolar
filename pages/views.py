from django.shortcuts import render
from services.models import Service
from .models import Faq, HomeImg
from django.core.mail import EmailMessage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

def index_view(request):
    context = {
        'services': Service.objects.all(),
        'homeimg': HomeImg.objects.all(),
        'faq': Faq.objects.all(),
    }
    
    if request.method == 'POST':
        
        if request.POST.get('valor_conta'):
            tipo_instalacao = request.POST.get('tipoInstalacaoSelect')
            valor_conta = request.POST.get('valor_conta') 
            kwh = int(valor_conta)/0.80 #Entendendo que o valor do kwh pago seja de R$ 0,80
            indece_de_radiacao = 5.0
            eficiencia_do_microinversor = 0.88
            potencia = int(kwh) / (30.4375*indece_de_radiacao*eficiencia_do_microinversor)
            numero_de_placas = potencia / 0.33
            painel_gera_kw_dia = 1113*arredonda_float(numero_de_placas)
            area_do_painel = 1.96*0.99
            peso_do_painel = 22.5
            investimento_estimado_min = arredonda_float(numero_de_placas)*1950
            investimento_estimado_max = arredonda_float(numero_de_placas)*2050
            economia_media = int(kwh)*0.57 # Economia média da conta usadndo o sistema cerca de 72% do valor da distribuidora R$ 0,80
            context = {
                'valor_conta': int(valor_conta),
                'instalacao': tipo_instalacao,
                'kwh': int(kwh),
                'numero_de_placas': arredonda_float(numero_de_placas),
                'painel_gera_kw_dia': painel_gera_kw_dia,
                'area_dos_paineis': arredonda_float(arredonda_float(numero_de_placas)*area_do_painel),
                'peso_dos_paineis': arredonda_float(numero_de_placas)*peso_do_painel,
                'investimento_estimado_min': investimento_estimado_min,
                'investimento_estimado_max': investimento_estimado_max,
                'economia_media': economia_media,
            }
            return render(request, 'resultado_economia.html', context)

        subject = request.POST.get('subject')
        messagefirst = request.POST.get('message')
        name = request.POST.get('name')
        from_email = request.POST.get('email')
        message = 'Você recebeu menssagem de ' + name + '\nE-mail: ' + from_email + '\nConteudo: \n' + messagefirst
        
        email = EmailMessage(subject, message, from_email, ['solarrns@gmail.com'])

        if request.FILES:
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            filename = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            email.attach_file(filename)
        
        email.send()

        return render(request, 'yes_send_email.html')
    
    return render(request, 'index.html', context)

def service_details(request, slug, pk):
    context = {
        'service': Service.objects.get(id=pk)
    }
    return render(request, "service_details.html", context)

# Arredonda o float para mais e transforma em numero inteiro
def arredonda_float(numero_de_placas):
    
    if type(numero_de_placas) is float:
        numero_de_placas = int(numero_de_placas) + 1
        return numero_de_placas
    else:
        return numero_de_placas