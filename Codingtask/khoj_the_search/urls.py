from django.urls import path
from khoj_the_search.views import SearchView, GetInputValues

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('get_input_values/', GetInputValues.as_view(), name='get_input_values'),
]