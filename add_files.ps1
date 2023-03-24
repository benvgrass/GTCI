function New-Py-File {
    param (
        $Tld,
        $Fpath,
        $Fname
    )

    New-Item -Path .\$Tld\$Fpath -ItemType Directory
    New-Item -Path .\$Tld\$Fpath\$Fname -ItemType File
    
}

New-Py-File 07-k-merge 01-mergesort-arr merge_sort_arr.py
New-Py-File 07-k-merge 02-ksmallest ksmallest.py
New-Py-File 07-k-merge 03-find-k-pairs find_k_pairs.py
New-Py-File 07-k-merge 04-merge-k-lists merge_k_lists.py
New-Py-File 07-k-merge 05-kth-smallest kth_smallest.py
New-Py-File 07-k-merge 06-median-arrays median_arrays.py

New-Py-File 08-top-k 01-kth-largest kth_largest.py
New-Py-File 08-top-k 02-reorg-string reorg-string.py
New-Py-File 08-top-k 03-k-closest k-closest.py
New-Py-File 08-top-k 04-topk topk.py
New-Py-File 08-top-k 05-kth-largest-arr kth_largest_arr.py
New-Py-File 08-top-k 06-kth-smallest kth_smallest.py

New-Py-File 09-mod-binary 01-search-arr search_arr.py
New-Py-File 09-mod-binary 02-first-bad first_bad.py
New-Py-File 09-mod-binary 03-rand-pick rand_pick.py
New-Py-File 09-mod-binary 04-k-closest k_closest.py
New-Py-File 09-mod-binary 05-single-element single_element.py
New-Py-File 09-mod-binary 06-search-arr-2 search_arr2.py

New-Py-File 10-subsets 01-subsets subset.py
New-Py-File 10-subsets 02-permutations permutations.py
New-Py-File 10-subsets 03-letter-combos letter_combos.py
New-Py-File 10-subsets 04-generate-parentheses parentheses.py
New-Py-File 10-subsets 05-ksum-subsets ksum_subsets.py

New-Py-File 11-greedy 01-jump-game-1 jump_game1.py
New-Py-File 11-greedy 02-boats boats.py
New-Py-File 11-greedy 03-gas-stations gas_stations.py
New-Py-File 11-greedy 04-two-city city_scheduling.py
New-Py-File 11-greedy 05-min-stops min_stops.py
New-Py-File 11-greedy 06-jump-game-2 jump_game2.py

New-Py-File 12-backtracking 01-n-queens n_queens.py
New-Py-File 12-backtracking 02-word-search word_search.py
New-Py-File 12-backtracking 03-house-robber house_robber.py
New-Py-File 12-backtracking 04-restore-ip restore_ip.py
New-Py-File 12-backtracking 05-sudoku sudoku.py
New-Py-File 12-backtracking 06-matchsticks matchsticks.py

New-Py-File 13-dp 01-knapsack knapsack.py
New-Py-File 13-dp 02-coin-change coin_change.py
New-Py-File 13-dp 03-tribonacci tribonacci.py
New-Py-File 13-dp 04-partition-subsum subsum.py
New-Py-File 13-dp 05-word-break word_break.py
New-Py-File 13-dp 06-climbing-stairs climbing_stairs.py

New-Py-File 14-cyclic-sort 01-missing-number missing_number.py
New-Py-File 14-cyclic-sort 02-missing-positive missing_positive.py
New-Py-File 14-cyclic-sort 03-duplicate find_duplicate.py
New-Py-File 14-cyclic-sort 04-corrupt-pair corrupt_pair.py
New-Py-File 14-cyclic-sort 05-k-missing k_missing.py

New-Py-File 15-topological-sort 01-compilation-order compilation_order.py
New-Py-File 15-topological-sort 02-alien-dict alien_dict.py
New-Py-File 15-topological-sort 03-verify-alien verify_alien.py
New-Py-File 15-topological-sort 04-course-schedule-2 course_schedule2.py
New-Py-File 15-topological-sort 05-course-schedule course_schedule.py
New-Py-File 15-topological-sort 06-all-recipes all_recipes.py

New-Py-File 16-stacks 01-basic-calculator calculator.py
New-Py-File 16-stacks 02-remove-dupes remove_duplicates.py
New-Py-File 16-stacks 03-min-remove min_remove.py
New-Py-File 16-stacks 04-execution-time execution_time.py
New-Py-File 16-stacks 05-list-iterator list_iterator.py
New-Py-File 16-stacks 06-valid-parentheses valid_parentheses.py

New-Py-File 17-tree-dfs 01-tree-to-list tree_to_list.py
New-Py-File 17-tree-dfs 02-tree-diameter tree_diameter.py
New-Py-File 17-tree-dfs 03-serialize-tree serialize_tree.py
New-Py-File 17-tree-dfs 04-invert-tree invert_tree.py
New-Py-File 17-tree-dfs 05-max-path-sum max_path.py
New-Py-File 17-tree-dfs 06-max-depth max_depth.py

New-Py-File 18-tree-bfs 01-tree-traversal tree_traversal.py
New-Py-File 18-tree-bfs 02-zigzag-traversal zigzag_traversal.py
New-Py-File 18-tree-bfs 03-populate-pointers populate_pointers.py
New-Py-File 18-tree-bfs 04-vertical-traversal vertical_traversal.py
New-Py-File 18-tree-bfs 05-connect-siblings connect_siblings.py

