from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app1.models import Article


def index(request):
    return HttpResponse('hello, world')


def show_detail(request):
    first_article = Article.objects.all()
    return render(request, 'xiangqing.html', {
        'article': first_article,
    })


def show_aticle(request):
    article = Article.objects.all()
    return render(request, 'show.html', {'articls': article
                                         }
                  )


def bigso(request, article_id):
    all_article = Article.objects.all()  # 取出所有文章
    curr_article = None
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    # return render(request, 'blog/show_info.html', {'bloginfo': curr_article,
    #                                                'section_list': section_list
    #                                                })

    return render(request, 'xiangqing.html', {'article': curr_article,
                                              'previous_article': previous_article,
                                              'next_article': next_article})
