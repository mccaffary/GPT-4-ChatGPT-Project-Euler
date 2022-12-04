#!/bin/bash
ground_truth_values=(233168 4613732 6857 906609 232792560 25164150 104743 23514624000 31875000 142913828922 70600674 76576500 5537376230 837799 137846528820 1366 21124 1074 171 648 31626 871198282 4179871 2783915460 4782 983 -59231 669171001 9183 443839)

for i in "${!ground_truth_values[@]}"; do
    ground_truth_val="${ground_truth_values[i]}"
    #echo $ground_truth_val
    #echo ""$i+1" : $ground_truth_val"
    echo "$((i+1)) : $ground_truth_val"
done
