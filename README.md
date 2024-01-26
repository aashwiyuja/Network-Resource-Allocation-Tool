# Network Resource Allocation Tool

This Python script generates input files for a network resource allocation problem. It allows users to define the number of ports for each switch, the migration coefficient, and various parameters related to VM pairs and middleboxes. The generated input file follows the format required for solving a minimum-cost flow problem.

## Usage

1. Run the script.
2. Input the number of ports each switch should have.
3. Input the migration coefficient.
4. Specify the number of VM pairs.
5. If the number of ports is less than the number of VM pairs, provide additional information about middleboxes, initial resource capacity of each PM, and other parameters.
6. The script will generate an input file named "scf_migration.inp" containing the details of the network resource allocation problem.


Please note that the generated random numbers for arc parameters ensure variety in the input file.

## Requirements

- Python 3
