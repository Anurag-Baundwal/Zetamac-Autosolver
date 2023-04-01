import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    url = "https://arithmetic.zetamac.com/"

    # Replace with the path to your WebDriver
    driver_path = "C:\\path\\to\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    browser = webdriver.Chrome(service=service)
    try:
        browser.get(url)
    except Exception as e:
        print("Error while accessing the website:", e)
        browser.quit()
        return

    # Start the game
    try:
        start_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']"))
        )
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']"))
        )
        start_button.click()
    except Exception as e:
        print("Error while finding the start button:", e)
        browser.quit()
        return

    # Inject the JavaScript code
    js_code = '''
    function triggerEvent(el, type) {
        var e = new KeyboardEvent(type, {bubbles: true, cancelable: true});
        el.dispatchEvent(e);
    }

    var question, answer, answerField;
    answerField = document.getElementsByClassName('answer')[0];

    var interval = setInterval(() => {
        question = document.getElementsByClassName('problem')[0].innerText.replace('×', '*').replace('÷', '/').replace('–', '-');
        answer = eval(question);
        answerField.value = answer;
        triggerEvent(answerField, 'keydown');
    }, 0);
    '''

    browser.execute_script(js_code)

    # Wait for the game to end
    try:
        WebDriverWait(browser, 125).until(
            EC.presence_of_element_located((By.ID, "finalscore"))
        )
    except Exception as e:
        print("Error or game over:", e)

    # Close the browser
    browser.quit()

if __name__ == "__main__":
    main()
