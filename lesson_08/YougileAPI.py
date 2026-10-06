import requests


class YougileAPI:
    def __init__(self):
        self.base_url = "https://yougile.com/api-v2/projects"
        self.token = ""
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        """Позитивный метод создания проекта (принимает название)."""
        body = {"title": title}
        response = requests.post(
            self.base_url,
            json=body,
            headers=self.headers
        )
        return response

    def create_project_negative(self, body):
        """Негативный метод создания проекта (принимает любое ломаное тело)."""
        response = requests.post(
            self.base_url,
            json=body,
            headers=self.headers
        )
        return response

    def update_project(self, project_id, new_title):
        """PUT-запрос: изменяет название проекта по его ID."""
        url = f"{self.base_url}/{project_id}"
        body = {"title": new_title}
        response = requests.put(url, json=body, headers=self.headers)
        return response

    def get_project_by_id(self, project_id):
        """GET-запрос: получает информацию о конкретном проекте по его ID."""
        url = f"{self.base_url}/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response
