from django.urls import path

from habit.apps import HabitConfig
from habit.views import (HabitCreateAPIView, HabitListAPIView,
                         HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView, HabitsPublicListAPIView)


app_name = HabitConfig.name


urlpatterns = [
    path('public/', HabitsPublicListAPIView.as_view(), name='habits_public_list'),
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path("habits/<int:pk>", HabitRetrieveAPIView.as_view(), name="habits_retrieve"),
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits_create"),
    path("habits/<int:pk>/delete", HabitDestroyAPIView.as_view(), name="habits_delete"),
    path("habits/<int:pk>/update", HabitUpdateAPIView.as_view(), name="habits_update"),

]




