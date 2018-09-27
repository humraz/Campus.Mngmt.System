"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from education import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'.*addattendance.html/$', v.addattendance),
    url(r'.*addcourse.html/$', v.addcourse),
    url(r'.*logindex.html/$', v.logindex),
    url(r'.*resetatt.html/$', v.resetatt),

    url(r'.*addsemester.html/$', v.addattendance),
    url(r'.*addsubject.html/$', v.addsubject),
    url(r'.*viewattendance.html/$', v.addattendance),
    url(r'.*viewsubs.html/$', v.viewdeps),
    url(r'.*viewfeedback.html/$', v.viewf),
    url(r'.*marks.html/$', v.markss),
    url(r'.*feedback.html/$', v.feed),
    url(r'.*register.html/$', v.register),
    url(r'.*fee.html/$', v.feees),

    url(r'.*material.html/$', v.materialup),

    url(r'.*viewmets.html/$', v.viewmats),

    
    url(r'.*login.html/$', v.login),

    

    url(r'.*addparent.html/$', v.addpp),




    url(r'.*adddepartment.html/$', v.adddepartment),
    url(r'.*addattendance.html/$', v.addattendance),
    url(r'.*hi$', v.front),
]
