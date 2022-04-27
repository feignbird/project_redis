from rest_framework import serializers
from redis_app.models import TableA, TableB, TableC, TableD, TableE


class TableESerializer(serializers.ModelSerializer):
    class Meta:
        model = TableE
        fields = ('id', 'e_str', 'e_bool', 'e_int')

class TableDSerializer(serializers.ModelSerializer):
    table_e_to_d = TableESerializer(many = True, read_only = True)
    class Meta:
        model = TableD
        fields = ('id', 'd_str', 'd_bool', 'd_int', 'table_e_to_d')

class TableCSerializer(serializers.ModelSerializer):
    table_d_to_c = TableDSerializer(many = True, read_only = True)
    class Meta:
        model = TableC
        fields = ('id', 'c_str', 'c_bool', 'c_int', "table_d_to_c")

class TableBSerializer(serializers.ModelSerializer):
    table_c_to_b = TableCSerializer(many = True, read_only = True)
    class Meta:
        model = TableB
        fields = ('id', 'b_str', 'b_bool', 'b_int', 'table_c_to_b')

class TableASerializer(serializers.ModelSerializer):
    table_b_to_a = TableBSerializer(many = True, read_only = True)
    class Meta:
        model = TableA
        fields = ('id', 'a_str', 'a_bool', 'a_int', 'table_b_to_a')
