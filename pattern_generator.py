import xml.etree.ElementTree as ET
import argparse
from copy import deepcopy

def strip_units(value):
    """ Strip the units from a value and convert to float. """
    return float(value.rstrip('mm').rstrip('cm').rstrip('px'))

def create_pattern_matrix(svg_file, output_file, gap_x_percent, gap_y_percent, shift_x_percent, shift_y_percent, replications_x, replications_y):
    # Parse the input SVG file
    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Get the dimensions of the original pattern
    width = strip_units(root.attrib['width'])
    height = strip_units(root.attrib['height'])

    # Calculate the gap and shift values based on percentages
    gap_x = width * (gap_x_percent / 100.0)
    gap_y = height * (gap_y_percent / 100.0)
    shift_x = width * (shift_x_percent / 100.0)
    shift_y = height * (shift_y_percent / 100.0)

    # Create a new SVG root
    new_svg = ET.Element('svg', attrib={
        'xmlns': 'http://www.w3.org/2000/svg',
        'width': f'{(width + gap_x) * replications_x + shift_x}px',
        'height': f'{(height + gap_y) * replications_y + shift_y}px',
    })

    def add_pattern(x, y, original_content):
        g = ET.Element('g', attrib={'transform': f'translate({x},{y})'})
        for elem in deepcopy(original_content):
            g.append(elem)
        new_svg.append(g)

    original_content = list(root)

    # Create the first array
    for i in range(replications_x):  # Adjust the range for more patterns
        for j in range(replications_y):  # Adjust the range for more patterns
            add_pattern(i * (width + gap_x), j * (height + gap_y), original_content)

    # Create the second array with a shift
    for i in range(replications_x):  # Adjust the range for more patterns
        for j in range(replications_y):  # Adjust the range for more patterns
            add_pattern(i * (width + gap_x) + shift_x, j * (height + gap_y) + shift_y, original_content)

    # Write the new SVG to a file
    tree = ET.ElementTree(new_svg)
    tree.write(output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a matrix of patterns from an SVG file.')
    parser.add_argument('svg_file', type=str, help='Input SVG file')
    parser.add_argument('output_file', type=str, help='Output SVG file')
    parser.add_argument('--gap_x_percent', type=float, default=10, help='Gap between columns as a percentage of the original width')
    parser.add_argument('--gap_y_percent', type=float, default=10, help='Gap between rows as a percentage of the original height')
    parser.add_argument('--shift_x_percent', type=float, default=50, help='Shift in x direction for the second array as a percentage of the original width')
    parser.add_argument('--shift_y_percent', type=float, default=50, help='Shift in y direction for the second array as a percentage of the original height')
    parser.add_argument('--replications_x', type=int, default=5, help='Number of replications in x direction')
    parser.add_argument('--replications_y', type=int, default=5, help='Number of replications in y direction')

    args = parser.parse_args()

    create_pattern_matrix(args.svg_file, args.output_file, args.gap_x_percent, args.gap_y_percent, args.shift_x_percent, args.shift_y_percent, args.replications_x, args.replications_y)
