begin_version
3
end_version
begin_metric
0
end_metric
2
begin_variable
var0
-1
2
Atom position(p0)
Atom position(p1)
end_variable
begin_variable
var1
-1
2
Atom up()
NegatedAtom up()
end_variable
1
begin_mutex_group
2
0 0
0 1
end_mutex_group
begin_state
0
1
end_state
begin_goal
2
0 1
1 0
end_goal
6
begin_operator
climb p0
1
0 0
1
0 1 1 0
0
end_operator
begin_operator
climb-down 
0
1
0 1 0 1
0
end_operator
begin_operator
walk-left p1 p0
1
1 1
1
0 0 1 0
0
end_operator
begin_operator
walk-on-beam_DETDUP_0 p0 p1
1
1 0
1
0 0 0 1
0
end_operator
begin_operator
walk-on-beam_DETDUP_1 p0 p1
0
2
0 0 0 1
0 1 0 1
0
end_operator
begin_operator
walk-right p0 p1
1
1 1
1
0 0 0 1
0
end_operator
0
