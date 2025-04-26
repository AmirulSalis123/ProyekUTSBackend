from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    # Waktu tunggu antar task dalam detik (misal 1-3 detik)
    wait_time = between(1, 3)

    @task
    def index(self):
        # Mengakses halaman utama
        self.client.get("/")

    @task
    def items(self):
        # Mengakses halaman items
        self.client.get("/items/")

    @task
    def item_detail(self):
        # Mengakses halaman detail item, ganti dengan ID item yang valid
        self.client.get("/items/edit/1/")

    @task
    def stock_summary(self):
        # Mengakses halaman stock summary
        self.client.get("/stock-summary/")

