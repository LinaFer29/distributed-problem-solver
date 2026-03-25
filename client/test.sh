#!/bin/bash

YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Assigning default file names
command="./" #If the code is not compiled, please ue here the interpreter
executable="client"
arguments=" problemSolver fizzbuzz 10 100 400 print"
expected_output="expected_output.txt"
generated_output="output.txt"
diff_output="diff_output.txt"

if [ $# -eq 1 ]; then
  executable=$1
elif [ $# -eq 2 ]; then
  executable=$1
  expected_output=$2
elif [ $# -eq 3 ]; then
  executable=$1
  expected_output=$2
  generated_output=$3
elif [ $# -gt 3 ]; then
  echo "Usage: $0 [executable name] [expected output name] [generated output name]"
  echo "       If no arguments are provided, defaults names are assigned: 'main', 'expected_output.txt' and 'generated_output.txt'"
  exit 1
fi

#Compiles the executable
go build -o $executable

# Check if the executable exists
if [ ! -f "$executable" ]; then   
  echo -e "${YELLOW}Executable $executable not found.${NC}"
  exit 1
fi




echo -e "Invoking $command$executable$arguments"
$command$executable$arguments > $generated_output

bash file_compare.sh $expected_output $generated_output $diff_output