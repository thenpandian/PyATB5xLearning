class RestfulBooker:

    def __init__(self, list_of_apis, links):
        self.list_of_apis = list_of_apis
        self.links = links

    def print_apis(self):
        for api in self.list_of_apis:
            print(f"{api}")

    def print_links(self):
        for link in self.links:
            print(f"{link}")


restfulBooker_ref = RestfulBooker(list_of_apis=["Login Page", "Create Id", "Update ID"],
links = {"https://api.restfulbooker.com/login", "https://api.restfulbooker.com/create",
         "https://api.restfulbooker.com/update"})

restfulBooker_ref.print_apis()
restfulBooker_ref.print_links()
