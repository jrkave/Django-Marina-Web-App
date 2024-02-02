from .models import BoatSpace 

# Create and save 100 BoatSpace objects
for i in range(1, 101):
    BoatSpace.objects.create(
        id=i,
        availability_status=True,  # Adjust based on your model's fields
        # Add other fields as needed
    )

# Verify the creation by checking the count
BoatSpace.objects.count()
