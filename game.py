import flet as ft
from random import randint

def main(page:ft.Page):
    page.title = "Guess Me"
    page.theme_mode = "light"
    page.fonts = {
        "Cheese":"cheese.otf",
        "Super":"super.ttf"
    }
    page.padding = 10
    answer = randint(1,100)
    print(answer)

    player1 = ft.TextField(hint_text="Guess a number between (1-100)...",label="Player 1",border_radius=30)
    player2 = ft.TextField(hint_text="Guess a number between (1-100)...",label="Player 2",border_radius=30)

    result = ft.Text(font_family="super",size=20)
    def check_guess_player1(e):
        if int(player1.value)<answer:
            result.value = "Guess a higher value"
        elif int(player1.value) >answer:
            result.value = "Guess a lower value"
        elif int(player1.value)== answer:
            result.value = "Congratulations! player 1 won the match"
        else:
            result.value("Something went wrong ")
        page.update()

    def check_guess_player2(e):
        if int(player2.value)<answer:
            result.value = "Guess a higher value"
        elif int(player2.value) >answer:
            result.value = "Guess a lower value"
        elif int(player2.value)== answer:
            result.value = "Congratulations! player 2 won the match"
        else:
            result.value("Something went wrong ")
        page.update()

    check_player1 = ft.ElevatedButton("Check your guess",on_click=check_guess_player1)
    check_player2 = ft.ElevatedButton("Check your guess",on_click=check_guess_player2)

    page.add(
        ft.Card(
            ft.Container(

            content =ft.Row(
            controls = [ft.Text(value="GUESS ME",font_family="Cheese",size=25)],
            alignment = "center"    
        ),
        padding =50
        )
        )
        ,
        ft.Container(
            content =ft.Column(
            controls =[ft.Row(controls = [player1,check_player1],alignment="center"),
            ft.Row(controls=[player2,check_player2],alignment="center"),
            ft.Row(controls=[result],alignment="center")
            ]
        ),padding=40
        )
    )


ft.app(target=main,assets_dir="assets")