
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try :
    # Open the Python website
    driver.get("https://stage.pijarsekolah.id")
    driver.maximize_window()

    # Get page title
    title = driver.title

    # Test if title is correct
    assert "Aplikasi Sekolah Pembelajaran Online Terbaik | Pijar Sekolah" in title
    print(f"TEST 0:",title, "testcase passed")
    sleep(5)

    try:
        contenjdl1 = driver.find_element(By.CSS_SELECTOR, "h1.text-center")
        # Print the text of the located element
        print(f"TEST 1: {contenjdl1.text} testcase passed")
        contenisi1 = driver.find_element(By.CSS_SELECTOR, "p.text-lg")
        # Print the text of the located element
        print(f"TEST 2: {contenisi1.text} testcase passed")
          # scrolling down slowly
        driver.execute_script("window.scrollBy(0, 1000);") 
        sleep(5)
        contenjdl2 = driver.find_element(By.CSS_SELECTOR, ".max-w-\[1000px\]")
        # Print the text of the located element
        print(f"TEST 3: {contenjdl2.text} testcase passed")
        contenjdl3 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 4: {contenjdl3.text} testcase passed")
        conten4 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > p:nth-child(2)")
         # Print the text of the located element
        print(f"TEST 5: {conten4.text} testcase passed")

        pengajar = driver.find_element(By.ID, "radix-:R26t6:-trigger-teaching")
        pengajar.click()
        contenjdl5 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 6: {contenjdl5.text} testcase passed")
        contenjdl6 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 7: {contenjdl6.text} testcase passed")
        sleep(5)

        student = driver.find_element(By.ID, "radix-:R26t6:-trigger-student")
        student.click()
        contenjdl8 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 8: {contenjdl8.text} testcase passed")
        contenjdl9 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 9: {contenjdl9.text} testcase passed")
        sleep(5)

        admin = driver.find_element(By.ID, "radix-:R26t6:-trigger-admin")
        admin.click()
        contenjdl10 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 10: {contenjdl10.text} testcase passed")
        contenjdl11 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 11: {contenjdl11.text} testcase passed")
        sleep(5)

        education = driver.find_element(By.ID,"radix-:R26t6:-trigger-education_authorities")
        education.click()
        contenjdl12 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 12: {contenjdl12.text} testcase passed")
        contenjdl13 = driver.find_element(By.CSS_SELECTOR, ".gap-y-2 > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 13: {contenjdl13.text} testcase passed")
        sleep(5)

        # scrolling down slowly
        driver.execute_script("window.scrollBy(0, 1000);") 
        contenjdl14 = driver.find_element(By.CSS_SELECTOR, "h2.max-w-\[800px\]:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 14: {contenjdl14.text} testcase passed")
        contenjdl15 = driver.find_element(By.CSS_SELECTOR, "div.flex-col:nth-child(4) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 15: {contenjdl15.text} testcase passed")
        contenjdl16 = driver.find_element(By.CSS_SELECTOR, "div.max-w-screen-xl:nth-child(4) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 16: {contenjdl16.text} testcase passed")

        sleep(5)
        
         # scrolling down slowly
        driver.execute_script("window.scrollBy(0, 1000);") 
        contenjdl17 = driver.find_element(By.CSS_SELECTOR, "section.fadeInBottom:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > h3:nth-child(1)")
        # Print the text of the located element
        print(f"TEST 17: {contenjdl17.text} testcase passed")
        contenjdl18 = driver.find_element(By.CSS_SELECTOR, "section.fadeInBottom:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > p:nth-child(2)")
        # Print the text of the located element
        print(f"TEST 18: {contenjdl18.text} testcase passed")
        sleep(5)
        # driver.execute_script("window.scrollBy(0, -1000);") 
        # sleep(5)

    except NoSuchElementException:
        # Handle the case where the element is not found
        print("Element with the specified CSS selector was not found.")


       

finally:
    # Close the browser
    driver.quit()
