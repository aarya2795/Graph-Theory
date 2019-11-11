<h1>Bridge Detection Algorithm</h1>
<br>Detecting bridges in Les Mis network
 
<br>Require: Connected graph G(V, E)
<br>1: return Bridge Edges
<br>2: bridgeSet = {}
<br>3: for e(u, v) ∈ E do
<br>4:     G' = Remove e from G
<br>5:     Disconnected = False;
<br>6:     if BFS in G 0 starting at u does not visit v then
<br>7:        Disconnected = True;
<br>8:     end if
<br>9:     if Disconnected then
<br>10:       bridgeSet = bridgeSet ∪ {e}
<br>11:    end if
<br>12: end for
<br>13: Return bridgeSet
