from flask import Flask, request, jsonify
from app.coupons import get_final_price

app = Flask(__name__)

@app.route('/price', method=['POST'])
def get_price():
  data = request.get_json()
  price = data.get("price")
  coupon = data.get("coupon")
  tax_rate = data.get("tax-rate", 0.19)

  final = get_final_price(price, coupon, tax_rate)
  return jsonify({"final_price": final})