#!/bin/bash

# Parent folder
PARENT="NeetCode Problems"
mkdir -p "$PARENT"
cd "$PARENT" || exit

# Global problem counter
counter=1

# Helper function to create problem folders inside a category
create_problems() {
    local category_dir="$1"
    shift
    local problems=("$@")
    mkdir -p "$category_dir"
    cd "$category_dir" || exit
    for problem in "${problems[@]}"; do
        # folder name: "1. Contains Duplicate"
        local folder="${counter}. ${problem}"
        mkdir -p "$folder"
        touch "$folder/solution.py" "$folder/explanation.md"
        ((counter++))
    done
    cd ..
}

# =============================================
# 01. Arrays & Hashing
# =============================================
ah_problems=("Contains Duplicate" "Valid Anagram" "Two Sum" "Group Anagrams" \
    "Top K Frequent Elements" "Product of Array Except Self" "Valid Sudoku" \
    "Encode And Decode Strings" "Longest Consecutive Sequence")
create_problems "01. Arrays & Hashing" "${ah_problems[@]}"

# =============================================
# 02. Two Pointers
# =============================================
tp_problems=("Valid Palindrome" "Two Sum II Input Array Is Sorted" "3Sum" \
    "Container With Most Water" "Trapping Rain Water")
create_problems "02. Two Pointers" "${tp_problems[@]}"

# =============================================
# 03. Sliding Window
# =============================================
sw_problems=("Best Time to Buy And Sell Stock" "Longest Substring Without Repeating Characters" \
    "Longest Repeating Character Replacement" "Permutation In String" \
    "Minimum Window Substring" "Sliding Window Maximum")
create_problems "03. Sliding Window" "${sw_problems[@]}"

# =============================================
# 04. Stack
# =============================================
st_problems=("Valid Parentheses" "Min Stack" "Evaluate Reverse Polish Notation" \
    "Generate Parentheses" "Daily Temperatures" "Car Fleet" "Largest Rectangle In Histogram")
create_problems "04. Stack" "${st_problems[@]}"

# =============================================
# 05. Binary Search
# =============================================
bs_problems=("Binary Search" "Search a 2D Matrix" "Koko Eating Bananas" \
    "Search In Rotated Sorted Array" "Find Minimum In Rotated Sorted Array" \
    "Time Based Key Value Store" "Median of Two Sorted Arrays")
create_problems "05. Binary Search" "${bs_problems[@]}"

# =============================================
# 06. Linked List
# =============================================
ll_problems=("Reverse Linked List" "Merge Two Sorted Lists" "Reorder List" \
    "Remove Nth Node From End of List" "Copy List With Random Pointer" \
    "Add Two Numbers" "Linked List Cycle" "Find The Duplicate Number" \
    "LRU Cache" "Merge K Sorted Lists" "Reverse Nodes In K Group")
create_problems "06. Linked List" "${ll_problems[@]}"

# =============================================
# 07. Trees
# =============================================
tr_problems=("Invert Binary Tree" "Maximum Depth of Binary Tree" "Diameter of Binary Tree" \
    "Balanced Binary Tree" "Same Tree" "Subtree of Another Tree" \
    "Lowest Common Ancestor of a Binary Search Tree" "Binary Tree Level Order Traversal" \
    "Binary Tree Right Side View" "Count Good Nodes In Binary Tree" \
    "Validate Binary Search Tree" "Kth Smallest Element In a Bst" \
    "Construct Binary Tree From Preorder And Inorder Traversal" \
    "Binary Tree Maximum Path Sum" "Serialize And Deserialize Binary Tree")
create_problems "07. Trees" "${tr_problems[@]}"

# =============================================
# 08. Heap / Priority Queue
# =============================================
hp_problems=("Kth Largest Element In a Stream" "Last Stone Weight" \
    "K Closest Points to Origin" "Kth Largest Element In An Array" \
    "Task Scheduler" "Design Twitter" "Find Median From Data Stream")
