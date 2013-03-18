Feature: Главная страница системы с последними новостями и пунктами меню

    Scenario: Главная страница открывается со статусом 200
        Given site page with URL "/"
        When we send GET-request to given page
        Then response must have code equals 200
