from django.urls import path
from . import views
from .views import ScheList, ScheDetail, ScheCreate, ScheUpdate, ScheDelete

urlpatterns = [
    path("", ScheList.as_view(), name="schedules"),
    path("schedule/<int:pk>/", ScheDetail.as_view(), name="schedule"),
    path("create-schedule", ScheCreate.as_view(), name="create"),
    path("edit-schedule/<int:pk>/", ScheUpdate.as_view(), name="edit"),
    path("delete-schedule/<int:pk>/", ScheDelete.as_view(), name="delete" )
]