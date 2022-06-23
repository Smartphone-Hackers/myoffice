"""myoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from officeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view()),
    path('new-student', views.NewStudent.as_view(), name='new-student'),
    path('edit-student/<int:pk>', views.EditStudent.as_view()),
    path('delete-student/<int:pk>', views.DeleteStudent.as_view()),
    path('pay-fees', views.PayFees.as_view(), name='pay-fees'),
    path('course-list', views.CourseList.as_view(), name='course-list'),
    path('delete-course/<int:pk>', views.DeleteCourse.as_view()),
    path('fees-details/<int:pk>', views.FeesDetails.as_view()),
    path('delete-fees-details/<int:pk>/<int:id>', views.DeleteFeesDetails.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)