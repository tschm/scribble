# ✍️ Scribble

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CodeFactor](https://www.codefactor.io/repository/github/tschm/scribble/badge)](https://www.codefactor.io/repository/github/tschm/scribble)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/renovatebot/renovate)

![Happy Birthday](Happy%20Birthday.png)

## 💫 About

A creative tool for generating artistic text effects,
originally created to design wedding name plates.
Scribble transforms ordinary text into visually
stunning designs by applying mathematical transformations to letter shapes.

## ✨ How It Works

Each letter is represented as a sequence of points with lines connecting them.
These segments are discretized using n=100 points, and then an analytic
function is applied to create beautiful effects on the size, orientation,
and position of all letters in a name.

The underlying idea is inspired by (but implemented differently from)
the [Chebfun Birthday example](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/23972/versions/22/previews/chebfun/examples/fun/html/Birthday.html)
Unlike the original, this implementation doesn't use Chebyshev polynomials,
making it accessible without requiring MATLAB.

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.10+
- Dependencies listed in `requirements.txt`

### 🔧 Installation

```bash

# Clone the repository
git clone https://github.com/tschm/scribble.git
cd scribble

# Install dependencies
make install
```

### 🎨 Running the Application

```bash
# Start the Marimo app
make app

# For development mode
make marimo
```

## 🐳 Docker Support

```bash
# Build and run the Docker container
make build
```

## 📄 License

This project is licensed under the MIT License - see
the [LICENSE](LICENSE) file for details.
