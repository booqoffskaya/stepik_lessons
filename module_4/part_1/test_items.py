def test_button_add_to_basket(browser, request):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(5)

    button_text = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button').text
    print(button_text)

    language = request.config.getoption("language")
    expected_button_text = {
        'ru': 'Добавить в корзину',
        'en-GB': 'Add to basket',
        'es': 'Añadir al carrito',
        'fr': 'Ajouter au panier'
    }.get(language)

    assert button_text == expected_button_text
