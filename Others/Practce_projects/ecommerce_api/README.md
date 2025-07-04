# 💼 E-commerce API Setup Guide

Welcome to the E-commerce API! Follow these steps to set up and test core features like user registration, login, profile management, product listing, and Stripe payment integration.

---

## 🔐 Step 1: Add Secret Credentials

Open `ecommerce_api/settings.py` and add the following secret credentials (from >>https://docs.google.com/document/d/1TggludGiZLcyo1RVfqYYXPswBLRY02ih-WpZLBepHNs/edit?usp=sharing):

* **Gmail SMTP**: For password reset emails.
* **Stripe API Keys**: For payment processing.
* **Cloudinary**: For image uploads.

---

## 🚀 Step 2: Run the Development Server

Make sure your environment is set up and credentials are added. Then start the Django server:

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👤 Step 3: Create a User Account

Go to:
[http://127.0.0.1:8000/users/api/signup/](http://127.0.0.1:8000/users/api/signup/)

Send a `POST` request with the following JSON:

```json
{
  "email": "user1@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "01712345678",
  "bio": "I'm a test user signing up to this awesome platform.",
  "password": "StrongPass@123",
  "confirm_password": "StrongPass@123"
}
```

💡 *Tip: You can upload a profile picture using the browsable API form. The image will be uploaded to Cloudinary and its URL will be returned.*

---

## 🔓 Step 4: Login to Your Account

Go to:
[http://127.0.0.1:8000/users/api/login/](http://127.0.0.1:8000/users/api/login/)

Send a `POST` request:

```json
{
  "email": "user1@example.com",
  "password": "StrongPass@123"
}
```

Successful response:

```json
{
  "message": "Login successful",
  "your data": {
    "email": "user1@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "01712345678",
    "bio": "I'm a test user signing up to this awesome platform.",
    "profile_image": "https://res.cloudinary.com/your_image_url"
  }
}
```

> ✅ Uses session-based login (cookie authentication).

---

## 👁️ Step 5: View Profile Data

To view the logged-in user's profile:

**GET**
[http://127.0.0.1:8000/users/api/profile/](http://127.0.0.1:8000/users/api/profile/)

> Requires authentication.

---

## 🚪 Step 6: Logout

**GET**
[http://127.0.0.1:8000/users/logout/](http://127.0.0.1:8000/users/logout/)

> Logs out the current session using Django's built-in logout view.

---

## 🔑 Step 7: Password Reset (Forgot Password Flow)

**POST**
[http://127.0.0.1:8000/users/password\_reset/](http://127.0.0.1:8000/users/password_reset/)

> Submit your email to receive a password reset link.

---

## 🛍️ Step 8: View Product List

**GET**
[http://127.0.0.1:8000/products/api/products/list/](http://127.0.0.1:8000/products/api/products/list/)

### 🔍 Optional Query Parameters

| Parameter   | Description                                             |
| ----------- | ------------------------------------------------------- |
| `search`    | Search by product name or description                   |
| `category`  | Filter by category name (e.g., Electronics, Fashion)    |
| `ordering`  | Sort by `price` or `name` (use `-price` for descending) |
| `page`      | Page number (for pagination)                            |
| `page_size` | Items per page (default: 10, max: 100)                  |

---

## 💳 Step 9: Stripe Payment Integration (Test Checkout)

**GET**
`http://127.0.0.1:8000/payments/create-checkout-session/<int:product_id>/`

Example:

```url
http://127.0.0.1:8000/payments/create-checkout-session/1/
```

> Ensure the product with ID `1` exists in your database.

### 📌 Notes:

* Product name and price are pulled from your database.
* This redirects to the Stripe checkout page.
* After test payment, Stripe redirects to your configured success URL.

### 🔮 Stripe Test Card:

```
Card Number: 4242 4242 4242 4242
Exp: Any future date
CVC: Any 3 digits
Zip: Any zip code
```

---

Happy developing! 🚀
