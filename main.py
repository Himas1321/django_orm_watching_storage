import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

<<<<<<< HEAD
# passcards = Passcard.objects.all()
=======
passcards = Passcard.objects.all()
>>>>>>> 90d7a278545fd8095d5172cbb20e175fd46c7611

active_passcards = Passcard.objects.filter(is_active=True)
active_cards = len(active_passcards)


if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', active_cards)
