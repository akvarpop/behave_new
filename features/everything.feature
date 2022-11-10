Feature: test ui Hillel aq
  Scenario: We enter the page of the site and log in
    Given open site "https://www.aqa.science/admin/"
    Then enter data in the field username "admin" By.ID "id_username"
    Then enter data in the username login "admin123" By.XPATH "//*[@id="id_password"]"
    And press the button for Login to enter the admin panel By.XPATH "//*[@id="login-form"]/div[3]/input"
    Then go screenshot for allure "Login_on_main_page"
    Then checking a successful login to the admin page, By.XPATH "//*[@id="site-name"]/a"

  Scenario: create new user in admin panel
    Given click button create user By.XPATH "//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a"
    Then enter data in the username By.XPATH "//*[@id="id_username"]" send keys "Popravka"
    And enter data in the password By.XPATH "//*[@id="id_password1"]" send keys "test12345"
    And enter data in the password confirm By.XPATH "//*[@id="id_password2"]" send keys "test12345"
    And click button save new user By.XPATH "//*[@id="user_form"]/div/div/input[1]"
    Then go screenshot for allure "new_user"
    Then checking a successful create new user, By.XPATH "//*[@id="main"]/div/ul/li"

    Scenario: search for the user we created
      Given click button users,go to the user page By.XPATH "//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a"
      Then in the search box By.XPATH "//*[@id="searchbar"]" send data "Popravka"
      And click button Search By.XPATH "//*[@id="changelist-search"]/div/input[2]"
      Then checking a successful find new user, By.XPATH "//*[@id="result_list"]/tbody/tr/th/a"

    Scenario: update_data_user
      Given click button users,go to the user page By.XPATH "//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a"
      Then in the search box By.XPATH "//*[@id="searchbar"]" send data "Popravka"
      And click button Search By.XPATH "//*[@id="changelist-search"]/div/input[2]"
      And click on user  and go to the user page to edit it By.XPATH "//*[@id="result_list"]/tbody/tr/th/a"
      Then update user data in the field first name By.XPATH "//*[@id="id_first_name"]" send keys "test"
      And update user data in the field last name By.XPATH "//*[@id="id_last_name"]" send keys "test"
      And update user data in the field email By.XPATH "//*[@id="id_email"]" send keys "test@test.test"
      And change staff status By.XPATH "//*[@id="id_is_staff"]"
      Then go screenshot for allure "update_data_user"
      And click the button to save the result By.XPATH "//*[@id="user_form"]/div/div/input[3]"

    Scenario: check the fields filled in earlier
      Given check update user data in the field first name By.XPATH "//*[@id="id_first_name"]" keys "test"
      And check update user data in the field last name By.XPATH "//*[@id="id_last_name"]" keys "test"
      And check update user data in the field email By.XPATH "//*[@id="id_email"]" keys "test@test.test"
      And check staff status true By.XPATH "//*[@id="id_is_staff"]" keys "true"

    Scenario: delete user
      Given click button users,go to the user page By.XPATH "//*[@id="nav-sidebar"]/div/table/tbody/tr[2]/th/a"
      Then in the search box By.XPATH "//*[@id="searchbar"]" send data "Popravka"
      And click button Search By.XPATH "//*[@id="changelist-search"]/div/input[2]"
      And tick the user you want to delete By.XPATH "//*[@id="action-toggle"]"
      And click on the drop down list to select By.XPATH "//*[@id="changelist-form"]/div[1]/label/select"
      And click on the drop down list to select options delete By.XPATH "//*[@id="changelist-form"]/div[1]/label/select/option[2]"
      And click button GO to confirm deletion By.XPATH "//*[@id="changelist-form"]/div[1]/button"
      Then click button YES I AM SURE By.XPATH "//*[@id="content"]/form/div/input[4]"
      Then go screenshot for allure "delete user"
      Then check delete user By.XPATH "//*[@id="main"]/div/ul/li" result: "Successfully deleted 1 user."





