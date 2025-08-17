# ALX Travel App 🌍

A comprehensive Django REST API for managing travel listings, bookings, and payments with integrated Chapa payment gateway.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Payment Integration](#payment-integration)
- [Database Models](#database-models)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Travel Listings Management**: Create, read, update, and delete travel packages
- **Booking System**: Complete booking functionality for travel packages
- **Payment Integration**: Integrated with Chapa payment gateway for secure transactions
- **Review System**: Allow users to leave reviews and ratings for listings
- **RESTful API**: Well-structured REST API with proper serialization
- **API Documentation**: Swagger/OpenAPI documentation
- **Asynchronous Tasks**: Celery integration for background tasks (email notifications)
- **CORS Support**: Cross-origin resource sharing enabled for frontend integration

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5, Django REST Framework
- **Database**: MySQL
- **Payment Gateway**: Chapa (Ethiopian payment processor)
- **Task Queue**: Celery
- **API Documentation**: drf-yasg (Swagger)
- **Environment Management**: django-environ

## 📁 Project Structure

```
alx_travel_app_0x02/
├── alx_travel_app/
│   ├── listings/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed.py
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── .gitignore
├── manage.py
├── README.md
└── LICENSE
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Derick-Obeng/alx_travel_app_0x02.git
   cd alx_travel_app_0x02
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip3 install django djangorestframework django-cors-headers django-environ drf-yasg mysqlclient celery
   ```

## ⚙️ Configuration

1. **Create a `.env` file in the project root**
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   
   # Database Configuration
   MYSQL_DB=your_database_name
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   
   # Chapa Payment Gateway
   CHAPA_SECRET_KEY=your-chapa-secret-key
   ```

2. **Database Setup**
   ```bash
   # Create and run migrations
   python manage.py makemigrations
   python manage.py migrate
   
   # Create a superuser
   python manage.py createsuperuser
   ```

## 🔗 API Endpoints

### Listings
- `GET /api/listings/` - Get all travel listings
- `POST /api/listings/` - Create a new listing
- `GET /api/listings/{id}/` - Get specific listing
- `PUT /api/listings/{id}/` - Update listing
- `DELETE /api/listings/{id}/` - Delete listing

### Bookings
- `GET /api/bookings/` - Get all bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Get specific booking
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Delete booking

### Payments
- `POST /api/initiate-payment/{booking_id}/` - Initiate payment for booking
- `GET /api/verify-payment/{tx_ref}/` - Verify payment status

### Documentation
- `GET /swagger/` - Swagger API documentation

## 💳 Payment Integration

The application integrates with **Chapa**, a popular Ethiopian payment gateway:

- **Payment Initiation**: Creates payment record and redirects to Chapa checkout
- **Payment Verification**: Verifies payment status and updates booking
- **Webhook Support**: Handles payment callbacks from Chapa
- **Email Notifications**: Sends confirmation emails via Celery tasks

## 🗄️ Database Models

### Listing
- Title, description, location
- Price and creation timestamp
- Related bookings and reviews

### Booking
- Links to listing and user
- Guest information (name, email)
- Date range (start_date, end_date)
- Booking timestamp

### Payment
- Links to booking
- Amount and Chapa transaction reference
- Status tracking (PENDING, COMPLETED, FAILED)

### Review
- Links to listing
- Reviewer information and rating
- Comment and timestamp

## 🏃‍♂️ Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - API Base URL: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`
   - API Documentation: `http://localhost:8000/swagger/`

3. **Start Celery (for background tasks)**
   ```bash
   celery -A alx_travel_app worker --loglevel=info
   ```

## 📚 API Documentation

Interactive API documentation is available at `/swagger/` when running the development server. This provides:

- Complete endpoint documentation
- Request/response schemas
- Interactive testing interface
- Authentication requirements

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Derick Obeng** - *Initial work* - [GitHub](https://github.com/Derick-Obeng)

## 🙏 Acknowledgments

- ALX Software Engineering Program
- Django and Django REST Framework communities
- Chapa payment gateway for Ethiopian market integration

---

**Note**: This project is part of the ALX Software Engineering curriculum and demonstrates full-stack development skills with Django, REST APIs, payment integration, and modern web development practices.