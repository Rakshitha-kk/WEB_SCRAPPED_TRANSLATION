from mlapp import views
from django.urls import path

urlpatterns = [
    path("",views.home,name="home"),
    path("scrape_page",views.scrape_page,name="scrape_page"),
    # path('download_paragraphs/', views.download_paragraphs, name='download_paragraphs'),
]