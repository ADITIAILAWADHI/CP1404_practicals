from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    bill = 0.0
    current_taxi = None
    choices = "q)uit, c)hoose taxi, d)rive"
    print(choices)
    user_input = input('>>> ').lower()
    while user_input != 'q':
        if user_input == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print('{} - {}'.format(i, taxi))
            current_taxi = taxis[int(input('Choose taxi: '))]
        elif user_input == 'd':
            current_taxi.start_fare()
            distance = int(input('Drive how far? '))
            current_taxi.drive(distance)
            print('Your {} trip cost you ${}'.format(current_taxi.name, current_taxi.get_fare()))
            bill += current_taxi.get_fare()
        print('Bill to date: ${:.2f}'.format(bill))
        print(choices)
        user_input = input('>>> ').lower()

    print('Total trip cost: ${:.2f}'.format(bill))
    print('Taxis are now:')
    for i, taxi in enumerate(taxis):
        print('{} - {}'.format(i, taxi))


main()
