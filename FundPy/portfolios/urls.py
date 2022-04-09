from django.urls import include, re_path
from portfolios import views


urlpatterns = [
    re_path(r'^api/portfolios$',views.portfolio_list),
    re_path(r'^api/portfolios/(?P<pk>[0-9]+)$',views.portfolio_detail),
    re_path(r'^api/portfolios/published$',views.portfolio_list_published)
]