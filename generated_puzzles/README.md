# Generated puzzle performance

| Combination | Mean solve time (s) | Mean expanded states |
|---|---:|---:|
| [7x7_3box](7x7_3box/) | 0.008422 | 108.8 |
| [8x8_3box](8x8_3box/) | 0.018453 | 173.3 |
| [8x8_4box](8x8_4box/) | 0.027364 | 233.1 |
| [9x9_3box](9x9_3box/) | 0.062690 | 642.8 |
| [9x9_4box](9x9_4box/) | 0.041018 | 345.7 |
| [9x9_5box](9x9_5box/) | 0.037740 | 234.8 |
| [10x10_3box](10x10_3box/) | 0.027093 | 141.9 |
| [10x10_4box](10x10_4box/) | 0.071856 | 385.3 |
| [10x10_5box](10x10_5box/) | 0.012032 | 79.6 |
| [10x10_6box](10x10_6box/) | 0.291884 | 1362.3 |
| [10x10_7box](10x10_7box/) | 0.128352 | 589.5 |
| [10x10_8box](10x10_8box/) | 0.756517 | 2899.0 |

All boards met the generator's difficulty 5 criteria. IDA* ran once per board with a 60-second limit. Mean solve time uses solved runs. Mean expanded states uses all runs. Timing covers `solve()`. Solutions were replayed to verify each push and the final goal state.

## Per-puzzle results

