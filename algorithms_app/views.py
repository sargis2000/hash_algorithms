from django.shortcuts import render
from .forms import HashForm
import hashlib


# Create your views here.

def hasher(request):
    data = request.POST

    try:
        hash_algorithm = hashlib.new(data['alg_name'])
        hash_algorithm.update(data['text'].encode())
        return {'hash': hash_algorithm.hexdigest(), 'text': data['text']}
    except ValueError as exception:
        return {'error': exception, 'text': data['text']}


def sha_view(request):
    available_algorithms = list(
        hashlib.algorithms_available ^ {'whirlpool', 'whirlpool', 'md4', 'ripemd160', 'shake_128', 'shake_256'}
    )
    available_algorithms.sort()
    available_algorithms = {'available_algorithms': available_algorithms}

    if request.method == 'POST':
        form = HashForm(request.POST)
        if form.is_valid():
            data = hasher(request=request)
            data = {**data, **available_algorithms}
            return render(request, 'sha.html', context=data)
        else:
            print(form.errors)
    return render(request, 'sha.html', available_algorithms)
