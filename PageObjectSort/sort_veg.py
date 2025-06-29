from selenium.webdriver.common.by import By


class SortVeg:
    def __init__(self, driver):
        self.driver = driver
        self.veg_table_name = (By.XPATH, "//span[text()='Veg/fruit name']")
        self.veg_fruit_list = (By.XPATH, "//tbody/tr/td[1]")
        self.veg_fruit_list_data = []


    def get_veg_list(self):
        self.driver.maximize_window()
        self.driver.find_element(*self.veg_table_name).click()
        # get the column list of veg/fruit name - veglist
        veg_fruit = self.driver.find_elements(*self.veg_fruit_list)

        for v in veg_fruit:
            self.veg_fruit_list_data.append(str(v.text))
        print(self.veg_fruit_list_data)



    def validate_sort_list(self):
        sort_list = sorted(self.veg_fruit_list_data)
        print("sort_list: ", sort_list)
        # sortlist should be equal to veglist
        assert sort_list == self.veg_fruit_list_data