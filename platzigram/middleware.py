"""Platzigram middleware catalog"""


# Django imports
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile complletion middleware
    
    Ensure every user that is interacting with the platadorm
    have their profile pictur and biography.
    """

    
    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response




    def __call__(self, request):
        """Aqui va la chicha
        
        Code to be execute for each request beforee the view is
        call
        """
        if not (request.user.is_anonymous):
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')


        response = self.get_response(request)
        return response 

        