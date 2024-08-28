class Stock:
    def __init__(self, name, m_avg, cost):
        self.name = name
        self.m_avg = m_avg
        self.cost = cost

    def bulk_calculation(self, month):
        bulk_qty = self.m_avg * month
        total_cost = bulk_qty * self.cost
        print(f"QTY: {bulk_qty}, Total cost: ${total_cost}")

    def current_stock_level(self, current_qty):
        c_level = current_qty / self.m_avg
        return c_level

    def order_warning(self, current_qty):
        if current_qty < self.m_avg * 2:
            min_qty = self.bulk_calculation(3)
            print(f"Need to place a new order right now. Min QTY: {min_qty}")
        else:
            print("Still fine. You need to keep monitoring.")
