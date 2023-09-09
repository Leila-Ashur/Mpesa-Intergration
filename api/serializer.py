
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        models=Comments
        fields= "__all__"