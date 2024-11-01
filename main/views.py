from django.shortcuts import render , redirect
from .models import Produtos
from django.contrib.auth.decorators import login_required


@login_required
def lista_produtos(request):
    produto = Produtos.objects.all()
    print(produto)
    return render(request,'produto/lista_produtos.html', {'produto':produto})

@login_required
def produtos_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        estoque = request.POST.get('estoque')
        print(nome, descricao, preco , estoque)
        if nome and descricao:
            Produtos.objects.create(nome=nome, descricao=descricao, preco=preco ,estoque=estoque )
        return redirect('lista_produtos')
    return render(request,'produto/criar_produto.html')

@login_required
def delete_produto(request, produto_id):
    produto = Produtos.objects.get (id=produto_id)    
    produto.delete()
    return redirect('lista_produtos')





    
    
