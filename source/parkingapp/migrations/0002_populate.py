# Generated by Django 3.1.6 on 2021-03-02 22:24
from django.contrib.auth.hashers import make_password
from django.db import migrations
from django.conf import settings
from datetime import date


def populate_db(apps, schema_editor):
    Profile = apps.get_model('parkingapp', 'Profile')
    Event = apps.get_model('parkingapp', 'Event')
    ParkingLot = apps.get_model('parkingapp', 'ParkingLot')
    ParkingLotInfo = apps.get_model('parkingapp', 'ParkingLotEventData')
    ParkingSpot = apps.get_model('parkingapp', 'ParkingSpot')
    User = apps.get_model(*settings.AUTH_USER_MODEL.split('.'))

    # Supervisor Account Profile
    supervisor = User.objects.create(
        email='alexthurston@hotmail.com',
        username='alexthurston',
        password=make_password('cs3450lover'),
        first_name='Alex',
        last_name='Thurston',
    )
    supervisorProfile = Profile(user=supervisor, isSupervisor=True)
    supervisorProfile.save()

    # Lot Attendant Profile
    lotAttendant = User.objects.create(
        email='jaypeterson@hotmail.com',
        username='jaypeterson',
        password=make_password('cs3450lover2'),
        first_name='Jay',
        last_name='Peterson',
    )
    lotAttendantProfile = Profile(user=lotAttendant)
    lotAttendantProfile.save()

    # Customer Profile
    customer = User.objects.create(
        email='natemerrill@hotmail.com',
        username='natemerrill',
        password=make_password('cs3450lover3'),
        first_name='Nate',
        last_name='Merrill',
    )
    customerProfile = Profile(user=customer)
    customerProfile.save()

    # Events
    event1 = Event.objects.create(
        supervisor=supervisorProfile.user,
        name='USU Basketball',
        address='900 E 900 N, Logan, UT 84322',
        date=date(2021, 6, 10),
    )

    event2 = Event.objects.create(
        supervisor=supervisorProfile.user,
        name='USU Football',
        address='E 1000 N, Logan, UT 84341',
        date=date(2021, 5, 10),
    )

    # Lots

    lot1 = ParkingLot.objects.create(
        owner=lotAttendantProfile.user,
        nickname="Lot 1",
        address="435 Logan Place",
        numMotorcycleSpots=3,
        numCarSpots=5,
        numOversizeSpots=1,
        motorcycleSpotPrice=5,
        carSpotPrice=10,
        oversizeSpotPrice=15,
    )
    lot1.save()

    lot2 = ParkingLot.objects.create(
        owner=lotAttendantProfile.user,
        nickname="Lot 2",
        address="123 Old Main Hill",
        numMotorcycleSpots=5,
        numCarSpots=8,
        numOversizeSpots=2,
        motorcycleSpotPrice=5,
        carSpotPrice=10,
        oversizeSpotPrice=15,
    )
    lot2.save()

    # Lot Event Info
    lot1EventInfo = ParkingLotInfo.objects.create(
        parkingLot=lot1,
        event=event1,
        distanceFromEvent=3.2,
        availableMotorcycleSpots=lot1.numMotorcycleSpots,
        availableCarSpots=lot1.numCarSpots,
        availableOversizeSpots=lot1.numOversizeSpots,
    )
    lot1EventInfo.save()

    lot2EventInfo = ParkingLotInfo.objects.create(
        parkingLot=lot2,
        event=event2,
        distanceFromEvent=0.5,
        availableMotorcycleSpots=lot2.numMotorcycleSpots,
        availableCarSpots=lot2.numCarSpots,
        availableOversizeSpots=lot2.numOversizeSpots,
    )
    lot2EventInfo.save()

    # Parking Spots

    # Lot1
    for i in range(lot1.numMotorcycleSpots):
        ParkingSpot(parkingLotEventData=lot1EventInfo, spotType='1', price=lot1.motorcycleSpotPrice).save()
    for i in range(lot1.numCarSpots):
        ParkingSpot(parkingLotEventData=lot1EventInfo, spotType='2', price=lot1.carSpotPrice).save()
    for i in range(lot1.numOversizeSpots):
        ParkingSpot(parkingLotEventData=lot1EventInfo, spotType='3', price=lot1.oversizeSpotPrice).save()

    # Lot2
    for i in range(lot2.numMotorcycleSpots):
        ParkingSpot(parkingLotEventData=lot2EventInfo, spotType='1', price=lot2.motorcycleSpotPrice).save()
    for i in range(lot2.numCarSpots):
        ParkingSpot(parkingLotEventData=lot2EventInfo, spotType='2', price=lot2.carSpotPrice).save()
    for i in range(lot2.numOversizeSpots):
        ParkingSpot(parkingLotEventData=lot2EventInfo, spotType='3', price=lot2.oversizeSpotPrice).save()



class Migration(migrations.Migration):
    dependencies = [
        ('parkingapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]