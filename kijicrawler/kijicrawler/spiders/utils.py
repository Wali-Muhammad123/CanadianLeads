def hiddenvaluescraper(response,name):
    """
    This function is used to scrape hidden values from the login page.It takes care of the error that occurs when the value is not found.
    """
    try:
        value=response.css(f'input[name="{name}"]::attr(value)').extract_first()
        return value
    except:
        value=""
        return value
