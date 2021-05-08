from prac_08.taxi import Taxi

prius = Taxi('Prius 1', 100)
prius.drive(40)
print(prius)
print("Current fare: ${}\n".format(prius.get_fare()))
prius.start_fare()
prius.drive(100)
print(prius)
print("Current fare: ${}".format(prius.get_fare()))
