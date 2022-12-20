from rest_framework import serializers

# from Todoapi.serializers import UserPublicSerializer

from .models import Task
# from .models import User
# from .models import Entry

class TaskSerializer(serializers.ModelSerializer):
    # owner = UserPublicSerializer(source="user", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Task
        fields = '__all__'
        # fields = ('title', 'date', 'periode', 'status', 'important', 'logo', 'is_deleted', 'objects')
    
    def validate_title(self, value):
        request = self.context.get('request')
        qs = Task.objects.filter(title__iexact=value)
        if qs.exists():
           raise serializers.ValidationError(f"le produit {value} existe deja")
        return value
            
        
         
    # class Meta:
    #     model = User
    #     fields = '__all__'
        
    # class Meta: 
    #     model = Entry
    #     fields = '__all__'

