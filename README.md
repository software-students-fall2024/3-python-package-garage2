# Python Package Exercise

An exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

# 🔮 Fortunes
![Build Status](https://github.com/yourusername/fortunes/actions/workflows/ci.yml/badge.svg) [![PyPI Version](https://badge.fury.io/py/fortunes.svg)](https://pypi.org/project/fortunes/)

## 👥 Team Members
- [Yuhao Sheng (ys4689)](https://github.com/imyhalex)
- [Ryoma Nagano (rn2247)](https://github.com/RYOMA-NAGANO)
- [Qiyun Yin (qy765)](https://github.com/Bryccce)
- [Andrea Tang (xt2073)](https://github.com/AndreaTang123)

## Description

`Fortunes` is a delightful Python package that brings a touch of randomness and inspiration into your projects. Whether you're looking for a daily dose of wisdom, a lucky number, or the ability to send personalized fortunes via email, Fortunes has you covered.

### Features
- __Random Fortune Generation:__ Retrieve one or multiple unique fortunes along with lucky numbers.
- __Email Integration:__ Send personalized fortunes to any email address effortlessly.
- __Customizable Quotes:__ Get your own collection of fortunes and quotes.

## 📦 Installation
Install the latest version of Fortunes from PyPI using `pip`:
```bash
pip install fortune.package
```

## 📖 Documentation

__Importing Fortunes into Your Project__

To start using Fortunes in your Python code, simply import the desired functions:

```python
from fortunes.random_fortune import get_fortune_cookie
from fortunes.get_quotes_by_author import get_quotes_by_author
from fortunes.send_email import send_fortune_email
from fortunes.getMultipleFortunes import getMultipleFortunes

# Example Usage:
fortune = get_fortune_cookie()
print(fortune)

quotes = get_quotes_by_author(quotes_dict)
print(quotes)

send_fortune_email("recipient@example.com", fortune)

multiple_fortunes = getMultipleFortunes(3)
for f in multiple_fortunes:
    print(f)
```

### Function Documentation

#### `get_fortune_cookie()`

**Description:**  
Generates a single random fortune along with a lucky number.

**Usage:**

```python
from fortunes.random_fortune import get_fortune_cookie

fortune = get_fortune_cookie()
print(fortune)
```

**Output Example:**

```
🔮 Your Fortune: Good luck is on the way!
🍀 Your Lucky Number: 42
```


#### `get_quotes_by_author(quotes_dict)`

**Description:**  
Retrieves quotes from a specified author. Users can choose to get one or multiple quotes.

**Usage:**

```python
from fortunes.get_quotes_by_author import get_quotes_by_author

quotes_dict = {
    "Albert Claude": [
        "Once Ptolemy and Plato, yesterday Newton, today Einstein, and tomorrow new faiths, new beliefs, and new dimensions.",
        "When I went to the University, the medical school was the only place where one could hope to find the means to study life, its nature, its origins, and its ills.",
        "Looking back 25 years later, what I may say is that the facts have been far better than the dreams. In the long course of cell life on this earth it remained, for our age for our generation, to receive the full ownership of our inheritance.",
    ],
    "Mikhail Bakunin": [
        "The urge to destroy is also a creative urge.",
        "If God really existed, it would be necessary to abolish Him.",
        "People go to church for the same reasons they go to a tavern: to stupefy themselves, to forget their misery, to imagine themselves, for a few minutes anyway, free and happy."
    ]
}

quotes = get_quotes_by_author(quotes_dict)
print(quotes)
```

**Output Example:**

```
🔮 Your Fortune: The urge to destroy is also a creative urge.
🍀 Your Lucky Number: 17
~ Mikhail Bakunin

🔮 Your Fortune: If God really existed, it would be necessary to abolish Him.
🍀 Your Lucky Number: 23
~ Mikhail Bakunin
```


#### `send_fortune_email(recipient_email, fortune)`

**Description:**  
Sends a fortune to the specified email address.

**Usage:**

```python
from fortunes.send_email import send_fortune_email

recipient = "friend@example.com"
fortune = "🔮 Your Fortune: Happiness is around the corner.\n🍀 Your Lucky Number: 12"

send_fortune_email(recipient, fortune)
```

**Note:**  
Ensure that you have the necessary SMTP configurations and environment variables set up before using this function.



#### `getMultipleFortunes(n)`

**Description:**  
Generates multiple unique fortunes based on the number specified.

**Usage:**

```python
from fortunes.getMultipleFortunes import getMultipleFortunes

fortunes = getMultipleFortunes(3)
for f in fortunes:
    print(f)
```

**Output Example:**

```
🔮 Your Fortune: Fortune 1
🍀 Your Lucky Number: 42

🔮 Your Fortune: Fortune 2
🍀 Your Lucky Number: 88

🔮 Your Fortune: Fortune 3
🍀 Your Lucky Number: 7
```

### 📂 Example Programs

For comprehensive examples of how to use Fortunes in real-world scenarios, refer to our [examples](https://github.com/yourusername/fortunes/tree/main/examples) directory on GitHub.



## 🤝 Contributing

We welcome contributions from the community! Here's how you can get started:

### 🛠️ Setup Development Environment

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/fortunes.git
   cd fortunes
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -e .[dev]
   ```

   *This installs the package in editable mode along with development dependencies.*

4. **Run Tests:**

   Ensure that all tests pass before making changes.

   ```bash
   pytest
   ```

### Making Changes

1. **Create a New Branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement Your Changes:**

   Make your desired changes to the codebase.

3. **Run Tests:**

   Ensure that your changes do not break existing functionality.

   ```bash
   pytest
   ```

4. **Commit and Push:**

   ```bash
   git add .
   git commit -m "Add feature: your-feature-description"
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request:**

   Navigate to the repository on GitHub and open a pull request detailing your changes.

### 📝 Guidelines

- **Follow PEP 8:** Ensure your code adheres to Python's style guidelines.
- **Write Tests:** Add tests for new features or bug fixes.
- **Document Your Code:** Update documentation to reflect changes.


## 🚀 Getting Started

### 📋 Prerequisites

- **Python 3.10+**
- **pip**
- **Virtual Environment Tool** (optional)

### 🛠️ Configuration and Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/fortunes.git
   cd fortunes
   ```

2. **Set Up Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -e .[dev]
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the root directory with the following content:

   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your_email@gmail.com
   SMTP_PASSWORD=your_email_password
   ```

   **Note:** Replace the placeholders with your actual SMTP server details and credentials.

5. **Import Starter Data:**

   If your project requires starter data (e.g., initial fortunes or quotes), ensure they are placed in the appropriate directories or imported using provided scripts.

### Running the Project

1. **Generating a Fortune:**

   ```python
   from fortunes.random_fortune import get_fortune_cookie

   fortune = get_fortune_cookie()
   print(fortune)
   ```

2. **Sending a Fortune via Email:**

   ```python
   from fortunes.send_email import send_fortune_email

   recipient = "friend@example.com"
   fortune = "🔮 Your Fortune: Happiness is around the corner.\n🍀 Your Lucky Number: 12"

   send_fortune_email(recipient, fortune)
   ```

3. **Retrieving Quotes by Author:**

   ```python
   from fortunes.get_quotes_by_author import get_quotes_by_author

   quotes_dict = {
       "Albert Claude": [
           "Once Ptolemy and Plato, yesterday Newton, today Einstein, and tomorrow new faiths, new beliefs, and new dimensions.",
           # Add more quotes...
       ],
       # Add more authors...
   }

   quotes = get_quotes_by_author(quotes_dict)
   for q in quotes:
       print(q)
   ```

### Platform Compatibility

Fortunes is designed to work seamlessly across all major platforms, including:

- **Windows**
- **macOS**
- **Linux**

Ensure that Python 3.10 or higher is installed on your system.

---

## 🔒 Handling Secret Configuration Files (Optional)

**Important:**  
Configuration files containing sensitive information, such as `.env`, are **not** included in the version control repository for security reasons.

### 📄 Creating a `.env` File

1. **Create the File:**

   In the root directory of your project, create a file named `.env`.

2. **Add the Following Content:**

   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USERNAME=your_email@gmail.com
   SMTP_PASSWORD=your_email_password
   ```

   **Explanation of Variables:**

   - `SMTP_SERVER`: The address of your SMTP server.
   - `SMTP_PORT`: The port number for your SMTP server (commonly `587` for TLS).
   - `SMTP_USERNAME`: Your SMTP server username (usually your email address).
   - `SMTP_PASSWORD`: Your SMTP server password.

3. **Secure Your Credentials:**

   - **Do Not Share:** Never share your `.env` file or its contents publicly.
   - **Add to `.gitignore`:** Ensure that your `.env` file is listed in `.gitignore` to prevent it from being tracked by Git.

   ```gitignore
   # .gitignore
   __pycache__/
   *.pyc
   build/
   dist/
   *.egg-info/
   .env
   ```