New-Py-File 19-trie 01-implement-trie trie.py
New-Py-File 19-trie 02-search-suggestions search_suggestions.py
New-Py-File 19-trie 03-replace-words replace_words.py
New-Py-File 19-trie 04-add-search-structure add_search.py
New-Py-File 19-trie 05-word-search-2 word-search2.py
New-Py-File 19-trie 06-lexicographical-numbers lex_nums.py

New-Py-File 20-hash-maps 01-design-hashmap hashmap.py
New-Py-File 20-hash-maps 02-recurring-decimal recurring_decimal.py
New-Py-File 20-hash-maps 03-logger-rate-limiter rate_limiter.py
New-Py-File 20-hash-maps 04-next-greater-element next_greater_element.py
New-Py-File 20-hash-maps 05-isomorphic-strings isomorphic_strings.py
New-Py-File 20-hash-maps 06-longest-palindrome longest_palindrome.py

New-Py-File 21-what-to-track 01-palindrome-permutation palindrome_permutation.py
New-Py-File 21-what-to-track 02-tic-tac-toe tic_tac_toe.py
New-Py-File 21-what-to-track 03-group-anagram anagram.py
New-Py-File 21-what-to-track 04-max-freq-stack max_freq_stack.py
New-Py-File 21-what-to-track 05-first-unique-char first_unique_char.py
New-Py-File 21-what-to-track 06-find-anagrams find_anagrams.py
New-Py-File 21-what-to-track 07-ransom-note ransom_note.py

New-Py-File 22-union-find 01-redundant-connection redundant_connection.py
New-Py-File 22-union-find 02-num-islands num_islands.py
New-Py-File 22-union-find 03-last-day last_day.py
New-Py-File 22-union-find 04-regions-cut regions_cut.py
New-Py-File 22-union-find 05-minimize-malware minimize_malware.py
New-Py-File 22-union-find 06-evaluate-division evaluate_division.py

New-Py-File 23-custom-structs 01-snapshot-array snapshot_array.py
New-Py-File 23-custom-structs 02-time-keystore time_keystore.py
New-Py-File 23-custom-structs 03-lru-cache lru.py
New-Py-File 23-custom-structs 04-insert-delete-getrandom ins_del_getrandom.py
New-Py-File 23-custom-structs 05-min-stack min_stack.py
New-Py-File 23-custom-structs 06-lfu-cache lfu.py

New-Py-File 24-bitwise-manipulation 01-find-diff find_diff.py
New-Py-File 24-bitwise-manipulation 02-complement-base10 base10_comp.py
New-Py-File 24-bitwise-manipulation 03-flip-img img_flip.py
New-Py-File 24-bitwise-manipulation 04-single-number single_number.py
New-Py-File 24-bitwise-manipulation 05-two-single-numbers two_singlenums.py
New-Py-File 24-bitwise-manipulation 06-reverse-bits reverse_bits.py

New-Py-File 25-challenge 01-shortest-bridge shortest_bridge.py
New-Py-File 25-challenge 02-connected-components connected_components.py
New-Py-File 25-challenge 03-ocean-flow ocean_flow.py
New-Py-File 25-challenge 04-contains-duplicate contains_duplicate.py
New-Py-File 25-challenge 05-max-subarray max_subarr.py
New-Py-File 25-challenge 06-two-sum two_sum.py
New-Py-File 25-challenge 07-min-sorted-array find_min.py
New-Py-File 25-challenge 08-non-overlapping-intervals intervals.py
New-Py-File 25-challenge 09-meeting-rooms meeting_rooms.py
New-Py-File 25-challenge 10-largest-rectangle largest_rectangle.py
New-Py-File 25-challenge 11-tree-subtree subtree_of_tree.py
New-Py-File 25-challenge 12-sort-list sort_list.py
New-Py-File 25-challenge 13-num-1bits num_1bits.py
New-Py-File 25-challenge 14-most-water most_water.py
New-Py-File 25-challenge 15-reverse-polish-notation reverse-pol-notation.py
New-Py-File 25-challenge 16-4sum 4sum.py
New-Py-File 25-challenge 17-loud-and-rich loud_and_rich.py
New-Py-File 25-challenge 18-product-array product_of_array.py
New-Py-File 25-challenge 19-longest-inc-subsequence increasing_subsequence.py
New-Py-File 25-challenge 20-sum-two-ints sum_of_two_ints.py
New-Py-File 25-challenge 21-majority-element majority-element.py
New-Py-File 25-challenge 22-unique-paths unique_paths.py
New-Py-File 25-challenge 23-longest-palindromic-substring palindromic_substring.py
New-Py-File 25-challenge 24-permutations-2 permutations2.py
New-Py-File 25-challenge 26-num-provinces provinces.py
New-Py-File 25-challenge 27-topk-words top_k_words.py
New-Py-File 25-challenge 28-list-cycle-2 ll_cycle2.py
New-Py-File 25-challenge 29-min-flips min_flips.py
New-Py-File 25-challenge 30-lemonade-change change.py
New-Py-File 25-challenge 31-house-robber robber.py
New-Py-File 25-challenge 32-disappeared-numbers disappeared.py
New-Py-File 25-challenge 33-find-duplicates duplicates.py
New-Py-File 25-challenge 34-same-tree same_tree.py
New-Py-File 25-challenge 35-in-memory-fs inmemory_fs.py
New-Py-File 25-challenge 36-design-fs fs.py
New-Py-File 25-challenge 37-asteroid-collision asteroid_collision.py
New-Py-File 25-challenge 38-rotting-oranges rotting_oranges.py