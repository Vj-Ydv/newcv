"""newcv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from curriculum.views import export_single_page, export_classic, export_class,export_classic1,addlanguage,addlanguageitem,addresume, addskill, addskillitem, addcertification, addcertificationitem, addexperience, addproject, addprojectitem, addtraining, menulist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classic/',export_classic,name='classic'),
    path('classic1/',export_classic1,name='classic1'),
    path('modern/',export_single_page,name='modern'),
    path('htmltest/<str:first_name>/',export_class,name='test'),
    path('language/',addlanguage,name='language'),
    path('languageitem/',addlanguageitem,name='languageitem'),
    path('resume/',addresume,name='resume'),
    path('skill/',addskill,name='skill'),
    path('skillitem/',addskillitem,name='skillitem'),
    path('certification/',addcertification,name='certification'),
    path('certificationitem/',addcertificationitem,name='certificationitem'),
    path('experience/',addexperience,name='experience'),
    path('project/',addproject,name='project'),
    path('projectitem/',addprojectitem,name='projectitem'),
    path('training/',addtraining,name='training'),
    path('',menulist,name='showmenu'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
