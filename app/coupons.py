def apply(price,coupon):
  discounts = {
    "SALES10":0.10,
    "SUPER20":0.20,
    "WELCOME":0.15,
  }
  if coupon in discounts:
    return round(price * (1 - discounts[coupon]),2)
  return price

def get_final_price(base_price, coupon, tax_rate=0.19):
  final_price = apply(base_price,coupon)
  return round(final_price * (1 + tax_rate),2)