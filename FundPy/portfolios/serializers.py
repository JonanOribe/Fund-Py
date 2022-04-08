from rest_framework import serializers 
from FundPy.portfolios.models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        models = Portfolio
        fields = ('id',
                'title',
                'description',
                'published')