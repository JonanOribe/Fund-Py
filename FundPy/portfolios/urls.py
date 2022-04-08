from django.conf.urls import url
from portfolios import views


urlpatterns = [
    url(r'^api/portfolios$',views.portfolio_list),
    url(r'^api/portfolios/(?P<pk>[0-9]+)$',views.portfolio_detail),
    url(r'^api/portfolios/published$',views.portfolio_list_published)
]