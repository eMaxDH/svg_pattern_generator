# SVG Pattern Matrix Generator

This Python script generates a matrix of patterns from an input SVG file. The user can define the gap between patterns, the shift for a secondary matrix, and the number of replications. Gaps and shifts are specified as percentages of the original pattern's dimensions.

## Features

- Create a matrix of replicated SVG patterns.
- Define gaps and shifts as percentages of the original SVG dimensions.
- Supports a secondary shifted matrix for added flexibility.
- Customize the number of replications in each direction.

## Prerequisites

- Python 3.x
- Required libraries:
  - `argparse`
  - `xml.etree.ElementTree`

## Installation

1. Clone or download the repository.
2. Install the required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```bash
python pattern_matrix.py input.svg output.svg --gap_x_percent 20 --gap_y_percent 20 --shift_x_percent 50 --shift_y_percent 50 --replications 5
```

### Arguments

- `input.svg`: Path to the input SVG file.
- `output.svg`: Path to save the output SVG file.
- `--gap_x_percent`: (Optional) Horizontal gap as a percentage of the original pattern's width. Default is 10.
- `--gap_y_percent`: (Optional) Vertical gap as a percentage of the original pattern's height. Default is 10.
- `--shift_x_percent`: (Optional) Horizontal shift for the secondary matrix as a percentage of the original width. Default is 50.
- `--shift_y_percent`: (Optional) Vertical shift for the secondary matrix as a percentage of the original height. Default is 50.
- `--replications`: (Optional) Number of replications in each direction. Default is 5.

## Example

To generate a pattern matrix with a 10% gap, a secondary matrix shifted by 55% in both directions, and 5 replications in x and 8 in y:

```bash
python3 pattern_generator.py input/fabric_single.svg output/fabric.svg --gap_x_percent 10 --gap_y_percent 1
0 --shift_x_percent 55 --shift_y_percent 55 --replications_x 5 --replications_y 8
```

## Output

The script generates a new SVG file with the pattern matrix based on the specified parameters.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
