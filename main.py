import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

def main():
    active_passcards = Passcard.objects.filter(is_active=True)
    active_cards = len(active_passcards)
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', active_cards)

if __name__ == '__main__':
    main()
    
