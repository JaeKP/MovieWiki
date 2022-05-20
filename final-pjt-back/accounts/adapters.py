from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user = super().save_user(request, user, form, False)
        
        age = data.get("age")
        nickname = data.get("nickname")
        region = data.get("region")
        
        if age:
            user.age = age
        if nickname:
            user.nickname = nickname
        if region:
            user.region = region
            

        user.save()
        return user