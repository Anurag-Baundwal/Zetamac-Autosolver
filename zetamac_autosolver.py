import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calculate_expression(expression: str) -> str:
    return str(eval(expression))

def main():
    url = "https://arithmetic.zetamac.com/"

    # Replace with the path to your WebDriver
    driver_path = "C:\\Users\\Anurag Baundwal\\Downloads\\chromedriver_win32\\chromedriver.exe"

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

    # time.sleep(5000)
    # Solve problems until the game is over
    while True:
        try:
            expression_element = browser.find_element(By.CLASS_NAME, "problem")
            expression = expression_element.text
            expression = expression.replace("×", "*")
            expression = expression.replace("÷", "/")
            expression = expression.replace("–", "-")
            expression = expression.replace("+", "+")

            answer = calculate_expression(expression)

            answer_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "answer"))
        )
            try:
                start_button = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "answer"))
                )
                answer_input.clear()
                answer_input.send_keys(answer)
                answer_input.send_keys(Keys.RETURN)
            except Exception as e:
                print("Error while finding the answer field:", e)
                browser.quit()
                return

            time.sleep(0.000000001)
        except Exception as e:
            print("Game over or error:", e)
            break

    # browser.quit()

if __name__ == "__main__":
    main()