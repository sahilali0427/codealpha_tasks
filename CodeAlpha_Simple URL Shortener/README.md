# Simple URL Shortener

A simple web application built with Flask that converts long URLs into short and easy-to-share links. The project stores URL mappings in a SQLite database and redirects users to the original website when they access the shortened link.

## Features

* Convert long URLs into short links
* Generate unique short codes automatically
* Store URL mappings in a SQLite database
* Redirect users to the original URL
* Simple and beginner-friendly user interface
* Built using Flask and SQLite

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS

## How It Works

1. The user enters a long URL.
2. The application generates a random short code.
3. The original URL and short code are stored in the database.
4. A shortened URL is displayed to the user.
5. When the shortened URL is opened, the application redirects the user to the original website.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/simple-url-shortener.git
```

2. Navigate to the project folder:

```bash
cd simple-url-shortener
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Future Improvements

* Custom short URLs
* Copy-to-clipboard button
* URL analytics and click tracking
* User authentication
* QR code generation

## Learning Outcome

This project helped me understand Flask routing, form handling, database integration using SQLite, URL redirection, and basic frontend development using HTML and CSS.


