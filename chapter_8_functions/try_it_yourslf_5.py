

import os 
os.system('clear')


def make_sandwich(*items):
    """ Makes sandwich with list of items provided"""
    print(f"\nMaking sandiwch with below items: ")
    for item in items:
        print(f"Adding - {item}")


make_sandwich('corn','cheese','olive')
make_sandwich('corn','butter')

def build_car(company, model , **kwargs):
    """ Builds a car profile with all the information provided."""
    kwargs['company'] = company
    kwargs['model']   = model
    return kwargs

print('\n\nBuilding car profile: ')
print(build_car('TATA','Altroz',year=2026,engine='automatic'))