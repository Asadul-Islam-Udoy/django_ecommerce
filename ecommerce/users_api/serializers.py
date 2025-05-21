from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CustomSerializer(serializers.ModelSerializer):
    #    validators=[validate_password] include password file
    password = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','email','phone','password','password2','is_staff']
        read_only_fields=['id','is_staff']
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password:confirm password is not match"})
        return attrs
    def create(self, validated_data):
        if not validated_data.get('username'):
            base_name = validated_data.get('email').split("@")[0]
            validated_data["username"] = base_name
        validated_data.pop("password2")
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    def update(self, instance, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")
        for attr,value in validated_data.items():
            setattr(instance,attr,value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.name
        token['email'] = user.email
        return token
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add user data to the response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'phone': getattr(self.user, 'phone', ''),
            'username': self.user.username,  # or self.user.name if you have a field
        }

        return data