from django.urls import path
# from django.views.generic import TemplateView -- started w/ to get project going
from . import views

urlpatterns = [
    # path(
    #   "",
    #   TemplateView.as_view(template_name="cards/base.html"),
    #   name="home"
    # ), -- this also changes with line 3
    path(
      "",
      views.CardListView.as_view(),
      name="card-list"
    ),
    path(
      "new", 
      views.CardCreateView.as_view(), 
      name="card-create"),
    path(
      "edit/<int:pk>", #grabing the primary key of the card being edited
      views.CardUpdateView.as_view(),
      name="card-update"),
    path(
      "box/<int:box_num>",
      views.BoxView.as_view(),
      name="box"
    )
]
