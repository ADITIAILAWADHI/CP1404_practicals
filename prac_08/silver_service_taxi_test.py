from prac_08.silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi('Hummer', 300, 2)
silver_service_taxi.drive(18)
print(silver_service_taxi)
print('${:.2f}'.format(silver_service_taxi.get_fare()))