create_problems "08. Heap_Priority Queue" "${hp_problems[@]}"

# =============================================
# 09. Backtracking
# =============================================
bt_problems=("Subsets" "Combination Sum" "Permutations" "Subsets II" \
    "Combination Sum II" "Word Search" "Palindrome Partitioning" \
    "Letter Combinations of a Phone Number" "N Queens")
create_problems "09. Backtracking" "${bt_problems[@]}"

# =============================================
# 10. Tries
# =============================================
trie_problems=("Implement Trie Prefix Tree" "Design Add And Search Words Data Structure" \
    "Word Search II")
create_problems "10. Tries" "${trie_problems[@]}"

# =============================================
# 11. Graphs
# =============================================
gr_problems=("Number of Islands" "Clone Graph" "Max Area of Island" \
    "Pacific Atlantic Water Flow" "Surrounded Regions" "Rotting Oranges" \
    "Walls And Gates" "Course Schedule" "Course Schedule II" \
    "Redundant Connection" "Number of Connected Components In An Undirected Graph" \
    "Graph Valid Tree" "Word Ladder")
create_problems "11. Graphs" "${gr_problems[@]}"

# =============================================
# 12. Advanced Graphs
# =============================================
ag_problems=("Reconstruct Itinerary" "Min Cost to Connect All Points" \
    "Network Delay Time" "Swim In Rising Water" "Alien Dictionary" \
    "Cheapest Flights Within K Stops")
create_problems "12. Advanced Graphs" "${ag_problems[@]}"

# =============================================
# 13. 1-D Dynamic Programming
# =============================================
dp1_problems=("Climbing Stairs" "Min Cost Climbing Stairs" "House Robber" \
    "House Robber II" "Longest Palindromic Substring" "Palindromic Substrings" \
    "Decode Ways" "Coin Change" "Maximum Product Subarray" "Word Break" \
    "Longest Increasing Subsequence" "Partition Equal Subset Sum")
create_problems "13. 1-D Dynamic Programming" "${dp1_problems[@]}"

# =============================================
# 14. 2-D Dynamic Programming
# =============================================
dp2_problems=("Unique Paths" "Longest Common Subsequence" \
    "Best Time to Buy And Sell Stock With Cooldown" "Coin Change II" \
    "Target Sum" "Interleaving String" "Longest Increasing Path In a Matrix" \
    "Distinct Subsequences" "Edit Distance" "Burst Balloons" \
    "Regular Expression Matching")
create_problems "14. 2-D Dynamic Programming" "${dp2_problems[@]}"

# =============================================
# 15. Greedy
# =============================================
gr_problems2=("Maximum Subarray" "Jump Game" "Jump Game II" "Gas Station" \
    "Hand of Straights" "Merge Triplets to Form Target Triplet" \
    "Partition Labels" "Valid Parenthesis String")
create_problems "15. Greedy" "${gr_problems2[@]}"

# =============================================
# 16. Intervals
# =============================================
int_problems=("Insert Interval" "Merge Intervals" "Non Overlapping Intervals" \
    "Meeting Rooms" "Meeting Rooms II" "Minimum Interval to Include Each Query")
create_problems "16. Intervals" "${int_problems[@]}"

# =============================================
# 17. Math & Geometry
# =============================================
mg_problems=("Rotate Image" "Spiral Matrix" "Set Matrix Zeroes" "Happy Number" \
    "Plus One" "Pow(x, n)" "Multiply Strings" "Detect Squares")
create_problems "17. Math & Geometry" "${mg_problems[@]}"

# =============================================
# 18. Bit Manipulation
# =============================================
bm_problems=("Single Number" "Number of 1 Bits" "Counting Bits" "Reverse Bits" \
    "Missing Number" "Sum of Two Integers" "Reverse Integer")
create_problems "18. Bit Manipulation" "${bm_problems[@]}"

echo "✅ Folder structure with global numbering (1–150) created inside 'Anki - NeetCode'"