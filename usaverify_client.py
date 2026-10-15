import time
import requests

API_KEY = "YOUR_USAVERIFYPRO_API_KEY"
BASE_URL = "[https://usaverifypro.com/api/v1](https://usaverifypro.com/api/v1)"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_balance():
    """Check current account wallet balance in USD."""
    response = requests.get(f"{BASE_URL}/balance", headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()

def rent_us_number(service_code="openai", area_code=None):
    """
    Rent a real Tier-1 US physical SIM number.
    Example service codes: 'whatsapp', 'openai', 'google', 'telegram', 'tiktok', 'discord'
    """
    payload = {"service": service_code, "country": "US"}
    if area_code:
        payload["area_code"] = area_code
        
    response = requests.post(f"{BASE_URL}/rent", json=payload, headers=headers, timeout=15)
    response.raise_for_status()
    return response.json()

def poll_for_otp(order_id, timeout_seconds=180, poll_interval=4):
    """Poll the order endpoint until the SMS OTP arrives or the timer expires."""
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        response = requests.get(f"{BASE_URL}/order/{order_id}", headers=headers, timeout=10)
        data = response.json()
        
        status = data.get("status")
        if status == "COMPLETED" and data.get("otp_code"):
            return data["otp_code"]
        elif status in ("CANCELLED", "EXPIRED"):
            raise RuntimeError("Order expired or cancelled. 100% of funds automatically refunded.")
            
        time.sleep(poll_interval)
        
    # Cancel order for instant refund if no SMS arrived within timeout
    requests.post(f"{BASE_URL}/cancel/{order_id}", headers=headers, timeout=10)
    raise TimeoutError("No SMS received within timeout window. Order cancelled with full auto-refund.")

if __name__ == "__main__":
    print("Connecting to USAVerify Pro REST API...")
    # 1. Rent a number for OpenAI / ChatGPT verification ($0.35)
    order = rent_us_number(service_code="openai", area_code="212")
    print(f"Rented US Number: {order.get('phone_number')} | Order ID: {order.get('order_id')}")
    
    # 2. Wait for incoming SMS OTP
    otp = poll_for_otp(order_id=order.get("order_id"))
    print(f"Received Verification Code: {otp}")









const API_KEY = process.env.USAVERIFY_API_KEY || "YOUR_USAVERIFYPRO_API_KEY";
const BASE_URL = "[https://usaverifypro.com/api/v1](https://usaverifypro.com/api/v1)";

async function rentAndVerify(service = "whatsapp") {
  const res = await fetch(`${BASE_URL}/rent`, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ service, country: "US" })
  });

  const order = await res.json();
  console.log(`Rented US Physical SIM: ${order.phone_number} (ID: ${order.order_id})`);
  return order;
}
