from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    user_lista = [
        {"nome": "Emerson", "matricula": "20261282120004", "idade": 15, "cidade": "Boa Saúde"},
        {"nome": "Renan", "matricula": "20261282120018", "idade": 16, "cidade": "Elói de Souza"},
        {"nome": "Mateus", "matricula": "20261282120033", "idade": 15, "cidade": "Riachuelo"}, 
        {"nome": "Arthur", "matricula": "20261282120020", "idade": 16, "cidade": "São Paulo do Potengi"},
        {"nome": "Isaac", "matricula": "20261282120002", "idade": 15, "cidade": "Santa Maria"},
    ]

    context = {
        "usuarios": user_lista,
    }
    return render(request, 'usuarios.html', context)