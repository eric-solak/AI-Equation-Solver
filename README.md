# AI Equation Solver

This project utilizes AI to solve mathematical equations extracted from images and graph the results.

## Features

- **Image to Text Conversion**: Converts mathematical equations from images into machine-readable text using AI.
- **Equation Solving**: Uses AI algorithms to solve mathematical equations extracted from images.
- **Graphing**: Graphs the solved equations to visualize the results.

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Program
   ```bash
   python3 src/main.py images/example1.png
   ```

### 1. Image to Text Conversion
   - Ensure you have images containing mathematical equations in a readable format (typed or handwritten)
   - Program uses `imageParse.py` to extract the equation.

### 2. Equation Solving (Incomplete)
   - After converting images to text, program uses the `equationParse.py` script to solve equations.

### 3. Graphing
   - Program graphs the solved equations using `plotter.py`

## APIs Used

This project utilizes the following Hugging Face APIs:
- [TrOCR Math Handwritten](https://huggingface.co/fhswf/TrOCR_Math_handwritten) for image-to-text conversion.
- [Qwen2.5-Math-1.5B](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B) for equation solving.


## Roadmap

- Transition AI from running locally to the HuggingFace server.
- Implement complete functionality for equation solving and graphing.
- Enhance accuracy and performance of image to text conversion.
