from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://albelli.nl')
assert browser.find_element_by_id('hero-shot').is_displayed()
browser.quit()
