from django.shortcuts import render
from .forms import CaseForm
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def home(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case_type = form.cleaned_data['case_type']
            case_number = form.cleaned_data['case_number']
            filing_year = form.cleaned_data['case_year']

            # Firefox setup (headless optional)
            firefox_options = Options()
            firefox_options.headless = False  # Set to True for headless mode

            driver = webdriver.Firefox(options=firefox_options)

            try:
                url = "https://delhihighcourt.nic.in/app/get-case-type-status"
                driver.get(url)

                # Fill form
                driver.find_element(By.NAME, "case_type").send_keys(case_type)
                driver.find_element(By.NAME, "case_number").send_keys(case_number)
                driver.find_element(By.NAME, "case_year").send_keys(filing_year)

                # CAPTCHA Handling — give time to manually solve it
                time.sleep(15)  # Allow user to fill CAPTCHA manually 
                
                driver.find_element(By.ID,"search").click()
                time.sleep(5)  # Wait for page load

                # Extract details
                
                box=driver.find_elements(By.XPATH,"//table[@id='caseTable']//tbody//tr//td")
                petitioner=box[2].text.split('VS.')[0]
                respondent=box[2].text.split('VS. ')[1]
                next_hearing=box[3].text.split(' ')[2].replace('Last', ' ')

                #Here is href link of Orders Date
                link = driver.find_element(By.LINK_TEXT,'Orders')
                href_link = link.get_attribute('href')
                data = {
                    'petitioner': petitioner,
                    'respondent': respondent,
                    'next_hearing': next_hearing,
                    'href_link':href_link
                }

            except Exception as e:
                data = {'error': f"Error occurred: {str(e)}"}

            finally:
                driver.quit()

            return render(request, 'cases/result.html', {'data': data})

    else:
        form = CaseForm()

    return render(request, 'cases/forms.html', {'form': form})
