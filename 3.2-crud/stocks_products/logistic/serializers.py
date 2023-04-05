from pprint import pprint

from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description']



class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product','quantity','price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id','address','positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position).save()

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # print('stock = ', instance)
        # print('product = ', positions)
        # print('validated_data=', validated_data)
        # print(stock.address)

        for position in positions:
            StockProduct.objects.update_or_create(
                stock=instance, product=position['product'], defaults=position
            )

        return stock
