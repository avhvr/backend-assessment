from apis import views


api_urls = [
    ("/", views.index, ["GET"], "flask scaffolding index url"),
    ("/login", views.login, ["POST"], "flask scaffolding login user url"),
    ("/register", views.register, ["POST"], "flask scaffolding register user url"),
]

other_urls = []

all_urls = api_urls + other_urls
