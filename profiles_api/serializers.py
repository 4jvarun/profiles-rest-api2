from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView

       Serializers converts data inputs to python objects and vice versa

       If we are using post or update functionality to our hello API view then we need to create serialiers to receive the content
       that we post to the API

       Creating a simple serlizer that accepts a name input and then we are adding this to our API view and then test the post functionality
       of our API View

       """
    name = serializers.CharField(max_length=10)
