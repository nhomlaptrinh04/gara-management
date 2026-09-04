from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Tự động tạo các tài khoản nhân viên cho gara'

    def handle(self, *args, **options):
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
                self.stdout.write(self.style.SUCCESS(f"Đã tạo tài khoản: {username}"))

            group, _ = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS(f"Đã gán {username} vào nhóm {group_name}"))
