from marina.models import BoatSpace 

# Create and save 100 BoatSpace objects
def create_spaces():
    for i in range(1, 101):
        BoatSpace.objects.create(
            id=i,
            availability_status=True,
        )
    return BoatSpace.objects.count()
