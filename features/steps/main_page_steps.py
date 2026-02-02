from behave import given

@given('Open Target main page')
def open_main(context):
    context.driver.get('https://target.com')
    #context.app.main_page.open_main_page()