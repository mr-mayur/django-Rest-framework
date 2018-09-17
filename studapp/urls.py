from rest_framework import routers
from .views import StudentViewSet, UniversityViewSet
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API name')




router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls

urlpatterns = [

    url(r'^docs/$', schema_view, name="schema_view") #swagger -- rest api
]
urlpatterns += router.urls