# FastAPI Backend Project

This project is a FastAPI backend application designed to manage gold purchases and user settings, as well as to fetch current and historical gold prices. It is built with PostgreSQL as the database and is containerized using Docker for easy deployment.

## Project Structure

```
fastapi-backend
├── app
│   ├── main.py                  # Entry point of the FastAPI application
│   ├── api                      # Contains API endpoint definitions
│   │   ├── gold_purchases.py    # CRUD operations for gold purchases
│   │   ├── gold_price.py        # Endpoints for fetching gold prices
│   │   └── settings.py          # Endpoints for user settings
│   ├── models                   # Database models
│   │   ├── gold_purchase.py      # GoldPurchase model
│   │   └── settings.py          # Settings model
│   ├── schemas                  # Pydantic schemas for request/response validation
│   │   ├── gold_purchase.py      # Schemas for GoldPurchase
│   │   └── settings.py          # Schemas for Settings
│   ├── crud                     # Database interaction functions
│   │   ├── gold_purchase.py      # CRUD functions for gold purchases
│   │   └── settings.py          # CRUD functions for user settings
│   └── db                       # Database connection setup
│       └── database.py          # SQLAlchemy database session setup
├── alembic                      # Database migration scripts
│   └── env.py                  # Alembic environment setup
├── alembic.ini                  # Alembic configuration
├── requirements.txt             # Project dependencies
├── Dockerfile                   # Docker image build instructions
├── docker-compose.yml           # Docker Compose configuration
├── .env                         # Environment variables
└── README.md                    # Project documentation
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd fastapi-backend
   ```

2. **Create a `.env` File**
   Create a `.env` file in the root directory and add your database connection details:
   ```
   DATABASE_URL=postgresql://user:password@db:5432/database_name
   ```

3. **Build and Run with Docker**
   Use Docker Compose to build and run the application:
   ```bash
   docker-compose up --build
   ```

4. **Access the API**
   The FastAPI application will be available at `http://localhost:8000`. You can access the interactive API documentation at `http://localhost:8000/docs`.

## Usage

- **Gold Purchases API**
  - `GET /gold-purchases`: Retrieve all gold purchases for a user.
  - `POST /gold-purchases`: Create a new gold purchase.
  - `PUT /gold-purchases/{id}`: Update an existing gold purchase.
  - `DELETE /gold-purchases/{id}`: Delete a gold purchase.

- **Gold Price API**
  - `GET /gold-price/current`: Fetch the current gold price.
  - `GET /gold-price/historical`: Fetch historical gold prices for a specified number of days back.
  - `GET /gold-price/historical/{date}`: Fetch the gold price for a specific date.

- **Settings API**
  - `GET /settings`: Retrieve user settings.
  - `PUT /settings`: Update user settings.

## Dependencies

The project uses the following main dependencies:
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

You can install the dependencies using:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.