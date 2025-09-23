from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import random
from datetime import datetime, timedelta
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Dummy database - In real implementation, this would be a proper database
dummy_database = {
    "abandoned_carts": [],
    "customers": [],
    "recovery_attempts": [],
    "whatsapp_messages": [],
    "calling_team_notifications": []
}

# Sample customer data
sample_customers = [
    {
        "id": 1,
        "name": "Rajesh Kumar",
        "phone": "+91-9876543210",
        "email": "rajesh.kumar@email.com",
        "location": "Mumbai, Maharashtra",
        "total_orders": 5,
        "avg_order_value": 2500
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "phone": "+91-9876543211",
        "email": "priya.sharma@email.com",
        "location": "Delhi, NCR",
        "total_orders": 12,
        "avg_order_value": 1800
    },
    {
        "id": 3,
        "name": "Amit Patel",
        "phone": "+91-9876543212",
        "email": "amit.patel@email.com",
        "location": "Bangalore, Karnataka",
        "total_orders": 3,
        "avg_order_value": 3200
    },
    {
        "id": 4,
        "name": "Sneha Reddy",
        "phone": "+91-9876543213",
        "email": "sneha.reddy@email.com",
        "location": "Hyderabad, Telangana",
        "total_orders": 8,
        "avg_order_value": 2100
    },
    {
        "id": 5,
        "name": "Vikram Singh",
        "phone": "+91-9876543214",
        "email": "vikram.singh@email.com",
        "location": "Pune, Maharashtra",
        "total_orders": 15,
        "avg_order_value": 1500
    }
]

# Sample product data
sample_products = [
    {"id": 1, "name": "Wireless Headphones", "price": 2999, "category": "Electronics"},
    {"id": 2, "name": "Smart Watch", "price": 8999, "category": "Electronics"},
    {"id": 3, "name": "Running Shoes", "price": 2499, "category": "Sports"},
    {"id": 4, "name": "Laptop Bag", "price": 1299, "category": "Accessories"},
    {"id": 5, "name": "Bluetooth Speaker", "price": 1999, "category": "Electronics"},
    {"id": 6, "name": "Fitness Tracker", "price": 3999, "category": "Sports"},
    {"id": 7, "name": "Phone Case", "price": 499, "category": "Accessories"},
    {"id": 8, "name": "Power Bank", "price": 1499, "category": "Electronics"}
]

def generate_dummy_data():
    """Generate dummy abandoned cart data"""
    current_time = datetime.now()
    
    for i in range(8):
        customer = random.choice(sample_customers)
        cart_items = random.sample(sample_products, random.randint(1, 3))
        cart_value = sum(item["price"] for item in cart_items)
        
        # Random abandonment time (5-30 minutes ago)
        abandonment_time = current_time - timedelta(minutes=random.randint(5, 30))
        
        abandoned_cart = {
            "id": i + 1,
            "customer_id": customer["id"],
            "customer_name": customer["name"],
            "customer_phone": customer["phone"],
            "customer_email": customer["email"],
            "cart_items": cart_items,
            "cart_value": cart_value,
            "abandoned_at": abandonment_time.isoformat(),
            "status": random.choice(["pending", "recovered", "lost"]),
            "recovery_attempts": random.randint(0, 3),
            "priority": "high" if cart_value > 5000 else "medium" if cart_value > 2000 else "low"
        }
        
        dummy_database["abandoned_carts"].append(abandoned_cart)
        dummy_database["customers"].append(customer)

# Initialize dummy data
generate_dummy_data()

@app.route('/')
def home():
    return jsonify({
        "message": "Cart Abandonment Recovery API",
        "version": "1.0.0",
        "endpoints": {
            "abandoned_carts": "/api/abandoned-carts",
            "customers": "/api/customers",
            "recovery_attempts": "/api/recovery-attempts",
            "send_whatsapp": "/api/send-whatsapp",
            "notify_calling_team": "/api/notify-calling-team",
            "dashboard_stats": "/api/dashboard-stats"
        }
    })

@app.route('/api/abandoned-carts')
def get_abandoned_carts():
    """Get all abandoned carts"""
    return jsonify({
        "success": True,
        "data": dummy_database["abandoned_carts"],
        "count": len(dummy_database["abandoned_carts"])
    })

@app.route('/api/customers')
def get_customers():
    """Get all customers"""
    return jsonify({
        "success": True,
        "data": dummy_database["customers"],
        "count": len(dummy_database["customers"])
    })

@app.route('/api/dashboard-stats')
def get_dashboard_stats():
    """Get dashboard statistics"""
    total_carts = len(dummy_database["abandoned_carts"])
    recovered_carts = len([cart for cart in dummy_database["abandoned_carts"] if cart["status"] == "recovered"])
    pending_carts = len([cart for cart in dummy_database["abandoned_carts"] if cart["status"] == "pending"])
    total_value = sum(cart["cart_value"] for cart in dummy_database["abandoned_carts"])
    recovered_value = sum(cart["cart_value"] for cart in dummy_database["abandoned_carts"] if cart["status"] == "recovered")
    
    recovery_rate = (recovered_carts / total_carts * 100) if total_carts > 0 else 0
    
    return jsonify({
        "success": True,
        "data": {
            "total_abandoned_carts": total_carts,
            "recovered_carts": recovered_carts,
            "pending_carts": pending_carts,
            "recovery_rate": round(recovery_rate, 1),
            "total_cart_value": total_value,
            "recovered_value": recovered_value,
            "potential_revenue": total_value - recovered_value,
            "whatsapp_messages_sent": len(dummy_database["whatsapp_messages"]),
            "calling_team_notifications": len(dummy_database["calling_team_notifications"])
        }
    })

