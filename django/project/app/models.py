from django.db import models


class UserManager(BaseUserManager):

    def create_user(self,
                    username,
                    email,
                    password=None,
                    first_name=None,
                    last_name=None) -> user:
        if not username:
            raise TypeError('Users should have a username')
        if not email:
            raise TypeError('Users should have a Email')

        user = self.model(username=username,
                          email=self.normalize_email(email),
                          first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None) -> user:
        if password is None:
            raise TypeError('Password should not be none')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user

