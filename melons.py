"""Classes for melon orders."""

class AbstractMelonOrder():
    
    def __init__(self, species, qty, shipped, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = shipped
        self.order_type = order_type
        self.tax = tax

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, shipped):
        """Initialize melon order attributes."""
        tax = 0.08
        order_type = "domestic"
        # self.species = species
        # self.qty = qty
        # self.shipped = False

        super().__init__(tax, order_type)
        #self.order_type = "domestic"
        #self.tax = 0.08

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
