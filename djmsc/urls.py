from django.conf.urls import url, include

from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r"event", views.EventViewSet)
router.register(r"person", views.PersonViewSet)
router.register(r"usuario", views.UsuarioViewSet)
router.register(r"transaccion", views.TransaccionViewSet)


urlpatterns = [
    url(r"^", include(router.urls)),

]
