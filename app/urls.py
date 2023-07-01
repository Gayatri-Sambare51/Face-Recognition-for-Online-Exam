from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login.html',views.login,name='login') ,
    path('login.html',views.logout,name='logout') ,
    path('verifyRequest',views.verifyRequest, name='verifyRequest'),
    path('verify.html',views.verify,name='verify') ,
    path('indexes.html',views.indexes,name='indexes') ,
    path('home',views.home,name='home') ,
    path('about_us.html',views.about,name='about') ,
    path('contact.html',views.contact,name='contact') ,
    path('privacypolicy.html',views.privacypolicy,name='privacypolicy') ,
    path('register.html',views.register,name='register') ,
  # path('captureImg',views.captureImg,name='captureImg') ,

    path('c_questions.html',views.cques,name='cques') ,
    path('c_start.html',views.cstart,name='cstart') ,

    path('python_questions.html',views.questions,name='questions') ,
    path('python_start.html',views.quizStart,name='quizStart') ,

    path('java_questions.html',views.javaques,name='javaques') ,
    path('java_start.html',views.java,name='java') ,

    path('javascript_questions.html',views.javascriptques,name='javascriptques') ,
    path('javascript_start.html',views.javascript,name='javascript') ,

    path('cpp_questions.html',views.cppques,name='cppques') ,
    path('cpp_start.html',views.cpp,name='cpp') ,

    path('logout',views.logout,name='logout') 

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
