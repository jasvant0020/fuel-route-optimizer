# Fuel Route Optimizer API

## Overview
A Django REST API that processes fuel station data and provides optimized search, filtering, and analytics features.

---

## Features
- Cheapest fuel station finder
- Filter stations by state
- Filter by price range
- Sorting (price ascending/descending)
- Pagination support
- Cached CSV data loading (performance optimized)
- Swagger API documentation

---

## Tech Stack
- Django
- Django REST Framework
- Pandas
- drf-yasg (Swagger)

---

## API Endpoints

### Get cheapest station
GET /api/fuel/cheapest/

### Get stations
GET /api/fuel/stations/

Query Params:
- states=TX,CA
- min_price=2.5
- max_price=3.5
- ordering=price | -price
- page=1
- page_size=10

### Available states
GET /api/fuel/states/

---

## Swagger Docs
http://127.0.0.1:8000/swagger/