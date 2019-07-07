from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("schools/",hello.views.schools,name = "schools"),
    path("research/",hello.views.research,name = "research"),
    path("visuals/",hello.views.visuals,name = "visuals"),
    path("login/",hello.views.login_user,name = "login"),
    path("logout/",hello.views.logout_user, name="logout"),
    path("dea/",hello.views.dea, name="dea"),
    path("experimentalstudies/",hello.views.experimentalstudies,name = "experimentalstudies"),
    path("simulateddata/",hello.views.simulateddata,name = "simulateddata"),
    path("contact/",hello.views.showform,name = "showform"),
    path("quizdata/",hello.views.quiz,name = "quiz"),
    path("search/",hello.views.search,name = "search"),
]
