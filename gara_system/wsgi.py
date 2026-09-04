"""
WSGI config for gara_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gara_system.settings')

application = get_wsgi_application()
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gara_system.settings')
application = get_wsgi_application()

# Tự động tạo tài khoản nhân viên khi app khởi động trên Render
try:
    from django.contrib.auth.models import User, Group
    staff_accounts = [
        ("Thukho01", "ThuKho"),
        ("Letan05", "LeTan"),
        ("Thungan02", "KeToan"),
        ("Thosuachua03", "ThoMay"),
        ("Quandoc04", "QuanLyKyThuat"),
        ("chamsockh06", "CSKH"),
    ]
    for username, group_name in staff_accounts:
        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password("MatKhauMacDinh123@")
            user.is_staff = True
            user.save()
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
except Exception:
    pass