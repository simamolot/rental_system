from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


class LogoutView(APIView):
    def get(self, request):
        confirmation_html = """
        <html>
            <body>
                <h1>Confirm Logout</h1>
                <p>Are you sure you want to log out?</p>
                <form method="post" action="">
                    <button type="submit">Yes, Logout</button>
                </form>
                <a href="/">Cancel</a>
            </body>
        </html>
        """
        return HttpResponse(confirmation_html, content_type="text/html")

    def post(self, request):
        response = HttpResponse(
            "<h1>Logout Successful</h1><p>You have been logged out.</p>",
            content_type="text/html"
        )
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response







