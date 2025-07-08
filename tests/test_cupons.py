from app.coupons import apply, get_final_price

def test_discount_sales10():
  assert apply(100,"SALES10") == 90.0
def test_discount_super20():
  assert apply(200,"SUPER20") == 160.0
def test_discount_welcome():
  assert apply(100,"WELCOME") == 85.0
def test_tax_rate():
  assert get_final_price(100,"SALES10") == 107.1