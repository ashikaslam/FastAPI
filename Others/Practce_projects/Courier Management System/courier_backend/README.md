# 📦 Courier Management System API Guide
# 📦 for some End pont we have to pass jwt access pont 
![Eample  Screenshot](https://i.ibb.co/M5RKdf81/Screenshot-from-2025-07-06-18-06-20.png)
---

## 👤 Step 1: Create a Superuser

```bash
python manage.py shell
```

Then:

```python
from core.models import User
User.objects.create_superuser(email='Superuser@example.com', password='StrongPassword123!')
```

---

## 📝 Step 2: Register a User

**Endpoint:**  
`POST http://127.0.0.1:8000/api/v1/auth/register/`

**Request JSON:**

```json
{
  "email": "Customer@example.com",
  "password": "StrongPassword123!",
  "confirm_password": "StrongPassword123!"
}
```

**Response JSON:**

```json
{
  "id": 5,
  "email": "Customer@example.com",
  "role": "user"
}
```

---

## 🔑 Step 3: Role Assignment via Admin

**Admin Panel URLs:**

- Login: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- User Role Assignment: [http://127.0.0.1:8000/admin/core/user/](http://127.0.0.1:8000/admin/core/user/)

![Admin Panel Screenshot](https://i.ibb.co/d4gMj8NY/Screenshot-from-2025-07-06-16-51-20.png)
![Admin Panel Screenshot](https://i.ibb.co/F4HrL31z/Screenshot-from-2025-07-06-16-51-51.png)


Default role for users is `user`. Assign roles like `admin` or `deliveryman` from the admin panel.

---

## 🔐 Step 4: Login as User/Admin/Deliveryman

### Customer Login
```json
{
  "email": "Customer@example.com",
  "password": "StrongPassword123!"
}
```

### Admin Login
```json
{
  "email": "Admin@example.com",
  "password": "StrongPassword123!"
}
```

### Deliveryman Login
```json
{
  "email": "Deliveryman@example.com",
  "password": "StrongPassword123!"
}
```

**Login Response:**

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

## 🔄 Step 5: Refresh Access Token

**Endpoint:**  
`POST http://127.0.0.1:8000/api/v1/auth/token/refresh/`

**Request JSON:**

```json
{
  "refresh": "<refresh_token>"
}
```

---

## 🛒 Step 6: Create an Order (Customer) >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`POST http://127.0.0.1:8000/api/v1/orders/create/`

**Request JSON:**

```json
{
  "address": "123 Main Street, City, Country",
  "cost_ammount": 99.99,
  "payment_method": "online"
}
```

**Response JSON:**

```json
{
  "id": 2,
  "address": "123 Main Street, City, Country",
  "cost_ammount": "99.99",
  "status": "pending",
  "payment_method": "online",
  "payment_status": "pending",
  "created_at": "2025-07-06T11:18:15.595173Z",
  "delivery_completed_at": null,
  "user": 5,
  "delivery_man": null
}
```

---

## 📦 Step 7: View Customer Orders >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/orders/user/`

**Response JSON:**

```json
[
  {
    "id": 2,
    "address": "123 Main Street, City, Country",
    "cost_ammount": "99.99",
    "status": "pending",
    "payment_method": "online",
    "payment_status": "pending",
    "created_at": "2025-07-06T11:18:15.595173Z",
    "delivery_completed_at": null,
    "user": 5,
    "delivery_man": null
  }
]
```

---

## 💳 Step 8: Create Stripe Checkout Session >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/payments/create-checkout-session/<int:order_id>/`

**Response JSON:**

```json
{
  "success": true,
  "checkout_url": "https://checkout.stripe.com/c/pay/...",
  "message": "Stripe checkout session created."
}
```

---

## 🧾 Step 9: Admin Views All Orders >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/orders/admin/`

**Response JSON:**

```json
[
  {
    "id": 2,
    "address": "123 Main Street, City, Country",
    "cost_ammount": "99.99",
    "status": "pending",
    "payment_method": "online",
    "payment_status": "pending",
    "created_at": "2025-07-06T11:18:15.595173Z",
    "delivery_completed_at": null,
    "user": 5,
    "delivery_man": null
  }
]
```

---

## 📬 Step 10: Admin Assigns Order to Deliveryman >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/orders/admin/assignorders/admin/assign/<int:order_id>/<int:deliveryman_id>/`

**Response JSON:**

```json
{
  "success": true,
  "message": "Delivery man (ID: 6) assigned to order (ID: 2).",
  "order_id": 2,
  "delivery_man": "Deliveryman@example.com",
  "status": "assigned"
}
```

---

# 🚚 Deliveryman API

---

## 📥 View Assigned Orders >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/orders/delivery/`

**Response JSON:**

```json
[
  {
    "id": 2,
    "address": "123 Main Street, City, Country",
    "cost_ammount": "99.99",
    "status": "assigned",
    "payment_method": "online",
    "payment_status": "pending",
    "created_at": "2025-07-06T11:18:15.595173Z",
    "delivery_completed_at": null,
    "user": 5,
    "delivery_man": 6
  }
]
```

---

## 📤 Update Order Status >> this eind piont is protected for authenticated user we have to pass jwt access tokne 

**Endpoint:**  
`GET http://127.0.0.1:8000/api/v1/delivery/update-status/<int:order_id>/<str:status_value>/`

**Valid Status Values:**  
`pending`, `assigned`, `delivered`, `complete`

**Response JSON:**

```json
{
  "success": true,
  "message": "Order status updated successfully.",
  "order_id": 2,
  "status": "delivered"
}
```