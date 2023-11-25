from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer
from rest_framework.permissions import IsAuthenticated

class PetListAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated
    
    def get(self, request):
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(posted_by=request.user)  # Associate pet with logged-in user
            return Response({'msg':"Pet Added Successfully!", 'data':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PetDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            pet = Pet.objects.get(pk=pk)
        except Pet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PetSerializer(pet)
        data = serializer.data

        # Include information about who posted the pet
        data['posted_by'] = {
            'id': pet.posted_by.id,
            'name': pet.posted_by.name,
            'email': pet.posted_by.email,
            # Add other fields as needed
        }

        return Response(data)
