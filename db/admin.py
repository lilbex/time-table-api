from django.contrib import admin
from db.models import (user,classe,subject,teacher,term)


admin.site.register(user.User)
admin.site.register(classe.Classe)
admin.site.register(subject.Subject)
admin.site.register(teacher.Teacher)
admin.site.register(term.Term)



# idahosa igbebalo