begin_version
3
end_version
begin_metric
0
end_metric
10
begin_variable
var0
-1
2
Atom flattire()
NegatedAtom flattire()
end_variable
begin_variable
var1
-1
2
Atom hasspare()
NegatedAtom hasspare()
end_variable
begin_variable
var2
-1
2
Atom spare-in(n10)
NegatedAtom spare-in(n10)
end_variable
begin_variable
var3
-1
2
Atom spare-in(n12)
NegatedAtom spare-in(n12)
end_variable
begin_variable
var4
-1
2
Atom spare-in(n16)
NegatedAtom spare-in(n16)
end_variable
begin_variable
var5
-1
2
Atom spare-in(n4)
NegatedAtom spare-in(n4)
end_variable
begin_variable
var6
-1
2
Atom spare-in(n5)
NegatedAtom spare-in(n5)
end_variable
begin_variable
var7
-1
2
Atom spare-in(n7)
NegatedAtom spare-in(n7)
end_variable
begin_variable
var8
-1
2
Atom spare-in(n8)
NegatedAtom spare-in(n8)
end_variable
begin_variable
var9
-1
17
Atom vehicle-at(n0)
Atom vehicle-at(n1)
Atom vehicle-at(n10)
Atom vehicle-at(n11)
Atom vehicle-at(n12)
Atom vehicle-at(n13)
Atom vehicle-at(n14)
Atom vehicle-at(n15)
Atom vehicle-at(n16)
Atom vehicle-at(n2)
Atom vehicle-at(n3)
Atom vehicle-at(n4)
Atom vehicle-at(n5)
Atom vehicle-at(n6)
Atom vehicle-at(n7)
Atom vehicle-at(n8)
Atom vehicle-at(n9)
end_variable
1
begin_mutex_group
17
9 0
9 1
9 2
9 3
9 4
9 5
9 6
9 7
9 8
9 9
9 10
9 11
9 12
9 13
9 14
9 15
9 16
end_mutex_group
begin_state
1
1
0
0
0
0
0
0
0
9
end_state
begin_goal
1
9 0
end_goal
96
begin_operator
changetire_DETDUP_1 
0
2
0 0 0 1
0 1 0 1
0
end_operator
begin_operator
loadtire n10
1
9 2
2
0 1 1 0
0 2 0 1
0
end_operator
begin_operator
loadtire n12
1
9 4
2
0 1 1 0
0 3 0 1
0
end_operator
begin_operator
loadtire n16
1
9 8
2
0 1 1 0
0 4 0 1
0
end_operator
begin_operator
loadtire n4
1
9 11
2
0 1 1 0
0 5 0 1
0
end_operator
begin_operator
loadtire n5
1
9 12
2
0 1 1 0
0 6 0 1
0
end_operator
begin_operator
loadtire n7
1
9 14
2
0 1 1 0
0 7 0 1
0
end_operator
begin_operator
loadtire n8
1
9 15
2
0 1 1 0
0 8 0 1
0
end_operator
begin_operator
move-car_DETDUP_0 n0 n12
1
0 1
1
0 9 0 4
0
end_operator
begin_operator
move-car_DETDUP_0 n0 n16
1
0 1
1
0 9 0 8
0
end_operator
begin_operator
move-car_DETDUP_0 n1 n2
1
0 1
1
0 9 1 9
0
end_operator
begin_operator
move-car_DETDUP_0 n1 n3
1
0 1
1
0 9 1 10
0
end_operator
begin_operator
move-car_DETDUP_0 n10 n12
1
0 1
1
0 9 2 4
0
end_operator
begin_operator
move-car_DETDUP_0 n10 n13
1
0 1
1
0 9 2 5
0
end_operator
begin_operator
move-car_DETDUP_0 n10 n5
1
0 1
1
0 9 2 12
0
end_operator
begin_operator
move-car_DETDUP_0 n11 n16
1
0 1
1
0 9 3 8
0
end_operator
begin_operator
move-car_DETDUP_0 n12 n0
1
0 1
1
0 9 4 0
0
end_operator
begin_operator
move-car_DETDUP_0 n12 n10
1
0 1
1
0 9 4 2
0
end_operator
begin_operator
move-car_DETDUP_0 n12 n16
1
0 1
1
0 9 4 8
0
end_operator
begin_operator
move-car_DETDUP_0 n12 n9
1
0 1
1
0 9 4 16
0
end_operator
begin_operator
move-car_DETDUP_0 n13 n10
1
0 1
1
0 9 5 2
0
end_operator
begin_operator
move-car_DETDUP_0 n13 n15
1
0 1
1
0 9 5 7
0
end_operator
begin_operator
move-car_DETDUP_0 n13 n3
1
0 1
1
0 9 5 10
0
end_operator
begin_operator
move-car_DETDUP_0 n13 n7
1
0 1
1
0 9 5 14
0
end_operator
begin_operator
move-car_DETDUP_0 n14 n16
1
0 1
1
0 9 6 8
0
end_operator
begin_operator
move-car_DETDUP_0 n14 n3
1
0 1
1
0 9 6 10
0
end_operator
begin_operator
move-car_DETDUP_0 n14 n6
1
0 1
1
0 9 6 13
0
end_operator
begin_operator
move-car_DETDUP_0 n15 n13
1
0 1
1
0 9 7 5
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n0
1
0 1
1
0 9 8 0
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n11
1
0 1
1
0 9 8 3
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n12
1
0 1
1
0 9 8 4
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n14
1
0 1
1
0 9 8 6
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n5
1
0 1
1
0 9 8 12
0
end_operator
begin_operator
move-car_DETDUP_0 n16 n9
1
0 1
1
0 9 8 16
0
end_operator
begin_operator
move-car_DETDUP_0 n2 n1
1
0 1
1
0 9 9 1
0
end_operator
begin_operator
move-car_DETDUP_0 n3 n1
1
0 1
1
0 9 10 1
0
end_operator
begin_operator
move-car_DETDUP_0 n3 n13
1
0 1
1
0 9 10 5
0
end_operator
begin_operator
move-car_DETDUP_0 n3 n14
1
0 1
1
0 9 10 6
0
end_operator
begin_operator
move-car_DETDUP_0 n3 n4
1
0 1
1
0 9 10 11
0
end_operator
begin_operator
move-car_DETDUP_0 n4 n3
1
0 1
1
0 9 11 10
0
end_operator
begin_operator
move-car_DETDUP_0 n5 n10
1
0 1
1
0 9 12 2
0
end_operator
begin_operator
move-car_DETDUP_0 n5 n16
1
0 1
1
0 9 12 8
0
end_operator
begin_operator
move-car_DETDUP_0 n5 n8
1
0 1
1
0 9 12 15
0
end_operator
begin_operator
move-car_DETDUP_0 n6 n14
1
0 1
1
0 9 13 6
0
end_operator
begin_operator
move-car_DETDUP_0 n7 n13
1
0 1
1
0 9 14 5
0
end_operator
begin_operator
move-car_DETDUP_0 n7 n9
1
0 1
1
0 9 14 16
0
end_operator
begin_operator
move-car_DETDUP_0 n8 n5
1
0 1
1
0 9 15 12
0
end_operator
begin_operator
move-car_DETDUP_0 n8 n9
1
0 1
1
0 9 15 16
0
end_operator
begin_operator
move-car_DETDUP_0 n9 n12
1
0 1
1
0 9 16 4
0
end_operator
begin_operator
move-car_DETDUP_0 n9 n16
1
0 1
1
0 9 16 8
0
end_operator
begin_operator
move-car_DETDUP_0 n9 n7
1
0 1
1
0 9 16 14
0
end_operator
begin_operator
move-car_DETDUP_0 n9 n8
1
0 1
1
0 9 16 15
0
end_operator
begin_operator
move-car_DETDUP_1 n0 n12
0
2
0 0 1 0
0 9 0 4
0
end_operator
begin_operator
move-car_DETDUP_1 n0 n16
0
2
0 0 1 0
0 9 0 8
0
end_operator
begin_operator
move-car_DETDUP_1 n1 n2
0
2
0 0 1 0
0 9 1 9
0
end_operator
begin_operator
move-car_DETDUP_1 n1 n3
0
2
0 0 1 0
0 9 1 10
0
end_operator
begin_operator
move-car_DETDUP_1 n10 n12
0
2
0 0 1 0
0 9 2 4
0
end_operator
begin_operator
move-car_DETDUP_1 n10 n13
0
2
0 0 1 0
0 9 2 5
0
end_operator
begin_operator
move-car_DETDUP_1 n10 n5
0
2
0 0 1 0
0 9 2 12
0
end_operator
begin_operator
move-car_DETDUP_1 n11 n16
0
2
0 0 1 0
0 9 3 8
0
end_operator
begin_operator
move-car_DETDUP_1 n12 n0
0
2
0 0 1 0
0 9 4 0
0
end_operator
begin_operator
move-car_DETDUP_1 n12 n10
0
2
0 0 1 0
0 9 4 2
0
end_operator
begin_operator
move-car_DETDUP_1 n12 n16
0
2
0 0 1 0
0 9 4 8
0
end_operator
begin_operator
move-car_DETDUP_1 n12 n9
0
2
0 0 1 0
0 9 4 16
0
end_operator
begin_operator
move-car_DETDUP_1 n13 n10
0
2
0 0 1 0
0 9 5 2
0
end_operator
begin_operator
move-car_DETDUP_1 n13 n15
0
2
0 0 1 0
0 9 5 7
0
end_operator
begin_operator
move-car_DETDUP_1 n13 n3
0
2
0 0 1 0
0 9 5 10
0
end_operator
begin_operator
move-car_DETDUP_1 n13 n7
0
2
0 0 1 0
0 9 5 14
0
end_operator
begin_operator
move-car_DETDUP_1 n14 n16
0
2
0 0 1 0
0 9 6 8
0
end_operator
begin_operator
move-car_DETDUP_1 n14 n3
0
2
0 0 1 0
0 9 6 10
0
end_operator
begin_operator
move-car_DETDUP_1 n14 n6
0
2
0 0 1 0
0 9 6 13
0
end_operator
begin_operator
move-car_DETDUP_1 n15 n13
0
2
0 0 1 0
0 9 7 5
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n0
0
2
0 0 1 0
0 9 8 0
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n11
0
2
0 0 1 0
0 9 8 3
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n12
0
2
0 0 1 0
0 9 8 4
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n14
0
2
0 0 1 0
0 9 8 6
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n5
0
2
0 0 1 0
0 9 8 12
0
end_operator
begin_operator
move-car_DETDUP_1 n16 n9
0
2
0 0 1 0
0 9 8 16
0
end_operator
begin_operator
move-car_DETDUP_1 n2 n1
0
2
0 0 1 0
0 9 9 1
0
end_operator
begin_operator
move-car_DETDUP_1 n3 n1
0
2
0 0 1 0
0 9 10 1
0
end_operator
begin_operator
move-car_DETDUP_1 n3 n13
0
2
0 0 1 0
0 9 10 5
0
end_operator
begin_operator
move-car_DETDUP_1 n3 n14
0
2
0 0 1 0
0 9 10 6
0
end_operator
begin_operator
move-car_DETDUP_1 n3 n4
0
2
0 0 1 0
0 9 10 11
0
end_operator
begin_operator
move-car_DETDUP_1 n4 n3
0
2
0 0 1 0
0 9 11 10
0
end_operator
begin_operator
move-car_DETDUP_1 n5 n10
0
2
0 0 1 0
0 9 12 2
0
end_operator
begin_operator
move-car_DETDUP_1 n5 n16
0
2
0 0 1 0
0 9 12 8
0
end_operator
begin_operator
move-car_DETDUP_1 n5 n8
0
2
0 0 1 0
0 9 12 15
0
end_operator
begin_operator
move-car_DETDUP_1 n6 n14
0
2
0 0 1 0
0 9 13 6
0
end_operator
begin_operator
move-car_DETDUP_1 n7 n13
0
2
0 0 1 0
0 9 14 5
0
end_operator
begin_operator
move-car_DETDUP_1 n7 n9
0
2
0 0 1 0
0 9 14 16
0
end_operator
begin_operator
move-car_DETDUP_1 n8 n5
0
2
0 0 1 0
0 9 15 12
0
end_operator
begin_operator
move-car_DETDUP_1 n8 n9
0
2
0 0 1 0
0 9 15 16
0
end_operator
begin_operator
move-car_DETDUP_1 n9 n12
0
2
0 0 1 0
0 9 16 4
0
end_operator
begin_operator
move-car_DETDUP_1 n9 n16
0
2
0 0 1 0
0 9 16 8
0
end_operator
begin_operator
move-car_DETDUP_1 n9 n7
0
2
0 0 1 0
0 9 16 14
0
end_operator
begin_operator
move-car_DETDUP_1 n9 n8
0
2
0 0 1 0
0 9 16 15
0
end_operator
0