| Test folder | Input | Boxes | Pushes | Expanded states | Solve time (s) |
|---|---|---:|---:|---:|---:|
| [7x7_3box](7x7_3box/) | [7x7_3box_01.txt](7x7_3box/7x7_3box_01.txt) | 3 | 17 | 20 | 0.005307 |
| [7x7_3box](7x7_3box/) | [7x7_3box_02.txt](7x7_3box/7x7_3box_02.txt) | 3 | 16 | 269 | 0.016761 |
| [7x7_3box](7x7_3box/) | [7x7_3box_03.txt](7x7_3box/7x7_3box_03.txt) | 3 | 18 | 38 | 0.002195 |
| [7x7_3box](7x7_3box/) | [7x7_3box_04.txt](7x7_3box/7x7_3box_04.txt) | 3 | 16 | 97 | 0.006557 |
| [7x7_3box](7x7_3box/) | [7x7_3box_05.txt](7x7_3box/7x7_3box_05.txt) | 3 | 17 | 127 | 0.012342 |
| [7x7_3box](7x7_3box/) | [7x7_3box_06.txt](7x7_3box/7x7_3box_06.txt) | 3 | 16 | 170 | 0.015073 |
| [7x7_3box](7x7_3box/) | [7x7_3box_07.txt](7x7_3box/7x7_3box_07.txt) | 3 | 16 | 71 | 0.007419 |
| [7x7_3box](7x7_3box/) | [7x7_3box_08.txt](7x7_3box/7x7_3box_08.txt) | 3 | 16 | 154 | 0.010574 |
| [7x7_3box](7x7_3box/) | [7x7_3box_09.txt](7x7_3box/7x7_3box_09.txt) | 3 | 17 | 37 | 0.001673 |
| [7x7_3box](7x7_3box/) | [7x7_3box_10.txt](7x7_3box/7x7_3box_10.txt) | 3 | 16 | 105 | 0.006320 |
| [8x8_3box](8x8_3box/) | [8x8_3box_01.txt](8x8_3box/8x8_3box_01.txt) | 3 | 16 | 16 | 0.001158 |
| [8x8_3box](8x8_3box/) | [8x8_3box_02.txt](8x8_3box/8x8_3box_02.txt) | 3 | 19 | 747 | 0.078736 |
| [8x8_3box](8x8_3box/) | [8x8_3box_03.txt](8x8_3box/8x8_3box_03.txt) | 3 | 27 | 27 | 0.002603 |
| [8x8_3box](8x8_3box/) | [8x8_3box_04.txt](8x8_3box/8x8_3box_04.txt) | 3 | 16 | 43 | 0.005142 |
| [8x8_3box](8x8_3box/) | [8x8_3box_05.txt](8x8_3box/8x8_3box_05.txt) | 3 | 18 | 259 | 0.029142 |
| [8x8_3box](8x8_3box/) | [8x8_3box_06.txt](8x8_3box/8x8_3box_06.txt) | 3 | 22 | 494 | 0.054653 |
| [8x8_3box](8x8_3box/) | [8x8_3box_07.txt](8x8_3box/8x8_3box_07.txt) | 3 | 20 | 23 | 0.001970 |
| [8x8_3box](8x8_3box/) | [8x8_3box_08.txt](8x8_3box/8x8_3box_08.txt) | 3 | 16 | 37 | 0.004465 |
| [8x8_3box](8x8_3box/) | [8x8_3box_09.txt](8x8_3box/8x8_3box_09.txt) | 3 | 16 | 16 | 0.001249 |
| [8x8_3box](8x8_3box/) | [8x8_3box_10.txt](8x8_3box/8x8_3box_10.txt) | 3 | 21 | 71 | 0.005415 |
| [8x8_4box](8x8_4box/) | [8x8_4box_01.txt](8x8_4box/8x8_4box_01.txt) | 4 | 22 | 151 | 0.020273 |
| [8x8_4box](8x8_4box/) | [8x8_4box_02.txt](8x8_4box/8x8_4box_02.txt) | 4 | 18 | 550 | 0.077588 |
| [8x8_4box](8x8_4box/) | [8x8_4box_03.txt](8x8_4box/8x8_4box_03.txt) | 4 | 17 | 235 | 0.029754 |
| [8x8_4box](8x8_4box/) | [8x8_4box_04.txt](8x8_4box/8x8_4box_04.txt) | 4 | 33 | 33 | 0.002530 |
| [8x8_4box](8x8_4box/) | [8x8_4box_05.txt](8x8_4box/8x8_4box_05.txt) | 4 | 17 | 152 | 0.023830 |
| [8x8_4box](8x8_4box/) | [8x8_4box_06.txt](8x8_4box/8x8_4box_06.txt) | 4 | 18 | 113 | 0.007664 |
| [8x8_4box](8x8_4box/) | [8x8_4box_07.txt](8x8_4box/8x8_4box_07.txt) | 4 | 17 | 34 | 0.003043 |
| [8x8_4box](8x8_4box/) | [8x8_4box_08.txt](8x8_4box/8x8_4box_08.txt) | 4 | 16 | 16 | 0.002026 |
| [8x8_4box](8x8_4box/) | [8x8_4box_09.txt](8x8_4box/8x8_4box_09.txt) | 4 | 17 | 17 | 0.001678 |
| [8x8_4box](8x8_4box/) | [8x8_4box_10.txt](8x8_4box/8x8_4box_10.txt) | 4 | 26 | 1030 | 0.105255 |
| [9x9_3box](9x9_3box/) | [9x9_3box_01.txt](9x9_3box/9x9_3box_01.txt) | 3 | 32 | 5680 | 0.534407 |
| [9x9_3box](9x9_3box/) | [9x9_3box_02.txt](9x9_3box/9x9_3box_02.txt) | 3 | 22 | 22 | 0.002374 |
| [9x9_3box](9x9_3box/) | [9x9_3box_03.txt](9x9_3box/9x9_3box_03.txt) | 3 | 23 | 24 | 0.002276 |
| [9x9_3box](9x9_3box/) | [9x9_3box_04.txt](9x9_3box/9x9_3box_04.txt) | 3 | 29 | 32 | 0.002658 |
| [9x9_3box](9x9_3box/) | [9x9_3box_05.txt](9x9_3box/9x9_3box_05.txt) | 3 | 24 | 100 | 0.013660 |
| [9x9_3box](9x9_3box/) | [9x9_3box_06.txt](9x9_3box/9x9_3box_06.txt) | 3 | 18 | 18 | 0.001430 |
| [9x9_3box](9x9_3box/) | [9x9_3box_07.txt](9x9_3box/9x9_3box_07.txt) | 3 | 20 | 20 | 0.001439 |
| [9x9_3box](9x9_3box/) | [9x9_3box_08.txt](9x9_3box/9x9_3box_08.txt) | 3 | 18 | 490 | 0.064770 |
| [9x9_3box](9x9_3box/) | [9x9_3box_09.txt](9x9_3box/9x9_3box_09.txt) | 3 | 24 | 24 | 0.002371 |
| [9x9_3box](9x9_3box/) | [9x9_3box_10.txt](9x9_3box/9x9_3box_10.txt) | 3 | 18 | 18 | 0.001515 |
| [9x9_4box](9x9_4box/) | [9x9_4box_01.txt](9x9_4box/9x9_4box_01.txt) | 4 | 24 | 2884 | 0.314743 |
| [9x9_4box](9x9_4box/) | [9x9_4box_02.txt](9x9_4box/9x9_4box_02.txt) | 4 | 16 | 16 | 0.000956 |
| [9x9_4box](9x9_4box/) | [9x9_4box_03.txt](9x9_4box/9x9_4box_03.txt) | 4 | 19 | 56 | 0.007095 |
| [9x9_4box](9x9_4box/) | [9x9_4box_04.txt](9x9_4box/9x9_4box_04.txt) | 4 | 16 | 26 | 0.004495 |
| [9x9_4box](9x9_4box/) | [9x9_4box_05.txt](9x9_4box/9x9_4box_05.txt) | 4 | 17 | 17 | 0.001561 |
| [9x9_4box](9x9_4box/) | [9x9_4box_06.txt](9x9_4box/9x9_4box_06.txt) | 4 | 19 | 85 | 0.015514 |
| [9x9_4box](9x9_4box/) | [9x9_4box_07.txt](9x9_4box/9x9_4box_07.txt) | 4 | 33 | 39 | 0.004121 |
| [9x9_4box](9x9_4box/) | [9x9_4box_08.txt](9x9_4box/9x9_4box_08.txt) | 4 | 35 | 46 | 0.004550 |
| [9x9_4box](9x9_4box/) | [9x9_4box_09.txt](9x9_4box/9x9_4box_09.txt) | 4 | 30 | 263 | 0.053485 |
| [9x9_4box](9x9_4box/) | [9x9_4box_10.txt](9x9_4box/9x9_4box_10.txt) | 4 | 19 | 25 | 0.003654 |
| [9x9_5box](9x9_5box/) | [9x9_5box_01.txt](9x9_5box/9x9_5box_01.txt) | 5 | 16 | 67 | 0.015444 |
| [9x9_5box](9x9_5box/) | [9x9_5box_02.txt](9x9_5box/9x9_5box_02.txt) | 5 | 24 | 353 | 0.043401 |
| [9x9_5box](9x9_5box/) | [9x9_5box_03.txt](9x9_5box/9x9_5box_03.txt) | 5 | 17 | 93 | 0.013098 |
| [9x9_5box](9x9_5box/) | [9x9_5box_04.txt](9x9_5box/9x9_5box_04.txt) | 5 | 22 | 168 | 0.036692 |
| [9x9_5box](9x9_5box/) | [9x9_5box_05.txt](9x9_5box/9x9_5box_05.txt) | 5 | 43 | 82 | 0.010285 |
| [9x9_5box](9x9_5box/) | [9x9_5box_06.txt](9x9_5box/9x9_5box_06.txt) | 5 | 41 | 100 | 0.016703 |
| [9x9_5box](9x9_5box/) | [9x9_5box_07.txt](9x9_5box/9x9_5box_07.txt) | 5 | 30 | 188 | 0.041150 |
| [9x9_5box](9x9_5box/) | [9x9_5box_08.txt](9x9_5box/9x9_5box_08.txt) | 5 | 24 | 41 | 0.006257 |
| [9x9_5box](9x9_5box/) | [9x9_5box_09.txt](9x9_5box/9x9_5box_09.txt) | 5 | 19 | 1133 | 0.179290 |
| [9x9_5box](9x9_5box/) | [9x9_5box_10.txt](9x9_5box/9x9_5box_10.txt) | 5 | 16 | 123 | 0.015082 |
| [10x10_3box](10x10_3box/) | [10x10_3box_01.txt](10x10_3box/10x10_3box_01.txt) | 3 | 22 | 28 | 0.003358 |
| [10x10_3box](10x10_3box/) | [10x10_3box_02.txt](10x10_3box/10x10_3box_02.txt) | 3 | 25 | 234 | 0.037638 |
| [10x10_3box](10x10_3box/) | [10x10_3box_03.txt](10x10_3box/10x10_3box_03.txt) | 3 | 18 | 18 | 0.001793 |
| [10x10_3box](10x10_3box/) | [10x10_3box_04.txt](10x10_3box/10x10_3box_04.txt) | 3 | 23 | 467 | 0.104160 |
| [10x10_3box](10x10_3box/) | [10x10_3box_05.txt](10x10_3box/10x10_3box_05.txt) | 3 | 30 | 46 | 0.007116 |
| [10x10_3box](10x10_3box/) | [10x10_3box_06.txt](10x10_3box/10x10_3box_06.txt) | 3 | 17 | 17 | 0.001412 |
| [10x10_3box](10x10_3box/) | [10x10_3box_07.txt](10x10_3box/10x10_3box_07.txt) | 3 | 44 | 47 | 0.005187 |
| [10x10_3box](10x10_3box/) | [10x10_3box_08.txt](10x10_3box/10x10_3box_08.txt) | 3 | 30 | 462 | 0.097287 |
| [10x10_3box](10x10_3box/) | [10x10_3box_09.txt](10x10_3box/10x10_3box_09.txt) | 3 | 20 | 29 | 0.004194 |
| [10x10_3box](10x10_3box/) | [10x10_3box_10.txt](10x10_3box/10x10_3box_10.txt) | 3 | 31 | 71 | 0.008785 |
| [10x10_4box](10x10_4box/) | [10x10_4box_01.txt](10x10_4box/10x10_4box_01.txt) | 4 | 29 | 41 | 0.005327 |
| [10x10_4box](10x10_4box/) | [10x10_4box_02.txt](10x10_4box/10x10_4box_02.txt) | 4 | 23 | 48 | 0.006152 |
| [10x10_4box](10x10_4box/) | [10x10_4box_03.txt](10x10_4box/10x10_4box_03.txt) | 4 | 31 | 1236 | 0.253400 |
| [10x10_4box](10x10_4box/) | [10x10_4box_04.txt](10x10_4box/10x10_4box_04.txt) | 4 | 25 | 25 | 0.002839 |
| [10x10_4box](10x10_4box/) | [10x10_4box_05.txt](10x10_4box/10x10_4box_05.txt) | 4 | 27 | 1636 | 0.284248 |
| [10x10_4box](10x10_4box/) | [10x10_4box_06.txt](10x10_4box/10x10_4box_06.txt) | 4 | 37 | 41 | 0.004815 |
| [10x10_4box](10x10_4box/) | [10x10_4box_07.txt](10x10_4box/10x10_4box_07.txt) | 4 | 19 | 19 | 0.001683 |
| [10x10_4box](10x10_4box/) | [10x10_4box_08.txt](10x10_4box/10x10_4box_08.txt) | 4 | 19 | 92 | 0.019952 |
| [10x10_4box](10x10_4box/) | [10x10_4box_09.txt](10x10_4box/10x10_4box_09.txt) | 4 | 18 | 21 | 0.002514 |
| [10x10_4box](10x10_4box/) | [10x10_4box_10.txt](10x10_4box/10x10_4box_10.txt) | 4 | 30 | 694 | 0.137629 |
| [10x10_5box](10x10_5box/) | [10x10_5box_01.txt](10x10_5box/10x10_5box_01.txt) | 5 | 33 | 88 | 0.014459 |
| [10x10_5box](10x10_5box/) | [10x10_5box_02.txt](10x10_5box/10x10_5box_02.txt) | 5 | 23 | 48 | 0.005287 |
| [10x10_5box](10x10_5box/) | [10x10_5box_03.txt](10x10_5box/10x10_5box_03.txt) | 5 | 18 | 24 | 0.002420 |
| [10x10_5box](10x10_5box/) | [10x10_5box_04.txt](10x10_5box/10x10_5box_04.txt) | 5 | 26 | 384 | 0.063815 |
| [10x10_5box](10x10_5box/) | [10x10_5box_05.txt](10x10_5box/10x10_5box_05.txt) | 5 | 27 | 27 | 0.003137 |
| [10x10_5box](10x10_5box/) | [10x10_5box_06.txt](10x10_5box/10x10_5box_06.txt) | 5 | 44 | 71 | 0.008828 |
| [10x10_5box](10x10_5box/) | [10x10_5box_07.txt](10x10_5box/10x10_5box_07.txt) | 5 | 18 | 70 | 0.010126 |
| [10x10_5box](10x10_5box/) | [10x10_5box_08.txt](10x10_5box/10x10_5box_08.txt) | 5 | 16 | 27 | 0.004621 |
| [10x10_5box](10x10_5box/) | [10x10_5box_09.txt](10x10_5box/10x10_5box_09.txt) | 5 | 21 | 21 | 0.003011 |
| [10x10_5box](10x10_5box/) | [10x10_5box_10.txt](10x10_5box/10x10_5box_10.txt) | 5 | 29 | 36 | 0.004617 |
| [10x10_6box](10x10_6box/) | [10x10_6box_01.txt](10x10_6box/10x10_6box_01.txt) | 6 | 36 | 3489 | 0.932473 |
| [10x10_6box](10x10_6box/) | [10x10_6box_02.txt](10x10_6box/10x10_6box_02.txt) | 6 | 16 | 58 | 0.008767 |
| [10x10_6box](10x10_6box/) | [10x10_6box_03.txt](10x10_6box/10x10_6box_03.txt) | 6 | 30 | 946 | 0.133177 |
| [10x10_6box](10x10_6box/) | [10x10_6box_04.txt](10x10_6box/10x10_6box_04.txt) | 6 | 21 | 174 | 0.054437 |
| [10x10_6box](10x10_6box/) | [10x10_6box_05.txt](10x10_6box/10x10_6box_05.txt) | 6 | 26 | 297 | 0.039135 |
| [10x10_6box](10x10_6box/) | [10x10_6box_06.txt](10x10_6box/10x10_6box_06.txt) | 6 | 18 | 18 | 0.004799 |
| [10x10_6box](10x10_6box/) | [10x10_6box_07.txt](10x10_6box/10x10_6box_07.txt) | 6 | 20 | 122 | 0.016691 |
| [10x10_6box](10x10_6box/) | [10x10_6box_08.txt](10x10_6box/10x10_6box_08.txt) | 6 | 31 | 115 | 0.025450 |
| [10x10_6box](10x10_6box/) | [10x10_6box_09.txt](10x10_6box/10x10_6box_09.txt) | 6 | 41 | 7685 | 1.550625 |
| [10x10_6box](10x10_6box/) | [10x10_6box_10.txt](10x10_6box/10x10_6box_10.txt) | 6 | 48 | 719 | 0.153284 |
| [10x10_7box](10x10_7box/) | [10x10_7box_01.txt](10x10_7box/10x10_7box_01.txt) | 7 | 43 | 1300 | 0.317294 |
| [10x10_7box](10x10_7box/) | [10x10_7box_02.txt](10x10_7box/10x10_7box_02.txt) | 7 | 16 | 24 | 0.003754 |
| [10x10_7box](10x10_7box/) | [10x10_7box_03.txt](10x10_7box/10x10_7box_03.txt) | 7 | 27 | 914 | 0.148667 |
| [10x10_7box](10x10_7box/) | [10x10_7box_04.txt](10x10_7box/10x10_7box_04.txt) | 7 | 23 | 576 | 0.132283 |
| [10x10_7box](10x10_7box/) | [10x10_7box_05.txt](10x10_7box/10x10_7box_05.txt) | 7 | 22 | 175 | 0.055066 |
| [10x10_7box](10x10_7box/) | [10x10_7box_06.txt](10x10_7box/10x10_7box_06.txt) | 7 | 20 | 64 | 0.008599 |
| [10x10_7box](10x10_7box/) | [10x10_7box_07.txt](10x10_7box/10x10_7box_07.txt) | 7 | 27 | 817 | 0.188693 |
| [10x10_7box](10x10_7box/) | [10x10_7box_08.txt](10x10_7box/10x10_7box_08.txt) | 7 | 30 | 1091 | 0.214399 |
| [10x10_7box](10x10_7box/) | [10x10_7box_09.txt](10x10_7box/10x10_7box_09.txt) | 7 | 48 | 561 | 0.131017 |
| [10x10_7box](10x10_7box/) | [10x10_7box_10.txt](10x10_7box/10x10_7box_10.txt) | 7 | 27 | 373 | 0.083744 |
| [10x10_8box](10x10_8box/) | [10x10_8box_01.txt](10x10_8box/10x10_8box_01.txt) | 8 | 19 | 308 | 0.052541 |
| [10x10_8box](10x10_8box/) | [10x10_8box_02.txt](10x10_8box/10x10_8box_02.txt) | 8 | 27 | 914 | 0.116046 |
| [10x10_8box](10x10_8box/) | [10x10_8box_03.txt](10x10_8box/10x10_8box_03.txt) | 8 | 17 | 17 | 0.002028 |
| [10x10_8box](10x10_8box/) | [10x10_8box_04.txt](10x10_8box/10x10_8box_04.txt) | 8 | 27 | 160 | 0.037394 |
| [10x10_8box](10x10_8box/) | [10x10_8box_05.txt](10x10_8box/10x10_8box_05.txt) | 8 | 22 | 550 | 0.163082 |
| [10x10_8box](10x10_8box/) | [10x10_8box_06.txt](10x10_8box/10x10_8box_06.txt) | 8 | 27 | 17570 | 4.815761 |
| [10x10_8box](10x10_8box/) | [10x10_8box_07.txt](10x10_8box/10x10_8box_07.txt) | 8 | 26 | 729 | 0.270212 |
| [10x10_8box](10x10_8box/) | [10x10_8box_08.txt](10x10_8box/10x10_8box_08.txt) | 8 | 48 | 1576 | 0.354818 |
| [10x10_8box](10x10_8box/) | [10x10_8box_09.txt](10x10_8box/10x10_8box_09.txt) | 8 | 26 | 7130 | 1.746764 |
| [10x10_8box](10x10_8box/) | [10x10_8box_10.txt](10x10_8box/10x10_8box_10.txt) | 8 | 24 | 36 | 0.006527 |