@app.route('/api/send-whatsapp', methods=['POST'])
def send_whatsapp():
    """Simulate sending WhatsApp message"""
    data = request.get_json()
    cart_id = data.get('cart_id')
    
    # Find the cart
    cart = next((c for c in dummy_database["abandoned_carts"] if c["id"] == cart_id), None)
    if not cart:
        return jsonify({"success": False, "message": "Cart not found"}), 404
    
    # Create WhatsApp message
    message = {
        "id": len(dummy_database["whatsapp_messages"]) + 1,
        "cart_id": cart_id,
        "customer_phone": cart["customer_phone"],
        "customer_name": cart["customer_name"],
        "message": f"Hi {cart['customer_name']}! You left some great items worth ₹{cart['cart_value']} in your cart. Complete your purchase now and save 10%! View Cart: https://example.com/cart/{cart_id}",
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    }
    
    dummy_database["whatsapp_messages"].append(message)
    
    # Simulate API delay
    time.sleep(1)
    
    return jsonify({
        "success": True,
        "message": "WhatsApp message sent successfully",
        "data": message
    })

@app.route('/api/notify-calling-team', methods=['POST'])
def notify_calling_team():
    """Simulate notifying calling team"""
    data = request.get_json()
    cart_id = data.get('cart_id')
    
    # Find the cart
    cart = next((c for c in dummy_database["abandoned_carts"] if c["id"] == cart_id), None)
    if not cart:
        return jsonify({"success": False, "message": "Cart not found"}), 404
    
    # Create calling team notification
    notification = {
        "id": len(dummy_database["calling_team_notifications"]) + 1,
        "cart_id": cart_id,
        "customer_name": cart["customer_name"],
        "customer_phone": cart["customer_phone"],
        "cart_value": cart["cart_value"],
        "priority": cart["priority"],
        "message": f"New lead: {cart['customer_name']} - ₹{cart['cart_value']} cart value - {cart['priority']} priority - Call within 30 minutes",
        "created_at": datetime.now().isoformat(),
        "status": "pending"
    }
    
    dummy_database["calling_team_notifications"].append(notification)
    
    return jsonify({
        "success": True,
        "message": "Calling team notified successfully",
        "data": notification
    })

@app.route('/api/recovery-attempts', methods=['POST'])
def create_recovery_attempt():
    """Create a recovery attempt"""
    data = request.get_json()
    cart_id = data.get('cart_id')
    attempt_type = data.get('type', 'whatsapp')  # whatsapp, call, email
    
    # Find the cart
    cart = next((c for c in dummy_database["abandoned_carts"] if c["id"] == cart_id), None)
    if not cart:
        return jsonify({"success": False, "message": "Cart not found"}), 404
    
    # Create recovery attempt
    attempt = {
        "id": len(dummy_database["recovery_attempts"]) + 1,
        "cart_id": cart_id,
        "type": attempt_type,
        "customer_name": cart["customer_name"],
        "created_at": datetime.now().isoformat(),
        "status": "completed"
    }
    
    dummy_database["recovery_attempts"].append(attempt)
    
    # Update cart recovery attempts count
    cart["recovery_attempts"] += 1
    
    return jsonify({
        "success": True,
        "message": "Recovery attempt recorded",
        "data": attempt
    })

@app.route('/api/simulate-recovery', methods=['POST'])
def simulate_recovery():
    """Simulate the complete recovery process"""
    data = request.get_json()
    cart_id = data.get('cart_id')
    
    # Find the cart
    cart = next((c for c in dummy_database["abandoned_carts"] if c["id"] == cart_id), None)
    if not cart:
        return jsonify({"success": False, "message": "Cart not found"}), 404
    
    # Simulate the recovery process
    # 1. Send WhatsApp message
    whatsapp_response = send_whatsapp()
    
    # 2. Notify calling team
    notification_response = notify_calling_team()
    
    # 3. Create recovery attempt
    attempt_response = create_recovery_attempt()
    
    # 4. Simulate recovery success (70% chance)
    recovery_success = random.random() < 0.7
    if recovery_success:
        cart["status"] = "recovered"
    
    return jsonify({
        "success": True,
        "message": "Recovery process completed",
        "recovery_success": recovery_success,
        "whatsapp_sent": True,
        "calling_team_notified": True,
        "cart_status": cart["status"]
    })

if __name__ == '__main__':
    print("🚀 Starting Cart Abandonment Recovery API...")
    print("📊 Dummy data generated with 8 abandoned carts")
    print("🌐 API available at: http://localhost:5000")
    print("📱 WhatsApp simulation ready")
    print("📞 Calling team notifications ready")
    app.run(debug=True, port=5000)
