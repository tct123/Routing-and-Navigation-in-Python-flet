from flet import *
from pages.home import *
from pages.login import *


def views_handler(page):
    return {
        "/": View(
            route="/",
            controls=[
                Column(
                    controls=[
                        Container(
                            height=800,
                            width=300,
                            bgcolor="red",
                            content=Column(
                                controls=[
                                    Text("Welcome to the homepage"),
                                    Container(
                                        on_click=lambda _: page.go("/login"),
                                        content=Text(
                                            "Goto Login", size=25, color="black"
                                        ),
                                    ),
                                ]
                            ),
                        )
                    ]
                )
            ],
        ),
        "/login": View(
            route="/login",
            controls=[
                Column(
                    controls=[
                        Container(
                            height=800,
                            width=200,
                            bgcolor="blue",
                            content=Column(
                                controls=[
                                    Text("Welcome back \n This is the login pages"),
                                    Container(
                                        on_click=lambda _: page.go("/"),
                                        content=Text(
                                            "Goto Home", size=25, color="black"
                                        ),
                                    ),
                                ]
                            ),
                        )
                    ]
                )
            ],
        ),
    }
