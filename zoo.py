class Zoo:
    def get_ticket_price(self, age):
        if age < 0: #init b1 block
            return None
        if 0 <= age <= 12: #change 0 < age to 0 <= age
            return 50
        elif 13 <= age <= 20: #change 20 < get to 20 <= age
            return 100
        elif 21 <= age <= 60: #change 21 < age to 21 <= age
            return 150
        elif age > 60: #change >= to >
            return 100