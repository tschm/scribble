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

The tool creates beautiful visualizations where each letter in a name is
transformed using complex mathematical functions, resulting in unique
artistic patterns that can be used for invitations, decorations, or
personalized gifts.

## ✨ Features

- 🔤 Transform text into artistic visual designs
- 🧮 Apply complex mathematical functions to letter shapes
- 🎭 Choose from multiple transformation functions (tanh, sinh, exp)
- 📝 Customize with different names and event descriptions
- 📥 Download generated designs as PNG images
- 🖥️ Interactive web interface built with Marimo

## 🔍 How It Works

Each letter is represented as a sequence of points with lines connecting them.
These segments are discretized using n=100 points, and then an analytic
function is applied to create beautiful effects on the size, orientation,
and position of all letters in a name.

The process works in several steps:

1. Each letter is defined as a set of points in the complex plane
2. The points are connected by straight line segments
3. Each segment is discretized into 100 points
4. A complex mathematical function (like `sinh(3*z)`) is applied to each point
5. The transformed points are plotted to create the artistic effect

The underlying idea is inspired by (but implemented differently from)
the [Chebfun Birthday example](https://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/23972/versions/22/previews/chebfun/examples/fun/html/Birthday.html).
Unlike the original, this implementation doesn't use Chebyshev polynomials,
making it accessible without requiring MATLAB.

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.12+
- Dependencies:
  - marimo==0.13.15: For the interactive web interface
  - numpy==2.2.3: For numerical operations
  - plotly==6.1.2: For creating interactive visualizations

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/tschm/scribble.git
cd scribble

# Install uv (Python package manager)
make uv
```

### 🎨 Running the Application

```bash
# Start the Marimo app in development mode
make marimo
```

## 🎮 Usage

1. Enter a name in the "Name" field
2. Select a complex function from the dropdown menu
3. Enter an event name (e.g., "Wedding", "Birthday")
4. The visualization will be generated automatically
5. Use the download button to save the image as a PNG file

## 🧪 Testing

The project includes tests to ensure functionality:

```bash
# Run tests
make test
```

This will install the necessary dependencies and run the tests using pytest.

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure everything works (`make test`)
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please make sure to update tests as appropriate.

## 📄 License

This project is licensed under the MIT License - see
the [LICENSE](LICENSE) file for details.
