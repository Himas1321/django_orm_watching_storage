import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

passcards = Passcard.objects.all()
# some_post = passcards[0]

active_passcards = Passcard.objects.filter(is_active=True)

# for card in passcards:
#     if card.is_active:
#         active_passcards.append(card.is_active)


active_cards = len(active_passcards)


if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', active_cards)